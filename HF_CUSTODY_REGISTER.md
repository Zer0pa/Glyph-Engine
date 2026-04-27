# Hugging Face Custody Register — `gnosis-glyph-engine`

Date: 2026-04-24 (initial); 2026-04-26 (HF lane brief refresh; HF
storage execution brief refresh); 2026-04-27 (DR migration off
Zer0pa org).
Verifier: autonomous lane-A run.
Authentication: production HF token `Zer0pa HF Storage` (user
`Architect-Prime`, org membership `Zer0pa` admin).

This register names every HF repository this workstream claims as
remote custody. Every row is verified against a live API response from
the production token, not against documentation-only claims.

## Current Custody Truth (2026-04-27)

**The canonical and only Hugging Face custody surface for this lane
is `Architect-Prime/glyph-engine-artefacts` (private, dataset).**
The Zer0pa org HF namespace is intentionally NOT used by this lane.
GitHub `Zer0pa/Glyph-Engine` (private, INTERNAL) plus
`Architect-Prime/glyph-engine-artefacts` together constitute the
durable disaster-recovery surface for the lane: if the local Mac is
lost, those two remotes cumulatively hold every artefact of value.

## Spelling Policy

This lane uses the British spelling **`artefact`** in code, docs, and
HF repo ids. Other Gnosis lanes may use the American spelling
`artifact` (e.g. `Zer0pa/gnosis-morph-bench-artifacts`). Both are
valid; cross-lane consolidation is a portfolio-level decision (owner
action), not a lane-level rename.

## Rows

### HF-CANONICAL — `Architect-Prime/glyph-engine-artefacts`

| Field | Value |
|---|---|
| Repo ID | `Architect-Prime/glyph-engine-artefacts` |
| Repo type | `dataset` |
| Visibility | `private` (permanently — Gnosis HF Storage Brief §1.3 hard rule: never make an `Architect-Prime/*` Gnosis repo public) |
| Latest commit SHA | `301b0756e858d73261cea509150d235ed5da8e07` |
| Last verified | 2026-04-27 via production token |
| Consuming GitHub repo | `Zer0pa/Glyph-Engine` (private, INTERNAL) |
| Rights class | `PRIVATE_INTERNAL_ONLY` (no licence grant; see `NOTICE.md`) |
| Card | Authored to Gnosis HF Storage Brief 2026-04-26 §5.2 |
| Inventory | 10 files, 53,544 B (~52.3 KB) total |

Files present (each verified byte-for-byte by SHA256 against the
pre-migration Zer0pa source on 2026-04-27):

| Path in HF repo | Size (B) | SHA256 (full) |
|---|---:|---|
| `.gitattributes` | 2504 | (HF-managed) |
| `README.md` | 4771 | (card; AP §5.2 canonical) |
| `artifacts/ablation/ablation_report.json` | 2642 | `32f83e5ac60c2b73304829c6f8d75cabe397c17d632f8d03a558f6e11ae3428c` |
| `artifacts/ablation/per_arm/baseline_orb.manifest.json` | 13714 | `8f526060416b7fb40ac54da6cade36bea132e4927ec619cb38ef0a632a953657` |
| `artifacts/ablation/per_arm/baseline_orb.smoke_report.json` | 921 | `2a8b4a66192ab234f8c3739b070eb27c3f416b78d1512e68d15dcebcec12d886` |
| `artifacts/ablation/per_arm/baseline_hu_regionprops.manifest.json` | 6142 | `10fbe19ead566901768a9c521f4dc6fc4690d3560104f4db5002d867ae34aff7` |
| `artifacts/ablation/per_arm/baseline_hu_regionprops.smoke_report.json` | 965 | `c3b30202d70896e352d0fd7c23a14c88be0f9a9f5518247712445a9bd8a5bb1c` |
| `artifacts/ablation/per_arm/baseline_hog.manifest.json` | 10135 | `eaabaaba9829297f0886529103f41f1ca7c4614b2ce1651b9ff394c37789b0c8` |
| `artifacts/ablation/per_arm/baseline_hog.smoke_report.json` | 941 | `decd0a3c87a37c0d9f6c5d65fb86ebc288fc1513c41a8f349860ea26b558d995` |
| `artifacts/robustness/robustness_report.json` | 10809 | `c2510b61b64e781e862b65d3bbd4f83a3a53265558de83baf824eeac6f076ffb` |

Origin: every artefact file in the table above was generated on the
RunPod execution substrate, pulled into git on the local Mac, and
committed to `Zer0pa/Glyph-Engine` before being uploaded to
Hugging Face. The on-disk copies in
`<LOCAL_WORKSTREAM_ROOT>/artifacts/...` (also tracked in git on `main`
at commit `cca8350` and successors) are byte-identical to the AP
copies as of 2026-04-27.

### HF-RETIRED — `Zer0pa/glyph-engine-artefacts` — DELETED 2026-04-27

