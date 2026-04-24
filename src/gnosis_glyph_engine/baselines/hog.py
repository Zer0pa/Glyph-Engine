"""HOG + PCA baseline (scikit-image + scikit-learn).

This is the only descriptor in Phase 02a that requires :meth:`fit` — PCA is
fit unsupervised on the 12-item fixture and the same fit is then applied at
``encode`` time.
"""

from __future__ import annotations

from typing import Sequence

import numpy as np
from skimage.feature import hog
from sklearn.decomposition import PCA


def _hog_vector(image: np.ndarray) -> np.ndarray:
    grayscale = image.astype(np.float32) / 255.0
    features = hog(
        grayscale,
        orientations=9,
        pixels_per_cell=(8, 8),
        cells_per_block=(2, 2),
        block_norm="L2-Hys",
        feature_vector=True,
    )
    return np.asarray(features, dtype=np.float32)


class HogPcaDescriptor:
    """skimage HOG → sklearn PCA(n_components=dim) → 32-d vector."""

    name: str = "baseline_hog"
    dim: int = 32

    def __init__(self, *, seed: int = 42) -> None:
        self._seed = seed
        self._pca: PCA | None = None

    def fit(self, images: Sequence[np.ndarray]) -> "HogPcaDescriptor":
        if not images:
            raise ValueError("fit requires at least one image")
        raw = np.stack([_hog_vector(image) for image in images])
        n_components = min(self.dim, raw.shape[0], raw.shape[1])
        if n_components < self.dim:
            # Not enough samples or raw features: deterministically zero-pad
            # at encode time. Train on what we have.
            pass
        self._pca = PCA(n_components=n_components, random_state=self._seed)
        self._pca.fit(raw)
        return self

    def encode(self, image: np.ndarray) -> np.ndarray:
        if self._pca is None:
            raise RuntimeError("HogPcaDescriptor.encode called before fit")
        raw = _hog_vector(image).reshape(1, -1)
        reduced = self._pca.transform(raw).reshape(-1).astype(np.float32)
        if reduced.shape[0] == self.dim:
            return reduced
        # Pad deterministically to the declared dim so downstream length
        # invariants hold.
        padded = np.zeros(self.dim, dtype=np.float32)
        padded[: reduced.shape[0]] = reduced
        return padded
