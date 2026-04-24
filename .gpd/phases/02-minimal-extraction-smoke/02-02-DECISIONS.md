# Phase 02c Decisions — OSS-Baseline Robustness + Closeout Scope

Date: 2026-04-24
Status: `FROZEN`
Context: closeout brief dated 2026-04-24, lane `Glyph-Engine`.

## D-02c-01 Multi-seed robustness supersedes the seed=42 saturation narrative

- Decision: the Phase 02a finding "`baseline_orb` saturates the 12-glyph
  fixture" was **seed=42 specific**. Over ten seeds (0..9) the measured
  ceiling is substantially lower and the D-04 pass rule is plausible.
- Evidence: `artifacts/robustness/robustness_report.json`, generated
  2026-04-24, 10 seeds × 3 borrowed-baseline arms, `null_repeats=32`,
  `n_clusters=3`.

Summary per arm (mean ± stdev over 10 seeds):

| Arm | σ mean | σ stdev | σ range | NMI mean | NMI range | mean_jaccard mean | silhouette mean |
|---|---:|---:|---|---:|---|---:|---:|
| `baseline_orb` | 4.138 | 1.116 | 2.73 – 6.23 | 0.765 | 0.58 – 1.00 | 0.899 | 0.288 |
| `baseline_hu_regionprops` | 2.954 | 1.056 | 0.70 – 4.10 | 0.575 | 0.31 – 0.74 | 0.943 | 0.488 |
| `baseline_hog` | 1.153 | 1.168 | -0.59 – 2.99 | 0.362 | 0.15 – 0.57 | 0.435 | 0.023 |

Notes:
- `baseline_orb` achieves NMI = 1.0 in only 2 of 10 seeds. The seed=42
  saturation was a real observation but a non-representative one.
- `baseline_hog` can fall **below** the null (σ < 0) on some seeds,
  i.e. can be worse than random. This is consistent with HOG+PCA being a
  poor descriptor for this binary-glyph family, not with HOG being
  generally weak.
- D-04 pass rule re-interpreted under multi-seed:
  - Best mean baseline σ ≈ 4.14 (ORB).
  - Target for an owned arm: mean σ ≥ 4.64 and `mean_jaccard` ≥ 0.90
    (tie-or-beat against ORB's mean).
  - This is a *plausible* target for a descriptor tuned to this family,
    not an impossible one.

## D-02c-02 Glyph-Engine stays sovereign — adapter-only scope NOT recommended at this time

- Decision: reject the "collapse to adapter-only" recommendation from
  the closeout brief's default framing. Preserve the sovereign
  `gnosis-glyph-engine` repo boundary.
- Rationale:
  1. The closeout brief's default recommendation hinged on the Phase 02a
     saturation finding. D-02c-01 retires that finding as seed-specific.
  2. The multi-seed baseline ceiling is beatable by a small positive
     margin (≥ 0.5 σ over ~4.14 mean), which is a realistic threshold
     for a purpose-built descriptor.
  3. No owned-arm evidence exists yet (D-06 blocker), so "owned beats
     borrowed" is genuinely `UNTESTED` rather than "failed".
  4. Collapsing the lane now would erase the purpose of the sovereign
     repo (the falsifiable ablation on gate 4) before the falsification
     has been attempted.
- Rollback trigger (adapter-only reinstated): Phase 02b, once D-06 clears,
  produces owned-arm metrics and either:
  - owned arms fail to beat ORB mean σ by ≥ 0.5 over the same 10-seed
    sample, OR
  - owned arms tie/underperform on `mean_jaccard`,
  in which case the sovereign boundary is genuinely not earned and the
  lane demotes to an adapter inside `gnosis-morph-bench` or
  `gnosis-indus`.

## D-02c-03 D-02a-06 is retired

- Decision: Phase 01 decision D-02a-06 ("record baseline saturation as
  Phase 03 risk") is **retired** by D-02c-01. The pass rule can be
  evaluated on the existing fixture without a fixture-hardening detour.
- Rollback: if Phase 02b itself shows fixture saturation across seeds
  (i.e. both borrowed and owned arms hitting NMI=1.0 reliably), a
  fixture-hardening phase would still be warranted. That is not the
  current evidence.

## D-02c-04 Keep `baseline_hog` despite its weak multi-seed performance

- Decision: `baseline_hog` stays in the borrowed-baseline set even though
  it sometimes underperforms the null.
- Rationale: its weakness on this fixture is scientifically honest
  evidence about HOG+PCA for binary-glyph family separation. Removing it
  would cherry-pick the ablation in favour of "strong baseline ORB"
  only. Honest ablations include negative arms.
- Documented in `artifacts/robustness/robustness_report.json` and cited
  in `02-02-VERIFICATION.md`.

## D-02c-05 Closeout scope-fixes folded into the phase record

- Cross-repo contract test (`test_morph_bench_loader_accepts_manifest`)
  now uses `pytest.importorskip` against `gnosis_morph_bench.schema`.
  Verified on the pod: 17 passed when morph-bench is installed; 16
  passed + 1 skipped in a clean venv without morph-bench.
- A local schema-v1 contract test
  (`test_manifest_matches_local_schema_contract`) was added so that
  `build_manifest` shape invariants remain exercised without morph-bench.
- `pyproject.toml` clarifies that `gnosis-morph-bench` is not a hard
  dependency; it is supplied by the execution host.
- Public-facing paths (`RunPod` host, pod id, local portfolio paths, HF
  cache paths, SSH keys) replaced by symbolic labels per
  `docs/PROVENANCE_LABELS.md`. Scientific provenance preserved.
- `PRIVATE_INTERNAL_LICENSE_NOTICE.md` added. `LICENSE_PLACEHOLDER.md`
  kept; canonical `LICENSE` deferred to Zer0pa legal.
- `HF_CUSTODY_REGISTER.md` added, verifying `Zer0pa/glyph-engine-artefacts`
  with the production token and recording SHA, files, and rights class.

## D-02c-06 Closeout verdict

Lane `Glyph-Engine` passes the closeout-brief P1 fix (dependency
boundary) and produces the smallest fair OSS-baseline comparison required
by the brief. The sovereign-or-adapter routing is **deferred to
Phase 02b** under D-02c-02, not answered prematurely now. `package_boundary_earned`
remains `UNTESTED`; gates 1–3 stay PASSED; gate 4 stays BLOCKED on D-06.
