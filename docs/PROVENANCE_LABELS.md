# Provenance Labels

This repo replaces operational endpoints and absolute local paths with
symbolic labels in all public-facing surfaces. Scientific provenance is
preserved; operational fingerprinting is not. Real values live only in
owner-held records and internal GPD state.

| Label | Refers to | Handled by |
|---|---|---|
| `<LOCAL_MONOREPO_ROOT>` | Path to the live-monorepo source checkout used to seed this workstream | Owner's local workstation |
| `<LOCAL_WORKSTREAM_ROOT>` | Path to this scaffold on an authoring host | Author's local workstation |
| `<RUNPOD_HOST>` | The RunPod TCP endpoint used as execution substrate | Owner via RunPod dashboard |
| `<RUNPOD_POD_ID>` | The RunPod pod identifier | Owner via RunPod dashboard |
| `<RUNPOD_WORKSPACE>` | The `/workspace/...` path on the pod | Provisioning script |
| `<HF_ORG>` | The Hugging Face organisation hosting the artefact dataset | Owner via HF dashboard |
| `<HF_DATASET>` | The HF dataset repo id for artefacts | `HF_CUSTODY_REGISTER.md` |
| `<GH_ORG>` | The GitHub organisation hosting this repo | Owner via GitHub |
| `<GH_REPO>` | The GitHub repo id | Owner via GitHub |

Rules:

- Every surface a reviewer can read from a public clone must use the
  symbolic labels above, never the literal values.
- Internal provenance surfaces (owner-held notes, session memory,
  off-repo transfer logs) may keep literal values.
- Replacement is mechanical and lossless. If a surface required a
  literal value for scientific reproduction, it is not replaced; it is
  moved into `HF_CUSTODY_REGISTER.md` (for remote repo identity) or
  annotated with "operational; verify with owner".
