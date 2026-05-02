# Gnosis Glyph Engine

> Live window into the Zer0pa lab. Useful now, improving continuously; blockers are part of the public surface.

## What This Is

Glyph-Engine tests whether a standalone glyph-descriptor package boundary is earned; borrowed baselines run, owned-arm authority remains blocked.

`gnosis-glyph-engine` is the Gnosis research lane that asks one falsifiable
question:

> Is a standalone glyph-engine package boundary earned by a real consumer,
> a monorepo-free smoke path, and a descriptor ablation against borrowed
> baselines?

It is an extraction-target scaffold for reusable glyph geometry, stroke, and
descriptor kernels. It is **not a public library**, **not a product**, and
**not a decipherment claim**.

**Defensible headline metrics (as of 2026-04-28):** Borrowed-baseline ablation
across 10 seeds: mean σ `baseline_orb` 4.14 ± 1.12, `baseline_hu_regionprops`
2.95 ± 1.06, `baseline_hog` 1.15 ± 1.17 (artifact:
`artifacts/robustness/robustness_report.json`). Determinism:
`replay_all_identical == true` for every arm in the seed-42 ablation;
reference-freeze SHA256 is byte-stable across arms. 17 pytest tests pass when
sibling `gnosis-morph-bench` is installed; 16 pass + 1 cleanly skips when it
is not — preserving repo independence.

**Honest blocker:** The owned-arm authority metric `package_boundary_earned`
is `UNTESTED`. Two Indus source files (`scripts/indus/stroke_native_encoding.py`,
`scripts/indus/phase3_common.py`) are not present in the portfolio snapshot;
D-06 retrieval is the unblock. Phase 02b cannot start until D-06 clears.

## Method Mechanics

| Field | Value |
| --- | --- |
| Architecture | GNOSIS_GLYPH_DESCRIPTOR_METHOD |
| Method | Descriptor extraction scaffold with synthetic 12-glyph fixture |
| Baselines | OpenCV ORB, Hu regionprops, HOG borrowed arms |
| Manifest Contract | `BenchmarkManifest` consumed by Morph-Bench |
| Authority Gate | `package_boundary_earned` owned-arm metric |
| Open Gate | D-06 source retrieval blocks Phase 02b |

## Key Metrics

| Metric | Value | Baseline |
| --- | --- | --- |
| Borrowed-baseline robustness | ORB 4.14 +/- 1.12; Hu 2.95 +/- 1.06; HOG 1.15 +/- 1.17 | 10 seeds |
| Deterministic replay | `replay_all_identical == true` | seed-42 ablation |
| Pytest surface | 17 pass with Morph-Bench; 16 pass + 1 skip without sibling | repo independence preserved |
| Authority gate | `package_boundary_earned == UNTESTED` | D-06 blocker |

> Source: `artifacts/robustness/robustness_report.json`, `artifacts/ablation/ablation_report.json`, `.gpd/phases/02-minimal-extraction-smoke/`, and `SOURCE_BOUNDARY.md`.

## Repo Identity

| Field | Value |
| --- | --- |
| Identifier | Glyph-Engine |
| Repository | https://github.com/Zer0pa/Glyph-Engine |
| Portfolio | Gnosis |
| Visibility | PUBLIC |
| Default Branch | main |
| Authority Source | `SOVEREIGN_PRD.md`; `.gpd/phases/02-minimal-extraction-smoke/` |
| License | Apache-2.0 code; CC-BY-4.0 docs |

## Readiness

| Field | Value |
| --- | --- |
| Verdict | BLOCKED |
| Posture | `package_boundary_unearned_pending_owned_arm_d06` |
| Checks | borrowed-baseline and repo-independence checks pass |
| Authority metric | `package_boundary_earned` is `UNTESTED` |
| Authority | `SOURCE_BOUNDARY.md`; `SOVEREIGN_PRD.md` |

### Honest Blocker

The owned-arm authority metric is `UNTESTED`. Gate 4 cannot run until D-06 retrieves the two missing Indus source files.

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

## Verification Status

| Code | Check | Verdict |
| --- | --- | --- |
| V_01 | `pip install -e .[dev]` on Python 3.13 | PASS |
| V_02 | pytest without Morph-Bench sibling: 16 pass + 1 skip | PASS |
| V_03 | pytest with Morph-Bench sibling: 17 pass | PASS |
| V_04 | seed-42 ablation matches verification to 6 decimals | PASS |
| V_05 | D-06 owned-arm source retrieval | BLOCKED |

## Proof Anchors

