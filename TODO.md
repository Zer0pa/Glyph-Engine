# TODO

## Phase 01 (Consumer And Interface Freeze) — COMPLETE 2026-04-24

- [x] Freeze first consumer, interface, fixture, ablation, destination paths.

## Phase 02a (Borrowed-Baseline Sanity Path) — COMPLETE 2026-04-24

- [x] Provision RunPod workspace (Python 3.13 venv + borrowed deps +
      editable morph-bench).
- [x] Implement `src/gnosis_glyph_engine/` tree for borrowed-only arms.
- [x] Write 16-test pytest suite; all pass on pod.
- [x] Run `run_ablation.py`; produce `artifacts/ablation/ablation_report.json`.
- [x] Mirror artefacts to HF dataset `Zer0pa/glyph-engine-artefacts`.
- [x] Update extraction ledger (Phase 02a: zero monorepo copies).

## Phase 02b (Owned-Arm Ablation) — BLOCKED ON D-06

Blocker: owner retrieves
`scripts/indus/stroke_native_encoding.py` and
`scripts/indus/phase3_common.py` from the live monorepo (or grants pod
access to a monorepo clone).

Work ready to start the moment D-06 clears:

- [ ] Record path-rewrite ledger rows for the two copied files.
- [ ] Implement `src/gnosis_glyph_engine/owned/stroke_compass.py` from
      `stroke_native_encoding.py` (32-d fixed output).
- [ ] Implement `src/gnosis_glyph_engine/owned/topology.py` from
      `phase3_common.py` (≈16-d fixed output).
- [ ] Remove the `SourceRetrievalPending` placeholders.
- [ ] Add unit tests for the two owned descriptors.
- [ ] Extend `run_ablation.py` to include both owned arms.
- [ ] Regenerate `ablation_report.json` with five arms.

## Phase 03 (Package-Boundary Review) — BLOCKED ON PHASE 02b

- [ ] Decide on fixture-saturation risk (D-02a-06): accept tight D-04
      threshold, or insert a fixture-hardening phase first.
- [ ] Apply D-04 numeric pass rule to the five-arm ablation.
- [ ] Declare `package_boundary_earned` `PASSED` / `FAILED` /
      `INCONCLUSIVE` in `SOVEREIGN_PRD.md` and `STATE.md`.
- [ ] If `PASSED`: author private release packet, license text, and contact
      surface.
- [ ] If `FAILED`: add `Generic glyph-engine package` to
      `BUILD_VS_BORROW_CANON.md` `Do Not Build`; close scaffold as a
      negative result.

## Required Before Any Public Moves

- [ ] Final license text (owner-deferred).
- [ ] Public contact surface (owner-deferred).
- [ ] Phase 03 verdict `PASSED`.

## Blocked Public Moves

- Public promotion.
- Performance claims.
- Cross-domain library claims.
- Ownership of Indus or cuneiform findings.