| Field | Value |
|---|---|
| Repo ID at the time | `Zer0pa/glyph-engine-artefacts` |
| Final state | DELETED. The Zer0pa namespace currently lists 0 datasets, 0 models, 0 spaces (verified 2026-04-27 via production token). |
| Reason | Owner directive 2026-04-27: free Zer0pa org HF storage; canonicalise heavy-store on Architect-Prime per Gnosis HF Storage Brief §3 routing table; `Zer0pa/*` is no longer used by this lane. |
| Migration evidence | Every artefact byte-for-byte SHA256-verified between source and destination across two independent verification passes before deletion. The migration also briefly produced an auto-rename to `Architect-Prime/zeropa-org-glyph-engine-artefacts`; that orphan duplicate was deleted on 2026-04-27 after a third byte-for-byte integrity check confirmed it was payload-identical to the canonical `Architect-Prime/glyph-engine-artefacts`. |

### HF-02 (SUPERSEDED) — earlier "AP not created" decision

The 2026-04-26 `HF-02` row in this register said
`Architect-Prime/glyph-engine-artefacts` would not be created at that
time. **That decision is superseded by the 2026-04-27 owner directive**
to migrate everything off Zer0pa org storage. The repo was created on
2026-04-27 and is the row HF-CANONICAL above.

## Disaster-Recovery Posture

If the local Mac dies, every artefact of value for this lane is
recoverable from these two remotes:

| What | Where | Verification |
|---|---|---|
| Source code (full repo, every commit) | GitHub `Zer0pa/Glyph-Engine` (private/INTERNAL) | `git clone https://github.com/Zer0pa/Glyph-Engine.git` |
| Phase 02a + 02c JSON artefacts | Architect-Prime `glyph-engine-artefacts` (private dataset) | `huggingface-cli download Architect-Prime/glyph-engine-artefacts --repo-type dataset` |
| Provenance, conventions, GPD state | inside the GitHub repo (`.gpd/`, `NOTICE.md`, `HF_CUSTODY_REGISTER.md`, etc.) | recovered with the git clone above |

The synthetic 12-glyph fixture is *not* a stored artefact; it is
deterministically regenerated by
`gnosis_glyph_engine.fixtures.synthesize_twelve_glyphs(seed=...)`
from source. No real-glyph corpus exists for this lane.

The owned-arm files referenced in Phase 01 D-06 do not exist on
either remote; their absence is the lane's open scientific blocker
and is recorded in `SOURCE_BOUNDARY.md`.

## Cross-Lane Claims NOT Owned Here

The following HF ids may be referenced elsewhere in the portfolio
brief set but are **not** owned or verified by this lane:

- `Zer0pa/gnosis-morph-bench-artifacts` — owned by Lane E.
- `Zer0pa/cuneiform-control-artefacts` — owned by Lane C.
- `Architect-Prime/<other-lane>*` — owned by the corresponding lane.

Each owning lane must verify its own rows independently.

## Verification Command

```python
from huggingface_hub import HfApi
info = HfApi(token=<production_token>).dataset_info(
    "Architect-Prime/glyph-engine-artefacts",
    files_metadata=True,
)
print(info.private, info.sha, info.last_modified)
for s in info.siblings:
    print(s.rfilename, s.size)

# And to confirm the Zer0pa namespace stays empty for this lane:
list(HfApi(token=<production_token>).list_datasets(author="Zer0pa"))  # → []
```

Expected on 2026-04-27 baseline:

- `private = True`
- `sha = 301b0756e858d73261cea509150d235ed5da8e07`
- 10 siblings totalling 53,544 B
- `Zer0pa` namespace empty for this lane.

## Follow-Ups

- [ ] If Phase 02b owned-arm extraction (currently blocked on D-06)
      ever produces heavy outputs (model weights, real-glyph imagery,
      bulky benchmark dumps), upload them to
      `Architect-Prime/glyph-engine-artefacts`, recompute SHA256, and
      append a new row above.
- [ ] If the consuming GitHub repo is ever published publicly, the
      Portfolio Register at the Master Resolver Endpoint will record
      the licence matrix; until then, this dataset stays private.

## Migration Log

| Date | Event | Evidence |
|---|---|---|
| 2026-04-24 | `Zer0pa/glyph-engine-artefacts` created; initial pre-02c upload (sha `58cbc2e6`). | initial register row |
| 2026-04-24 | Phase 02c artefacts (`artifacts/robustness/`) added (sha `76fa5fff`). | post-02c row |
| 2026-04-26 | Card aligned to HF Lane Execution Brief 2026-04-26 §5 (sha `32a8b5ee`). | post-card-refresh row |
| 2026-04-26 | Storage-tier section added per HF Storage Brief §5.1 (sha `46cca8b9`). | post-storage-tier row |
| 2026-04-27 | Owner directive: migrate off Zer0pa org HF storage entirely. Mirror created at `Architect-Prime/glyph-engine-artefacts` (sha `301b0756`); every artefact SHA256-verified byte-for-byte; orphan auto-rename `Architect-Prime/zeropa-org-glyph-engine-artefacts` cleaned up; `Zer0pa/glyph-engine-artefacts` deleted; Zer0pa namespace verified empty (0 datasets / 0 models / 0 spaces). | this register; HF API responses captured during execution |
