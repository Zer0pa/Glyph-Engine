# Project: gnosis-glyph-engine

## What This Is

`gnosis-glyph-engine` is an internal extraction target for reusable glyph
geometry, descriptor, and transport helpers. It is not yet an installable
package or public library.

## Core Question

Is a standalone glyph-engine package boundary earned by a real consumer,
monorepo-free smoke path, and descriptor ablation against borrowed baselines?

## Authority Metric

`package_boundary_earned`

Passes only when all are true:

1. one admitted consumer requires the extracted interface,
2. the extracted code runs without live-monorepo imports or hardcoded paths,
3. a tiny smoke path passes from repo custody,
4. an ablation shows owned descriptors matter versus OpenCV, scikit-image,
   scikit-learn, Faiss, or baseline embeddings.

Current verdict: `UNTESTED`.

Phase 01 froze the consumer, interface, fixture, and ablation rule. Phase 02
must run them, Phase 03 applies the pass rule.

## Scope

In scope:

- source-family inventory for reusable glyph kernels
- `Descriptor` / `LearnedDescriptor` protocol + `manifest_builder` interface
- build-vs-borrow ablation against OpenCV / scikit-image / scikit-learn
- tiny fixture and ablation execution plan

Out of scope:

- public library promotion
- Indus, cuneiform, or benchmark-method claims
- HTR/OCR, vector database, viewer, annotation UI, or workflow-manager builds
- generic image-descriptor framework branding

## Anchor Registry

| Anchor ID | Locator | Role |
|---|---|---|
| `ref-prd` | `SOVEREIGN_PRD.md` | extraction-target contract |
| `ref-source-boundary` | `SOURCE_BOUNDARY.md` | candidate and excluded sources, destination paths, owned-arm blocker |
| `ref-data-policy` | `DATA_POLICY.md` | no-data and fixture posture |
| `ref-build-borrow` | `_control/research/BUILD_VS_BORROW_CANON.md` | borrow-first constraint |
| `ref-consumer` | `workstreams/gnosis-morph-bench/05_repo_scaffold/src/gnosis_morph_bench/schema.py` | frozen consumer interface |
| `ref-phase-01-decisions` | `.gpd/phases/01-consumer-and-interface-freeze/01-DECISIONS.md` | frozen Phase 01 outputs |

## False Progress To Reject

- adding a `pyproject.toml` before code is extracted,
- copying broad domain logic from Indus or cuneiform,
- claiming cross-domain generality without ablation,
- building commodity layers already solved by OSS.

## Current Position

Phase 00 and Phase 01 complete. Phase 02 begins once D-06 clears and the
RunPod workspace is provisioned.
