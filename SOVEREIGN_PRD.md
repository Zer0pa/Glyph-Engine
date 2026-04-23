# Sovereign PRD: Gnosis Glyph Engine Extraction Target

Date: 2026-04-23
Last updated: 2026-04-24 (Phase 01 freeze recorded)
Status: `HOLD_EXTRACTION_ONLY`
Class: `INTERNAL_EXTRACTION_TARGET`

## Sovereign Objective

Determine whether the reusable glyph geometry, stroke, descriptor, and
transport helpers in the source repo deserve a real package boundary. Until a
consumer or ablation proves that boundary, this scaffold is a hold surface, not
a public repo candidate.

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
| 02 Minimal Extraction Smoke | Blocked on D-06 | `.gpd/STATE.md` |
| 03 Package-Boundary Review | Pending | - |

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
- future smoke path design

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
