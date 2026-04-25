> **Notice:** This is a private internal repository. See `NOTICE.md`.

# Gnosis Glyph Engine

## What This Is

`gnosis-glyph-engine` is the Gnosis private research lane that asks one
falsifiable question:

> Is a standalone glyph-engine package boundary earned by a real consumer,
> a monorepo-free smoke path, and a descriptor ablation against borrowed
> baselines?

It is an internal extraction-target scaffold for reusable glyph geometry,
stroke, and descriptor kernels. It is **not a public library**, **not a
product**, and **not a decipherment claim**. The authority metric
`package_boundary_earned` is currently `UNTESTED`.

## What We Prove

- The frozen Phase 01 interface (`Descriptor`, `LearnedDescriptor`,
  `manifest_builder`) is implementable using only borrowed OSS — OpenCV,
  scikit-image, scikit-learn, NumPy.
- The package installs cleanly with `pip install -e .[dev]` on Python 3.13
  with no live-monorepo imports and no monorepo path coupling.
- The 17-test pytest suite passes when sibling `gnosis-morph-bench` is
  installed; 16 pass + 1 cleanly skips when it is not — preserving repo
  independence.
- The frozen `BenchmarkManifest` shape is consumed unmodified by
  `gnosis_morph_bench.schema.load_manifest`, producing finite `sigma`,
  `null_mean`, `null_std`, `silhouette`, and `mean_jaccard` per arm.
- A multi-seed (10-seed) borrowed-baseline ceiling is recorded in
  `artifacts/robustness/robustness_report.json`; mean σ across seeds
  comes out to `baseline_orb` 4.14 ± 1.12, `baseline_hu_regionprops`
  2.95 ± 1.06, `baseline_hog` 1.15 ± 1.17.
- Determinism is checked: `replay_all_identical == true` for every arm
  in the seed-42 ablation; reference-freeze SHA256 is byte-stable across
  arms.

## What We Don't Claim

- We do not claim that any owned descriptor beats borrowed baselines.
  Phase 02b is BLOCKED on D-06 (two Indus source files are not present
  in the portfolio snapshot) and the gate-4 verdict is `UNTESTED`.
- We do not claim cross-corpus generalisation. The fixture is a
  deterministic 12-glyph synthetic generator; rights-cleared real-glyph
  evidence does not yet exist in this repo.
- We do not claim public-release readiness, performance superiority, or
  product readiness.
- We do not claim Indus or cuneiform domain results — those are owned by
  sibling lanes.

## Tests and Verification

- Local CI: `.github/workflows/ci.yml` runs `pip install -e .[dev]` then
  `pytest -q` on every push and PR to `main`.
- Local repro:

  ```bash
  python3.13 -m venv .venv && source .venv/bin/activate
  pip install -e .[dev]
  pytest -q                         # → 16 passed, 1 skipped
  pip install -e /path/to/gnosis-morph-bench    # optional contract test
  pytest -q                         # → 17 passed
  python -m gnosis_glyph_engine.scripts.run_ablation
  python -m gnosis_glyph_engine.scripts.run_robustness
  ```

- Provenance: `seed=42` ablation matches
  `.gpd/phases/02-minimal-extraction-smoke/02-01-VERIFICATION.md`
  to 6 decimal places; `seeds=0..9` robustness matches `02-02-VERIFICATION.md`.
- Endpoint-leak scan is part of the closeout verification (Gate D in
  `02-02-VERIFICATION.md`); see `docs/PROVENANCE_LABELS.md` for the
  symbolic-label convention.

## Proof Anchors

