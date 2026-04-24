"""Hu moments + scalar region properties baseline (scikit-image)."""

from __future__ import annotations

import numpy as np
from skimage.measure import label, moments_central, moments_hu, moments_normalized, regionprops


class HuRegionpropsDescriptor:
    """Return 7 Hu moments + 5 scalar region properties as a 12-d vector.

    Hu moments are log-compressed to stabilise their dynamic range:

        h_i := -sign(M_i) * log10(|M_i| + 1e-12)

    which is a standard robustness trick from OpenCV and scikit-image
    tutorials. Region properties included: area (fractional), perimeter
    (fractional), eccentricity, solidity, extent — each of the largest
    connected component.
    """

    name: str = "baseline_hu_regionprops"
    dim: int = 12

    def encode(self, image: np.ndarray) -> np.ndarray:
        if image.ndim != 2:
            raise ValueError(f"expected 2-D image, got shape {image.shape}")
        binary = (image > 127).astype(np.uint8)

        # Hu moments via scikit-image (order follows cv2 convention).
        central = moments_central(binary.astype(float))
        normalised = moments_normalized(central)
        hu_raw = moments_hu(normalised)
        hu = -np.sign(hu_raw) * np.log10(np.abs(hu_raw) + 1e-12)

        # Region props on the largest component.
        labelled = label(binary, connectivity=2)
        props = regionprops(labelled)
        if not props:
            region_scalars = np.zeros(5, dtype=np.float32)
        else:
            largest = max(props, key=lambda p: p.area)
            total = binary.size
            region_scalars = np.array(
                [
                    largest.area / total,
                    largest.perimeter / total,
                    float(largest.eccentricity),
                    float(largest.solidity),
                    float(largest.extent),
                ],
                dtype=np.float32,
            )

        return np.concatenate([hu.astype(np.float32), region_scalars]).astype(np.float32)
