"""Determinism and shape tests for the Phase 01 D-03 fixture."""

from __future__ import annotations

import numpy as np

from gnosis_glyph_engine.fixtures import (
    FAMILIES,
    IMAGE_SIZE,
    VARIANTS_PER_FAMILY,
    synthesize_twelve_glyphs,
)


def test_item_count_and_families():
    items = synthesize_twelve_glyphs(seed=42)
    assert len(items) == len(FAMILIES) * VARIANTS_PER_FAMILY == 12
    family_counts = {fam: sum(1 for it in items if it.family == fam) for fam in FAMILIES}
    assert family_counts == {"A": 4, "B": 4, "C": 4}


def test_shape_and_dtype():
    items = synthesize_twelve_glyphs(seed=42)
    for item in items:
        assert item.image.shape == (IMAGE_SIZE, IMAGE_SIZE)
        assert item.image.dtype == np.uint8
        unique_values = set(int(v) for v in np.unique(item.image))
        assert unique_values.issubset({0, 255})


def test_reference_labels():
    items = synthesize_twelve_glyphs(seed=42)
    for item in items:
        assert item.reference_labels == {"family": item.family}


def test_deterministic_across_runs():
    left = synthesize_twelve_glyphs(seed=42)
    right = synthesize_twelve_glyphs(seed=42)
    for l_item, r_item in zip(left, right):
        assert l_item.item_id == r_item.item_id
        assert np.array_equal(l_item.image, r_item.image)


def test_different_seed_changes_images():
    left = synthesize_twelve_glyphs(seed=42)
    right = synthesize_twelve_glyphs(seed=43)
    # Item ids are family-variant, so same ids, different images expected.
    differences = sum(
        int(not np.array_equal(l.image, r.image)) for l, r in zip(left, right)
    )
    assert differences > 0, "seed change must perturb at least one variant"


def test_non_empty_foreground():
    items = synthesize_twelve_glyphs(seed=42)
    for item in items:
        assert item.image.sum() > 0, f"item {item.item_id} has no foreground pixels"
