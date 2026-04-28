# Sovereign PRD: Gnosis Glyph Engine Extraction Target

Date: 2026-04-23
Last updated: 2026-04-28 (Phase 02c evidence and Ops-Gates adoption recorded)
Status: `BLOCKED_ON_D-06`
Class: `INTERNAL_EXTRACTION_TARGET`

## Sovereign Objective

Determine whether the reusable glyph geometry, stroke, descriptor, and
transport helpers in the source repo deserve a real package boundary. Until
D-06, Phase 02b owned-arm evidence, and Phase 03 package-boundary review close,
this repo is an extraction/review surface, not a public package candidate.

## Authority Metric

`package_boundary_earned`

Passes only when all are true:

1. at least one admitted consumer requires the extracted interface,
2. extracted code runs without live-monorepo imports or hardcoded paths,
3. a tiny smoke path passes from repo custody,
4. an ablation or benchmark shows why the owned descriptor layer matters versus
   borrowed OpenCV/skimage/scikit-learn baselines.

Current verdict: `UNTESTED`.

## Phase Progress

| Phase | Status | Evidence |
|---|---|---|
| 00 Hold-Surface Bootstrap | Complete (2026-04-23) | `.gpd/phases/00-workstream-bootstrap/` |
| 01 Consumer And Interface Freeze | Complete (2026-04-24) | `.gpd/phases/01-consumer-and-interface-freeze/` |
| 02a Borrowed-Baseline Sanity Path | Complete (2026-04-24) | `artifacts/ablation/`, `.gpd/phases/02-minimal-extraction-smoke/02-01-*` |
| 02c OSS-Baseline Robustness + Closeout | Complete (2026-04-24) | `artifacts/robustness/`, `.gpd/phases/02-minimal-extraction-smoke/02-02-*` |
| 02b Owned-Arm Ablation | Blocked on D-06 | `.gpd/STATE.md`, `SOURCE_BOUNDARY.md` |
| 03 Package-Boundary Review | Pending Phase 02b evidence | - |

Frozen by Phase 01:

- first admitted consumer: `gnosis-morph-bench`,
- minimum interface: `Descriptor` / `LearnedDescriptor` + `manifest_builder`,
- smoke fixture: 12-glyph synthetic generator, 3 families × 4 variants,
- ablation rule: 5 arms (3 borrowed baselines + 2 owned candidates) with a
  numeric pass threshold against morph-bench `sigma` and `mean_jaccard`.

## In Scope

- source-family inventory for glyph geometry and descriptor candidates
- boundary design for future `gnosis_glyph_engine` package
- explicit build-vs-borrow decisions
- repo-local smoke, ablation, robustness, and operational-hygiene evidence

## Out Of Scope

- public library promotion
- Indus or cuneiform scientific claims
- generic image-descriptor framework branding
- HTR/OCR, vector database, viewer, or annotation UI construction
- performance claims without repo-local benchmark evidence

## Build Vs Borrow

Borrow OpenCV, scikit-image, NumPy, SciPy, scikit-learn, Faiss where needed, and
baseline embeddings. Own only the domain-specific descriptor contract if it
survives extraction and ablation.

## Stop Conditions

- extraction requires copying broad domain logic from Indus or cuneiform,
- no consumer needs the boundary,
- public baselines match or beat the proposed owned descriptors,
- the repo starts narrating generality before replay evidence exists.
