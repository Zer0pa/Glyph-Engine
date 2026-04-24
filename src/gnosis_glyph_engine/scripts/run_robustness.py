"""Phase 02c: multi-seed OSS-baseline robustness check.

Smallest fair OSS-baseline comparison per the 2026-04-24 closeout brief
(lane `Glyph-Engine`, item 2). Runs the three frozen Phase 01 D-04
borrowed baselines across N seeds on the synthetic 12-glyph fixture and
reports per-arm distributional summaries (mean, stdev, min, max of σ,
NMI, and `mean_jaccard`).

Purpose: falsify or confirm the Phase 02a finding that `baseline_orb`
saturates the fixture. If the saturation is a single-seed artefact, the
Phase 03 routing should proceed with the frozen D-04 rule. If it holds
across seeds, the fixture is genuinely too easy for the owned arms to
beat, and the scaffold's adapter-only-vs-sovereign recommendation
(Phase 02c-01 DECISIONS) is driven by that evidence.

This script intentionally does **not** add new descriptors, new metrics,
or new pass rules. It widens the sample of the existing frozen evaluator
output.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import math
import statistics
from pathlib import Path

from gnosis_glyph_engine import __version__
from gnosis_glyph_engine.baselines import (
    HogPcaDescriptor,
    HuRegionpropsDescriptor,
    OrbDescriptor,
)
from gnosis_glyph_engine.fixtures import images_only, synthesize_twelve_glyphs
from gnosis_glyph_engine.manifest_builder import build_manifest


def _per_arm_result(manifest: dict, *, seed: int, n_clusters: int, null_repeats: int) -> dict:
    from gnosis_morph_bench.benchmark import EvaluationConfig, evaluate_routes
    from gnosis_morph_bench.schema import load_manifest
    from gnosis_morph_bench.stability import leave_fraction_out

    from tempfile import NamedTemporaryFile

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
    route_result = evaluate_routes(loaded, config)[0]
    jaccard = leave_fraction_out(loaded, route_result["route_name"], config, fraction=0.25, repeats=6)
    return {
        "arm": route_result["route_name"],
        "seed": seed,
        "nmi": route_result["nmi"],
        "sigma": route_result["sigma"],
        "null_mean": route_result["null_mean"],
        "null_std": route_result["null_std"],
        "silhouette": route_result["silhouette"],
        "mean_jaccard": jaccard["mean_jaccard"],
    }


def _summary(values: list[float]) -> dict[str, float]:
    finite = [v for v in values if v is not None and math.isfinite(v)]
    if not finite:
        return {"n": 0, "mean": None, "stdev": None, "min": None, "max": None}
    return {
        "n": len(finite),
        "mean": round(statistics.fmean(finite), 6),
        "stdev": round(statistics.pstdev(finite), 6) if len(finite) > 1 else 0.0,
        "min": round(min(finite), 6),
        "max": round(max(finite), 6),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Phase 02c multi-seed OSS-baseline robustness check.")
    parser.add_argument(
        "--seeds",
        type=int,
        nargs="+",
        default=list(range(10)),
        help="Seeds to evaluate (default: 0..9).",
    )
    parser.add_argument("--clusters", type=int, default=3)
    parser.add_argument("--null-repeats", type=int, default=32)
    parser.add_argument(
        "--output",
        default="artifacts/robustness/robustness_report.json",
        help="Destination path for the aggregated JSON report.",
    )
    args = parser.parse_args(argv)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    per_arm: dict[str, list[dict]] = {}
    for seed in args.seeds:
        items = synthesize_twelve_glyphs(seed=seed)
        images = images_only(items)
        arms = [
            OrbDescriptor(),
            HuRegionpropsDescriptor(),
            HogPcaDescriptor(seed=seed).fit(images),
        ]
        for arm in arms:
            manifest = build_manifest(
                manifest_name=f"phase02c-{arm.name}-seed{seed}",
                items=items,
                descriptors=[arm],
            )
            row = _per_arm_result(
                manifest,
                seed=seed,
                n_clusters=args.clusters,
                null_repeats=args.null_repeats,
            )
            per_arm.setdefault(arm.name, []).append(row)

    summary: list[dict] = []
    for arm_name in sorted(per_arm):
        rows = per_arm[arm_name]
        summary.append(
            {
                "arm": arm_name,
                "n_seeds": len(rows),
                "sigma": _summary([r["sigma"] for r in rows]),
                "nmi": _summary([r["nmi"] for r in rows]),
                "mean_jaccard": _summary([r["mean_jaccard"] for r in rows]),
                "silhouette": _summary([r["silhouette"] for r in rows]),
                "per_seed": rows,
            }
        )

    # Rank arms by mean sigma, descending (saturating arms sort to top).
    summary.sort(key=lambda entry: (entry["sigma"]["mean"] is None, -entry["sigma"]["mean"]))

    report = {
        "schema_version": 1,
        "phase": "02c",
        "phase_name": "OSS-Baseline Robustness",
        "generated_at": _dt.datetime.now(_dt.timezone.utc).isoformat(),
        "gnosis_glyph_engine_version": __version__,
        "seeds": args.seeds,
        "n_clusters": args.clusters,
        "null_repeats": args.null_repeats,
        "fixture": {
            "generator": "gnosis_glyph_engine.fixtures.synthesize_twelve_glyphs",
            "n_items_per_seed": 12,
        },
        "arms": summary,
        "interpretation_notes": [
            "This run evaluates only the borrowed-baseline arms; owned arms remain BLOCKED on D-06.",
            "Saturation is defined as mean NMI == 1.0 and mean mean_jaccard == 1.0 across seeds.",
            "A saturating baseline implies the Phase 01 D-04 pass rule is near-impossible on the current fixture; Phase 03 must judge routing.",
        ],
    }
    output_path.write_text(json.dumps(report, indent=2))
    print(str(output_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
