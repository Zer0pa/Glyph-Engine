# Security

## Reporting

Security-sensitive issues should be routed through the owner-controlled private
coordination path. Do not place secrets, exploit details, operational endpoints,
or private corpus material in public-facing issues or docs.

## Current Boundary

- Extracted borrowed-baseline package code is present; no service is shipped.
- No secrets, corpus images, model weights, or runtime logs belong in this
  repo.
- The pinned Ops-Gates coupling audit runs in CI over `src`, `tests`, and
  `scripts` to catch concrete operational leakage in Python surfaces.
- If future D-06 extraction introduces owned code, update `SOURCE_BOUNDARY.md`
  first and rerun the coupling audit before committing.

## Response Targets

Owner-controlled until a public support process is explicitly approved.
