# Research State

## Current Position

Current phase: `02`
Current phase name: Minimal Extraction Smoke
Status: `BLOCKED_ON_OWNED_ARM_SOURCE_RETRIEVAL`
Last activity: 2026-04-24

Progress: 40%

## Active Work

- Resolve Phase 01 decision D-06: retrieve `scripts/indus/stroke_native_encoding.py`
  and `scripts/indus/phase3_common.py` from the live monorepo (or grant
  access to a live-monorepo clone on the RunPod host).
- Provision RunPod workspace for Phase 02 execution.
- Begin extraction only after D-06 is resolved and the path-rewrite ledger is
  recorded in `SOURCE_BOUNDARY.md`.

## Open Questions

- Who retrieves the two owned-arm source files, and via which path?
- Does `cv2.ORB_create` run headless on the RunPod host under
  `opencv-python-headless`? (expected yes; confirm at Phase 02 kickoff).
- Is the 12-item fixture large enough for a stable `mean_jaccard`? (trial
  during Phase 02; expand to 24 items if variance is excessive).

## Blockers

- `D-06`: owned-arm source files not present in portfolio snapshot.
- No code extraction until `D-06` clears and the ledger is updated.
- No package claim until a monorepo-free smoke path passes Phase 02.
- No public promotion until `package_boundary_earned` passes Phase 03.

## Resume

Resume at Phase 02 PLAN authoring after D-06 clears. Reference artefacts:

- `.gpd/phases/01-consumer-and-interface-freeze/01-RESEARCH.md`
- `.gpd/phases/01-consumer-and-interface-freeze/01-DECISIONS.md`
- `.gpd/phases/01-consumer-and-interface-freeze/01-SUMMARY.md`
- `.gpd/phases/01-consumer-and-interface-freeze/01-VERIFICATION.md`
