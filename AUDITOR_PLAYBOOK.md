# Auditor Playbook

## Goal

Verify that this scaffold is not overclaiming a glyph-engine package.

## Fast Path

1. Read the authority block in `README.md`.
2. Read `SOVEREIGN_PRD.md`.
3. Read `SOURCE_BOUNDARY.md`.
4. Confirm `code/README.md` says no code is extracted.
5. Check `.gpd/STATE.md` for the current phase.

## Claim Replay Map

| Claim | Evidence path | Verifiable? | Caveat |
|---|---|---|---|
| Candidate source families are identified | `SOURCE_BOUNDARY.md` | yes | source code remains in parent repo |
| No public package boundary is proven | `SOVEREIGN_PRD.md`, `code/README.md` | yes | future work may change this |
| Public promotion is blocked | `README.md`, `RELEASING.md` | yes | license and evidence gates open |

## Fail Conditions

- README claims an installable package.
- Docs claim descriptor superiority.
- Domain results from Indus or cuneiform are presented as glyph-engine proof.
