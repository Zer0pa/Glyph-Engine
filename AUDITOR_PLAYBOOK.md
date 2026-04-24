# Auditor Playbook

Last updated: 2026-04-24 (Phase 02c closeout-brief lane-A compliance
complete; Phase 02a "saturation" framing retired by D-02c-01).

## Goal

Verify that this scaffold is not overclaiming a `gnosis-glyph-engine`
package. Authority metric `package_boundary_earned` is currently
`UNTESTED`: gates 1–3 have PASSED, gate 4 is BLOCKED on D-06 and unrun.

## Fast Path

1. Read the authority block in `README.md`.
2. Read `SOVEREIGN_PRD.md` for the extraction gate.
3. Read `SOURCE_BOUNDARY.md` including the **Phase 02a Extraction Ledger**
   (every file newly authored; zero monorepo copies) and the empty **Phase
   02b Extraction Ledger** (will populate when D-06 clears).
4. Read `.gpd/STATE.md` for current phase + blockers.
5. Read `.gpd/phases/01-consumer-and-interface-freeze/01-DECISIONS.md` for
   the frozen consumer, interface, fixture, and ablation rule.
6. Read `.gpd/phases/02-minimal-extraction-smoke/02-01-VERIFICATION.md` for
   the seed=42 metric matrix and the gate-by-gate PASS/BLOCKED record.
7. Read `.gpd/phases/02-minimal-extraction-smoke/02-02-VERIFICATION.md` for
   the multi-seed robustness closeout and the six closeout gates A–F.
8. Read `.gpd/phases/02-minimal-extraction-smoke/02-02-DECISIONS.md` for
   the scope routing (D-02c-02 sovereign stays; adapter-only is a
   conditional rollback, not a present recommendation).
9. Confirm `artifacts/ablation/ablation_report.json` is present and its
   `owned_arms_status` = `BLOCKED_ON_D-06`.
10. Confirm `artifacts/robustness/robustness_report.json` is present and
    `arms[*].sigma.n == 10`.
11. Confirm `code/README.md` reflects `BORROWED_ARMS_EXTRACTED`.
12. Read `PRIVATE_INTERNAL_LICENSE_NOTICE.md` and `HF_CUSTODY_REGISTER.md`
    — they own the rights-posture and HF-custody truth.

## Claim Replay Map

| Claim | Evidence path | Verifiable? | Caveat |
|---|---|---|---|
| Candidate source families are identified | `SOURCE_BOUNDARY.md` | yes | two Indus files absent from snapshot (D-06) |
| First admitted consumer is `gnosis-morph-bench` | `.gpd/phases/01-consumer-and-interface-freeze/01-DECISIONS.md` D-01 + `workstreams/gnosis-morph-bench/05_repo_scaffold/src/gnosis_morph_bench/schema.py` | yes | consumer lives in sibling workstream, not this repo |
| Interface is minimal (`Descriptor` + `LearnedDescriptor` + `manifest_builder`) | `src/gnosis_glyph_engine/protocols.py`, `src/gnosis_glyph_engine/manifest_builder.py` | yes | signatures match Phase 01 D-02 verbatim |
| Scaffold is monorepo-free | `pyproject.toml`, `pip install -e .[dev]` on Python 3.13 + `pytest` pass on RunPod | yes | reproduce via `<RUNPOD_WORKSPACE>/gnosis-glyph-engine/` on pod |
| Three borrowed baselines produce valid metrics | `artifacts/ablation/ablation_report.json`, `artifacts/ablation/per_arm/*` | yes | one fixture, seed=42, not a generalisation claim |
| `baseline_orb` saturates the 12-glyph fixture (seed=42 only) | `artifacts/ablation/ablation_report.json::arms[0]` | yes | seed=42 single-seed observation; retired as a general claim by Phase 02c D-02c-01 |
| `baseline_orb` does NOT saturate robustly across seeds | `artifacts/robustness/robustness_report.json::arms[0].sigma` + `nmi` | yes | mean σ = 4.14, NMI=1.0 in 2/10 seeds only |
| Owned arms are not yet run | `src/gnosis_glyph_engine/owned/__init__.py` (raises `SourceRetrievalPending`) | yes | D-06 blocker stated in every relevant surface |
| No public package boundary is proven | `SOVEREIGN_PRD.md`, `README.md` current-authority table | yes | gate 4 still `UNTESTED` |
| Public promotion is blocked | `README.md`, `RELEASING.md`, GitHub visibility `INTERNAL` | yes | license still `OWNER_DEFERRED` |

## Reproduce The Evidence

On any Python 3.13 host with internet access:

```bash
git clone https://github.com/Zer0pa/Glyph-Engine.git
cd Glyph-Engine
python3.13 -m venv .venv && source .venv/bin/activate
pip install -e .[dev]
pytest -q                         # expect: 16 passed, 1 skipped (morph-bench absent)

# Optional cross-repo contract test: install sibling morph-bench and rerun.
pip install -e /path/to/gnosis-morph-bench
pytest -q                         # expect: 17 passed

python -m gnosis_glyph_engine.scripts.run_ablation
# writes artifacts/ablation/ablation_report.json (seed=42 single-seed)

python -m gnosis_glyph_engine.scripts.run_robustness
# writes artifacts/robustness/robustness_report.json (seeds 0..9)
```

A successful seed=42 run matches
`.gpd/phases/02-minimal-extraction-smoke/02-01-VERIFICATION.md` to 6
decimal places. A successful multi-seed run matches
`.gpd/phases/02-minimal-extraction-smoke/02-02-VERIFICATION.md`.

## Fail Conditions

- README or docs claim a **public** installable library or cross-domain
  superiority.
- Docs claim owned-descriptor superiority (gate 4 is UNTESTED until
  Phase 02b and Phase 03 run).
- Domain results from Indus or cuneiform are presented as glyph-engine
  proof.
- `pyproject.toml` carries a canonical non-`OWNER_DEFERRED` licence
  without Phase 03 having declared PASS.
- `SOURCE_BOUNDARY.md` path-rewrite ledger contains rows for code the
  scaffold cannot produce on replay.
- Phase 02b results are presented without reference to the multi-seed
  borrowed ceiling (`artifacts/robustness/robustness_report.json`).
- The seed=42 ablation is cited as general evidence without the
  multi-seed correction (D-02c-01) being carried forward.

## Known Limitations Worth Checking

- Ten seeds now cover the synthetic 12-glyph fixture. No cross-corpus
  generalisation claim is valid yet; real-glyph fixtures will only
  appear post-D-06 once owner retrieval opens rights-cleared data.
- morph-bench sibling is optional at install time; the cross-repo
  contract test skips cleanly if absent, and a local schema-v1 fallback
  test keeps the invariants exercised.
- `opencv-python-headless` is used (no GUI backend); reproducibility on
  a full `opencv-python` install has not been re-verified.
- `baseline_hog` can fall below null on some seeds; this is preserved
  deliberately (D-02c-04). Treat it as evidence about HOG+PCA on binary
  glyphs, not as evidence of all HOG variants.
