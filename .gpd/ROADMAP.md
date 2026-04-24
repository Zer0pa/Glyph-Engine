# Roadmap: gnosis-glyph-engine

## Phases

- [x] **Phase 00: Hold-Surface Bootstrap** - Replace generic starter state
      with extraction-target truth. Completed 2026-04-23.
- [x] **Phase 01: Consumer And Interface Freeze** - Name the first consumer,
      interface, fixture, and baseline ablation. Completed 2026-04-24.
- [x] **Phase 02a: Borrowed-Baseline Sanity Path** - Monorepo-free install,
      16-test pytest pass, three-arm borrowed ablation. Completed 2026-04-24.
- [ ] **Phase 02b: Owned-Arm Ablation** - Add `owned_stroke_compass` and
      `owned_topology` to the ablation. Blocked on D-06.
- [ ] **Phase 03: Package-Boundary Review** - Apply D-04 numeric pass rule,
      decide `package_boundary_earned` PASSED/FAILED/INCONCLUSIVE.

## Current Gate

Phase 02b is blocked on D-06 (owner retrieval of two live-monorepo source
files). Phase 03 is blocked on Phase 02b evidence.

## Stop Conditions

- no consumer needs the boundary,
- borrowed baselines match or beat the proposed descriptor layer
  (Phase 02a already shows `baseline_orb` at NMI=1.0 — risk to gate 4),
- extraction requires copying domain science from another lane,
- the scaffold starts implying public-package readiness before Phase 03
  declares the verdict.

## Progress

| Phase | Status | Completed |
|---|---|---|
| 00. Hold-Surface Bootstrap | Complete | 2026-04-23 |
| 01. Consumer And Interface Freeze | Complete | 2026-04-24 |
| 02a. Borrowed-Baseline Sanity Path | Complete | 2026-04-24 |
| 02b. Owned-Arm Ablation | Blocked on D-06 | - |
| 03. Package-Boundary Review | Pending | - |

## Measured Outputs So Far

| Arm (Phase 02a) | sigma | nmi | mean_jaccard |
|---|---:|---:|---:|
| baseline_orb | 6.40 | 1.000 | 1.000 |
| baseline_hog | 3.77 | 0.568 | 0.400 |
| baseline_hu_regionprops | 3.40 | 0.496 | 0.833 |
