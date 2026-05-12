# Hugging Face Custody Register — `gnosis-glyph-engine`

Date: 2026-04-24 (initial); 2026-04-26 (HF lane brief refresh; HF
storage execution brief refresh); 2026-04-27 (DR migration to
Architect-Prime); **2026-05-12 (canonical re-migration to Zer0pa org
+ visibility flipped to PUBLIC to mirror the GitHub repo)**.
Verifier: autonomous corridor-agent run.
Authentication: production HF token `Live Project Storage` (user
`Architect-Prime`, org membership `Zer0pa`).

This register names every HF repository this workstream claims as
remote custody. Every row is verified against a live API response from
the production token, not against documentation-only claims.

## Current Custody Truth (2026-05-12)

**The canonical Hugging Face custody surface for this lane is
`Zer0pa/Glyph-Engine-lane-state` (PUBLIC, dataset).**

This supersedes the 2026-04-27 directive that placed canonical custody
under the personal `Architect-Prime` namespace. The 2026-05-12 owner
policy update reverses that for two reasons:

1. **Use the organization storage allocation** by default — multiple
   agents are operating on Zer0pa org storage concurrently and
   single-tenant personal namespaces are no longer the right home
   for lane state.
2. **Mirror the GitHub repo's visibility** — `Zer0pa/Glyph-Engine` is
   PUBLIC; the canonical HF custody surface mirrors that and is
   therefore PUBLIC.

The earlier `Architect-Prime/glyph-engine-artefacts` URL continues to
resolve via HF's repository-rename redirect; no historical link
breaks. The same dataset object now lives in the Zer0pa org under the
sibling-pattern name `Glyph-Engine-lane-state`.

GitHub `Zer0pa/Glyph-Engine` (PUBLIC) + `Zer0pa/Glyph-Engine-lane-state`
(PUBLIC dataset on HF) + PyPI `gnosis-glyph-engine==0.1.0a1` together
constitute the durable disaster-recovery surface for the lane: if
the local Mac is lost, those three remotes cumulatively hold every
artefact of value.

## Spelling Policy

This lane uses the British spelling **`artefact`** in code and docs.
The canonical HF repo name was changed to the sibling-pattern
**`Glyph-Engine-lane-state`** (no `artefact`/`artifact` token in the
name itself), eliminating that spelling ambiguity at the bucket-id
layer. Internal documentation continues to use British spelling.

## Rows

### HF-CANONICAL — `Zer0pa/Glyph-Engine-lane-state`

| Field | Value |
|---|---|
| Repo ID | `Zer0pa/Glyph-Engine-lane-state` |
| Repo type | `dataset` |
| Visibility | `PUBLIC` (mirrors GitHub `Zer0pa/Glyph-Engine` per 2026-05-12 policy) |
| Latest commit SHA | `62c41bf6936f4e465d220d89ca9232cf6c6d3ab0` (2026-05-12T23:48:31Z) |
| Last verified | 2026-05-12 via production token (`Live Project Storage`) |
| Consuming GitHub repo | `Zer0pa/Glyph-Engine` (PUBLIC) |
| Rights class | follows GitHub repo posture: Apache-2.0 code / CC-BY-4.0 docs (per `NOTICE.md`); the artefacts are research evidence under the same posture. |
| Card | Authored 2026-05-12 to reflect new canonical + PUBLIC mirror. |
| Inventory | 34 files (~4.4 MB): 10 phase-01/02 artefacts at the root + 24 lane-agent files under `lane-agent/`. |

### Phase-01/02 evidence artefacts (root of the bucket)

