# Phase 02 Context

## Entry Conditions

- Phase 01 complete (`.gpd/phases/01-consumer-and-interface-freeze/01-SUMMARY.md`).
- `package_boundary_earned = UNTESTED`.
- Executive decision (2026-04-24): split Phase 02 into two sub-phases to
  unblock execution while D-06 (owned-arm source retrieval) remains open:
  - **Phase 02a (Borrowed-Baseline Sanity Path)** — runs without D-06. Exists
    to prove the scaffold is truly monorepo-free, that `Descriptor` is
    implementable with three OSS libraries, and that morph-bench ingests the
    produced manifests unmodified.
  - **Phase 02b (Owned-Arm Ablation)** — blocked on D-06; runs once owned
    source files are retrieved.

## Input Artefacts

- `.gpd/phases/01-consumer-and-interface-freeze/01-DECISIONS.md`
- `.gpd/phases/01-consumer-and-interface-freeze/01-RESEARCH.md`
- `SOURCE_BOUNDARY.md`
- sibling `workstreams/gnosis-morph-bench/05_repo_scaffold/` (evaluator
  dependency)

## Execution Envelope

- Authoring: local Mac at `05_repo_scaffold/`.
- Execution: RunPod host `38.80.152.147:34587`, pod `7k3riasglemecu`,
  workspace `/workspace/gnosis-glyph-engine/`.
- Python: 3.13 venv.
- Borrowed deps: `opencv-python-headless`, `scikit-image`, `scikit-learn`,
  `numpy` (+ transitive `scipy`), plus editable install of the local
  morph-bench package.
- Autonomy: `high`; reporting `blockers_only`.

## Exit Conditions

Phase 02a PASSES when:

1. `src/gnosis_glyph_engine/` is installable with `pip install -e .` on the
   pod (no live-monorepo imports, no hidden path coupling),
2. `pytest tests/` passes on the pod,
3. `scripts/run_ablation.py` produces
   `artifacts/ablation/ablation_report.json` containing `sigma`,
   `null_mean`, `null_std`, `silhouette`, `mean_jaccard` per arm for the
   three borrowed baselines,
4. morph-bench's CLI consumes each arm's manifest without modification and
   writes a smoke report,
5. both results are captured in `02-VERIFICATION.md`.

Phase 02a does **NOT** attempt to apply the numeric pass rule (D-04), because
the rule compares owned arms to baselines and the owned arms are still
blocked on D-06. The rule applies in Phase 03 after 02b runs.
