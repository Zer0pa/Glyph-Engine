# Research State

## Current Position

Current phase: `02b`
Current phase name: Owned-Arm Ablation
Status: `BLOCKED_ON_D-06`
Last activity: 2026-04-24

Progress: 75%

Phases complete:

- Phase 00 Hold-Surface Bootstrap — 2026-04-23, PASS.
- Phase 01 Consumer And Interface Freeze — 2026-04-24, PASS.
- Phase 02a Borrowed-Baseline Sanity Path — 2026-04-24, PASS.
- Phase 02c OSS-Baseline Robustness + Closeout — 2026-04-24, PASS.

Phase 02b (Owned-Arm Ablation) remains blocked on D-06.

## Active Work

- Owner action required: retrieve
  `scripts/indus/stroke_native_encoding.py` and
  `scripts/indus/phase3_common.py`, or grant pod access at
  `<RUNPOD_HOST>` to a live-monorepo clone.
- Once D-06 clears, run owned-arm ablation against the multi-seed
  borrowed-baseline ceiling (Phase 02c robustness report).

## Open Questions

- (retired) Does the 12-glyph fixture need hardening before Phase 02b?
  Answer: No. Phase 02c multi-seed evidence retired the Phase 02a
  saturation concern. The existing fixture is discriminating across
  seeds and the D-04 pass rule is plausible.
- Does Phase 02b owned-arm evidence clear the plausible but non-trivial
  ORB ceiling (mean σ ≈ 4.14, NMI ≈ 0.77, mean_jaccard ≈ 0.90)?
- Does any sibling lane (Morph-Bench, Indus, Cuneiform) surface a
  second admitted consumer that would reshape the interface contract?

## Blockers

- `D-06`: owned-arm source files absent from portfolio snapshot.
- No public promotion until `package_boundary_earned` passes Phase 03 and
  operator/orchestrator release approval is explicit.
- (retired) `D-02a-06` baseline-saturation Phase-03 risk — retired by
  D-02c-01.

## Closeout Brief (2026-04-24) Compliance

| Brief item | Status |
|---|---|
| Fix Morph-Bench dependency/test boundary | DONE (Phase 02c, D-02c-05) |
| Smallest fair OSS-baseline comparison | DONE (Phase 02c robustness) |
| Sovereign-vs-adapter scope decision | DONE (D-02c-02: stay sovereign; adapter-only trigger defined) |
| Scrub public-facing paths via parameterisation | DONE (docs/PROVENANCE_LABELS.md) |
| Keep private/internal until operator changes visibility | IN FORCE |
| Apache/CC licence posture present without public-readiness implication | IN FORCE (`LICENSE`, `NOTICE`; `PRIVATE_INTERNAL_LICENSE_NOTICE.md` retired in Wave 2) |
| No negative evidence deleted | HONOURED (baseline_hog kept despite weakness) |
| HF custody register verified | DONE (HF_CUSTODY_REGISTER.md) |
| Verification run before reporting done | DONE (Phase 02c Gates A–F) |

## Artefact Inventory

- Code: `src/gnosis_glyph_engine/`, `tests/`, `scripts/`, `pyproject.toml`
  — committed to GitHub.
- Phase 01 freeze: `.gpd/phases/01-consumer-and-interface-freeze/`.
- Phase 02a execution: `.gpd/phases/02-minimal-extraction-smoke/02-01-*`
  + `artifacts/ablation/`.
- Phase 02c closeout: `.gpd/phases/02-minimal-extraction-smoke/02-02-*`
  + `artifacts/robustness/`.
- Closeout surfaces: `NOTICE.md` (canonical, Wave 2),
  `HF_CUSTODY_REGISTER.md`, `docs/PROVENANCE_LABELS.md`.
- Operational hygiene: Ops-Gates-derived coupling audit
  `tools/gnosis_ops_gates/coupling_audit.py` wired into CI.
- HF custody: `Architect-Prime/glyph-engine-artefacts` (private dataset,
  sha `301b0756…` as of 2026-04-27 owner-directed migration off Zer0pa
  org HF storage). Zer0pa namespace verified empty for this lane.
  See `HF_CUSTODY_REGISTER.md`.

## Resume

Resume at Phase 02b PLAN authoring after D-06 clears. Reference
artefacts:

- `.gpd/phases/02-minimal-extraction-smoke/02-02-SUMMARY.md`
- `.gpd/phases/02-minimal-extraction-smoke/02-02-VERIFICATION.md`
- `artifacts/robustness/robustness_report.json`
- `HF_CUSTODY_REGISTER.md`
