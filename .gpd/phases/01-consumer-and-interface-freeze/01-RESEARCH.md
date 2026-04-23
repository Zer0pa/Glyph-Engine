# Phase 01 Research: Consumer And Interface Freeze

Date: 2026-04-24
Author: autonomous execution (agent)
Scope: answer Phase 01 `ConsumerAndInterfaceFreeze` gate before any code
extraction begins in Phase 02.

## 1. Consumer Candidates Assessed

The `STATE.md` open question asks whether the first consumer is
`gnosis-morph-bench`, `gnosis-indus`, or a cuneiform rerun slice. Each
candidate was evaluated against the four extraction-forcing tests:

1. Does the candidate depend on a glyph-engine interface that does not yet
   exist in any admitted code?
2. Is the candidate's current smoke path blocked by the absence of that
   interface?
3. Does the candidate already own its own descriptor logic, making a
   glyph-engine package a net redundancy?
4. Is the candidate close enough to repo-custody execution that extraction
   pressure is real rather than aspirational?

### 1a. `gnosis-morph-bench`

Evidence reviewed:
- `workstreams/gnosis-morph-bench/05_repo_scaffold/PRD_GNOSIS_MORPH_BENCH_2026-04-23.md`
- `workstreams/gnosis-morph-bench/05_repo_scaffold/SOURCE_BOUNDARY.md`
- `workstreams/gnosis-morph-bench/05_repo_scaffold/src/gnosis_morph_bench/schema.py`
- `workstreams/gnosis-morph-bench/05_repo_scaffold/src/gnosis_morph_bench/benchmark.py`
- `workstreams/gnosis-morph-bench/05_repo_scaffold/src/gnosis_morph_bench/stability.py`
- `workstreams/gnosis-morph-bench/05_repo_scaffold/src/gnosis_morph_bench/cli.py`
- `workstreams/gnosis-morph-bench/05_repo_scaffold/fixtures/tiny_benchmark_manifest.json`

Key schema contract (`morph_bench.schema.BenchmarkManifest`):

```
BenchmarkItem:
    item_id: str
    reference_labels: dict[str, str]           # e.g. {"family": "alpha"}
    route_features: dict[str, tuple[float,...]] # e.g. {"route_clear": [0.1, 0.0]}
```

Observations:

- `route_features` are the numeric per-item per-route feature vectors that the
  route-scoring and stability helpers consume.
- The tiny smoke manifest ships those vectors as *hard-coded literal floats*
  with no provenance, no generator, and no link to any image.
- `PRD_GNOSIS_MORPH_BENCH_2026-04-23.md` explicitly names
  `workstreams/gnosis-glyph-engine/` as lane `L2 Glyph kernels` reachable
  `only through declared dependency`.
- The morph-bench source boundary lists its own admitted sources (Phase 4
  route-selection, stability, replay, benchmark manifest helpers). None of them
  produce image descriptors; all assume the vectors already exist.
- Therefore the morph-bench smoke path cannot be upgraded from literal floats
  to image-backed features without an external descriptor producer.

Verdict on the four tests:

1. Dependency on a missing interface: `YES`. The manifest schema requires
   `route_features`, and no repo currently owns a reproducible code path from
   an image to that vector.
2. Smoke blocked by the gap: `YES for image-backed smoke`. The current
   trivial-float smoke passes, but any realistic replay requires a descriptor
   producer.
3. Candidate already owns descriptors: `NO`. `SOURCE_BOUNDARY.md` forbids
   morph-bench from owning image preprocessing kernels.
4. Real extraction pressure: `YES`. The candidate is already a staged package
   with tests and an admitted PRD, so the gap is immediate, not aspirational.

### 1b. `gnosis-indus`

