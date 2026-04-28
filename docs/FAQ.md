# FAQ

## Is this an installable glyph-engine library?

It is installable for repo-local testing (`pip install -e .[dev]`), but it is
not a public library and the package boundary is not earned.

## Why keep the workstream?

Descriptor and glyph-geometry code may become reusable. The borrowed-baseline
smoke and robustness paths now exist; the remaining package-boundary question
depends on D-06, Phase 02b owned-arm evidence, and Phase 03 review.

## Does this repo prove descriptor superiority?

No. Borrowed-baseline ablation exists, but owned descriptors are still unrun.
Any superiority claim is blocked until Phase 02b and Phase 03.

## Why not build everything here now?

Most of the stack should be borrowed from OpenCV, scikit-image, scikit-learn,
Faiss, and related libraries. The only ownable slice is the domain-specific
descriptor contract if evidence supports it.
