# Source Boundary

## Lane Role

`gnosis-glyph-engine` is a hold/extraction target for reusable glyph geometry
and descriptor kernels. It owns no domain verdicts.

## Candidate Source Families

These are candidates for Phase 02 extraction, not admitted package code.
Availability audited on 2026-04-24 against the current portfolio snapshot.

| Candidate path | Intended owned arm | Availability | Phase 02 posture |
|---|---|---|---|
| `scripts/cuneiform/tokenizer_transfer.py` | deferred (not first-consumer need) | NOT PRESENT in snapshot | defer to Phase 03+ |
| `scripts/cuneiform/p8_components.py` | deferred | NOT PRESENT in snapshot | defer to Phase 03+ |
| `scripts/cuneiform/ensemble_encoder.py` | deferred | NOT PRESENT in snapshot | defer to Phase 03+ |
| `scripts/indus/phase3_common.py` | `owned_topology` | NOT PRESENT in snapshot | BLOCKED on retrieval (D-06) |
| `scripts/indus/stroke_native_encoding.py` | `owned_stroke_compass` | NOT PRESENT in snapshot | BLOCKED on retrieval (D-06) |
| `scripts/indus/stroke_zpe_pipeline.py` | deferred | NOT PRESENT in snapshot | defer to Phase 03+ |
| Indus Phase 4 route-selection helpers (cited) | deferred | cited-only | defer |

## Frozen First Consumer (Phase 01, D-01)

- Consumer: `gnosis-morph-bench`.
- Interface it requires: `Descriptor` and `LearnedDescriptor` protocols plus a
  `manifest_builder` helper that emits `morph_bench.schema.BenchmarkManifest`
  JSON.
- Coupling posture: one-way. `gnosis-morph-bench` imports nothing from
  `gnosis-glyph-engine`; `gnosis-glyph-engine` writes JSON that morph-bench
  already loads.

## Destination Path Map (Phase 02 target; empty in Phase 01)

```
05_repo_scaffold/
├── src/gnosis_glyph_engine/
│   ├── __init__.py
│   ├── protocols.py
│   ├── fixtures.py
│   ├── manifest_builder.py
│   ├── baselines/{__init__,orb,hu_regionprops,hog}.py
│   └── owned/{__init__,stroke_compass,topology}.py
├── tests/test_fixtures.py, test_baselines.py, test_owned.py, test_manifest_builder.py
└── scripts/run_ablation.py
```

## Borrowed Dependencies (Phase 02 target)

Per `_control/research/BUILD_VS_BORROW_CANON.md`:

- `numpy` — array math (borrow, definite).
- `opencv-python-headless` — ORB descriptor baseline.
- `scikit-image` — Hu moments, regionprops, HOG.
- `scikit-learn` — PCA reduction for HOG arm.
- `gnosis-morph-bench` — evaluator (local source dependency via path or future
  package pin; not vendored).

## Explicit Exclusions

- Indus catalogue, cluster, phonotactic, or search verdicts.
- Cuneiform benchmark/control verdicts.
- morph-bench metric ownership.
- Falsification-harness scorecard ownership.
- HTR/OCR engines, vector databases, viewers, and annotation tools.
- Public dataset release.
- Any learned-weights shipping.

## Coupling Risks Tracked

- Source files are path-coupled to the live monorepo and currently absent
  from the portfolio snapshot. Phase 02 is blocked on retrieval of the two
  Indus files listed under `BLOCKED on retrieval`.
- Descriptor logic in the original files is mixed with domain scripts;
  Phase 02 must record every copied file, every path rewrite, and every
  borrowed dependency before implementation (see `CONVENTIONS.md` extraction
  rule).

## Extraction Rule

Do not copy code into this scaffold until the owned-arm files are retrieved
and recorded here with `ADMITTED` status. Record every copied file, every
path rewrite, and every borrowed dependency in this file before
implementation.
