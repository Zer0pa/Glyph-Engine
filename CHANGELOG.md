# Changelog — gnosis-glyph-engine

All notable changes to this repository are documented here.

## [Unreleased] — Phase 02b blocked on D-06

Phase 02b (Owned-Arm Ablation) blocked pending D-06 source-file retrieval.
Phase 03 (Package-Boundary Review) not started.

## 2026-04-28 — Ops-Gates adoption and playbook coherence wave

- Added root `AGENTS.md` with current lane truth and agent check instructions.
- Added local Ops-Gates-derived coupling audit and wired it into CI before
  package installation without requiring a sibling checkout.
- Refreshed release, audit-limit, data-policy, roadmap, architecture, legal,
  and internal TODO/startup surfaces to remove stale pre-Phase-02 evidence and
  pre-license language.
- Preserved `package_boundary_earned = UNTESTED`, D-06 blocker, and all
  no-claim boundaries.

## 2026-04-28 — Public refresh wave

- Added live-window banner to README (Zer0pa ethos: always-in-beta).
- Added `## Commercial Readiness` section with canonical Verdict cell (`BLOCKED`)
  and Posture row (`package_boundary_unearned_pending_owned_arm_d06`).
- Added `§11 Upcoming Workstreams` section with 4-category taxonomy.
- Added headline-first defensible metric and honest-blocker line to §1 prose.
- Relocated agent-orchestration scaffolding to `_internal/` (not reader-facing).
- Added `CHANGELOG.md`, `CITATION.cff`, `CODE_OF_CONDUCT.md`.
- Applied ≥10 GitHub topics; rewrote repo description to public-truth line.
- Pre-commit verification: name-leakage grep = 0 results; no drift residue.

## 2026-04-24 — Phase 02c closeout (baseline robustness)

- Multi-seed (10-seed) borrowed-baseline robustness run complete.
  Results in `artifacts/robustness/robustness_report.json`.
- Retired D-02a-06 fixture-saturation risk via multi-seed evidence (D-02c-01).
- Sovereign-vs-adapter scope decision: stays sovereign (D-02c-02).
- Endpoint-leak scan passed (Gate D).
- `HF_CUSTODY_REGISTER.md` produced with production-token verification.
- Added `docs/PROVENANCE_LABELS.md` path-scrub convention.

## 2026-04-24 — Phase 02a (borrowed-baseline sanity path)

- Implemented `src/gnosis_glyph_engine/` borrowed-arm tree (ORB,
  hu_regionprops, HOG baselines).
- 17 pytest tests pass with sibling `gnosis-morph-bench`; 16 + 1 skip without.
- `artifacts/ablation/ablation_report.json` produced; SHA256-pinned.
- Mirrored artefacts to HF dataset `Architect-Prime/glyph-engine-artefacts`.

## 2026-04-24 — Phase 01 (consumer and interface freeze)

- Frozen consumer: `gnosis_morph_bench.schema.load_manifest`.
- Frozen interface: `Descriptor`, `LearnedDescriptor`, `manifest_builder`.
- Frozen fixture: deterministic 12-glyph synthetic generator.
- Frozen ablation rule (D-04 pass rule documented).

## 2026-04-23 — Phase 00 (workstream bootstrap)

- Repository scaffolded; GPD state machine initialised.
- `SOVEREIGN_PRD.md`, `SOURCE_BOUNDARY.md`, `DATA_POLICY.md` authored.
- `package_boundary_earned` authority metric defined: UNTESTED.
