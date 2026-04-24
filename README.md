# Gnosis Glyph Engine

> Internal extraction-target scaffold for glyph geometry, stroke, and descriptor
> kernels. Not a public library yet.

## What This Repo Is

`gnosis-glyph-engine` is a migration scaffold for auditing reusable
image-to-geometry and glyph-descriptor code currently spread across Indus and
cuneiform source families. Its job is to decide whether a real package boundary
exists. It does not yet prove a reusable library, performance superiority, or a
commercial product.

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
| License | `OWNER_DEFERRED` |
| Primary contact | owner-controlled private coordination path |

## Phase Progress

| Phase | Status |
|---|---|
| 00 Hold-Surface Bootstrap | Complete (2026-04-23) |
| 01 Consumer And Interface Freeze | Complete (2026-04-24) |
| 02a Borrowed-Baseline Sanity Path | **Complete (2026-04-24)** |
| 02b Owned-Arm Ablation | Blocked on D-06 |
| 03 Package-Boundary Review | Pending |

## What Phase 02a Proved

- The frozen Phase 01 interface is implementable using only borrowed OSS
  (OpenCV, scikit-image, scikit-learn, numpy).
- The scaffold installs with `pip install -e .[dev]` on a clean Python 3.13
  environment and imports nothing from the live monorepo.
- A 16-test pytest suite passes, covering fixture determinism, baseline
  protocol compliance, and morph-bench JSON roundtrip.
- `gnosis_morph_bench` consumes the produced `BenchmarkManifest` JSON
  unmodified and produces finite `sigma`, `null_mean`, `null_std`,
  `silhouette`, and `mean_jaccard` per arm.
- The full ablation is captured in
  `artifacts/ablation/ablation_report.json` and mirrored to the HF dataset.

## What Phase 02a Could Not Prove

- Whether any *owned* descriptor beats the borrowed baselines. Phase 02b is
  blocked on D-06 (two Indus source files not present in the portfolio
  snapshot).
- Whether the 12-glyph synthetic fixture is hard enough. `baseline_orb`
  achieves NMI = 1.0 and `mean_jaccard` = 1.0 on it; the D-04 pass rule
  therefore needs near-perfect owned-arm behaviour to succeed. Phase 03
  decides whether to tighten the fixture.

## Read Next

| Need | File |
|---|---|
| **Review team entry point (interim status)** | `AGENT_STATUS_REPORT_2026-04-24.md` |
| Auditor fast path + reproduce block | `AUDITOR_PLAYBOOK.md` |
| Sovereign hold/extraction brief | `SOVEREIGN_PRD.md` |
| Candidate source families + extraction ledger | `SOURCE_BOUNDARY.md` |
| Phase 01 frozen decisions | `.gpd/phases/01-consumer-and-interface-freeze/01-DECISIONS.md` |
| Phase 02a verification + metrics | `.gpd/phases/02-minimal-extraction-smoke/02-01-VERIFICATION.md` |
| Ablation report (machine-readable) | `artifacts/ablation/ablation_report.json` |
| Data and rights posture | `DATA_POLICY.md` |
| Architecture truth map | `docs/ARCHITECTURE.md` |
| Current gaps | `TODO.md` |
| GPD state | `.gpd/PROJECT.md`, `.gpd/STATE.md` |

## Current Gaps

- Owned-arm source files absent from portfolio snapshot (D-06).
- Phase 03 has not yet decided whether to widen the 12-glyph fixture
  (D-02a-06 saturation risk).
- Final license and public contact fields remain owner-deferred.