| Path | Size (B) | SHA256 |
|---|---:|---|
| `.gitattributes` | 2504 | (HF-managed) |
| `README.md` | (rewritten 2026-05-12) | (canonical card) |
| `artifacts/ablation/ablation_report.json` | 2642 | `32f83e5ac60c2b73304829c6f8d75cabe397c17d632f8d03a558f6e11ae3428c` |
| `artifacts/ablation/per_arm/baseline_orb.manifest.json` | 13714 | `8f526060416b7fb40ac54da6cade36bea132e4927ec619cb38ef0a632a953657` |
| `artifacts/ablation/per_arm/baseline_orb.smoke_report.json` | 921 | `2a8b4a66192ab234f8c3739b070eb27c3f416b78d1512e68d15dcebcec12d886` |
| `artifacts/ablation/per_arm/baseline_hu_regionprops.manifest.json` | 6142 | `10fbe19ead566901768a9c521f4dc6fc4690d3560104f4db5002d867ae34aff7` |
| `artifacts/ablation/per_arm/baseline_hu_regionprops.smoke_report.json` | 965 | `c3b30202d70896e352d0fd7c23a14c88be0f9a9f5518247712445a9bd8a5bb1c` |
| `artifacts/ablation/per_arm/baseline_hog.manifest.json` | 10135 | `eaabaaba9829297f0886529103f41f1ca7c4614b2ce1651b9ff394c37789b0c8` |
| `artifacts/ablation/per_arm/baseline_hog.smoke_report.json` | 941 | `decd0a3c87a37c0d9f6c5d65fb86ebc288fc1513c41a8f349860ea26b558d995` |
| `artifacts/robustness/robustness_report.json` | 10809 | `c2510b61b64e781e862b65d3bbd4f83a3a53265558de83baf824eeac6f076ffb` |

These payload bytes are unchanged across the 2026-04-27 (Architect-Prime
canonical) and 2026-05-12 (Zer0pa-org canonical) migrations; only the
namespace + visibility changed.

### `lane-agent/` subtree (added 2026-05-12)

24 files under `lane-agent/` covering: rendered product page
(`product-page/index.html` + 5 + 2 screenshots + 2 audit JSONs + 3
render scripts), 7 corridor-agent receipts (`receipts/`), 2 FPO §A
truth sources (`fpo-truth/`), 1 PyPI/Zenodo status snapshot
(`pypi-zenodo-status/`), and the subtree's navigation README. See
`lane-agent/README.md` on the bucket for the full file inventory.

### HF-LEGACY (REDIRECT) — `Architect-Prime/glyph-engine-artefacts`

| Field | Value |
|---|---|
| Repo ID at the time | `Architect-Prime/glyph-engine-artefacts` |
| State on 2026-05-12 | REDIRECT — moved to `Zer0pa/Glyph-Engine-lane-state` via `hf repos move`. HF preserves the old URL as a redirect to the new canonical name; no historical link breaks, but new uploads/pulls should use the canonical name. |
| Reason | Owner policy directive 2026-05-12: use org storage allocation by default; mirror GitHub visibility. |

### HF-RETIRED — `Zer0pa/glyph-engine-artefacts` — DELETED 2026-04-27

| Field | Value |
|---|---|
| Repo ID at the time | `Zer0pa/glyph-engine-artefacts` |
| Final state | DELETED on 2026-04-27. The Zer0pa namespace had been emptied of this lane's content by the Architect-Prime migration. |
| 2026-05-12 status | Distinct from the new canonical `Zer0pa/Glyph-Engine-lane-state`; this name has not been re-created. |

## Disaster-Recovery Posture

**The local Mac is a working surface, not a storage tier.** GitHub
holds the canonical code; HF holds the canonical artefacts and
lane-agent state; PyPI holds the canonical release. If the Mac dies,
every asset of value for this lane is recoverable from these three
remotes alone:

| What | Where | Verification |
|---|---|---|
| Source code (full repo, every commit) | GitHub `Zer0pa/Glyph-Engine` (PUBLIC) | `git clone https://github.com/Zer0pa/Glyph-Engine.git` |
| Phase 02a + 02c JSON artefacts | HF `Zer0pa/Glyph-Engine-lane-state` (PUBLIC dataset) | `hf download Zer0pa/Glyph-Engine-lane-state --repo-type dataset` |
| Lane-agent corridor work | same HF bucket under `lane-agent/` | as above |
| Live PyPI release | PyPI `gnosis-glyph-engine==0.1.0a1` (immutable) | `pip install gnosis-glyph-engine==0.1.0a1` |
| Provenance, conventions, GPD state | inside the GitHub repo (`.gpd/`, `NOTICE.md`, `HF_CUSTODY_REGISTER.md`, etc.) | recovered with the git clone above |

