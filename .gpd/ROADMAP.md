# Roadmap: gnosis-glyph-engine

## Phases

- [x] **Phase 00: Hold-Surface Bootstrap** - Replace generic starter state
      with extraction-target truth. Completed 2026-04-23.
- [x] **Phase 01: Consumer And Interface Freeze** - Name the first consumer,
      interface, fixture, and baseline ablation. Completed 2026-04-24.
- [ ] **Phase 02: Minimal Extraction Smoke** - Copy the smallest source slice
      and prove it runs outside the live monorepo. Blocked on D-06.
- [ ] **Phase 03: Package-Boundary Review** - Decide whether the package
      boundary is earned or the source remains embedded in consumers.

## Current Gate

Phase 02 runs the full five-arm ablation (or the three borrowed-baseline arms
if D-06 is still open) and writes a verdict JSON. It passes only if:

1. every arm runs from repo custody with no live-monorepo imports,
2. the morph-bench evaluator consumes the produced `BenchmarkManifest`
   without modification, and
3. the ablation report names a best arm and reports `sigma`, `null_mean`,
   `null_std`, `mean_jaccard` for every arm.

Phase 03 then applies the numeric pass rule from Phase 01 D-04 to declare
`package_boundary_earned` `PASSED` or `FAILED`.

## Stop Conditions

- no consumer needs the boundary,
- borrowed baselines match or beat the proposed descriptor layer,
- extraction requires copying domain science from another lane,
- the scaffold starts implying public-package readiness before smoke evidence.

## Progress

| Phase | Status | Completed |
|---|---|---|
| 00. Hold-Surface Bootstrap | Complete | 2026-04-23 |
| 01. Consumer And Interface Freeze | Complete | 2026-04-24 |
| 02. Minimal Extraction Smoke | Blocked on D-06 | - |
| 03. Package-Boundary Review | Pending | - |
