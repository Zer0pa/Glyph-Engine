"""Emit a ``gnosis_morph_bench`` schema-v1 manifest from glyph-engine parts.

The morph-bench evaluator is treated as an external dependency; this module
only produces a JSON-serialisable dict matching its loader contract. The
contract is fixed to:

- ``schema_version`` = 1
- ``manifest_name`` = str
- ``items`` = list of {``item_id``, ``reference_labels``, ``route_features``}

where ``route_features[name]`` is a plain tuple/list of floats of length
``Descriptor.dim``.
"""

from __future__ import annotations

from typing import Sequence, Union

import numpy as np

from .fixtures import GlyphItem
from .protocols import Descriptor, LearnedDescriptor

AnyDescriptor = Union[Descriptor, LearnedDescriptor]


def _to_float_tuple(vector: np.ndarray, expected_dim: int, route_name: str) -> list[float]:
    if vector.ndim != 1:
        raise ValueError(f"route '{route_name}' returned {vector.ndim}-D output; expected 1-D")
    if vector.shape[0] != expected_dim:
        raise ValueError(
            f"route '{route_name}' returned length {vector.shape[0]}; expected {expected_dim}"
        )
    return [float(x) for x in vector.astype(np.float32).tolist()]


def build_manifest(
    manifest_name: str,
    items: Sequence[GlyphItem],
    descriptors: Sequence[AnyDescriptor],
) -> dict:
    """Return a morph-bench schema-v1 dict.

    The caller is responsible for ``.fit``-ing any ``LearnedDescriptor``
    before passing it in; this builder is pure encoding.
    """
    if not items:
        raise ValueError("items must not be empty")
    if not descriptors:
        raise ValueError("descriptors must not be empty")

    names = [desc.name for desc in descriptors]
    if len(set(names)) != len(names):
        raise ValueError(f"descriptor names must be unique; got {names}")

    payload_items: list[dict] = []
    for item in items:
        route_features: dict[str, list[float]] = {}
        for desc in descriptors:
            vec = desc.encode(item.image)
            route_features[desc.name] = _to_float_tuple(vec, desc.dim, desc.name)
        payload_items.append(
            {
                "item_id": item.item_id,
                "reference_labels": dict(item.reference_labels),
                "route_features": route_features,
            }
        )

    return {
        "schema_version": 1,
        "manifest_name": manifest_name,
        "items": payload_items,
    }