| Path | State |
| --- | --- |
| `SOVEREIGN_PRD.md` | VERIFIED |
| `.gpd/phases/01-consumer-and-interface-freeze/01-DECISIONS.md` | VERIFIED |
| `artifacts/ablation/ablation_report.json` | VERIFIED |
| `artifacts/robustness/robustness_report.json` | VERIFIED |
| `SOURCE_BOUNDARY.md` | VERIFIED |
| `HF_CUSTODY_REGISTER.md` | VERIFIED |

## Repo Shape

| Field | Value |
| --- | --- |
| Proof Anchors | 6 display anchors |
| Portfolio | Gnosis |
| Package | gnosis-glyph-engine==0.1.0a1 |
| Primary Source | `src/gnosis_glyph_engine/` |
| Tests | `tests/` |
| Artifacts | `artifacts/ablation/`; `artifacts/robustness/` |
| Support Sections | Licensing; Quick Start; Current Gaps; Upcoming Workstreams |

```
.
├── NOTICE                                  # Apache-2.0 code and CC-BY-4.0 docs posture
├── HF_CUSTODY_REGISTER.md                  # HF artefact-dataset truth
├── README.md                               # this file
├── SOVEREIGN_PRD.md                        # authority metric + extraction gate
├── SOURCE_BOUNDARY.md                      # candidate sources, ledger, D-06
├── AUDITOR_PLAYBOOK.md                     # fast path + reproduce + claim-replay
├── CONTRIBUTING.md, GOVERNANCE.md, RELEASING.md, ROADMAP.md, SECURITY.md
├── CHANGELOG.md, CITATION.cff, CODE_OF_CONDUCT.md
├── DATA_POLICY.md, PUBLIC_AUDIT_LIMITS.md
├── THIRD_PARTY_NOTICES.md, TRADEMARKS.md
├── pyproject.toml                          # gnosis-glyph-engine==0.1.0a1
├── _internal/                              # agent-orchestration scaffolding (not reader-facing)
│   ├── AUTONOMOUS_EXECUTION_POLICY.md
│   ├── GPD_BOOTSTRAP_GUIDE.md
│   ├── UNIVERSAL_STARTUP_PROMPT.md
│   ├── TEMPLATE_USAGE.md
│   ├── MIGRATION_PLAN.md
│   ├── WORKSTREAM_GPD_INIT_CHECKLIST.md
│   ├── TODO.md
│   └── AGENT_STATUS_REPORT_2026-04-24.md
├── .github/
│   ├── workflows/ci.yml
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE.md
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

## Licensing

This repository is part of the Zer0pa Gnosis Portfolio.

**Code** in this repository is licensed under the Apache License 2.0. See
`LICENSE` for the full text. SPDX identifier: `Apache-2.0`.

**Documentation, reports, and written materials** are licensed under Creative
Commons Attribution 4.0 International. SPDX identifier: `CC-BY-4.0`. Canonical
terms: <https://creativecommons.org/licenses/by/4.0/>.

**Data and fixtures** are handled per dataset and artifact family. See
`DATA_POLICY.md` for this repository's data boundary. The code license does not
license raw corpora, image-bearing cultural-heritage assets, private HF
artifacts, model weights, endpoint logs, or operational transcripts.

**Trademarks** - "Gnosis", "Zer0pa Gnosis", and distinctive sub-marks are
trademarks of Zer0pa. Apache-2.0 and CC-BY-4.0 do not grant trademark rights.
See `TRADEMARKS.md`.

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
- No real-glyph fixture; the synthetic 12-glyph generator is the only
  ablation surface today. Rights-cleared real-glyph evidence does not yet
  exist in this repo.
- Public contact surface remains owner-held.

## Upcoming Workstreams

### Operations / External Dependency

- **D-06 source-file retrieval** — owner action: retrieve
  `scripts/indus/stroke_native_encoding.py` and
  `scripts/indus/phase3_common.py` from the live monorepo, or grant pod
  access to a monorepo clone. All Phase 02b work is gated on this.

### Research-Deferred — Investigation Underway

- **Real-glyph fixture** — replace the deterministic 12-glyph synthetic
  generator with rights-cleared real-glyph evidence. No rights-cleared
  fixture exists yet; investigation of sourcing options is underway. Cross-
  corpus generalisation claims cannot be made until this is resolved.

### Active Engineering

- **Phase 02b — owned-arm gate testing** — implement
  `src/gnosis_glyph_engine/owned/stroke_compass.py` and
  `src/gnosis_glyph_engine/owned/topology.py` from the retrieved Indus
  source files; run ablation + robustness against the Phase 02c baseline
  ceiling; apply D-04 pass rule under D-02c-02 sovereign routing. Starts
  the moment D-06 clears.

### Zero-Base Scientific Thinking — GPD Research and Planning Pending

- None at this time.