The synthetic 12-glyph fixture is *not* a stored artefact; it is
deterministically regenerated by
`gnosis_glyph_engine.fixtures.synthesize_twelve_glyphs(seed=...)` from
source. No real-glyph corpus exists for this lane.

The owned-arm files referenced in Phase 01 D-06 do not exist on any
remote; their absence is the lane's open scientific blocker and is
recorded in `SOURCE_BOUNDARY.md`.

## Cross-Lane Claims NOT Owned Here

The following HF ids may be referenced elsewhere in the portfolio
brief set but are **not** owned or verified by this lane. Sibling
lanes verify their own rows.

- `Zer0pa/Cuneiform-lane-state` — owned by Lane Cuneiform.
- `Zer0pa/Indus-Valley-lane-state` — owned by Lane Indus-Valley.
- `Zer0pa/DM3-lane-state` / `Zer0pa/DM3-archive` — owned by Lane DM3.
- `Zer0pa/<other-lane>-lane-state` — owned by the corresponding lane.

## Verification Command

```python
from huggingface_hub import HfApi
info = HfApi(token=<production_token>).dataset_info(
    "Zer0pa/Glyph-Engine-lane-state",
    files_metadata=True,
)
print(info.private, info.sha, info.last_modified)
for s in info.siblings:
    print(s.rfilename, s.size)
```

Expected on 2026-05-12 baseline:

- `private = False`  (mirrors GitHub PUBLIC)
- `sha = 62c41bf6936f4e465d220d89ca9232cf6c6d3ab0`  (or newer)
- 34 siblings (10 phase-01/02 artefacts at root + 24 under `lane-agent/`)

## Migration Log

| Date | Event | Evidence |
|---|---|---|
| 2026-04-24 | `Zer0pa/glyph-engine-artefacts` created; initial pre-02c upload (sha `58cbc2e6`). | initial register row |
| 2026-04-24 | Phase 02c artefacts (`artifacts/robustness/`) added (sha `76fa5fff`). | post-02c row |
| 2026-04-26 | Card aligned to HF Lane Execution Brief 2026-04-26 §5 (sha `32a8b5ee`). | post-card-refresh row |
| 2026-04-26 | Storage-tier section added per HF Storage Brief §5.1 (sha `46cca8b9`). | post-storage-tier row |
| 2026-04-27 | Owner directive: migrate off Zer0pa org HF storage. Mirror created at `Architect-Prime/glyph-engine-artefacts` (sha `301b0756`); every artefact SHA256-verified byte-for-byte; `Zer0pa/glyph-engine-artefacts` deleted; Zer0pa namespace verified empty. | 2026-04-27 register revision |
| 2026-05-12 | Corridor-agent DR snapshot: 24-file `lane-agent/` subtree (product page + receipts + FPO truth + PyPI status) uploaded to `Architect-Prime/glyph-engine-artefacts`. Round-trip byte-identical on README + receipt + 594KB binary PNG. Bucket sha `c98b12f37d076feae241d415d45eae0bd7846e69`. | `lane-agent/receipts/DR_SNAPSHOT_2026-05-12.md` |
| 2026-05-12 | Owner policy update: use org storage allocation by default; HF visibility mirrors GitHub repo visibility. Bucket moved `Architect-Prime/glyph-engine-artefacts` → `Zer0pa/Glyph-Engine-lane-state` via `hf repos move`; old URL preserved as redirect. Visibility flipped to PUBLIC to mirror PUBLIC GitHub repo. README + lane-agent README rewritten. Bucket sha `62c41bf6936f4e465d220d89ca9232cf6c6d3ab0`. | this register; bucket HEAD; lane-agent README on bucket |

## Follow-Ups

- [ ] If Phase 02b owned-arm extraction (currently blocked on D-06)
      ever produces heavy outputs (model weights, real-glyph imagery,
      bulky benchmark dumps), upload them to `Zer0pa/Glyph-Engine-lane-state`,
      recompute SHA256, and append a new row above. If any of those
      heavy outputs are private by content-rights, route them to a
      sibling `Zer0pa/Glyph-Engine-archive` (private dataset, matches
      DM3 sibling pattern) and add that row.
- [ ] On next D-06 unblock, refresh this register's "Expected baseline"
      with the new sha.
