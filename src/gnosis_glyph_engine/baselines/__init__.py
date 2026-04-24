"""Borrowed-baseline descriptors. All three satisfy ``protocols.Descriptor``
or ``protocols.LearnedDescriptor``.

Sources per Phase 01 D-04:

- :class:`OrbDescriptor` — OpenCV ``cv2.ORB_create``.
- :class:`HuRegionpropsDescriptor` — scikit-image Hu moments + regionprops.
- :class:`HogPcaDescriptor` — scikit-image HOG reduced by scikit-learn PCA.

These exist to make the glyph-engine boundary falsifiable: if the two owned
arms (Phase 02b, blocked on D-06) cannot beat these commodity OSS layers on
morph-bench's ``sigma`` and ``mean_jaccard``, the package boundary is not
earned.
"""

from __future__ import annotations

from .orb import OrbDescriptor
from .hu_regionprops import HuRegionpropsDescriptor
from .hog import HogPcaDescriptor

__all__ = ["OrbDescriptor", "HuRegionpropsDescriptor", "HogPcaDescriptor"]
