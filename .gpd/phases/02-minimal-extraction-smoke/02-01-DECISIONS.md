# Phase 02a Decisions

Date: 2026-04-24
Status: `FROZEN`

## D-02a-01 Split Phase 02 into two sub-phases

- Decision: Phase 02 splits into `02a Borrowed-Baseline Sanity Path` (runs
  now) and `02b Owned-Arm Ablation` (blocked on D-06).
- Rationale: running the three borrowed arms closes gate 2 of
  `package_boundary_earned` (monorepo-free execution) and validates the
  frozen Phase 01 interface against real implementations, without waiting
  for owner action on D-06.
- Rollback: if D-06 resolves inside the Phase 02a window, collapse 02a and
  02b into a single Phase 02 report.

## D-02a-02 Record zero path-rewrites for borrowed code

- Decision: all Phase 02a code is newly authored glue over public OSS
  imports (`cv2`, `skimage`, `sklearn`). No files were copied from the live
  monorepo in Phase 02a. `SOURCE_BOUNDARY.md` path-rewrite ledger gets a
  `Phase 02a: none` row.
- Rationale: keeps the ledger falsifiable; Phase 02b (D-06) is the only
  sub-phase that copies monorepo code, and it must record per-file rewrites.

## D-02a-03 Use the 12-glyph fixture unchanged

- Decision: run Phase 02a on the exact Phase 01 D-03 fixture
  (`synthesize_twelve_glyphs(seed=42)`).
- Rationale: D-03 froze the fixture to make metric comparisons across arms
  and phases direct. Phase 03 may decide to expand to 24 items if variance
  is problematic, but Phase 02a must use the frozen surface.

## D-02a-04 Morph-bench integration via editable install

- Decision: on the RunPod host, `gnosis-morph-bench` is installed editable
  from `<RUNPOD_WORKSPACE>/gnosis-morph-bench/`. `gnosis-glyph-engine` calls its
  `schema`, `benchmark`, and `stability` modules directly, not via
  subprocess.
- Rationale: morph-bench is a sibling Python package with a published
  import surface. Subprocess invocation would add noise without improving
  sovereignty.
- Rollback: if morph-bench renames or relocates its public helpers,
  `run_ablation.py` is the only touch point.

## D-02a-05 Console entry point `glyph-engine-ablation`

- Decision: expose the ablation driver as a `[project.scripts]` console
  script resolving to `gnosis_glyph_engine.scripts.run_ablation:main`.
- Rationale: allows `glyph-engine-ablation` to run after `pip install -e .`
  without CWD gymnastics. Preserves `python -m` and the `scripts/`
  top-level shim.

## D-02a-06 Record baseline saturation as a Phase 03 risk

- Decision: the `ablation_report.json` will be read into Phase 03 as input,
  and Phase 03 must evaluate whether the D-04 pass rule is achievable given
  the measured baseline ceiling on the 12-glyph fixture.
- Rationale: Phase 02a runs produced `baseline_orb` at NMI = 1.0,
  σ ≈ 6.40, mean_jaccard = 1.0 — effectively a saturation ceiling.
  Clearing D-04 on this fixture now requires owned-arm σ ≥ ~6.9 AND
  mean_jaccard ≥ 1.0, which may not be achievable. This is recorded as a
  material risk, not an edit to D-04.
- Rollback: Phase 03 may decide to (a) widen the fixture, (b) add harder
  distractor classes, or (c) declare the boundary test inconclusive on
  the current fixture and request an admitted-corpus fixture in a new
  phase.
