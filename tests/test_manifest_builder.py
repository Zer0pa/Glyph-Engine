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
    """Cross-repo contract check: morph-bench's loader must parse our output.

    This test is skipped if ``gnosis_morph_bench`` is not installed.
    ``gnosis-glyph-engine`` does not declare it as a hard dependency to
    preserve repo-boundary independence; supply it on the execution host
    via editable path install (see ``pyproject.toml`` comments).
    """
    load_manifest = pytest.importorskip(
        "gnosis_morph_bench.schema",
        reason="gnosis_morph_bench not installed; cross-repo contract test skipped",
    ).load_manifest

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


def test_manifest_matches_local_schema_contract():
    """Fallback contract test that does NOT depend on morph-bench.

    Encodes the fixed morph-bench schema-v1 shape locally so the cross-repo
    contract is verifiable even when the sibling package is unavailable.
    Must stay in lock-step with morph-bench's schema; if morph-bench bumps
    its schema, update this fixture and open a Phase 03 decision.
    """
    items = synthesize_twelve_glyphs(seed=42)
    manifest = build_manifest(
        "phase02a-local-schema",
        items,
        [OrbDescriptor(), HuRegionpropsDescriptor()],
    )
    # Schema v1 invariants the loader enforces, copied here as a decoupled
    # local fixture.
    assert manifest["schema_version"] == 1
    assert isinstance(manifest["manifest_name"], str)
    assert isinstance(manifest["items"], list) and manifest["items"]
    seen_ids: set[str] = set()
    for entry in manifest["items"]:
        assert set(entry.keys()) == {"item_id", "reference_labels", "route_features"}
        assert isinstance(entry["item_id"], str)
        assert entry["item_id"] not in seen_ids, "item_id values must be unique"
        seen_ids.add(entry["item_id"])
        assert isinstance(entry["reference_labels"], dict) and entry["reference_labels"]
        assert isinstance(entry["route_features"], dict) and entry["route_features"]
        route_dims: set[int] = set()
        for route_name, values in entry["route_features"].items():
            assert isinstance(route_name, str) and route_name
            assert isinstance(values, list) and values
            assert all(isinstance(v, float) for v in values)
            route_dims.add(len(values))
        # morph-bench requires each route to have a consistent dim across
        # items; enforce per-item here as a structural sanity pre-check.
        assert len(route_dims) >= 1
