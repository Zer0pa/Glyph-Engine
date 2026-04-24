"""Protocol-compliance and output-shape tests for the three borrowed baselines."""

from __future__ import annotations

import numpy as np
import pytest

from gnosis_glyph_engine.baselines import (
    HogPcaDescriptor,
    HuRegionpropsDescriptor,
    OrbDescriptor,
)
from gnosis_glyph_engine.fixtures import images_only, synthesize_twelve_glyphs
from gnosis_glyph_engine.protocols import Descriptor, LearnedDescriptor


@pytest.fixture(scope="module")
def fixture_images() -> list[np.ndarray]:
    return images_only(synthesize_twelve_glyphs(seed=42))


def test_orb_protocol(fixture_images):
    desc = OrbDescriptor()
    assert isinstance(desc, Descriptor)
    assert desc.name == "baseline_orb"
    assert desc.dim == 32
    for image in fixture_images:
        vector = desc.encode(image)
        assert vector.shape == (desc.dim,)
        assert vector.dtype == np.float32
        assert np.all(np.isfinite(vector))


def test_hu_regionprops_protocol(fixture_images):
    desc = HuRegionpropsDescriptor()
    assert isinstance(desc, Descriptor)
    assert desc.name == "baseline_hu_regionprops"
    assert desc.dim == 12
    for image in fixture_images:
        vector = desc.encode(image)
        assert vector.shape == (desc.dim,)
        assert vector.dtype == np.float32
        assert np.all(np.isfinite(vector))


def test_hog_pca_protocol(fixture_images):
    desc = HogPcaDescriptor().fit(fixture_images)
    assert isinstance(desc, LearnedDescriptor)
    assert desc.name == "baseline_hog"
    assert desc.dim == 32
    for image in fixture_images:
        vector = desc.encode(image)
        assert vector.shape == (desc.dim,)
        assert vector.dtype == np.float32
        assert np.all(np.isfinite(vector))


def test_hog_pca_requires_fit(fixture_images):
    desc = HogPcaDescriptor()
    with pytest.raises(RuntimeError):
        desc.encode(fixture_images[0])


def test_baselines_distinguish_families(fixture_images):
    """Quick sanity: mean inter-family distance > mean intra-family distance
    for at least one baseline. This is not the ablation verdict; it only
    guards against a fixture that is degenerate under every baseline."""
    items = synthesize_twelve_glyphs(seed=42)
    descriptors = [
        OrbDescriptor(),
        HuRegionpropsDescriptor(),
        HogPcaDescriptor().fit(fixture_images),
    ]
    for desc in descriptors:
        vectors = np.stack([desc.encode(it.image) for it in items])
        families = [it.family for it in items]
        # pairwise euclidean
        def _mean(mask_predicate):
            total = 0.0
            count = 0
            for i in range(len(items)):
                for j in range(i + 1, len(items)):
                    if mask_predicate(families[i], families[j]):
                        total += float(np.linalg.norm(vectors[i] - vectors[j]))
                        count += 1
            return total / max(count, 1)

        intra = _mean(lambda a, b: a == b)
        inter = _mean(lambda a, b: a != b)
        if inter > intra:
            return  # at least one baseline is non-degenerate; that's enough
    raise AssertionError("no baseline showed inter-family > intra-family mean distance")
