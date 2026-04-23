# TODO

## Phase 01 (Consumer And Interface Freeze) — COMPLETE

- [x] Freeze the first real consumer (`gnosis-morph-bench`).
- [x] Define the smallest descriptor or geometry interface worth extracting
      (`Descriptor`, `LearnedDescriptor`, `manifest_builder`).
- [x] Define the tiny fixture needed for a smoke path (12-glyph synthetic,
      3 families × 4 variants).
- [x] Define the ablation against public baselines (5 arms, numeric pass
      rule).
- [x] Freeze destination path map for Phase 02 extraction.

Frozen deliverables live under
`.gpd/phases/01-consumer-and-interface-freeze/`.

## Phase 02 (Minimal Extraction Smoke) — BLOCKED ON OWNER ACTION

Blocker: retrieve
`scripts/indus/stroke_native_encoding.py` and
`scripts/indus/phase3_common.py` from the live monorepo. Both owned-arm
ablations are blocked until those files are placed or access to a live-monorepo
clone is granted. Tracked as Phase 01 decision D-06.

Work ready to start once blocker clears:

- [ ] Provision RunPod workspace at `/workspace/gnosis-glyph-engine/` with
      Python 3.13 venv and borrowed baselines (`opencv-python-headless`,
      `scikit-image`, `scikit-learn`, `numpy`).
- [ ] Write path-rewrite ledger for each copied source file in
      `SOURCE_BOUNDARY.md`.
- [ ] Extract `src/gnosis_glyph_engine/` tree per frozen destination map.
- [ ] Implement `fixtures.synthesize_twelve_glyphs(seed=42)`.
- [ ] Implement the three borrowed-baseline descriptor classes.
- [ ] Implement the two owned-candidate descriptor classes (after source
      retrieval).
- [ ] Implement `manifest_builder.build_manifest(...)`.
- [ ] Add `pyproject.toml` (only after the `src/` tree lands).
- [ ] Implement `scripts/run_ablation.py` writing `artifacts/ablation_report.json`.
- [ ] Run the full ablation, hand the report to `gnosis-morph-bench.cli`, and
      record the numeric verdict.

## Phase 03 (Package-Boundary Review) — BLOCKED

- [ ] Verify `package_boundary_earned` against the four gate conditions
      (consumer, independence, smoke, ablation).
- [ ] Record verdict in `SOVEREIGN_PRD.md` and `STATE.md`.
- [ ] If PASSED: author `pyproject.toml`, package README claims, private
      release packet.
- [ ] If FAILED: add `Generic glyph-engine package` to the `Do Not Build`
      section of `BUILD_VS_BORROW_CANON.md` and close the scaffold as a
      recorded negative result.

## Required Before Any Public Moves

- [ ] Final license text (owner-deferred).
- [ ] Public contact surface (owner-deferred).
- [ ] Benchmark evidence that clears Phase 03.

## Blocked Public Moves

- Public promotion.
- Performance claims.
- Cross-domain library claims.
- Ownership of Indus or cuneiform findings.
