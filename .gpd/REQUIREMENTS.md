# Requirements: gnosis-glyph-engine

Defined: 2026-04-23
Last updated: 2026-04-24

## Primary Requirements

- [x] **DATA-01**: Establish the scaffold as a hold/extraction target, not a
      package claim. *(Phase 00, 2026-04-23)*
- [x] **DATA-02**: Freeze the first real consumer that needs a glyph-engine
      interface. *(Phase 01 D-01, `gnosis-morph-bench`, 2026-04-24)*
- [x] **DERV-01**: Define the smallest descriptor or geometry interface worth
      extracting. *(Phase 01 D-02, 2026-04-24)*
- [x] **DERV-02**: Define the ablation against borrowed public baselines.
      *(Phase 01 D-04, 2026-04-24)*
- [x] **SIMU-01**: Extract only the minimum code needed by the frozen
      consumer. *(Phase 02a, borrowed baselines + manifest builder;
      Phase 02b will extend with owned arms, 2026-04-24)*
- [x] **SIMU-02**: Run a tiny smoke path from repo custody with no
      live-monorepo imports. *(Phase 02a: `pip install -e .` + 16-test
      pytest + three-arm ablation + morph-bench JSON roundtrip all pass on
      RunPod host, 2026-04-24)*
- [ ] **VALD-01**: Verify `package_boundary_earned` against consumer,
      independence, smoke, and ablation gates. *(Gates 1–3 PASSED;
      gate 4 blocked on D-06.)*
- [ ] **WRIT-01**: Promote a private package boundary only if `VALD-01`
      passes.

## Out Of Scope

| Topic | Reason |
|---|---|
| Public package release | Boundary is unearned. |
| Domain science claims | Owned by Indus or cuneiform lanes. |
| Generic descriptor framework | Not proven beyond candidate source families. |
| Commodity OSS layers | Borrow OpenCV, scikit-image, NumPy, SciPy, scikit-learn, Faiss, and baseline embeddings. |

## Traceability

| Requirement | Phase | Status |
|---|---|---|
| `DATA-01` | Phase 00 | Complete |
| `DATA-02`, `DERV-01`, `DERV-02` | Phase 01 | Complete |
| `SIMU-01`, `SIMU-02` | Phase 02a | Complete (owned-arm extension in 02b blocked on D-06) |
| `VALD-01`, `WRIT-01` | Phase 03 | Blocked on Phase 02b evidence |
