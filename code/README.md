# Code Surface

No code is extracted in this scaffold yet.

Phase 01 froze the extraction target on 2026-04-24:

- first consumer: `gnosis-morph-bench`,
- interface: `Descriptor` / `LearnedDescriptor` protocols + `manifest_builder`
  helper (see `.gpd/phases/01-consumer-and-interface-freeze/01-DECISIONS.md`),
- fixture: 12-glyph synthetic generator, 3 families × 4 variants,
- ablation: 5 arms with a numeric pass rule against morph-bench `sigma` and
  `mean_jaccard`.

Phase 02 (Minimal Extraction Smoke) begins once the owned-arm source
retrieval blocker (D-06) is resolved. Until then, current code status remains:

`NO_CODE_EXTRACTED_YET`.

See also:

- `../SOURCE_BOUNDARY.md` — candidate families, destination paths, blocker
- `../.gpd/phases/01-consumer-and-interface-freeze/01-SUMMARY.md`
- `../.gpd/STATE.md`
