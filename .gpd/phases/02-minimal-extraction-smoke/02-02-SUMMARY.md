# Phase 02c Summary — OSS Robustness + Closeout

Date: 2026-04-24
Status: `COMPLETE`
Gate: `PASS`
Context: closeout run for lane `Glyph-Engine` per the Zer0pa closeout
brief dated 2026-04-24.

## What Was Done

- **Dependency/test boundary fix (P1 from brief).** The cross-repo
  contract test `test_morph_bench_loader_accepts_manifest` now skips
  cleanly when `gnosis_morph_bench` is not installed. A local schema
  contract test `test_manifest_matches_local_schema_contract` was added
  so invariants remain exercised. `pyproject.toml` clarifies that
  `gnosis-morph-bench` is supplied by the execution host, not declared
  as a hard dependency. Verified: 17 pass WITH morph-bench, 16 pass + 1
  skipped WITHOUT.
- **Multi-seed OSS robustness.** New script
  `gnosis_glyph_engine.scripts.run_robustness` (console entry
  `glyph-engine-robustness`) runs the three frozen borrowed-baseline
  arms across 10 seeds on the synthetic fixture. Result: `baseline_orb`
  does **not** robustly saturate — the Phase 02a seed=42 saturation
  was a non-representative observation. Mean σ ≈ 4.14 (stdev 1.12).
- **Sovereign-vs-adapter scope decision.** Under D-02c-02, the Glyph-Engine
  repo stays sovereign. Adapter-only collapse is **rollback-triggered**
  only if Phase 02b owned arms fail to beat the multi-seed ORB ceiling.
- **Retired D-02a-06.** The baseline-saturation Phase-03 risk is retired
  by the multi-seed evidence.
- **Public-facing path scrub.** All operational paths (RunPod host, pod
  id, local portfolio paths, SSH keys, HF cache paths) parameterised to
  symbolic labels per `docs/PROVENANCE_LABELS.md`. Scientific provenance
  preserved; operational fingerprinting removed.
- **Private licence notice.** `PRIVATE_INTERNAL_LICENSE_NOTICE.md` added.
  No public licence grant.
- **HF custody register.** `HF_CUSTODY_REGISTER.md` added with live
  API-verified rows for `Zer0pa/glyph-engine-artefacts`. Spelling policy
  noted: this lane uses `artefact`, some sibling lanes use `artifact`;
  not a consolidation target for this lane.

## Artefacts Produced

- `artifacts/robustness/robustness_report.json` — multi-seed OSS
  robustness report.
- `.gpd/phases/02-minimal-extraction-smoke/02-02-{DECISIONS,VERIFICATION,SUMMARY}.md`.
- `PRIVATE_INTERNAL_LICENSE_NOTICE.md`.
- `HF_CUSTODY_REGISTER.md`.
- `docs/PROVENANCE_LABELS.md`.
- `src/gnosis_glyph_engine/scripts/run_robustness.py`.
- Updated: `tests/test_manifest_builder.py`, `pyproject.toml`,
  and every previously path-leaking surface listed in the scrub.

## Closeout Brief Coverage (Lane A / `Glyph-Engine`)

| Closeout ask | Status | Evidence |
|---|---|---|
| Fix Morph-Bench dependency/test boundary | PASS | `pyproject.toml`, `tests/test_manifest_builder.py`, Gate B of `02-02-VERIFICATION.md` |
| Smallest fair OSS-baseline comparison | PASS | `artifacts/robustness/robustness_report.json`, Gate C |
| Sovereign-vs-adapter scope recommendation | PASS (sovereign preserved; adapter trigger defined) | D-02c-02 |
| Keep private/internal | PASS | `PRIVATE_INTERNAL_LICENSE_NOTICE.md`, GitHub visibility `INTERNAL`, HF dataset `private` |
| No public licence added | PASS | Gate E |
| No negative evidence deleted | PASS | `baseline_hog` stays in the ablation set per D-02c-04 |
| Public paths scrubbed via parameterisation | PASS | Gate D, `docs/PROVENANCE_LABELS.md` |
| Prefer OSS for commodity CV | PASS | all three baselines are OSS; no reimplementation |
| Verification run before reporting done | PASS | Gates A, B, C, D, E, F |

## Authority Metric

`package_boundary_earned`:

| Gate | Status |
|---|---|
| 1. Admitted consumer | PASSED (Phase 01) |
| 2. Monorepo-free execution | PASSED (Phase 02a) |
| 3. Tiny smoke from repo custody | PASSED (Phase 02a) |
| 4. Owned layer beats borrowed | **UNTESTED / BLOCKED on D-06** |

Overall: **`UNTESTED`** (unchanged).

## Remaining Blockers

- **D-06** (unchanged owner action): retrieve
  `scripts/indus/stroke_native_encoding.py` and
  `scripts/indus/phase3_common.py`, or grant pod access to a live-monorepo
  clone.

## Resume Point

Phase 02b (Owned-Arm Ablation) begins the moment D-06 clears. Phase 02c
retires the fixture-hardening detour; Phase 02b runs the owned arms
against the multi-seed ORB ceiling directly.
