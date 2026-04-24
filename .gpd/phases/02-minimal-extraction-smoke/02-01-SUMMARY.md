# Phase 02a Summary: Borrowed-Baseline Sanity Path

Date: 2026-04-24
Status: `COMPLETE`
Gate: `PASS`

## What Was Done

- Authored `pyproject.toml` with `gnosis-glyph-engine==0.1.0a1`, src-layout,
  and pinned borrowed deps (`numpy`, `opencv-python-headless`,
  `scikit-image`, `scikit-learn`).
- Implemented the Phase 01 D-02 interface:
  `src/gnosis_glyph_engine/protocols.py` (`Descriptor`, `LearnedDescriptor`,
  `SourceRetrievalPending`).
- Implemented the Phase 01 D-03 fixture:
  `src/gnosis_glyph_engine/fixtures.py::synthesize_twelve_glyphs`.
- Implemented three borrowed-baseline descriptors:
  `baselines/{orb.py,hu_regionprops.py,hog.py}`.
- Implemented the morph-bench manifest builder:
  `manifest_builder.py::build_manifest`.
- Placeholder `owned/__init__.py` raises `SourceRetrievalPending` while
  D-06 remains open.
- 16-test pytest suite covering fixture determinism, baseline shape /
  finite / fit-guard, manifest-builder shape, JSON roundtrip, and direct
  morph-bench loader compatibility.
- Ablation driver `scripts/run_ablation.py` and the in-package version
  under `gnosis_glyph_engine.scripts.run_ablation` (console script
  `glyph-engine-ablation`).
- Phase 02 sub-phase artefacts: `02-CONTEXT.md`, `02-01-PLAN.md`,
  `02-01-DECISIONS.md`, `02-01-VERIFICATION.md` (this file).

## Where It Ran

- Authoring: local Mac at
  `Gnosis Portfolio/workstreams/gnosis-glyph-engine/05_repo_scaffold/`.
- Execution: RunPod host `38.80.152.147:34587`, pod `7k3riasglemecu`,
  workspace `/workspace/gnosis-glyph-engine/`, Python 3.13 venv.
- Morph-bench: editable install from rsync'd
  `/workspace/gnosis-morph-bench/`.

## Artefacts Produced

Under `artifacts/ablation/`:

- `ablation_report.json` — aggregated metric table plus provenance.
- `per_arm/baseline_orb.manifest.json` + `.smoke_report.json`
- `per_arm/baseline_hog.manifest.json` + `.smoke_report.json`
- `per_arm/baseline_hu_regionprops.manifest.json` + `.smoke_report.json`

Uploaded to HF dataset `Zer0pa/glyph-engine-artefacts` for failover.

## Key Findings

- **Scaffold is monorepo-free.** `pip install -e .` and pytest run with no
  references to any live-monorepo path; `gnosis_morph_bench` is the only
  admitted sibling dep and it is itself installed as a package.
- **Fixture is non-degenerate.** All three borrowed arms produce finite,
  replay-stable metrics, with inter-family separation exceeding intra-family
  noise.
- **Baseline saturation risk.** `baseline_orb` achieves NMI = 1.0,
  σ ≈ 6.40, mean_jaccard = 1.0 — effectively perfect clustering on the
  12-glyph synthetic fixture. The D-04 pass rule now requires an owned arm
  to deliver σ ≥ ~6.9 AND mean_jaccard ≥ 1.0. This is recorded in
  `02-01-DECISIONS.md` D-02a-06 as a Phase 03 risk.
- **Deterministic replay.** `replay_all_identical == true` for every arm
  across three runs with `seed=42`.

## Authority Metric Impact

`package_boundary_earned`:

| Gate | Status after Phase 02a |
|---|---|
| 1. Admitted consumer | PASSED (Phase 01) |
| 2. Monorepo-free execution | PASSED (Phase 02a) |
| 3. Tiny smoke from repo custody | PASSED (Phase 02a) |
| 4. Owned layer beats borrowed | UNTESTED — blocked on D-06 |

Overall metric verdict: `UNTESTED` (unchanged; gate 4 is the only
outstanding dimension).

## Blockers Carried Forward

- **D-06** (unchanged): retrieve
  `scripts/indus/stroke_native_encoding.py` and
  `scripts/indus/phase3_common.py` to unblock Phase 02b.
- **D-02a-06 fixture-saturation risk** (new): Phase 03 must decide whether
  to tighten the fixture or accept that a pass on this surface requires
  near-perfect owned-arm behaviour.

## Resume Point

Phase 02b (`Owned-Arm Ablation`) begins once D-06 clears. If the owner
widens the fixture first, a new phase (`02.1 Fixture Hardening`) can be
inserted via `/gpd:insert-phase`.
