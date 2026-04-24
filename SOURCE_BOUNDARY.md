# Source Boundary

## Lane Role

`gnosis-glyph-engine` is a hold/extraction target for reusable glyph geometry
and descriptor kernels. It owns no domain verdicts.

## Candidate Source Families

Availability audited 2026-04-24 against the current portfolio snapshot.

| Candidate path | Intended owned arm | Availability | Phase posture |
|---|---|---|---|
| `scripts/cuneiform/tokenizer_transfer.py` | deferred | NOT PRESENT | Phase 03+ |
| `scripts/cuneiform/p8_components.py` | deferred | NOT PRESENT | Phase 03+ |
| `scripts/cuneiform/ensemble_encoder.py` | deferred | NOT PRESENT | Phase 03+ |
| `scripts/indus/phase3_common.py` | `owned_topology` | NOT PRESENT | Phase 02b — BLOCKED on D-06 |
| `scripts/indus/stroke_native_encoding.py` | `owned_stroke_compass` | NOT PRESENT | Phase 02b — BLOCKED on D-06 |
| `scripts/indus/stroke_zpe_pipeline.py` | deferred | NOT PRESENT | Phase 03+ |
| Indus Phase 4 route-selection helpers (cited) | deferred | cited-only | Phase 03+ |

## Frozen First Consumer (Phase 01, D-01)

- Consumer: `gnosis-morph-bench`.
- Interface it requires: `Descriptor` and `LearnedDescriptor` protocols plus
  a `manifest_builder` helper that emits `morph_bench.schema.BenchmarkManifest`
  JSON.
- Coupling posture: one-way. `gnosis-morph-bench` imports nothing from
  `gnosis-glyph-engine`; `gnosis-glyph-engine` emits JSON morph-bench loads
  and imports `gnosis_morph_bench.{schema,benchmark,stability}` at ablation
  time.

## Phase 02a Extraction Ledger

Phase 02a authored glue code over public OSS imports (`cv2`, `skimage`,
`sklearn`). **Zero monorepo source files were copied.** The path-rewrite
ledger is therefore empty for Phase 02a.

| File created | Source | Copied? | Rewrites |
|---|---|---|---|
| `src/gnosis_glyph_engine/__init__.py` | newly authored | no | — |
| `src/gnosis_glyph_engine/protocols.py` | newly authored | no | — |
| `src/gnosis_glyph_engine/fixtures.py` | newly authored | no | — |
| `src/gnosis_glyph_engine/manifest_builder.py` | newly authored | no | — |
| `src/gnosis_glyph_engine/baselines/__init__.py` | newly authored | no | — |
| `src/gnosis_glyph_engine/baselines/orb.py` | newly authored (wraps `cv2.ORB_create`) | no | — |
| `src/gnosis_glyph_engine/baselines/hu_regionprops.py` | newly authored (wraps `skimage.measure`) | no | — |
| `src/gnosis_glyph_engine/baselines/hog.py` | newly authored (wraps `skimage.feature.hog` + `sklearn.decomposition.PCA`) | no | — |
| `src/gnosis_glyph_engine/owned/__init__.py` | placeholder | no | — |
| `src/gnosis_glyph_engine/scripts/run_ablation.py` | newly authored | no | — |
| `tests/*.py` | newly authored | no | — |
| `scripts/run_ablation.py` | thin shim into package | no | — |

## Phase 02b Extraction Ledger (to be filled when D-06 clears)

| File to create | Source (live monorepo) | Rewrites planned |
|---|---|---|
| `src/gnosis_glyph_engine/owned/stroke_compass.py` | `scripts/indus/stroke_native_encoding.py` | TBD at Phase 02b kickoff |
| `src/gnosis_glyph_engine/owned/topology.py` | `scripts/indus/phase3_common.py` | TBD at Phase 02b kickoff |

## Destination Path Map (Phase 02 target; Phase 02a done, Phase 02b pending)

```
05_repo_scaffold/
├── src/gnosis_glyph_engine/
│   ├── __init__.py                   [02a ✓]
│   ├── protocols.py                  [02a ✓]
│   ├── fixtures.py                   [02a ✓]
│   ├── manifest_builder.py           [02a ✓]
│   ├── baselines/
│   │   ├── __init__.py               [02a ✓]
│   │   ├── orb.py                    [02a ✓]
│   │   ├── hu_regionprops.py         [02a ✓]
│   │   └── hog.py                    [02a ✓]
│   ├── owned/
│   │   ├── __init__.py               [02a ✓ placeholder]
│   │   ├── stroke_compass.py         [02b pending]
│   │   └── topology.py               [02b pending]
│   └── scripts/
│       ├── __init__.py               [02a ✓]
│       └── run_ablation.py           [02a ✓]
├── tests/                            [02a ✓]
└── scripts/run_ablation.py           [02a ✓ thin shim]
```

## Borrowed Dependencies (admitted 2026-04-24)

Per `_control/research/BUILD_VS_BORROW_CANON.md`:

- `numpy>=1.24` — array math.
- `opencv-python-headless>=4.8` — ORB descriptor baseline.
- `scikit-image>=0.22` — Hu moments, regionprops, HOG.
- `scikit-learn>=1.3` — PCA reduction for HOG arm.
- `gnosis-morph-bench` (sibling, editable path install on execution host).

## Explicit Exclusions

- Indus catalogue, cluster, phonotactic, or search verdicts.
- Cuneiform benchmark/control verdicts.
- morph-bench metric ownership.
- Falsification-harness scorecard ownership.
- HTR/OCR engines, vector databases, viewers, and annotation tools.
- Public dataset release.
- Any learned-weights shipping.

## Coupling Risks Tracked

- Source files path-coupled to live monorepo, currently absent from the
  snapshot. Phase 02b is blocked on retrieval of the two Indus files listed
  under `Phase 02b Extraction Ledger`.
- Phase 02a did not touch monorepo code; coupling risk is strictly deferred
  to Phase 02b.

## Extraction Rule

Do not copy code into this scaffold until the owned-arm files are retrieved
and recorded here with `COPIED` status. Record every copied file, every path
rewrite, and every borrowed dependency in this file before implementation.
