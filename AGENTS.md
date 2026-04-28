# Glyph-Engine Agent Instructions

## Governing Objective

Treat `package_boundary_earned` as the authority metric. The current value is
`UNTESTED`; do not promote the package boundary, public readiness, or descriptor
superiority until Phase 02b and Phase 03 evidence exists.

## Current Truth

- Phase 00, Phase 01, Phase 02a, and Phase 02c are complete.
- Phase 02b is `BLOCKED_ON_D-06`.
- D-06 requires retrieval of:
  - `scripts/indus/stroke_native_encoding.py`
  - `scripts/indus/phase3_common.py`
- Apache-2.0 code licensing and CC-BY-4.0 documentation licensing are present,
  but licensing does not imply package-boundary readiness.
- Morph-Bench is an optional contract partner. The repo must remain installable
  without a sibling editable install.
- `tools/gnosis_ops_gates/coupling_audit.py` is the local Ops-Gates adoption
  point for CI. Its rule set is derived from
  `Gnosis-Ops-Gates@54ed0a71:code/tools/coupling_audit.py`, with local
  literal-redaction adjustments so this repo does not publish the full
  operational strings it is meant to catch. Do not replace it with a
  sibling-repo install unless that is explicitly scoped.

## Required Checks Before Reporting Done

Run the repo-local checks that match CI:

```bash
python tools/gnosis_ops_gates/coupling_audit.py src tests scripts
pip install -e '.[dev]'
pytest -q
git status --short
```

If Morph-Bench is available on the host, also run the optional contract path;
if not, the skipped test is expected and must be stated honestly.

The live gate covers executable Glyph surfaces: `src`, `tests`, and `scripts`.
Do not broaden that CI scope unless the broader gate is explicitly scoped and
reviewed.

## Boundaries

- Do not copy owned Indus or cuneiform code until D-06 is resolved and
  `SOURCE_BOUNDARY.md` is updated first.
- Do not delete negative evidence such as weak baseline arms.
- Do not replace explicit non-claims with narrower caveats.
- Do not put local paths, endpoints, private keys, tokens, or operational
  fingerprints into public-facing surfaces.
- Keep `_internal/` as historical scaffolding, not reader-facing authority.
