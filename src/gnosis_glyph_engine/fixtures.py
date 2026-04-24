"""Synthetic smoke fixture frozen in Phase 01 decision D-03.

12 binary glyphs, 3 families × 4 variants, 64×64 ``uint8``, deterministic
given ``seed``. No external data, no rights coupling.

Families are deliberately geometrically distinct so NMI-vs-null is
non-degenerate:

- ``A``: cross strokes (vertical + horizontal bars).
- ``B``: ring with a downward stem.
- ``C``: triangle with an interior dot.

Variants apply bounded rotation, scale, stroke-thickness, and Gaussian noise
so that descriptors actually have to generalise across the within-family
perturbations.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import cv2
import numpy as np


IMAGE_SIZE: int = 64
FAMILIES: tuple[str, ...] = ("A", "B", "C")
VARIANTS_PER_FAMILY: int = 4


@dataclass(frozen=True)
class GlyphItem:
    """One fixture item with stable id, binary image, reference labels."""

    item_id: str
    family: str
    image: np.ndarray  # uint8, shape (IMAGE_SIZE, IMAGE_SIZE), values in {0, 255}

    @property
    def reference_labels(self) -> dict[str, str]:
        return {"family": self.family}


def _draw_family_a(canvas: np.ndarray, stroke: int) -> None:
    c = IMAGE_SIZE // 2
    cv2.line(canvas, (c, 8), (c, IMAGE_SIZE - 8), 255, thickness=stroke)
    cv2.line(canvas, (8, c), (IMAGE_SIZE - 8, c), 255, thickness=stroke)


def _draw_family_b(canvas: np.ndarray, stroke: int) -> None:
    c = IMAGE_SIZE // 2
    cv2.circle(canvas, (c, c - 6), 14, 255, thickness=stroke)
    cv2.line(canvas, (c, c + 6), (c, IMAGE_SIZE - 8), 255, thickness=stroke)


def _draw_family_c(canvas: np.ndarray, stroke: int) -> None:
    c = IMAGE_SIZE // 2
    pts = np.array(
        [[c, 10], [IMAGE_SIZE - 12, IMAGE_SIZE - 12], [12, IMAGE_SIZE - 12]],
        dtype=np.int32,
    )
    cv2.polylines(canvas, [pts], isClosed=True, color=255, thickness=stroke)
    cv2.circle(canvas, (c, c + 6), max(2, stroke - 1), 255, thickness=-1)


_DRAWERS = {"A": _draw_family_a, "B": _draw_family_b, "C": _draw_family_c}


def _apply_variant(
    canvas: np.ndarray,
    *,
    angle_deg: float,
    scale: float,
    noise_sigma: float,
    rng: np.random.Generator,
) -> np.ndarray:
    c = IMAGE_SIZE // 2
    matrix = cv2.getRotationMatrix2D((c, c), angle_deg, scale)
    warped = cv2.warpAffine(
        canvas,
        matrix,
        (IMAGE_SIZE, IMAGE_SIZE),
        flags=cv2.INTER_NEAREST,
        borderValue=0,
    )
    if noise_sigma > 0.0:
        noise = rng.normal(0.0, noise_sigma, warped.shape)
        noisy = warped.astype(np.float32) + noise * 255.0
        warped = np.clip(noisy, 0, 255).astype(np.uint8)
    # Re-binarize so the output stays a clean binary mask.
    _, binarized = cv2.threshold(warped, 127, 255, cv2.THRESH_BINARY)
    return binarized


def synthesize_twelve_glyphs(seed: int = 42) -> list[GlyphItem]:
    """Return the 12-item fixture in deterministic order.

    Item ids are ``"<family>-<variant_index>"`` with variants indexed 0..3.
    Same ``seed`` → byte-identical images.
    """
    rng = np.random.default_rng(seed)
    items: list[GlyphItem] = []

    # Pre-sample per-variant perturbations once per family so that the fixture
    # is deterministic and reproducible across interpreters.
    for family in FAMILIES:
        drawer = _DRAWERS[family]
        for variant in range(VARIANTS_PER_FAMILY):
            stroke = int(rng.integers(2, 5))  # 2, 3, or 4 pixels
            angle_deg = float(rng.uniform(-15.0, 15.0))
            scale = float(rng.uniform(0.9, 1.1))
            noise_sigma = float(rng.uniform(0.0, 0.04))

            canvas = np.zeros((IMAGE_SIZE, IMAGE_SIZE), dtype=np.uint8)
            drawer(canvas, stroke)
            final = _apply_variant(
                canvas,
                angle_deg=angle_deg,
                scale=scale,
                noise_sigma=noise_sigma,
                rng=rng,
            )
            items.append(
                GlyphItem(
                    item_id=f"{family}-{variant}",
                    family=family,
                    image=final,
                )
            )

    return items


def images_only(items: Iterable[GlyphItem]) -> list[np.ndarray]:
    """Convenience for descriptors that need an unordered list of images."""
    return [item.image for item in items]