Evidence reviewed (briefly): sibling workstream exists with its own scaffold.
Its `SOURCE_BOUNDARY` retains stroke/native/ZPE pipeline script references as
internal domain logic. Moving those into glyph-engine now would drag domain
decisions into a methods repo, which the sovereign PRD and
`BUILD_VS_BORROW_CANON.md` explicitly forbid (see "contribute upstream instead
of building a new product" row on stroke-compass / topology descriptors).

Verdict: `NOT THE FIRST CONSUMER`. It may become a second consumer once the
glyph-engine has proven a non-domain interface with morph-bench.

### 1c. Cuneiform rerun slice

Evidence reviewed (briefly): `gnosis-cuneiform` sibling has its own scaffold;
tokenizer, P8 components, ensemble encoder files are live-monorepo artefacts
not present in this portfolio snapshot. No cuneiform code is currently
attempting to import a glyph-engine descriptor, so there is no existing
pressure point to freeze against.

Verdict: `NOT THE FIRST CONSUMER`. Defer until Phase 02/03.

## 2. Source-File Availability Audit

`SOURCE_BOUNDARY.md` names these candidate monorepo paths:

- `scripts/cuneiform/tokenizer_transfer.py`
- `scripts/cuneiform/p8_components.py`
- `scripts/cuneiform/ensemble_encoder.py`
- `scripts/indus/phase3_common.py`
- `scripts/indus/stroke_native_encoding.py`
- `scripts/indus/stroke_zpe_pipeline.py`

Audit result (systemwide search on 2026-04-24): **none of these files are
present in the portfolio snapshot**. They are live-monorepo references that
the scaffold was seeded with as *aspirational* extraction targets.

Consequence: Phase 01 can freeze interface, fixture, and ablation without
these files, but Phase 02 (Minimal Extraction Smoke) is blocked on sourcing
them from the live monorepo. This is recorded as an explicit exit condition
below.

## 3. Interface Design Space

The morph-bench contract reduces the interface to a single responsibility:
**turn an image (or other glyph sample) into a fixed-length numeric vector,
with a stable route name, deterministically.**

Three design choices were evaluated:

| Option | Shape | Verdict |
|---|---|---|
| A: Pure function `encode(image) -> vector` | No state, no registration | Minimal; adopted as the core of the protocol. |
| B: Class with `fit`/`transform` | Learnable descriptors (PCA, HOG+PCA) | Needed; included as a small stateful variant rather than a separate protocol. |
| C: Full framework (registry, batch scheduler, ANN) | Generic descriptor framework | Rejected by `BUILD_VS_BORROW_CANON.md` as redundant vs OpenCV / Faiss / sklearn. |

The frozen interface is Option A as the minimum and Option B as the admitted
extension. No framework layer is introduced.

## 4. Fixture Space

The fixture must:

- be generable in-repo with no external dataset and no rights issues,
- admit at least three labelled families so that NMI with null can be
  computed without degeneracy,
- be small enough that every ablation arm runs in under one minute on CPU.

Chosen fixture design: **12 synthetic binary glyphs, 3 families × 4 variants**
generated deterministically by a single seeded function. Each family is a
distinct parametric shape (e.g. cross-stroke, circle-with-stem, triangle-with-
dot). Variants apply bounded rotation, scale, thickness, and Gaussian noise.
Reference label: `family ∈ {A, B, C}`. No external images, no corpora leakage.

## 5. Ablation Space

`package_boundary_earned` requires ablation against borrowed public baselines.
The chosen baseline set is strictly commodity OSS, aligned with
`BUILD_VS_BORROW_CANON.md`:

| Arm | Library | Descriptor | Reduction | Dim |
|---|---|---|---|---|
| `baseline_orb` | OpenCV `cv2.ORB_create` | ORB keypoint descriptors | mean-pool over keypoints | 32 |
| `baseline_hu_regionprops` | scikit-image `measure.moments_hu` + `regionprops` | 7 Hu moments + 5 region scalars | concat | 12 |
| `baseline_hog` | scikit-image `feature.hog` + sklearn `PCA` | HOG features | PCA to 32 | 32 |
| `owned_stroke_compass` | candidate slice from `scripts/indus/stroke_native_encoding.py` | stroke-angle histogram family | mean-pool | 32 |
| `owned_topology` | candidate slice from `scripts/indus/phase3_common.py` | endpoint/junction/loop counts + graph stats | concat | ~16 |

Pass rule for the glyph-engine boundary (per `package_boundary_earned` gate 4):

> On the 12-glyph synthetic fixture, at least one owned arm must beat the best
> baseline arm by **≥ 0.5** on morph-bench's NMI-vs-null `sigma`, AND tie-or-
> beat the best baseline on `mean_jaccard` from `leave_fraction_out(0.25)`.

If no owned arm clears this threshold, the boundary is **not earned** and the
scaffold remains a hold surface. This is the falsification condition for the
package decision.

## 6. Destination Path Map

When Phase 02 extracts, files land in:

```
05_repo_scaffold/
├── src/gnosis_glyph_engine/
│   ├── __init__.py
│   ├── protocols.py               # Descriptor, LearnedDescriptor protocols
│   ├── fixtures.py                # 12-glyph synthetic generator
│   ├── manifest_builder.py        # -> morph-bench BenchmarkManifest JSON
│   ├── baselines/
│   │   ├── __init__.py
│   │   ├── orb.py                 # borrow: opencv-python
│   │   ├── hu_regionprops.py      # borrow: scikit-image
│   │   └── hog.py                 # borrow: scikit-image + scikit-learn
│   └── owned/
│       ├── __init__.py
│       ├── stroke_compass.py      # copy-with-rewrite from scripts/indus/stroke_native_encoding.py
│       └── topology.py            # copy-with-rewrite from scripts/indus/phase3_common.py
├── tests/
│   ├── test_fixtures.py
│   ├── test_baselines.py
│   ├── test_owned.py              # marked xfail until source is sourced
│   └── test_manifest_builder.py
└── scripts/
    └── run_ablation.py            # produces ablation_report.json
```

No file in `src/`, `tests/`, or `scripts/` is created in Phase 01. This is the
*frozen target* that Phase 02 implements under
`.gpd/phases/02-minimal-extraction-smoke/`.

## 7. Gate Verdict

Phase 01 can exit with:

- consumer frozen: `gnosis-morph-bench`,
- interface frozen: `Descriptor` protocol + `LearnedDescriptor` protocol +
  `manifest_builder` helper,
- fixture frozen: 12-glyph synthetic generator, 3 families × 4 variants,
- ablation frozen: 3 borrowed baselines + 2 owned candidates, with a numeric
  pass rule,
- destination path map frozen,
- blocker declared: owned-arm source code is absent from the portfolio
  snapshot; Phase 02 cannot run the owned arm until the live monorepo paths
  are sourced.

All four gate-4 sub-conditions of `package_boundary_earned` remain
`UNTESTED` because none have been executed yet. They can only be tested in
Phase 02 and Phase 03.

## 8. Open Questions Carried To Phase 02

- Who retrieves the two owned-arm source files from the live monorepo, and
  under what path or access mechanism?
- Does `cv2.ORB_create` run headless on the RunPod host? (expected yes with
  `opencv-python-headless`).
- Is `mean_jaccard` on `leave_fraction_out(0.25)` stable enough on 12 items,
  or must the fixture grow to 24 items before Phase 02? Decision deferred
  until a trial run exists.
