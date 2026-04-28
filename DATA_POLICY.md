# Data Policy

## Current Policy

This repository carries source code, documentation, GPD state, deterministic
synthetic fixture generation code, and small JSON evidence artefacts. It does
not carry raw corpora, cultural-heritage imagery, model weights, endpoint logs,
or operational transcripts.

The synthetic 12-glyph fixture is generated from code in
`src/gnosis_glyph_engine/fixtures.py`; it is not a real-glyph corpus and must
not be described as cross-corpus evidence.

## Asset Classes

| Asset family | Policy | Current state |
|---|---|---|
| Scaffold docs and GPD state | `COPY_NOW` | Authored for this repo and tracked. |
| Package code | `COPY_NOW` | Borrowed-baseline package is tracked; owned arms blocked on D-06. |
| Tiny synthetic fixtures | `GENERATE_FROM_CODE` | Deterministic 12-glyph generator; no external rights coupling. |
| Descriptor benchmark outputs | `TRACK_SMALL_JSON` | Phase 02a and 02c JSON artefacts are tracked and mirrored to HF custody. |
| Candidate owned source files | `INVENTORY_NOW_EXTRACT_LATER` | D-06 files absent; must be ledgered in `SOURCE_BOUNDARY.md` before copying. |
| Indus/cuneiform images and corpora | `EXCLUDE` | Rights and domain ownership belong elsewhere. |
| Model weights / bulky outputs | `HF_PRIVATE_ONLY_IF_CREATED` | None exist for this lane today. |

## Public Boundary

Apache-2.0 code licensing and CC-BY-4.0 documentation licensing do not license
raw corpora, image-bearing assets, private HF artefacts, model weights,
endpoint logs, or operational transcripts.

No real-glyph data release is authorized from this scaffold. Any future
real-glyph fixture or heavy artefact must first supply source provenance,
rights clearance, and an updated custody row in `HF_CUSTODY_REGISTER.md`.
