# Requirements: gnosis-glyph-engine

Defined: 2026-04-23
Last updated: 2026-04-24 (Phase 02c closeout)

## Primary Requirements

- [x] **DATA-01**: Establish the scaffold as a hold/extraction target.
      *(Phase 00, 2026-04-23)*
- [x] **DATA-02**: Freeze the first real consumer.
      *(Phase 01 D-01, 2026-04-24)*
- [x] **DERV-01**: Define the smallest descriptor or geometry interface
      worth extracting. *(Phase 01 D-02, 2026-04-24)*
- [x] **DERV-02**: Define the ablation against borrowed public baselines.
      *(Phase 01 D-04, 2026-04-24; re-characterised under multi-seed
      evidence by Phase 02c D-02c-01)*
- [x] **SIMU-01**: Extract only the minimum code needed by the frozen
      consumer. *(Phase 02a + Phase 02c)*
- [x] **SIMU-02**: Run a tiny smoke path from repo custody with no
      live-monorepo imports. *(Phase 02a PASS; Phase 02c verified
      independently installable WITHOUT morph-bench.)*
- [ ] **VALD-01**: Verify `package_boundary_earned` against consumer,
      independence, smoke, and ablation gates. *(Gates 1–3 PASSED;
      gate 4 BLOCKED on D-06.)*
- [ ] **WRIT-01**: Promote a private package boundary only if `VALD-01`
      passes.

## Closeout Brief Requirements (2026-04-24, lane A)

- [x] **CLOSE-A1**: Fix Morph-Bench dependency/test boundary.
      *(Phase 02c D-02c-05: `importorskip` + local schema fallback
      test; 17 pass WITH morph-bench, 16 pass + 1 skipped WITHOUT.)*
- [x] **CLOSE-A2**: Run smallest fair OSS-baseline comparison.
      *(Phase 02c robustness report, 10 seeds × 3 arms.)*
- [x] **CLOSE-A3**: Sovereign-vs-adapter scope recommendation.
      *(D-02c-02: stay sovereign; adapter trigger = owned-arm failure
      to beat multi-seed ORB ceiling in Phase 02b.)*
- [x] **CLOSE-P2-paths**: Scrub public-facing paths via parameterisation.
      *(docs/PROVENANCE_LABELS.md + sed pass; zero matches on operational
      fingerprints.)*
- [x] **CLOSE-P2-licence**: Explicit private licence notice.
      *(Originally `PRIVATE_INTERNAL_LICENSE_NOTICE.md`; replaced in
      Wave 2 by canonical `NOTICE.md`.)*
- [x] **CLOSE-HF**: HF custody register with live token verification.
      *(HF_CUSTODY_REGISTER.md row HF-01.)*

## Out Of Scope

| Topic | Reason |
|---|---|
| Public package release | Boundary unearned; Phase 03 not run. |
| Domain science claims | Owned by Indus or cuneiform lanes. |
| Generic descriptor framework | `BUILD_VS_BORROW_CANON.md` `Do Not Build`. |
| Commodity OSS layers | Borrow OpenCV, scikit-image, NumPy, SciPy, scikit-learn, Faiss. |
| Public licence grant | Owner-deferred until Zer0pa legal decides. |

## Traceability

| Requirement | Phase | Status |
|---|---|---|
| `DATA-01` | Phase 00 | Complete |
| `DATA-02`, `DERV-01`, `DERV-02` | Phase 01 | Complete |
| `SIMU-01`, `SIMU-02` | Phase 02a + 02c | Complete |
| `CLOSE-A1..CLOSE-HF` | Phase 02c | Complete |
| `VALD-01`, `WRIT-01` | Phase 03 | Blocked on Phase 02b evidence |
