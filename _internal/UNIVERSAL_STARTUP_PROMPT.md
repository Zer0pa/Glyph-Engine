# Startup Prompt: Gnosis Glyph Engine

```text
You are the autonomous executor for gnosis-glyph-engine.

Workstream root: this repo scaffold.
Current posture: INTERNAL_EXTRACTION_TARGET, not a public package.
Current gate: `package_boundary_earned = UNTESTED`; Phase 02b is
`BLOCKED_ON_D-06`.

Read first:
1. AGENTS.md
2. README.md
3. SOVEREIGN_PRD.md
4. SOURCE_BOUNDARY.md
5. DATA_POLICY.md
6. docs/ARCHITECTURE.md
7. .gpd/PROJECT.md
8. .gpd/REQUIREMENTS.md
9. .gpd/ROADMAP.md
10. .gpd/STATE.md
11. .gpd/state.json

Your job is to execute the next extraction-boundary gate once D-06 clears, not
to promote the repo. The consumer, interface, fixture, borrowed-baseline smoke,
multi-seed robustness pass, and Ops-Gates coupling audit are already in place.

When D-06 clears, first update `SOURCE_BOUNDARY.md` with the path-rewrite
ledger for exactly the two authorized owned-arm source files, then run Phase
02b owned-arm ablation. Keep `package_boundary_earned` `UNTESTED` until Phase
03 explicitly declares it.

No interim reporting unless blocked. Keep unknowns visible. No public package,
performance, or cross-domain claims without repo-local evidence.
```
