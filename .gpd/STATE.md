# Research State

## Current Position

Current phase: `02b`
Current phase name: Owned-Arm Ablation
Status: `BLOCKED_ON_D-06`
Last activity: 2026-04-24

Progress: 65%

Phase 02a (Borrowed-Baseline Sanity Path) complete 2026-04-24 with gate
PASS. Phase 02b (Owned-Arm Ablation) remains blocked on the Phase 01 D-06
source-retrieval blocker.

## Active Work

- Owner action required: retrieve
  `scripts/indus/stroke_native_encoding.py` and
  `scripts/indus/phase3_common.py` from the live monorepo, OR grant the
  RunPod workspace access to a live-monorepo clone.
- Once D-06 clears, run owned-arm ablation on the frozen 12-glyph fixture
  and feed results through the existing `run_ablation.py` flow.

## Open Questions

- Does the 12-glyph fixture need hardening before Phase 02b? Baseline
  saturation (ORB achieves NMI=1.0, mean_jaccard=1.0) implies any owned
  arm must match near-perfect behaviour to clear D-04. Phase 03 decides:
  accept the tight threshold, or open a new phase to widen the fixture
  with harder distractors.
- Are there admitted consumers beyond morph-bench that would change the
  interface contract if Phase 02b fails? (Deferred to Phase 03.)

## Blockers

- `D-06`: owned-arm source files absent from portfolio snapshot.
- `D-02a-06`: fixture-saturation risk — two of the four D-04 sub-checks
  are already near the ceiling.
- No public promotion until `package_boundary_earned` passes Phase 03.

## Artefact Inventory

- Code: `src/gnosis_glyph_engine/`, `tests/`, `scripts/run_ablation.py`,
  `pyproject.toml` — all committed to GitHub.
- Phase 01 freeze artefacts: `.gpd/phases/01-consumer-and-interface-freeze/`.
- Phase 02a execution artefacts: `.gpd/phases/02-minimal-extraction-smoke/`
  + `artifacts/ablation/` (mirrored to HF dataset
  `Zer0pa/glyph-engine-artefacts`).

## Resume

Resume at Phase 02b plan authoring after D-06 clears. Or open
`/gpd:insert-phase` "02.1 Fixture Hardening" if baseline saturation is
judged unacceptable. Reference artefacts:

- `.gpd/phases/02-minimal-extraction-smoke/02-01-SUMMARY.md`
- `.gpd/phases/02-minimal-extraction-smoke/02-01-VERIFICATION.md`
- `artifacts/ablation/ablation_report.json`
