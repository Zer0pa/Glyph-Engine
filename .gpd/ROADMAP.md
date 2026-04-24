# Roadmap: gnosis-glyph-engine

## Phases

- [x] **Phase 00: Hold-Surface Bootstrap** — Completed 2026-04-23.
- [x] **Phase 01: Consumer And Interface Freeze** — Completed 2026-04-24.
- [x] **Phase 02a: Borrowed-Baseline Sanity Path** — Completed
      2026-04-24 (single-seed, seed=42).
- [x] **Phase 02c: OSS-Baseline Robustness + Closeout** — Completed
      2026-04-24 (10 seeds; retires D-02a-06; closeout-brief lane-A
      compliance).
- [ ] **Phase 02b: Owned-Arm Ablation** — Blocked on D-06.
- [ ] **Phase 03: Package-Boundary Review** — Blocked on Phase 02b
      evidence.

## Current Gate

Phase 02b is blocked on D-06 (owner retrieval of two live-monorepo
source files). Phase 03 is blocked on Phase 02b evidence.

## Stop Conditions

- no consumer needs the boundary,
- owned arms in Phase 02b fail to beat multi-seed ORB ceiling
  (mean σ ≈ 4.14) by ≥ 0.5 σ — adapter-only scope reinstated per
  D-02c-02,
- extraction requires copying domain science from another lane,
- the scaffold starts implying public-package readiness before
  Phase 03 declares PASS.

## Progress

| Phase | Status | Completed |
|---|---|---|
| 00. Hold-Surface Bootstrap | Complete | 2026-04-23 |
| 01. Consumer And Interface Freeze | Complete | 2026-04-24 |
| 02a. Borrowed-Baseline Sanity Path | Complete | 2026-04-24 |
| 02c. OSS-Baseline Robustness + Closeout | Complete | 2026-04-24 |
| 02b. Owned-Arm Ablation | Blocked on D-06 | - |
| 03. Package-Boundary Review | Pending | - |

## Measured Outputs So Far

Phase 02a (seed=42):

| Arm | σ | NMI | mean_jaccard |
|---|---:|---:|---:|
| baseline_orb | 6.40 | 1.000 | 1.000 |
| baseline_hog | 3.77 | 0.568 | 0.400 |
| baseline_hu_regionprops | 3.40 | 0.496 | 0.833 |

Phase 02c (mean over seeds 0..9):

| Arm | σ mean ± stdev | NMI mean | mean_jaccard mean |
|---|---|---:|---:|
| baseline_orb | 4.14 ± 1.12 | 0.765 | 0.899 |
| baseline_hu_regionprops | 2.95 ± 1.06 | 0.575 | 0.943 |
| baseline_hog | 1.15 ± 1.17 | 0.362 | 0.435 |

Phase 02b will use the multi-seed mean as the baseline ceiling against
which owned arms are judged by the D-04 rule.