| Claim | Evidence |
|---|---|
| Authority metric definition | `SOVEREIGN_PRD.md` §Authority Metric |
| Frozen consumer + interface | `.gpd/phases/01-consumer-and-interface-freeze/01-DECISIONS.md` D-01, D-02 |
| Frozen fixture + ablation rule | `.gpd/phases/01-consumer-and-interface-freeze/01-DECISIONS.md` D-03, D-04 |
| Phase 02a single-seed ablation | `artifacts/ablation/ablation_report.json` + `.gpd/phases/02-minimal-extraction-smoke/02-01-VERIFICATION.md` |
| Phase 02c multi-seed robustness | `artifacts/robustness/robustness_report.json` + `.gpd/phases/02-minimal-extraction-smoke/02-02-VERIFICATION.md` |
| Sovereign-vs-adapter scope decision | `.gpd/phases/02-minimal-extraction-smoke/02-02-DECISIONS.md` D-02c-02 |
| Owned-arm source-retrieval blocker | `SOURCE_BOUNDARY.md` (D-06) |
| HF custody truth | `HF_CUSTODY_REGISTER.md` HF-01 |
| Path/endpoint scrub convention | `docs/PROVENANCE_LABELS.md` |
| Reviewer interim status | `AGENT_STATUS_REPORT_2026-04-24.md` |
| Auditor fast path | `AUDITOR_PLAYBOOK.md` |

## Repo Shape

```
.
├── NOTICE.md                                  # root legal posture (Gnosis Phase 1)
├── PRIVATE_INTERNAL_LICENSE_NOTICE.md         # longer private notice
├── HF_CUSTODY_REGISTER.md                     # HF artefact-dataset truth
├── README.md                                  # this file
├── SOVEREIGN_PRD.md                           # authority metric + extraction gate
├── SOURCE_BOUNDARY.md                         # candidate sources, ledger, D-06
├── AUDITOR_PLAYBOOK.md                        # fast path + reproduce + claim-replay
├── AGENT_STATUS_REPORT_2026-04-24.md          # agent narrative layer for review
├── MIGRATION_PLAN.md, ROADMAP.md, GOVERNANCE.md, RELEASING.md, SECURITY.md, ...
├── DATA_POLICY.md, PUBLIC_AUDIT_LIMITS.md
├── pyproject.toml                             # gnosis-glyph-engine==0.1.0a1
├── .github/
│   ├── workflows/ci.yml
│   ├── ISSUE_TEMPLATE/, PULL_REQUEST_TEMPLATE.md
├── .gpd/
│   ├── PROJECT.md, STATE.md, ROADMAP.md, REQUIREMENTS.md, DECISIONS.md,
│   │   CONVENTIONS.md, NOTATION_GLOSSARY.md, state.json, config.json
│   └── phases/
│       ├── 00-workstream-bootstrap/*
│       ├── 01-consumer-and-interface-freeze/*
│       └── 02-minimal-extraction-smoke/*      # 02a + 02c artefacts
├── src/gnosis_glyph_engine/
│   ├── __init__.py, protocols.py, fixtures.py, manifest_builder.py
│   ├── baselines/{__init__,orb,hu_regionprops,hog}.py
│   ├── owned/__init__.py                      # raises SourceRetrievalPending until D-06
│   └── scripts/{__init__,run_ablation,run_robustness}.py
├── tests/{test_fixtures,test_baselines,test_manifest_builder}.py
├── scripts/run_ablation.py                    # thin shim
├── artifacts/
│   ├── ablation/   {ablation_report.json, per_arm/baseline_*.{manifest,smoke_report}.json}
│   └── robustness/ robustness_report.json
├── code/README.md                             # legacy code-surface marker
└── docs/{ARCHITECTURE,LEGAL_BOUNDARIES,PROVENANCE_LABELS,FAQ,SUPPORT,README}.md
```

## Quick Start

```bash
git clone https://github.com/Zer0pa/Glyph-Engine.git
cd Glyph-Engine
python3.13 -m venv .venv && source .venv/bin/activate
pip install -e .[dev]
pytest -q                          # → 16 passed, 1 skipped
python -m gnosis_glyph_engine.scripts.run_ablation
python -m gnosis_glyph_engine.scripts.run_robustness
```

Console scripts (after install): `glyph-engine-ablation`,
`glyph-engine-robustness`.

## Current Gaps

- **D-06** (owner action): retrieve
  `scripts/indus/stroke_native_encoding.py` and
  `scripts/indus/phase3_common.py` from the live monorepo, or grant pod
  access to a live-monorepo clone. Phase 02b cannot start until D-06
  clears.
- Final license/canonical legal text is owner-deferred (see `NOTICE.md`).
- Public contact surface is owner-deferred.
- No real-glyph fixture; the synthetic 12-glyph generator is the only
  ablation surface today.
