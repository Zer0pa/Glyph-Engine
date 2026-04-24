"""ORB baseline: OpenCV ORB keypoints, mean-pooled across keypoints."""

from __future__ import annotations

import cv2
import numpy as np


class OrbDescriptor:
    """OpenCV ORB → 32-d mean-pooled vector.

    Notes
    -----
    ORB returns up to ``nfeatures`` descriptors, each a 32-byte ``uint8`` row.
    We cast to ``float32``, normalise to [0, 1], and mean-pool across
    keypoints. Images with no keypoints (empty canvas) return a zero vector.
    """

    name: str = "baseline_orb"
    dim: int = 32

    def __init__(self, *, nfeatures: int = 64, scale_factor: float = 1.2, nlevels: int = 8) -> None:
        self._orb = cv2.ORB_create(
            nfeatures=nfeatures,
            scaleFactor=scale_factor,
            nlevels=nlevels,
            edgeThreshold=4,
        )

    def encode(self, image: np.ndarray) -> np.ndarray:
        if image.ndim != 2:
            raise ValueError(f"expected 2-D image, got shape {image.shape}")
        grayscale = image.astype(np.uint8)
        keypoints, descriptors = self._orb.detectAndCompute(grayscale, None)
        if descriptors is None or len(descriptors) == 0:
            return np.zeros(self.dim, dtype=np.float32)
        normalised = descriptors.astype(np.float32) / 255.0
        pooled = normalised.mean(axis=0)
        if pooled.shape[0] != self.dim:
            # ORB descriptor length is always 32; defensive cast for safety.
            pooled = np.resize(pooled, self.dim).astype(np.float32)
        return pooled.astype(np.float32)
