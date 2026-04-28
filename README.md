# Gnosis Glyph Engine

> Glyph descriptor/package-boundary research lane. Website-sync posture: staged/WIP, licensed code, public visibility blocked until the package boundary is earned.

## What This Is

`gnosis-glyph-engine` asks one falsifiable question: is a standalone glyph-engine package boundary earned by a real consumer, a monorepo-free smoke path, and a descriptor ablation against borrowed baselines? It is an extraction-target scaffold for reusable glyph geometry, stroke, and descriptor kernels. It is **not** a public library, **not** a product, and **not** a decipherment claim.

Headline metrics: 10-seed borrowed-baseline ablation records mean sigma `baseline_orb = 4.14 +/- 1.12`, `baseline_hu_regionprops = 2.95 +/- 1.06`, and `baseline_hog = 1.15 +/- 1.17`. Determinism holds with `replay_all_identical == true` for every arm in the seed-42 ablation.

Honest blocker: `package_boundary_earned = UNTESTED`. D-06 source-file retrieval is still required before owned-arm testing can begin. No real-glyph fixture exists yet.

| Field | Value |
|-------|-------|
| Architecture | GLYPH_DESCRIPTOR_STREAM |
| Encoding | GLYPH_DESCRIPTOR_ABLATION_V1 |

## Key Metrics

| Metric | Value | Baseline |
|---|---:|---|
| PYTEST_PASS | 16 passed / 1 skipped | no sibling |
| BORROWED_ORB_SIGMA | 4.14 +/- 1.12 | 10 seeds |
| BORROWED_HU_SIGMA | 2.95 +/- 1.06 | 10 seeds |
| PACKAGE_BOUNDARY_EARNED | UNTESTED | D-06 |

> Source: `tests/`, `artifacts/ablation/ablation_report.json`, `artifacts/robustness/robustness_report.json`, and `SOURCE_BOUNDARY.md`.

## What We Prove

- The frozen Phase 01 interface is implementable using borrowed OSS: OpenCV, scikit-image, scikit-learn, and NumPy.
- The package installs cleanly with `pip install -e .[dev]` without live-monorepo imports or path coupling.
- The test suite passes with one clean skip when sibling `gnosis-morph-bench` is unavailable, preserving repo independence.
- The Ops-Gates-derived coupling audit runs in CI before package installation.
- Borrowed-baseline ablation and robustness artifacts are recorded and deterministic.

## What We Don't Claim

- We do not claim any owned descriptor beats borrowed baselines.
- We do not claim the package boundary is earned; `package_boundary_earned` is `UNTESTED`.
- We do not claim cross-corpus generalization or rights-cleared real-glyph evidence.
- We do not claim public-release readiness, performance superiority, product readiness, or Indus/cuneiform domain results.

## Commercial Readiness

| Field | Value |
|-------|-------|
| Verdict | BLOCKED |
| Commit SHA | ede989f7a1f0 |
| Source | SOURCE_BOUNDARY.md |

`BLOCKED` is the honest state because the authority metric is untested. Code/docs are licensed, but public visibility and product framing wait for D-06, owned-arm evaluation, and real-glyph fixture provenance.

## Tests and Verification

| Code | Check | Verdict |
|---|---|---|
| V_01 | `python tools/gnosis_ops_gates/coupling_audit.py src tests scripts` | PASS |
| V_02 | `pip install -e .[dev]` | PASS |
| V_03 | `pytest -q` without sibling Morph-Bench | PASS |
| V_04 | borrowed-baseline ablation/robustness artifacts | PASS |

## Proof Anchors

| Path | State |
|---|---|
| `SOVEREIGN_PRD.md` | VERIFIED |
| `SOURCE_BOUNDARY.md` | VERIFIED |
| `artifacts/ablation/ablation_report.json` | VERIFIED |
| `artifacts/robustness/robustness_report.json` | VERIFIED |
| `.gpd/phases/02-minimal-extraction-smoke/02-02-VERIFICATION.md` | VERIFIED |
| `tools/gnosis_ops_gates/coupling_audit.py` | VERIFIED |
| `.github/workflows/ci.yml` | VERIFIED |
| `AUDITOR_PLAYBOOK.md` | VERIFIED |

## Repo Shape

| Field | Value |
|---|---|
| Package | `gnosis-glyph-engine` |
| Source | `src/gnosis_glyph_engine/` |
| Tests | `tests/` |
| Scripts | `scripts/run_ablation.py`, package console scripts |
| Evidence | `artifacts/ablation/`, `artifacts/robustness/`, `.gpd/` |
| Gate tooling | `tools/gnosis_ops_gates/coupling_audit.py` |
| Legal/Data | `LICENSE`, `NOTICE`, `DATA_POLICY.md`, `docs/LEGAL_BOUNDARIES.md` |

## Quick Start

```bash
git clone https://github.com/Zer0pa/Glyph-Engine.git
cd Glyph-Engine
python3.13 -m venv .venv
source .venv/bin/activate
python tools/gnosis_ops_gates/coupling_audit.py src tests scripts
pip install -e .[dev]
pytest -q
python -m gnosis_glyph_engine.scripts.run_ablation
python -m gnosis_glyph_engine.scripts.run_robustness
```

Expected without sibling Morph-Bench installed: `16 passed, 1 skipped`. With sibling Morph-Bench installed, the optional contract test should run.

## Upcoming Workstreams

> This section captures the active lane priorities — what the next agent or contributor picks up, and what investors should expect. Cadence is continuous, not milestoned.

- **D-06 source-file retrieval** — Operations / External Dependency. Retrieve `scripts/indus/stroke_native_encoding.py` and `scripts/indus/phase3_common.py`, or grant pod access to a live-monorepo clone.
- **Phase 02b owned-arm gate testing** — Active Engineering. Start only after D-06 clears; implement owned stroke/topology arms and compare against the Phase 02c borrowed-baseline ceiling.
- **Real-glyph fixture** — Research-Deferred — Investigation Underway. Replace the deterministic synthetic generator with rights-cleared real-glyph evidence before any cross-corpus claim.
- **Boundary rethink** — Zero-Base Scientific Thinking — GPD Research and Planning Pending. Trigger only if owned-arm evidence fails to justify a standalone package boundary.

## Licensing

This repository is part of the Zer0pa Gnosis Portfolio.

**Code** in this repository is licensed under the Apache License 2.0. See `LICENSE`. SPDX identifier: `Apache-2.0`.

**Documentation, reports, and written materials** are licensed under Creative Commons Attribution 4.0 International. SPDX identifier: `CC-BY-4.0`.

**Data, fixtures, corpora, image-bearing cultural-heritage assets, private HF artifacts, model weights, endpoint logs, and operational transcripts** are not licensed by the code or documentation licenses. Their boundary is governed by `DATA_POLICY.md`, artifact-specific notices, and any future owner admission record.

**Trademarks** - "Gnosis", "Zer0pa Gnosis", and distinctive sub-marks are trademarks of Zer0pa. Apache-2.0 and CC-BY-4.0 do not grant trademark rights. See `TRADEMARKS.md`.

Public visibility is a separate repository-setting action. These license files define the open code/docs posture; they do not publish rights-gated data.
