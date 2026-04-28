# Architecture

## Purpose

Technical truth map after Phase 02c and the Ops-Gates adoption wave. Phase 01
froze the architecture target; Phase 02a materialised the borrowed-baseline
runtime; Phase 02c added the multi-seed baseline ceiling and retired the
single-seed fixture-saturation concern. Phase 02b will materialise the
owned-arm half once D-06 clears.

## System Snapshot

| Layer | What Lives Here | Source Of Truth |
|---|---|---|
| Public docs | extraction posture, evidence, non-claims | `README.md`, `SOVEREIGN_PRD.md` |
| Candidate source families | extraction ledger + destination map | `SOURCE_BOUNDARY.md` |
| Code/runtime | borrowed baselines + fixture + manifest builder | `src/gnosis_glyph_engine/` |
| Tests | 17 tests with Morph-Bench; 16 pass + 1 skip without | `tests/` |
| Evidence artefacts | Phase 01 freeze, Phase 02a ablation, Phase 02c robustness | `.gpd/phases/`, `artifacts/ablation/`, `artifacts/robustness/` |
| Operational gate | Ops-Gates coupling audit on executable Python surfaces | `tools/gnosis_ops_gates/coupling_audit.py`, `.github/workflows/ci.yml` |
| Remotes | GitHub + private HF artefact dataset | `HF_CUSTODY_REGISTER.md`, `.gpd/CONVENTIONS.md` |

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
| `scripts.run_robustness` | produces `artifacts/robustness/robustness_report.json` | IMPLEMENTED (Phase 02c) |
| `tools/gnosis_ops_gates/coupling_audit.py` | rejects concrete operational leakage in `src`, `tests`, `scripts` | IMPLEMENTED (Ops-Gates adoption wave) |

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
  Phase 02a split-sub-phase decision and the now-retired seed=42
  baseline-saturation risk.
- `.gpd/phases/02-minimal-extraction-smoke/02-02-DECISIONS.md` owns the
  Phase 02c multi-seed correction and sovereign-vs-adapter routing.
- `artifacts/ablation/ablation_report.json` owns the measured metric matrix.
- `artifacts/robustness/robustness_report.json` owns the multi-seed borrowed
  baseline ceiling.
- No file may claim public package readiness until `package_boundary_earned`
  passes Phase 03.

## Known Gaps

- Owned-arm code not written (D-06).
- Phase 03 package-boundary review not started.
- No rights-cleared real-glyph fixture exists.
- Apache-2.0 / CC-BY-4.0 licensing is present but does not close the
  package-boundary gate.
