# Architecture

## Purpose

Technical truth map after Phase 02a. Phase 01 froze the architecture target;
Phase 02a materialised the borrowed-baseline half; Phase 02b will materialise
the owned-arm half once D-06 clears.

## System Snapshot

| Layer | What Lives Here | Source Of Truth |
|---|---|---|
| Public docs | hold/extraction posture | `README.md`, `SOVEREIGN_PRD.md` |
| Candidate source families | extraction ledger + destination map | `SOURCE_BOUNDARY.md` |
| Code/runtime | borrowed baselines + fixture + manifest builder | `src/gnosis_glyph_engine/` |
| Tests | 16-test pytest suite passing on Python 3.13 | `tests/` |
| Evidence artefacts | Phase 01 freeze + Phase 02a ablation | `.gpd/phases/`, `artifacts/ablation/` |
| Remotes | private GitHub + HF dataset | `MIGRATION_PLAN.md`, `.gpd/CONVENTIONS.md` |

## Component Map

| Component | Responsibility | Current status |
|---|---|---|
| `Descriptor` protocol | stateless `encode(image) -> vector` contract | IMPLEMENTED (Phase 02a) |
| `LearnedDescriptor` protocol | `fit` + `encode` | IMPLEMENTED (Phase 02a) |
| `manifest_builder.build_manifest` | emits morph-bench schema-v1 dict | IMPLEMENTED (Phase 02a) |
| `fixtures.synthesize_twelve_glyphs` | deterministic 12-glyph fixture | IMPLEMENTED (Phase 02a) |
| `baselines.OrbDescriptor` | OpenCV ORB mean-pool, 32-d | IMPLEMENTED (Phase 02a) |
| `baselines.HuRegionpropsDescriptor` | skimage Hu + regionprops, 12-d | IMPLEMENTED (Phase 02a) |
| `baselines.HogPcaDescriptor` | skimage HOG + sklearn PCA, 32-d | IMPLEMENTED (Phase 02a) |
| `owned.stroke_compass` | from `scripts/indus/stroke_native_encoding.py` | BLOCKED on D-06 |
| `owned.topology` | from `scripts/indus/phase3_common.py` | BLOCKED on D-06 |
| `scripts.run_ablation` | produces `artifacts/ablation/ablation_report.json` | IMPLEMENTED (Phase 02a; extendable for owned arms) |

## Data Flow (Phase 02a implementation; arrows that actually run today)

```text
fixtures.synthesize_twelve_glyphs(seed=42)
        |
        v
[12 binary uint8 images, family labels A/B/C]
        |
        +--> baselines.OrbDescriptor.encode()            --\
        +--> baselines.HuRegionpropsDescriptor.encode()   --\
        +--> baselines.HogPcaDescriptor.fit().encode()     --+--> build_manifest()
        +==  owned.stroke_compass (BLOCKED on D-06) =======+     (one manifest per arm)
        +==  owned.topology (BLOCKED on D-06)      =======/                 |
                                                                            v
                                                                    gnosis_morph_bench
                                                                    ├── schema.load_manifest
                                                                    ├── benchmark.evaluate_routes
                                                                    ├── stability.deterministic_replay
                                                                    └── stability.leave_fraction_out
                                                                            |
                                                                            v
                                                            artifacts/ablation/ablation_report.json
```

## Truth Surface Boundaries

- `README.md` owns current posture and phase-progress table.
- `SOVEREIGN_PRD.md` owns the extraction gate.
- `SOURCE_BOUNDARY.md` owns candidate source families, destination path
  map, and the path-rewrite ledger.
- `DATA_POLICY.md` owns what may be copied.
- `.gpd/phases/01-consumer-and-interface-freeze/01-DECISIONS.md` owns the
  frozen Phase 01 interface, fixture, and ablation rule.
- `.gpd/phases/02-minimal-extraction-smoke/02-01-DECISIONS.md` owns the
  Phase 02a split-sub-phase decision and the baseline-saturation risk.
- `artifacts/ablation/ablation_report.json` owns the measured metric matrix.
- No file may claim public package readiness until `package_boundary_earned`
  passes Phase 03.

## Known Gaps

- Owned-arm code not written (D-06).
- Phase 03 fixture-hardening decision not made (D-02a-06).
- No `pyproject.toml` license text; still `OWNER_DEFERRED`.
