# Architecture

## Purpose

This file states the current technical truth: there is no extracted
glyph-engine package yet. Phase 01 froze the architecture target; Phase 02
will materialise it.

## System Snapshot

| Layer | What Lives Here | Source Of Truth |
|---|---|---|
| Public docs | hold/extraction posture | `README.md`, `SOVEREIGN_PRD.md` |
| Candidate source families | monorepo source inventory (not present in snapshot; blocked retrieval) | `SOURCE_BOUNDARY.md` |
| Code/runtime | none extracted yet | `TODO.md`, `code/README.md` |
| Evidence artefacts | Phase 01 freeze artefacts only | `.gpd/phases/01-consumer-and-interface-freeze/` |
| Owner-held context | license, contact, private assets | `DATA_POLICY.md` |
| Remotes | private GitHub + HF dataset | `MIGRATION_PLAN.md`, `.gpd/CONVENTIONS.md` |

## Component Map (Phase 02 target)

| Component | Responsibility | Current status |
|---|---|---|
| `Descriptor` protocol | stateless `encode(image) -> vector` contract | FROZEN (Phase 01 D-02); unimplemented |
| `LearnedDescriptor` protocol | `fit` + `encode`, for HOG+PCA style arms | FROZEN (Phase 01 D-02); unimplemented |
| `manifest_builder` | emits morph-bench `BenchmarkManifest` JSON | FROZEN (Phase 01 D-02); unimplemented |
| `fixtures.synthesize_twelve_glyphs` | deterministic 12-glyph binary fixture | FROZEN (Phase 01 D-03); unimplemented |
| `baselines.orb` | OpenCV ORB keypoint mean-pool | FROZEN (Phase 01 D-04); unimplemented |
| `baselines.hu_regionprops` | Hu moments + regionprops | FROZEN (Phase 01 D-04); unimplemented |
| `baselines.hog` | skimage HOG + sklearn PCA(32) | FROZEN (Phase 01 D-04); unimplemented |
| `owned.stroke_compass` | owned descriptor candidate | FROZEN (Phase 01 D-04); BLOCKED on D-06 |
| `owned.topology` | owned descriptor candidate | FROZEN (Phase 01 D-04); BLOCKED on D-06 |
| `scripts.run_ablation` | produces `artifacts/ablation_report.json` | FROZEN (Phase 01 D-04); unimplemented |

## Data Flow (Phase 02 target)

```text
fixtures.synthesize_twelve_glyphs(seed=42)
        |
        v
[12 binary images, 3 family labels]
        |
        +--> baselines.orb -----------\
        +--> baselines.hu_regionprops --\
        +--> baselines.hog ---------------\       build one BenchmarkManifest
        +--> owned.stroke_compass --------+----->  per arm via manifest_builder
        +--> owned.topology --------------/
                                                        |
                                                        v
                                                  gnosis-morph-bench
                                                  (NMI+null, silhouette,
                                                   deterministic_replay,
                                                   leave_fraction_out)
                                                        |
                                                        v
                                       artifacts/ablation_report.json
```

## Truth Surface Boundaries

- `README.md` owns current posture.
- `SOVEREIGN_PRD.md` owns the extraction gate.
- `SOURCE_BOUNDARY.md` owns candidate source families, destination path map,
  and the owned-arm blocker.
- `DATA_POLICY.md` owns what may be copied.
- `.gpd/phases/01-consumer-and-interface-freeze/01-DECISIONS.md` owns the
  frozen interface, fixture, and ablation rule.
- No file may claim public package readiness until `package_boundary_earned`
  passes Phase 03.

## Known Gaps

- Phase 02 code not written.
- Owned-arm source files not retrieved (D-06).
- No RunPod workspace provisioned.
- No `pyproject.toml`, smoke path, or benchmark artefact yet.
