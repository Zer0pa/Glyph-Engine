# TODO

## Phase 01 (Consumer And Interface Freeze) — COMPLETE 2026-04-24

- [x] Freeze first consumer, interface, fixture, ablation, destination paths.

## Phase 02a (Borrowed-Baseline Sanity Path) — COMPLETE 2026-04-24

- [x] Provision RunPod workspace (Python 3.13 venv + borrowed deps +
      editable morph-bench).
- [x] Implement `src/gnosis_glyph_engine/` tree for borrowed-only arms.
- [x] Write pytest suite; all pass on pod.
- [x] Run `run_ablation.py`; produce `artifacts/ablation/ablation_report.json`.
- [x] Mirror artefacts to HF dataset `Zer0pa/glyph-engine-artefacts`.

## Phase 02c (OSS-Baseline Robustness + Closeout) — COMPLETE 2026-04-24

- [x] Fix dependency/test boundary: `importorskip` + local schema test.
- [x] Add `pyproject.toml` comments clarifying morph-bench is host-supplied.
- [x] Build multi-seed OSS-baseline robustness script + console entry.
- [x] Run verification: 17 pass WITH morph-bench, 16 pass + 1 skipped
      WITHOUT.
- [x] Retire D-02a-06 fixture-saturation risk via multi-seed evidence.
- [x] Decide Glyph-Engine stays sovereign (D-02c-02); define adapter-only
      rollback trigger.
- [x] Scrub public-facing paths via `docs/PROVENANCE_LABELS.md`.
- [x] Add `PRIVATE_INTERNAL_LICENSE_NOTICE.md` *(later retired in Wave 2 and superseded by canonical `NOTICE.md`)*.
- [x] Produce `HF_CUSTODY_REGISTER.md` with production-token verification.

## Phase 02b (Owned-Arm Ablation) — BLOCKED ON D-06

Blocker: owner retrieves
`scripts/indus/stroke_native_encoding.py` and
`scripts/indus/phase3_common.py` from the live monorepo, or grants pod
access to a monorepo clone.

Work ready to start the moment D-06 clears:

- [ ] Record path-rewrite ledger rows for the two copied files.
- [ ] Implement `src/gnosis_glyph_engine/owned/stroke_compass.py` from
      `stroke_native_encoding.py` (32-d fixed output).
- [ ] Implement `src/gnosis_glyph_engine/owned/topology.py` from
      `phase3_common.py` (≈16-d fixed output).
- [ ] Remove the `SourceRetrievalPending` placeholders.
- [ ] Add unit tests for the two owned descriptors.
- [ ] Extend `run_ablation.py` to include both owned arms.
- [ ] Extend `run_robustness.py` to include both owned arms across the
      same 10 seeds.
- [ ] Apply the D-04 pass rule under D-02c-02 routing (sovereign stays
      unless owned fails vs multi-seed ORB ceiling).

## Phase 03 (Package-Boundary Review) — BLOCKED ON PHASE 02b

- [ ] Declare `package_boundary_earned` `PASSED` / `FAILED` /
      `INCONCLUSIVE` in `SOVEREIGN_PRD.md` and `STATE.md`.
- [ ] If `PASSED`: await legal on canonical licence and public-release
      packet; do NOT self-promote.
- [ ] If `FAILED`: demote to adapter-only; add `Generic glyph-engine
      package` to `BUILD_VS_BORROW_CANON.md` `Do Not Build`.

## Optional Follow-Ups (P2 from closeout brief)

- [ ] Add minimal GitHub Actions CI (install + pytest + robustness
      smoke; do not fetch HF).
- [ ] Cross-lane `HF_CUSTODY_REGISTER.md` consolidation (portfolio-level,
      not this lane's call).

## Required Before Any Public Moves

- [ ] Canonical `LICENSE` file from Zer0pa legal.
- [ ] Public contact surface.
- [ ] Phase 03 verdict `PASSED`.

## Blocked Public Moves

- Public promotion.
- Performance claims (including across-seeds generalisation).
- Cross-domain library claims.
- Ownership of Indus or cuneiform findings.
