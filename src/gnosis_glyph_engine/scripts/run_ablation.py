"""Phase 02a ablation driver.

Produces ``artifacts/ablation/ablation_report.json`` by:

1. generating the deterministic 12-glyph fixture,
2. building one morph-bench manifest per borrowed baseline,
3. running ``gnosis_morph_bench`` CLI-equivalent helpers once per manifest,
4. aggregating per-arm metrics into a single report.

The owned arms (Phase 02b) are intentionally skipped; their source files are
blocked on Phase 01 D-06. The report records that explicitly so no downstream
reader can mistake Phase 02a for the full ablation.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
from pathlib import Path

from gnosis_glyph_engine import __version__
from gnosis_glyph_engine.baselines import (
    HogPcaDescriptor,
    HuRegionpropsDescriptor,
    OrbDescriptor,
)
from gnosis_glyph_engine.fixtures import images_only, synthesize_twelve_glyphs
from gnosis_glyph_engine.manifest_builder import build_manifest


def _run_morph_bench(manifest: dict, *, seed: int, n_clusters: int, null_repeats: int) -> dict:
    """Evaluate one manifest with morph-bench and return a condensed result dict."""
    from gnosis_morph_bench.benchmark import EvaluationConfig, evaluate_routes
    from gnosis_morph_bench.schema import freeze_reference
    from gnosis_morph_bench.stability import deterministic_replay, leave_fraction_out

    # Reconstruct a BenchmarkManifest object from our dict via a temp file to
    # exercise the exact loader used by morph-bench's CLI (no shortcuts).
    from tempfile import NamedTemporaryFile

    from gnosis_morph_bench.schema import load_manifest

    with NamedTemporaryFile("w", suffix=".json", delete=False) as handle:
        json.dump(manifest, handle)
        temp_path = Path(handle.name)
    try:
        loaded = load_manifest(temp_path)
    finally:
        temp_path.unlink(missing_ok=True)

    config = EvaluationConfig(
        reference_key="family",
        n_clusters=n_clusters,
        null_repeats=null_repeats,
        seed=seed,
    )
    route_results = evaluate_routes(loaded, config)
    best_route = route_results[0]["route_name"]
    frozen = freeze_reference(loaded, "family")
    replay = deterministic_replay(loaded, best_route, config)
    jaccard = leave_fraction_out(loaded, best_route, config, fraction=0.25, repeats=6)
    return {
        "best_route": best_route,
        "route_results": route_results,
        "reference_freeze_sha256": frozen["sha256"],
        "replay_all_identical": replay["all_identical"],
        "leave_fraction_out": jaccard,
    }


def _build_arms(images) -> list[object]:
    orb = OrbDescriptor()
    hu = HuRegionpropsDescriptor()
    hog = HogPcaDescriptor().fit(images)
    return [orb, hu, hog]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run Phase 02a borrowed-baseline ablation.")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--clusters", type=int, default=3)
    parser.add_argument("--null-repeats", type=int, default=32)
    parser.add_argument(
        "--output",
        default="artifacts/ablation/ablation_report.json",
        help="Destination path for the aggregated JSON report.",
    )
    parser.add_argument(
        "--per-arm-dir",
        default="artifacts/ablation/per_arm",
        help="Directory for per-arm morph-bench smoke reports.",
    )
    args = parser.parse_args(argv)

    output_path = Path(args.output)
    per_arm_dir = Path(args.per_arm_dir)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    per_arm_dir.mkdir(parents=True, exist_ok=True)

    items = synthesize_twelve_glyphs(seed=args.seed)
    images = images_only(items)
    arms = _build_arms(images)

    per_arm_summaries: list[dict] = []
    for arm in arms:
        manifest = build_manifest(
            manifest_name=f"phase02a-{arm.name}",
            items=items,
            descriptors=[arm],
        )
        manifest_path = per_arm_dir / f"{arm.name}.manifest.json"
        manifest_path.write_text(json.dumps(manifest, indent=2))

        result = _run_morph_bench(
            manifest,
            seed=args.seed,
            n_clusters=args.clusters,
            null_repeats=args.null_repeats,
        )

        arm_report_path = per_arm_dir / f"{arm.name}.smoke_report.json"
        arm_report_path.write_text(json.dumps(result, indent=2))

        # Condense to a flat per-arm row.
        route_row = result["route_results"][0]
        per_arm_summaries.append(
            {
                "arm": arm.name,
                "dim": arm.dim,
                "nmi": route_row["nmi"],
                "sigma": route_row["sigma"],
                "null_mean": route_row["null_mean"],
                "null_std": route_row["null_std"],
                "silhouette": route_row["silhouette"],
                "mean_jaccard": result["leave_fraction_out"]["mean_jaccard"],
                "min_jaccard": result["leave_fraction_out"]["min_jaccard"],
                "max_jaccard": result["leave_fraction_out"]["max_jaccard"],
                "replay_all_identical": result["replay_all_identical"],
                "reference_freeze_sha256": result["reference_freeze_sha256"],
                "manifest_path": str(manifest_path),
                "smoke_report_path": str(arm_report_path),
            }
        )

    # Order arms by morph-bench sigma, descending.
    per_arm_summaries.sort(key=lambda row: (row["sigma"] is None, -row["sigma"]))

    report = {
        "schema_version": 1,
        "phase": "02a",
        "phase_name": "Borrowed-Baseline Sanity Path",
        "generated_at": _dt.datetime.now(_dt.timezone.utc).isoformat(),
        "gnosis_glyph_engine_version": __version__,
        "seed": args.seed,
        "n_clusters": args.clusters,
        "null_repeats": args.null_repeats,
        "fixture": {
            "generator": "gnosis_glyph_engine.fixtures.synthesize_twelve_glyphs",
            "n_items": len(items),
            "families": sorted({it.family for it in items}),
        },
        "arms": per_arm_summaries,
        "owned_arms_status": "BLOCKED_ON_D-06",
        "owned_arms_blocker": (
            "scripts/indus/stroke_native_encoding.py and "
            "scripts/indus/phase3_common.py not present in portfolio "
            "snapshot; see .gpd/phases/01-consumer-and-interface-freeze/"
            "01-DECISIONS.md D-06."
        ),
        "pass_rule": (
            "Phase 02a does not evaluate the Phase 01 D-04 numeric pass rule. "
            "The rule compares owned arms to the best baseline and is applied "
            "in Phase 03 after Phase 02b runs."
        ),
    }
    output_path.write_text(json.dumps(report, indent=2))
    print(str(output_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
