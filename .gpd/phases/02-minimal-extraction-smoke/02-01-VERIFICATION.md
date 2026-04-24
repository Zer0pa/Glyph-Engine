# Phase 02a Verification

Date: 2026-04-24
Executed on: RunPod `b7fb18eddf65` (AMD EPYC 7713P, 32 vCPU, 995 GiB RAM)
Commit: will be appended on push

## Environment

- Python `3.13.5` (system) in `/workspace/.venv`
- `numpy==2.4.4`, `opencv-python-headless==4.13.0.92`,
  `scikit-image==0.26.0`, `scikit-learn==1.8.0`, `scipy==1.17.1`
- `gnosis-morph-bench==0.1.0` (editable from `/workspace/gnosis-morph-bench`)
- `gnosis-glyph-engine==0.1.0a1` (editable from `/workspace/gnosis-glyph-engine`)

## Gate 1 — monorepo-free install

`pip install -e /workspace/gnosis-glyph-engine[dev]` completed without
resolving any live-monorepo path. All transitive deps resolved from PyPI.
**PASS.**

## Gate 2 — pytest

Command: `python -m pytest -q` from `/workspace/gnosis-glyph-engine/`.
Result: `16 passed in 9.41s`. **PASS.**

Test coverage:

- `tests/test_fixtures.py` — 6 tests: item count + families, shape + dtype,
  reference labels, cross-run determinism, seed sensitivity, non-empty
  foreground.
- `tests/test_baselines.py` — 5 tests: one per baseline for protocol +
  shape + finite-ness, HOG-fit-required guard, cross-arm non-degeneracy
  sanity.
- `tests/test_manifest_builder.py` — 5 tests: shape, JSON roundtrip,
  duplicate-name rejection, empty-input rejection, morph-bench loader
  roundtrip.

## Gate 3 — ablation runs

Command: `python -m gnosis_glyph_engine.scripts.run_ablation`.
Output: `artifacts/ablation/ablation_report.json` + three per-arm
manifest and smoke-report pairs under `artifacts/ablation/per_arm/`.
**PASS.**

## Gate 4 — morph-bench ingestion

Each per-arm manifest is loaded by `gnosis_morph_bench.schema.load_manifest`
(exercised both in `test_manifest_builder.py::test_morph_bench_loader_accepts_manifest`
and inside `run_ablation.py::_run_morph_bench` via a `NamedTemporaryFile`
roundtrip). Morph-bench then produces `route_results`, `freeze_reference`,
`deterministic_replay`, and `leave_fraction_out` output consumed in the
final report. **PASS.**

## Measured Metrics (2026-04-24, seed=42, n_clusters=3, null_repeats=32)

| Arm | nmi | sigma | null_mean ± null_std | silhouette | mean_jaccard | min_jaccard | max_jaccard |
|---|---:|---:|---:|---:|---:|---:|---:|
| baseline_orb | 1.000 | **6.400** | 0.212 ± 0.123 | 0.268 | **1.000** | 1.000 | 1.000 |
| baseline_hog | 0.568 | 3.774 | 0.213 ± 0.094 | 0.022 | 0.400 | 0.294 | 0.692 |
| baseline_hu_regionprops | 0.496 | 3.399 | 0.191 ± 0.090 | **0.408** | 0.833 | 0.611 | 1.000 |

Reference-freeze sha256 identical across arms (same fixture, same labels):
`7729559a5b052623e47a995459b15a0fe44fb871e75b9e255d4417b362195dbd`.

`replay_all_identical == true` for every arm — deterministic.

## Phase 02a Gate Summary

All four implementation gates PASSED. The frozen Phase 01 interface is
proven implementable and ingestible by morph-bench. The scaffold runs
entirely from repo custody; no live-monorepo imports exist in the code or
the install graph.

## Phase 02a Findings For Phase 03

1. `baseline_orb` **saturates** the 12-glyph fixture: perfect NMI and
   jaccard with a large margin above the null distribution.
2. `baseline_hu_regionprops` is second-best on jaccard and has the
   strongest silhouette, but the weakest σ.
3. `baseline_hog` is mid on σ but very weak on jaccard and silhouette,
   meaning its clustering is unstable under leave-25%-out.
4. **Risk to the D-04 pass rule**: to pass, an owned arm must exceed
   σ ≈ 6.9 AND achieve `mean_jaccard` ≥ 1.0. On this fixture, clearing
   that is extremely tight.
5. Phase 03 decision point: accept the risk and evaluate owned arms under
   D-04 as-is, OR widen the fixture in a new phase before Phase 02b runs.
   Recommended option is recorded in Phase 03 once it opens.

## Authority Metric Impact

`package_boundary_earned`:

- Gate 1 (admitted consumer): still PASSED from Phase 01 freeze.
- Gate 2 (monorepo-free smoke): **now PASSED by Phase 02a**.
- Gate 3 (tiny smoke path passes from repo custody): **now PASSED by
  Phase 02a**.
- Gate 4 (owned layer beats borrowed baselines on ablation): still
  UNTESTED and BLOCKED on D-06.

Overall metric status: `UNTESTED` → remains `UNTESTED` until gate 4 resolves.
