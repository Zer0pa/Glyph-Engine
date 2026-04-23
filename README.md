# Gnosis Glyph Engine

> Internal extraction-target scaffold for glyph geometry, stroke, and descriptor
> kernels. Not a public library yet.

## What This Repo Is

`gnosis-glyph-engine` is a migration scaffold for auditing reusable
image-to-geometry and glyph-descriptor code currently spread across Indus and
cuneiform source families. Its job is to decide whether a real package boundary
exists. It does not yet prove a reusable library, performance superiority, or a
commercial product.

## Current Authority

| Item | Current Truth |
|---|---|
| Product lane | `INTERNAL_EXTRACTION_TARGET` |
| Repo URL | `Zer0pa/Glyph-Engine` (private GitHub remote) |
| Default branch | `main` |
| Artefact failover | `Zer0pa/glyph-engine-artefacts` (Hugging Face, private) |
| Acquisition surface | internal only |
| Current authority artifact | `SOURCE_BOUNDARY.md` and `SOVEREIGN_PRD.md` |
| Authority metric | `package_boundary_earned` |
| Metric verdict | `UNTESTED` |
| Active phase | Phase 02 (BLOCKED on owned-arm source retrieval, D-06) |
| License | `OWNER_DEFERRED` |
| Primary contact | owner-controlled private coordination path |

## Phase Progress

| Phase | Status |
|---|---|
| 00 Hold-Surface Bootstrap | Complete (2026-04-23) |
| 01 Consumer And Interface Freeze | Complete (2026-04-24) |
| 02 Minimal Extraction Smoke | Blocked on D-06 |
| 03 Package-Boundary Review | Pending |

Phase 01 froze the first consumer (`gnosis-morph-bench`), the minimum
`Descriptor` / `LearnedDescriptor` interface, the 12-glyph synthetic smoke
fixture, and a five-arm ablation with a numeric pass rule. See
`.gpd/phases/01-consumer-and-interface-freeze/` for the freeze artefacts.

## What We Prove Now

- The package has a named first consumer and a named minimum interface.
- The scaffold identifies candidate glyph/geometry source families for later
  extraction.
- The current evidence does not justify public library promotion.
- Any future extraction must be forced by Phase 02 execution of the frozen
  ablation.

## What We Do Not Claim

- No clean installable `gnosis_glyph_engine` package exists yet.
- No in-repo ablation result exists yet; the rule to produce one has been
  frozen but not executed.
- This scaffold does not own Indus or cuneiform scientific findings.

## Read Next

| Need | File |
|---|---|
| Sovereign hold/extraction brief | `SOVEREIGN_PRD.md` |
| Candidate source families + destination paths | `SOURCE_BOUNDARY.md` |
| Frozen consumer, interface, fixture, ablation | `.gpd/phases/01-consumer-and-interface-freeze/01-DECISIONS.md` |
| Data and rights posture | `DATA_POLICY.md` |
| Architecture truth map | `docs/ARCHITECTURE.md` |
| Current gaps | `TODO.md` |
| GPD state | `.gpd/PROJECT.md`, `.gpd/STATE.md` |

## Current Gaps

- No code has been extracted into this scaffold.
- No `pyproject.toml`, package root, smoke path, or blind-clone result exists
  yet (all deferred to Phase 02).
- Owned-arm source files not present in portfolio snapshot (D-06 blocker).
- Final license and public contact fields remain owner-deferred.
