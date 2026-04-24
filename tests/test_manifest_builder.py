"""Shape + morph-bench compatibility tests for ``build_manifest``."""

from __future__ import annotations

import json

import numpy as np
import pytest

from gnosis_glyph_engine.baselines import HuRegionpropsDescriptor, OrbDescriptor
from gnosis_glyph_engine.fixtures import synthesize_twelve_glyphs
from gnosis_glyph_engine.manifest_builder import build_manifest


def test_manifest_shape():
    items = synthesize_twelve_glyphs(seed=42)
    manifest = build_manifest(
        "phase02a-smoke",
        items,
        [OrbDescriptor(), HuRegionpropsDescriptor()],
    )
    assert manifest["schema_version"] == 1
    assert manifest["manifest_name"] == "phase02a-smoke"
    assert len(manifest["items"]) == 12
    for entry in manifest["items"]:
        assert set(entry.keys()) == {"item_id", "reference_labels", "route_features"}
        assert set(entry["route_features"].keys()) == {"baseline_orb", "baseline_hu_regionprops"}
        assert len(entry["route_features"]["baseline_orb"]) == 32
        assert len(entry["route_features"]["baseline_hu_regionprops"]) == 12
        for values in entry["route_features"].values():
            assert all(isinstance(v, float) for v in values)


def test_manifest_json_roundtrip():
    items = synthesize_twelve_glyphs(seed=42)
    manifest = build_manifest(
        "phase02a-smoke",
        items,
        [OrbDescriptor()],
    )
    blob = json.dumps(manifest)
    recovered = json.loads(blob)
    assert recovered["items"][0]["item_id"] == manifest["items"][0]["item_id"]


def test_duplicate_descriptor_names_rejected():
    class _Fake:
        name = "dup"
        dim = 4

        def encode(self, image: np.ndarray) -> np.ndarray:  # pragma: no cover
            return np.zeros(self.dim, dtype=np.float32)

    items = synthesize_twelve_glyphs(seed=42)
    with pytest.raises(ValueError):
        build_manifest("x", items, [_Fake(), _Fake()])


def test_empty_inputs_rejected():
    items = synthesize_twelve_glyphs(seed=42)
    with pytest.raises(ValueError):
        build_manifest("x", [], [OrbDescriptor()])
    with pytest.raises(ValueError):
        build_manifest("x", items, [])


def test_morph_bench_loader_accepts_manifest(tmp_path):
    """Integration check: morph-bench's loader must parse our output."""
    from gnosis_morph_bench.schema import load_manifest  # noqa: WPS433

    items = synthesize_twelve_glyphs(seed=42)
    manifest = build_manifest(
        "phase02a-smoke",
        items,
        [OrbDescriptor(), HuRegionpropsDescriptor()],
    )
    path = tmp_path / "manifest.json"
    path.write_text(json.dumps(manifest))
    loaded = load_manifest(path)
    assert loaded.manifest_name == "phase02a-smoke"
    assert len(loaded.items) == 12
    assert set(loaded.route_names) == {"baseline_orb", "baseline_hu_regionprops"}
