# Migration Plan

## Current Position

Phase 00 (hold-surface bootstrap) and Phase 01 (consumer + interface freeze)
are complete. The scaffold is paired with a private GitHub remote
`Zer0pa/Glyph-Engine` for durable custody and a Hugging Face dataset
`Zer0pa/glyph-engine-artefacts` for artefact failover.

## Next Gate

Phase 02: `Minimal Extraction Smoke`. Run the frozen ablation from repo
custody.

Pass condition:

1. owned-arm source files retrieved and recorded in `SOURCE_BOUNDARY.md`,
2. `src/gnosis_glyph_engine/` populated per frozen destination path map,
3. synthetic 12-glyph fixture generated deterministically,
4. five-arm (or three-arm borrowed-only, if owned retrieval still open)
   ablation executed and `artifacts/ablation_report.json` written,
5. `gnosis-morph-bench` evaluator consumes the produced `BenchmarkManifest`
   without modification.

## Blocked

- public remote or release: blocked until `package_boundary_earned = PASSED`
  and license text is supplied,
- package metadata creation (`pyproject.toml`, `src/` tree): blocked until
  Phase 02 kickoff,
- owned-arm execution: blocked on retrieval of
  `scripts/indus/stroke_native_encoding.py` and
  `scripts/indus/phase3_common.py` (Phase 01 decision D-06).

## Compute Substrate

- Authoring: local Mac at `Gnosis Portfolio/workstreams/gnosis-glyph-engine/`.
- Execution (Phase 02+): RunPod host `38.80.152.147:34587`, pod
  `7k3riasglemecu`, Python 3.13 venv under `/workspace/gnosis-glyph-engine/`.
- Artefact failover: Hugging Face `Zer0pa/glyph-engine-artefacts`.

## Do Not Do Yet

- do not create a public remote,
- do not write public README claims,
- do not extract broad domain scripts,
- do not build a generic descriptor framework.
