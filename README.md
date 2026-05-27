# Glyph-Engine

> Product-page mirror for `/gnosis/Gnosis-Glyph-Engine/`.
> Live public repo: [Zer0pa/Glyph-Engine](https://github.com/Zer0pa/Glyph-Engine).
> GitHub Markdown cannot reproduce the website typography, CSS, JavaScript, scroll behavior, or live bento layout; this README translates the product page into GitHub-safe Markdown evidence blocks.

## 0. Install / Developer Commands

The product page is the positioning authority. This section is the only retained developer-surface material from the previous root README.

```bash
reference-freeze SHA256 is byte-stable across arms. 17 pytest tests pass when
- The package installs cleanly with `pip install -e .[dev]` on Python 3.13
- The 17-test pytest suite passes when sibling `gnosis-morph-bench` is
git clone https://github.com/Zer0pa/Glyph-Engine.git
pip install -e .[dev]
pytest -q                          # → 16 passed, 1 skipped
```

## Product Page Mirror

**Product-page title:** Gnosis-Glyph-Engine · Public alpha descriptor baseline · Zer0pa

**Product-page description:** Gnosis-Glyph-Engine · public alpha glyph-descriptor baseline · borrowed ORB / Hu regionprops / HOG baselines on a synthetic 12-glyph fixture · seed-42 replay per borrowed arm · owned-arm tests UNTESTED until D-06 · PyPI 0.1.0a1 metadata incomplete

### Hero Translation

> 00 · GNOSIS-GLYPH-ENGINE · ANCIENT SCRIPT GEOMETRYRESEARCH-READY · OWNED ARM UNTESTED Ancient Script Geometry, Symbolic Shape Analysis Shape-only descriptor research for ancient script · Gnosis-Glyph-Engine · gnosis-glyph-engine v0.1.0a1 · github.com/Zer0pa/Glyph-Engine Ancient inscriptions carry geometry that no one has counted at the level of a single mark. Glyph-Engine runs three off-the-shelf shape algorithms — ORB, Hu regionprops, and HOG — across a 12-glyph fixture, ten seeds deep, and reports how steady each one is. HOG is the steadiest at sigma 1.15. Re-running with the same seed gives the same numbers, bit for bit. The page does not claim to read or decipher the marks, and the in-house descriptor stays UNTESTED until two missing Indus source files are recovered.

## Positioning

| Field | Value |
| --- | --- |
| Section | gnosis |
| Product route | /gnosis/Gnosis-Glyph-Engine/ |
| Live public repository | https://github.com/Zer0pa/Glyph-Engine |
| Repo identity used here | Glyph-Engine |
| Website display identity | Glyph-Engine |
| Verdict | BLOCKED |
| Posture | package_boundary_unearned_pending_owned_arm_d06 |
| Headline metric | Borrowed-baseline ablation across 10 seeds: mean σ baseline_orb 4.14±1.12, hu_regionprops 2.95±1.06, hog 1.15±1.17. Determinism: replay_all_identical for every arm. |
| Honest blocker | The owned-arm authority metric package_boundary_earned is UNTESTED. Two Indus source files are not present in the portfolio snapshot; D-06 retrieval is the unblock. |
| Mechanics asset from product page |  |

## Key Metrics

| Metric | Value | Baseline |
| --- | --- | --- |
| Borrowed-baseline robustness | ORB 4.14 +/- 1.12; Hu 2.95 +/- 1.06; HOG 1.15 +/- 1.17 | 10 seeds |
| Deterministic replay | `replay_all_identical == true` | seed-42 ablation |
| Pytest surface | 17 pass with Morph-Bench; 16 pass + 1 skip without sibling | repo independence preserved |
| Authority gate | `package_boundary_earned == UNTESTED` | D-06 blocker |

## Proof Anchors

| Path | State |
| --- | --- |
| Authority metric definition | SOVEREIGN_PRD.md §Authority Metric |
| Frozen consumer + interface | .gpd/phases/01-consumer-and-interface-freeze/01-DECISIONS.md D-01, D-02 |
| Frozen fixture + ablation rule | .gpd/phases/01-consumer-and-interface-freeze/01-DECISIONS.md D-03, D-04 |
| Phase 02a single-seed ablation | artifacts/ablation/ablation_report.json + .gpd/phases/02-minimal-extraction-smoke/02-01-VERIFICATION.md |
| Phase 02c multi-seed robustness | artifacts/robustness/robustness_report.json + .gpd/phases/02-minimal-extraction-smoke/02-02-VERIFICATION.md |
| Sovereign-vs-adapter scope decision | .gpd/phases/02-minimal-extraction-smoke/02-02-DECISIONS.md D-02c-02 |
| Owned-arm source-retrieval blocker | SOURCE_BOUNDARY.md (D-06) |
| HF custody truth | HF_CUSTODY_REGISTER.md (canonical: Architect-Prime/glyph-engine-artefacts; Zer0pa namespace empty for this lane post-2026-04-27 migration) |
| Path/endpoint scrub convention | docs/PROVENANCE_LABELS.md |
| Auditor fast path | AUDITOR_PLAYBOOK.md |

## What We Prove

- The frozen Phase 01 interface (`Descriptor`, `LearnedDescriptor`, `manifest_builder`) is implementable using only borrowed OSS — OpenCV, scikit-image, scikit-learn, NumPy.
- The package installs cleanly with `pip install -e .[dev]` on Python 3.13 with no live-monorepo imports and no monorepo path coupling.
- The 17-test pytest suite passes when sibling `gnosis-morph-bench` is installed; 16 pass + 1 cleanly skips when it is not — preserving repo independence.
- The frozen `BenchmarkManifest` shape is consumed unmodified by `gnosis_morph_bench.schema.load_manifest`, producing finite `sigma`, `null_mean`, `null_std`, `silhouette`, and `mean_jaccard` per arm.
- A multi-seed (10-seed) borrowed-baseline ceiling is recorded in `artifacts/robustness/robustness_report.json`; mean σ across seeds comes out to `baseline_orb` 4.14 ± 1.12, `baseline_hu_regionprops` 2.95 ± 1.06, `baseline_hog` 1.15 ± 1.17.
- Determinism is checked: `replay_all_identical == true` for every arm in the seed-42 ablation; reference-freeze SHA256 is byte-stable across arms.

## What We Do Not Claim

- We do not claim that any owned descriptor beats borrowed baselines. Phase 02b is BLOCKED on D-06 (two Indus source files are not present in the portfolio snapshot) and the gate-4 verdict is `UNTESTED`.
- We do not claim cross-corpus generalisation. The fixture is a deterministic 12-glyph synthetic generator; rights-cleared real-glyph evidence does not yet exist in this repo.
- We do not claim public-release readiness, performance superiority, or product readiness.
- We do not claim Indus or cuneiform domain results — those are owned by sibling lanes.

## Blockers / Failures

> The owned-arm authority metric package_boundary_earned is UNTESTED. Two Indus source files are not present in the portfolio snapshot; D-06 retrieval is the unblock.

## Verification Surface

| Code | Check | Verdict |
| --- | --- | --- |
| V_01 | `pip install -e .[dev]` on Python 3.13 | PASS |
| V_02 | pytest without Morph-Bench sibling: 16 pass + 1 skip | PASS |
| V_03 | pytest with Morph-Bench sibling: 17 pass | PASS |
| V_04 | seed-42 ablation matches verification to 6 decimals | PASS |
| V_05 | D-06 owned-arm source retrieval | STAGED |

## License

| Field | Value |
| --- | --- |
| License | Apache-2.0+CC-BY-4.0 |
| Authority source | README.md |

## Upcoming Workstreams

| Category | Summary |
| --- | --- |
| Active Engineering | Continue current authority-packet refinement on Gnosis-Glyph-Engine; surface new receipts as they land. |
| Operations / External Dependency | Maintain CI gates and license-resolver synchronization with Zer0pa/ZPE-License-Commercial. |

## Related Repos

No related repos are declared on the product page frontmatter.

<details>
<summary>Full Visible Product-Page Bento Translation</summary>

This section preserves the product page cells as Markdown text blocks. It intentionally omits shared site navigation, footer chrome, CSS, and scripts.

### Bento Cell 1

> 00 · GNOSIS-GLYPH-ENGINE · ANCIENT SCRIPT GEOMETRYRESEARCH-READY · OWNED ARM UNTESTED Ancient Script Geometry, Symbolic Shape Analysis Shape-only descriptor research for ancient script · Gnosis-Glyph-Engine · gnosis-glyph-engine v0.1.0a1 · github.com/Zer0pa/Glyph-Engine Ancient inscriptions carry geometry that no one has counted at the level of a single mark. Glyph-Engine runs three off-the-shelf shape algorithms — ORB, Hu regionprops, and HOG — across a 12-glyph fixture, ten seeds deep, and reports how steady each one is. HOG is the steadiest at sigma 1.15. Re-running with the same seed gives the same numbers, bit for bit. The page does not claim to read or decipher the marks, and the in-house descriptor stays UNTESTED until two missing Indus source files are recovered.

### Bento Cell 2

> 01 · THE GAPREADING VS MEASURING Paleography has names for ancient marks but no shared numbers for their shape. Glyph-Engine measures the shape without claiming to read it.

### Bento Cell 3

> 02 · MARKETSADJACENT FORECASTS Computer vision software'31 · $45.9B OCR software'30 · $22.4B Document AI'30 · $17.2B Heritage digitization'30 · $8.1B Digital humanities'30 · $3.2B Adjacent markets run on shape recognition; ancient-script geometry is the narrow, mostly unpriced corner inside them.

### Bento Cell 4

> 03 · VALUE $8.1B Heritage digitization '30 — the funded market where ancient-mark geometry becomes usable scholarly evidence.

### Bento Cell 5

> 04 · INSIGHT Ancient marks have a shape. Now it can be counted.

### Bento Cell 6

> 05.1 · CURRENT TECHDESCRIBED, NOT MEASURED Epigraphers and paleographers describe ancient marks by sign name, period, or catalogue entry. No common tool reports the geometry of the stroke itself, so visual arguments rest on prose and plates, not on numbers.

### Bento Cell 7

> 05.2 · OUR TECHGEOMETRY MEASUREMENT FIRST Glyph-Engine puts numbers on shape and reports how steady each number is. Three off-the-shelf algorithms — ORB, Hu regionprops, and HOG — run ten-seed sweeps over a 12-glyph synthetic fixture, with HOG at sigma 1.15 the steadiest. The same fixture and seeds are shared with the sibling Morph-Bench project. The in-house descriptor is not yet running, and nothing on this page claims to read a mark.

### Bento Cell 8

> 05.3 · BENCHMARKSBORROWED-ARM RESULTS ORB σ4.1410-seed mean Hu σ2.9510-seed mean HOG σ1.15most stable Tests17/17with sibling HOG σ1.15 Hu σ2.95 ORB σ4.14 Status: The three off-the-shelf algorithms have numbers; the in-house descriptor is UNTESTED until two missing Indus source files are recovered.

### Bento Cell 9

> 06 · MEASUREMENTBORROWED-ARM SIGMA Three off-the-shelf shape algorithms read the 12-glyph fixture. The in-house descriptor is not running yet.

### Bento Cell 10

> 06.1 · COMPARATIVE PERFORMANCE · 10-SEED SIGMA HOG (borrowed)σ 1.15 · most stable Hu regionprops (borrowed)σ 2.95 OpenCV ORB (borrowed)σ 4.14 Owned descriptorUNTESTED · D-06 unblocks 10-seed σ mean across borrowed ORB, Hu regionprops, and HOG over the 12-glyph synthetic fixture; lower σ means a more stable shape number. The owned descriptor has no number yet.

### Bento Cell 11

> 07 · KEY METRICSMEASURED RESULTS

### Bento Cell 12

> 07.1 · ORB ROBUSTNESS Σ 4.14 10-seed mean · borrowed OpenCV ORB

### Bento Cell 13

> 07.2 · HU REGIONPROPS Σ 2.95 10-seed mean · borrowed scikit-image regionprops

### Bento Cell 14

> 07.3 · HOG ROBUSTNESS Σ 1.15 10-seed mean · steadiest borrowed arm

### Bento Cell 15

> 07.4 · PYTEST SURFACE 17/17 17 pass with sibling · 16 pass plus 1 skip without it

### Bento Cell 16

> 07.5 · OWNED DESCRIPTOR Σ null Owned descriptor pending · D-06 is the unblock

### Bento Cell 17

> 08 · DETERMINISMPER-ARM REPLAY Seed-42 replay is per borrowed arm, not owned arms.

### Bento Cell 18

> 08.1 · WHAT DETERMINISM MEANSBORROWED BASELINES ONLY At seed 42, each borrowed ORB, Hu regionprops, and HOG arm replays identically: replay_all_identical == true. The reference-freeze SHA-256 is byte-stable across the declared 12-glyph fixture. The same fixture produces the same numbers, every run. That does not prove owned descriptors, real glyphs, or arbitrary scripts. The unit of bit-exactness is per-arm, per-seed, borrowed baselines only. Shape measurement without determinism is anecdote; determinism is the thin floor under everything else here.

### Bento Cell 19

> 08.2 · HONEST BLOCKER Honest Blocker · package_boundary_earned is UNTESTED. PyPI 0.1.0a1 is a public alpha with incomplete metadata. D-06 must retrieve scripts/indus/stroke_native_encoding.py and phase3_common.py before owned arms run. Claims stop at borrowed-baseline receipts: no release, no owned encoder, no production engine, no script understanding.

### Bento Cell 20

> 09 MARKS WITH A MEASURED SHAPE.

### Bento Cell 21

> 09.1 · THIS REPO'S AMBITION Glyph-Engine wants ancient-mark geometry to become an evidence layer that heritage researchers, paleographers, and decipherment specialists can share. The ambition is a shape vocabulary that travels between archives and journals without smuggling in a reading, so the conversation about what the marks mean can rest on what they actually look like.

### Bento Cell 22

> 09.2 · WHAT WORKS NOW Three borrowed shape arms produce stable, bit-identical numbers over a declared 12-glyph fixture today.

### Bento Cell 23

> 09.3 · WHAT'S STILL OPEN The owned descriptor and a real-glyph corpus stay UNTESTED until D-06 retrieves the missing Indus files.

### Bento Cell 24

> 09.4 · ARCHIVES · NEAR-TERM (12–24 MO) Heritage archives sort marks by shape A heritage archive curator can group thousands of unread marks by geometric similarity instead of cataloguer notes. The same descriptor numbers travel between corpora, so sorting decisions are reviewable by anyone, not stuck in one institution's house style.

### Bento Cell 25

> 09.5 · SCHOLARSHIP · NEAR-TERM (12–24 MO) Paleographers gain a measurement vocabulary A paleographer publishing a stroke-form argument can attach a sigma figure to the visual claim. Reviewers can re-run the descriptors against their own corpus and disagree on numbers instead of impressions, which moves epigraphic debate onto firmer ground.

### Bento Cell 26

> 09.6 · DECIPHERMENT DISCIPLINE · MID-TERM (24–48 MO) Shape and meaning stay separated Script-decipherment specialists working on contested scripts get a reusable shape layer that refuses to encode a reading. That keeps speculative translations from quietly leaking into descriptor metadata, which is how earlier decipherment programmes contaminated the evidence they were trying to weigh.

### Bento Cell 27

> 09.7 · TOOLING · MID-TERM (24–48 MO) Digital humanities tools share one floor A digital-humanities lab adopting Glyph-Engine baselines as a common floor can compare its custom descriptors against three well-understood arms before publishing a kernel. Comparison becomes the first step, not the last, so weak descriptors are caught before they reach a manuscript.

### Bento Cell 28

> 09.8 · METHOD · PARADIGM (48 MO+) Geometry travels across heritage domains A descriptor kernel that earns its independent boundary can move beyond ancient script into seals, pottery marks, textile motifs, and rock art. The portable object is the measurement method itself, which is what changes how heritage research builds reusable evidence.

</details>

---

Source mapping: product route `/gnosis/Gnosis-Glyph-Engine/` -> live public repo `Zer0pa/Glyph-Engine`. README generated from product-page authority plus retained install/dev commands only.
