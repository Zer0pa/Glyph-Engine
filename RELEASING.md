# Releasing

No package release, public release, or visibility flip is authorized from this
lane today.

## Current State

| Surface | Status |
|---|---|
| Code package | present: `gnosis-glyph-engine==0.1.0a1` |
| Install path | present: `pip install -e .[dev]` |
| Smoke path | present: `pytest -q` with Morph-Bench optional-contract skip |
| Borrowed-baseline evidence | present: Phase 02a + Phase 02c artefacts |
| Ops-Gates hygiene | present: pinned coupling audit in CI |
| Owned-arm ablation | `BLOCKED_ON_D-06` |
| Package-boundary review | pending Phase 02b evidence |

## Release Blockers

- `package_boundary_earned` remains `UNTESTED`.
- D-06 source retrieval has not happened.
- Phase 02b owned-arm ablation has not run.
- Phase 03 has not declared `PASSED`, `FAILED`, or `INCONCLUSIVE`.
- No rights-cleared real-glyph fixture exists.
- The repo must not claim descriptor superiority, cross-corpus
  generalisation, public-package readiness, or product readiness.

Apache-2.0 code licensing and CC-BY-4.0 documentation licensing are present.
They do not by themselves authorize package-boundary promotion, tagged release,
or public-readiness language.

Any future release plan must preserve the locked `Commercial Readiness`
verdict vocabulary and update `SOVEREIGN_PRD.md`, `.gpd/STATE.md`, and
`AUDITOR_PLAYBOOK.md` in the same wave.
