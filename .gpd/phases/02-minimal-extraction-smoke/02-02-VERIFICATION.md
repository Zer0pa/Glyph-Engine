# Phase 02c Verification

Date: 2026-04-24
Executed on: RunPod (AMD EPYC 7713P, Python 3.13.5)
Context: closeout run for lane `Glyph-Engine`.

## Gate A — pytest with morph-bench installed

Command: `python -m pytest -q` from `<RUNPOD_WORKSPACE>/gnosis-glyph-engine/`
with `gnosis-morph-bench` editable-installed into the same venv.
Result: **17 passed** in 10.17 s.

Breakdown:

- 16 tests inherited from Phase 02a.
- 1 new test `test_manifest_matches_local_schema_contract` (local schema
  fallback that does not depend on morph-bench).
- `test_morph_bench_loader_accepts_manifest` runs (not skipped) because
  morph-bench is importable.

## Gate B — pytest in a morph-bench-free venv

Command: fresh `/tmp/glyph-iso` venv, `pip install -e <RUNPOD_WORKSPACE>/gnosis-glyph-engine[dev]`,
`pytest -q`.
Result: **16 passed, 1 skipped** in 1.84 s.

Breakdown:

- `test_morph_bench_loader_accepts_manifest` skipped cleanly with the
  correct reason string "`gnosis_morph_bench not installed; cross-repo
  contract test skipped`".
- All 16 other tests pass. This confirms `gnosis-glyph-engine` is
  independently installable and testable, satisfying the closeout brief's
  dependency-boundary P1 fix.

## Gate C — multi-seed robustness

Command: `python -m gnosis_glyph_engine.scripts.run_robustness` with
defaults (seeds 0..9, `n_clusters=3`, `null_repeats=32`).
Output: `artifacts/robustness/robustness_report.json` (10809 B, SHA256
`c2510b61b64e781e862b65d3bbd4f83a3a53265558de83baf824eeac6f076ffb`).

Per-arm summary (mean ± stdev, 10 seeds):

| Arm | σ mean | σ stdev | σ min | σ max | NMI mean | NMI max | mean_jaccard mean | silhouette mean |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `baseline_orb` | 4.138 | 1.116 | 2.729 | 6.234 | 0.765 | 1.000 | 0.899 | 0.288 |
| `baseline_hu_regionprops` | 2.954 | 1.056 | 0.703 | 4.098 | 0.575 | 0.740 | 0.943 | 0.488 |
| `baseline_hog` | 1.153 | 1.168 | -0.593 | 2.989 | 0.362 | 0.573 | 0.435 | 0.023 |

Key numeric claims:

- `baseline_orb` NMI = 1.0 in only 2 of 10 seeds (3, 4), not robustly.
- `baseline_hog` σ < 0 in 2 of 10 seeds (4, 6), i.e. below-null
  performance — HOG+PCA is not a reliable descriptor for this binary
  glyph family.
- `baseline_hu_regionprops` is the most jaccard-stable borrower under
  leave-25%-out (mean 0.943) but its σ is the second-weakest.

## Gate D — scrub of public-facing paths

Command: `grep -rl -E "38\.80\.152\.147|7k3riasglemecu|/Users/zer0palab|/workspace/gnosis|ssh\.runpod\.io"` across the repo (excluding `.git`).
Result: **CLEAN** — zero matches after the sed pass.

Replacements use the symbolic labels defined in
`docs/PROVENANCE_LABELS.md`: `<RUNPOD_HOST>`, `<RUNPOD_POD_ID>`,
`<RUNPOD_WORKSPACE>`, `<LOCAL_PORTFOLIO_ROOT>`, `<LOCAL_WORKSTREAM_ROOT>`,
`<LOCAL_HOME>`, `<LOCAL_SSH_KEY>`, `<LOCAL_HF_CACHE>`, etc.

## Gate E — license / rights posture

- `PRIVATE_INTERNAL_LICENSE_NOTICE.md` present, declaring
  `PRIVATE_INTERNAL_ONLY`.
- `LICENSE_PLACEHOLDER.md` retained as an owner-deferred placeholder.
- `pyproject.toml` retains `license = { text = "OWNER_DEFERRED" }`.
- No public licence grant has been introduced.

## Gate F — HF custody register

- `HF_CUSTODY_REGISTER.md` present.
- Row HF-01 verified 2026-04-24 against production HF token: repo
  `Zer0pa/glyph-engine-artefacts`, private dataset, SHA
  `58cbc2e6cb1f3c72b6e5ec88dad9637028467657`, 9 siblings. The Phase 02c
  mirror push will append a new SHA row.

## Overall

All six closeout gates PASSED. The package `gnosis-glyph-engine` is
independently installable without `gnosis-morph-bench`; the cross-repo
contract is verified when `gnosis-morph-bench` is present; the OSS
ceiling is bounded by a multi-seed run; public paths are parameterised;
private-licence posture is explicit; HF custody is registered and
verified.

Authority metric `package_boundary_earned` remains `UNTESTED`: gates 1,
2, 3 stay PASSED; gate 4 stays BLOCKED on D-06. The adapter-only
recommendation is NOT adopted at this time per D-02c-02.
