# FAQ

## Is this an installable glyph-engine library?

No. It is a hold/extraction scaffold.

## Why keep the workstream?

Descriptor and glyph-geometry code may become reusable, but the package
boundary must be earned by a consumer, smoke path, and ablation.

## Does this repo prove descriptor superiority?

No. Any superiority claim is blocked until a benchmark or ablation runs from
repo custody.

## Why not build everything here now?

Most of the stack should be borrowed from OpenCV, scikit-image, scikit-learn,
Faiss, and related libraries. The only ownable slice is the domain-specific
descriptor contract if evidence supports it.
