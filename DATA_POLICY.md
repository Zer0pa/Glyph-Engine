# Data Policy

## Current Policy

This scaffold carries no raw corpus data, images, model weights, or generated
feature matrices. It is a source-boundary and package-boundary decision surface.

## Asset Classes

| Asset family | Policy | Reason |
|---|---|---|
| Scaffold docs and GPD state | `COPY_NOW` | Authored for this migration package. |
| Candidate source files | `INVENTORY_NOW_EXTRACT_LATER` | Must be disentangled from domain code before copying. |
| Tiny synthetic fixtures | `CREATE_LATER_IF_NEEDED` | Useful only after an interface exists. |
| Indus/cuneiform images and corpora | `EXCLUDE` | Rights and domain ownership belong elsewhere. |
| Descriptor benchmark outputs | `CREATE_LATER` | No ablation exists yet in this scaffold. |

## Public Boundary

No public data release is authorized from this scaffold. Any future release must
first supply source provenance, benchmark evidence, and data/artifact release clearance.
