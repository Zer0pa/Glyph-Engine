"""Protocol contracts frozen in Phase 01 decision D-02.

Any descriptor that satisfies ``Descriptor`` or ``LearnedDescriptor`` can be
passed to :func:`gnosis_glyph_engine.manifest_builder.build_manifest` without
further glue.

Design rules (Phase 01 D-02, enforced here by type shape):

- ``encode`` is a pure function of the image argument; it has no hidden state
  beyond what ``fit`` put there.
- The returned vector is a 1-D ``numpy.ndarray`` of ``float32`` of length
  exactly ``self.dim``.
- ``name`` is the route name morph-bench will see. Two descriptors with the
  same ``name`` must not both appear in a single manifest.
"""

from __future__ import annotations

from typing import Protocol, Sequence, runtime_checkable

import numpy as np


@runtime_checkable
class Descriptor(Protocol):
    """Stateless descriptor. Implementations typically borrow from OSS."""

    name: str
    dim: int

    def encode(self, image: np.ndarray) -> np.ndarray:
        """Return a 1-D ``float32`` vector of length ``self.dim``."""
        ...


@runtime_checkable
class LearnedDescriptor(Protocol):
    """Stateful descriptor needing an unsupervised fit (e.g. HOG + PCA)."""

    name: str
    dim: int

    def fit(self, images: Sequence[np.ndarray]) -> "LearnedDescriptor":
        """Fit any internal state from a sample of images. Returns ``self``."""
        ...

    def encode(self, image: np.ndarray) -> np.ndarray:
        """Return a 1-D ``float32`` vector of length ``self.dim``."""
        ...


class SourceRetrievalPending(RuntimeError):
    """Raised by :mod:`gnosis_glyph_engine.owned` until Phase 01 D-06 clears.

    See ``.gpd/phases/01-consumer-and-interface-freeze/01-DECISIONS.md`` D-06
    for the retrieval condition. Phase 02a runs without the owned arms.
    """
