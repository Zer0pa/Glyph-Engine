# Governance

## Scope

This repo governs extraction-boundary decisions for `gnosis-glyph-engine`.

## Truth Hierarchy

1. `SOVEREIGN_PRD.md`
2. `SOURCE_BOUNDARY.md`
3. repo-local artifacts from Phase 02a/02c and future phases
4. README and supporting docs

## Decision Rights

| Topic | Authority | Notes |
|---|---|---|
| Extraction boundary | repo owner or delegated maintainer | must update PRD and source boundary |
| Public package claims | blocked | requires D-06, Phase 02b, and Phase 03 package-boundary review |
| Release approval | blocked | requires package-boundary pass plus operator/orchestrator approval |
| Legal statements | owner | Apache-2.0 code and CC-BY-4.0 docs are present; licensing does not close the package gate |

## Status Vocabulary

Use status words only when an artifact path supports the state. The parser-facing
Commercial Readiness verdict enum is locked to `{STAGED, PASS, PARTIAL,
BLOCKED, FAIL, INCONCLUSIVE}`.
