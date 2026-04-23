# Phase 01 Decisions

Date: 2026-04-24
Status: `FROZEN`

These decisions are the authoritative output of Phase 01. Phase 02 implements
exactly what is named below, and no more.

## D-01 First admitted consumer

- Decision: `gnosis-morph-bench` is the first admitted consumer of
  `gnosis-glyph-engine`.
- Evidence: morph-bench's `BenchmarkManifest.route_features` schema requires
  per-item per-route numeric vectors that no repo currently produces from
  images; its staged `src/gnosis_morph_bench/` package is the only sibling
  whose smoke path is blocked by the gap.
- Rollback trigger: morph-bench re-internalises descriptor production, or a
  second consumer with stronger pressure appears and displaces it.

## D-02 Frozen interface

- Decision: the glyph-engine exposes exactly two protocols and one builder.

```python
# src/gnosis_glyph_engine/protocols.py  (target shape, Phase 02 implements)

from __future__ import annotations
from typing import Protocol, runtime_checkable
import numpy as np

@runtime_checkable
class Descriptor(Protocol):
    name: str
    dim: int

    def encode(self, image: np.ndarray) -> np.ndarray: ...


@runtime_checkable
class LearnedDescriptor(Protocol):
    name: str
    dim: int

    def fit(self, images: list[np.ndarray]) -> "LearnedDescriptor": ...
    def encode(self, image: np.ndarray) -> np.ndarray: ...
```

```python
# src/gnosis_glyph_engine/manifest_builder.py  (target shape, Phase 02 implements)

def build_manifest(
    manifest_name: str,
    items: list[tuple[str, np.ndarray, dict[str, str]]],
    descriptors: list[Descriptor | LearnedDescriptor],
) -> dict:
    """Return a JSON-serialisable dict matching morph-bench schema v1."""
```

- Rollback trigger: a morph-bench contract change that requires more than a
  `dict[str, tuple[float, ...]]` feature surface.

## D-03 Frozen fixture

- Decision: a deterministic 12-glyph synthetic fixture built in-package.
- Shape: 3 families (`family_A`, `family_B`, `family_C`) × 4 variants each.
- Generator: `gnosis_glyph_engine.fixtures.synthesize_twelve_glyphs(seed=42)`.
- Output: `np.ndarray[uint8]` binary images, 64×64.
- Reference labels: `{"family": "A" | "B" | "C"}`.
- No external data, no corpus rights dependency.

## D-04 Frozen ablation

Five arms; morph-bench runs once per arm. The glyph-engine produces a
separate `BenchmarkManifest` per arm by swapping the `Descriptor` implementation.

| Arm ID | Type | Source | Dim |
|---|---|---|---|
| `baseline_orb` | Borrowed | OpenCV `cv2.ORB_create` | 32 |
| `baseline_hu_regionprops` | Borrowed | scikit-image `moments_hu` + `regionprops` | 12 |
| `baseline_hog` | Borrowed (learned) | scikit-image `hog` + sklearn `PCA` | 32 |
| `owned_stroke_compass` | Owned candidate | from `scripts/indus/stroke_native_encoding.py` | 32 |
| `owned_topology` | Owned candidate | from `scripts/indus/phase3_common.py` | ~16 |

Pass rule: at least one owned arm must beat the best baseline by **≥ 0.5** on
morph-bench's NMI-vs-null `sigma` AND tie-or-beat on `mean_jaccard` from
`leave_fraction_out(fraction=0.25, repeats=6)` with `seed=42`.

If both owned arms fail this rule: `package_boundary_earned = FAILED`, the
scaffold stays a hold surface, and a `Do Not Build` row is added to
`BUILD_VS_BORROW_CANON.md`.

## D-05 Destination path map

As specified in `01-RESEARCH.md` §6. Files are not created in Phase 01.

## D-06 Extraction-source blocker for the owned arm

- Decision: Phase 02 execution of `owned_stroke_compass` and `owned_topology`
  is **blocked** until the live-monorepo files
  `scripts/indus/stroke_native_encoding.py` and
  `scripts/indus/phase3_common.py` (or their agreed replacements) are made
  available under a retrievable path.
- Phase 02 may still run the three borrowed baselines on the synthetic fixture
  as a sanity check; the full ablation verdict waits for the owned arm.
- Owner action required: retrieve the two files (or grant pod access to a
  clone of the live monorepo). Until then, owned-arm tests are `xfail` in
  Phase 02.

## D-07 Package metadata deferral

- Decision: no `pyproject.toml`, no `src/` tree, no tests are created in
  Phase 01. Scaffolding stays documentation-only.
- This preserves the `Do not create package metadata before code extraction`
  decision from Phase 00.

## D-08 Public posture unchanged

- Decision: `package_boundary_earned` remains `UNTESTED`. The private GitHub
  repo `Zer0pa/Glyph-Engine` will receive the scaffold but no public readme
  claims will change. `INTERNAL_EXTRACTION_TARGET` posture is preserved.
