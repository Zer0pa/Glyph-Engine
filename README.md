# Gnosis Glyph Engine

> Internal extraction-target scaffold for glyph geometry, stroke, and descriptor
> kernels. Not a public library yet.

## What This Repo Is

`gnosis-glyph-engine` is a migration scaffold for auditing reusable
image-to-geometry and glyph-descriptor code currently spread across Indus
and cuneiform source families. Its job is to decide whether a real package
boundary exists. It does not yet prove a reusable library, performance
superiority, or a commercial product.

## Current Authority

| Item | Current Truth |
|---|---|
| Product lane | `INTERNAL_EXTRACTION_TARGET` |
| Code remote | `Zer0pa/Glyph-Engine` (private GitHub) |
| Default branch | `main` |
| Artefact failover | `Zer0pa/glyph-engine-artefacts` (Hugging Face, private) |
| Acquisition surface | internal only |
| Current authority artifact | `SOVEREIGN_PRD.md` + `.gpd/phases/*/` |
| Authority metric | `package_boundary_earned` |
| Metric verdict | `UNTESTED` (gates 1–3 PASSED, gate 4 blocked on D-06) |
| Active phase | Phase 02b (BLOCKED on owned-arm source retrieval, D-06) |
| License | `PRIVATE_INTERNAL_ONLY` — see `PRIVATE_INTERNAL_LICENSE_NOTICE.md` |
| Primary contact | owner-controlled private coordination path |

## Phase Progress

| Phase | Status |
|---|---|
| 00 Hold-Surface Bootstrap | Complete (2026-04-23) |
| 01 Consumer And Interface Freeze | Complete (2026-04-24) |
| 02a Borrowed-Baseline Sanity Path | Complete (2026-04-24) |
| 02c OSS-Baseline Robustness + Closeout | **Complete (2026-04-24)** |
| 02b Owned-Arm Ablation | Blocked on D-06 |
| 03 Package-Boundary Review | Pending |

## What Phase 02a+02c Proved

- The frozen Phase 01 interface is implementable using only borrowed OSS
  (OpenCV, scikit-image, scikit-learn, NumPy).
- The scaffold installs with `pip install -e .[dev]` on a clean Python 3.13
  environment, imports nothing from the live monorepo, and is independently
  testable **without** `gnosis-morph-bench`.
- 17-test pytest suite passes when `gnosis-morph-bench` is installed; 16
  passed + 1 skipped in a clean venv without it.
- Borrowed-baseline ceiling across 10 seeds:

  | Arm | σ mean ± stdev | NMI mean | mean_jaccard mean |
  |---|---|---:|---:|
  | baseline_orb | 4.14 ± 1.12 | 0.765 | 0.899 |
  | baseline_hu_regionprops | 2.95 ± 1.06 | 0.575 | 0.943 |
  | baseline_hog | 1.15 ± 1.17 | 0.362 | 0.435 |

## What Phase 02a+02c Could Not Prove

- Whether any *owned* descriptor beats the borrowed baselines. Phase 02b
  is blocked on D-06 (two Indus source files not present in the portfolio
  snapshot).
- Cross-corpus generalisation. The fixture is synthetic; a rights-cleared
  real-glyph fixture appears only after owner action on D-06.

## Prior Framing Corrected

An earlier single-seed (seed=42) reading suggested `baseline_orb` saturated
the fixture and that Phase 03 would need to widen the fixture before
running Phase 02b. **That framing has been retired by Phase 02c.** The
multi-seed evidence shows `baseline_orb` does not robustly saturate;
Phase 02b can proceed directly against the 10-seed ceiling when D-06
clears. See `.gpd/phases/02-minimal-extraction-smoke/02-02-DECISIONS.md`
(D-02c-01, D-02c-02, D-02c-03).

## Read Next

| Need | File |
|---|---|
| Review team entry point (interim status) | `AGENT_STATUS_REPORT_2026-04-24.md` |
| Auditor fast path + reproduce block | `AUDITOR_PLAYBOOK.md` |
| Rights posture | `PRIVATE_INTERNAL_LICENSE_NOTICE.md` |
| HF custody truth | `HF_CUSTODY_REGISTER.md` |
| Public-path label convention | `docs/PROVENANCE_LABELS.md` |
| Sovereign hold/extraction brief | `SOVEREIGN_PRD.md` |
| Candidate source families + extraction ledger | `SOURCE_BOUNDARY.md` |
| Phase 01 frozen decisions | `.gpd/phases/01-consumer-and-interface-freeze/01-DECISIONS.md` |
| Phase 02a verification (seed=42) | `.gpd/phases/02-minimal-extraction-smoke/02-01-VERIFICATION.md` |
| Phase 02c verification (multi-seed + closeout) | `.gpd/phases/02-minimal-extraction-smoke/02-02-VERIFICATION.md` |
| Phase 02c scope decision | `.gpd/phases/02-minimal-extraction-smoke/02-02-DECISIONS.md` |
| Ablation report (machine-readable) | `artifacts/ablation/ablation_report.json` |
| Robustness report (machine-readable) | `artifacts/robustness/robustness_report.json` |
| Data and rights posture | `DATA_POLICY.md` |
| Architecture truth map | `docs/ARCHITECTURE.md` |
| Current gaps | `TODO.md` |
| GPD state | `.gpd/PROJECT.md`, `.gpd/STATE.md` |

## Current Gaps

- Owned-arm source files absent from portfolio snapshot (D-06).
- Final license and public contact fields remain owner-deferred (see
  `PRIVATE_INTERNAL_LICENSE_NOTICE.md`).
- No GitHub Actions CI yet. Brief's guidance: add minimal CI only after
  P1 fixes; with P1 done on this lane, CI can be added as a follow-up.
