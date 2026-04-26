# Hugging Face Custody Register — `gnosis-glyph-engine`

Date: 2026-04-24 (initial); 2026-04-26 (HF lane brief refresh).
Verifier: autonomous lane-A run against the Zer0pa closeout brief
dated 2026-04-24, refreshed against the HF lane execution brief dated
2026-04-26.
Authentication: production HF token `Zer0pa HF Storage` (user
`Architect-Prime`, org membership `Zer0pa`).

This register names every HF repository that this workstream claims as
remote custody. Every row must be verified against a live API response
from the production token, not against documentation-only claims. The
closeout brief notes that several cross-lane HF repos were not visible to
a reviewer token; this file documents the ground truth for `Glyph-Engine`
only.

## Spelling Policy

This repo uses the British spelling **`artefact`** in code, docs, and HF
repo ids. Other Gnosis lanes may use the American spelling **`artifact`**
(e.g. `Zer0pa/gnosis-morph-bench-artifacts`). Both spellings are
considered valid within Gnosis; cross-lane agents must not assume one
spelling when the other is in use. If cross-lane consolidation is needed,
it is a portfolio-level decision (owner action), not a lane-level
rename.

## Rows

### HF-01 — `Zer0pa/glyph-engine-artefacts`

| Field | Value |
|---|---|
| Repo ID | `Zer0pa/glyph-engine-artefacts` |
| Repo type | `dataset` |
| Visibility | `private` |
| Verified via | `HfApi().dataset_info(...)` with production token, 2026-04-24 |
| Latest commit SHA | `58cbc2e6cb1f3c72b6e5ec88dad9637028467657` (pre-Phase 02c) |
| Last modified | 2026-04-24 03:36:49 UTC |
| Consuming GitHub repo | `Zer0pa/Glyph-Engine` |
| Rights class | `PRIVATE_INTERNAL_ONLY` (no licence grant; see `NOTICE.md`) |
| Intended contents | Phase 02 ablation + robustness artefacts (ablation_report.json, per-arm manifests and smoke reports, robustness_report.json). |

Files present at registered SHA (pre-02c refresh):

| Path in HF repo | Size | Local SHA256 | Origin |
|---|---:|---|---|
| `README.md` | (HF-managed) | n/a | `Zer0pa/glyph-engine-artefacts`, agent-authored 2026-04-24 |
| `.gitattributes` | (HF-managed) | n/a | default |
| `artifacts/ablation/ablation_report.json` | 2642 B | `32f83e5a…ae3428c` | pod run, seed=42 |
| `artifacts/ablation/per_arm/baseline_orb.manifest.json` | 13714 B | `8f526060…6a953657` | pod run, seed=42 |
| `artifacts/ablation/per_arm/baseline_orb.smoke_report.json` | 921 B | `2a8b4a66…ecec12d886` | pod run, seed=42 |
| `artifacts/ablation/per_arm/baseline_hu_regionprops.manifest.json` | 6142 B | `10fbe19e…02d867ae34aff7` | pod run, seed=42 |
| `artifacts/ablation/per_arm/baseline_hu_regionprops.smoke_report.json` | 965 B | `c3b30202…45a9bd8a5bb1c` | pod run, seed=42 |
| `artifacts/ablation/per_arm/baseline_hog.manifest.json` | 10135 B | `eaabaaba…94c37789b0c8` | pod run, seed=42 |
| `artifacts/ablation/per_arm/baseline_hog.smoke_report.json` | 941 B | `decd0a3c…8ea26b558d995` | pod run, seed=42 |

Phase 02c will append:

| Path in HF repo | Size | Local SHA256 | Origin |
|---|---:|---|---|
| `artifacts/robustness/robustness_report.json` | 10809 B | `c2510b61…08eac6f076ffb` | pod run, seeds 0..9 |

After Phase 02c push, this register will be re-verified and the new HF
SHA recorded as a follow-up row below.

## Cross-Lane Claims NOT Owned Here

The following HF ids appear in the closeout brief as potentially related
but are **not** owned or verified by this lane:

- `Zer0pa/gnosis-morph-bench-artifacts` — owned by Lane E (`Morph-Bench`).
- `Zer0pa/gnosis-morph-bench-authority-bundle` — owned by Lane E.
- `Zer0pa/cuneiform-control-artefacts` — owned by Lane C (`Cuneiform`).
- `Zer0pa/gnosis-indus-artifacts` — owned by Lane F (`Indus-Valley`).
- `Zer0pa/gnosis-indus-models` — owned by Lane F.

The reviewer in the closeout brief reported that these were not visible
to the reviewer token. This lane makes no assertion about their status;
each owning lane must verify its own rows.

## Verification Command

The register is falsifiable with the production HF token:

```python
from huggingface_hub import HfApi
info = HfApi(token=<production_token>).dataset_info(
    "Zer0pa/glyph-engine-artefacts"
)
print(info.private, info.sha, info.last_modified)
for s in info.siblings:
    print(s.rfilename)
```

Expected `private = True` and `sha = 58cbc2e6cb1f3c72b6e5ec88dad9637028467657`
at the pre-02c point, or a later SHA after the 02c mirror push (also
recorded here once complete).

## Follow-Ups

- [x] Append the post-02c HF SHA once `artifacts/robustness/` is mirrored.
- [ ] If cross-lane `HF_CUSTODY_REGISTER.md` consolidation is scoped by
      the Zer0pa roadmap team, surface this file as the Glyph-Engine
      canonical row source.

### HF-01 post-02c state (verified 2026-04-24)

| Field | Value |
|---|---|
| Latest commit SHA | `76fa5fff552eb47af120ca795e8a7ed5f1eb330c` |
| Siblings added since pre-02c SHA | `artifacts/robustness/robustness_report.json`, README.md refreshed |
| Verification | `HfApi().dataset_info("Zer0pa/glyph-engine-artefacts")` via production token, 2026-04-24 |

### HF-01 post-card-refresh state (verified 2026-04-26)

| Field | Value |
|---|---|
| Latest commit SHA | `32a8b5eeb78198c62a18158f81205ce1aa03a0c6` |
| Change | README.md rewritten to match HF Lane Execution Brief 2026-04-26 §5 template (no SAL wording, no open-source license, license frontmatter omitted, internal-only posture made explicit). No artefact payload changed; the nine artefact files under `artifacts/ablation/` and `artifacts/robustness/` are unchanged. |
| Classification (per §6.2) | Canonical and keep; card refreshed. |
| Visibility decision (per §4.4) | PRIVATE (Glyph-Engine is `private for now` in the brief's lane direction table). Maintained. |
| Architect-Prime drift | NONE for this lane (verified 2026-04-26: zero datasets, zero models, zero spaces under `Architect-Prime`). |
| Verification | `HfApi().dataset_info("Zer0pa/glyph-engine-artefacts")` via production token, 2026-04-26 18:31:47 UTC. |
