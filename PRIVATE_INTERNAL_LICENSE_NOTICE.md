# Private Internal License Notice

Date: 2026-04-24
Status: `PRIVATE_INTERNAL_ONLY`

No public license is granted unless and until a canonical `LICENSE` file is
added by Zer0pa. This repository, its source code, its tests, its
documentation, its artefacts, and all associated Hugging Face datasets and
model assets are Zer0pa-internal.

Current posture:

- GitHub visibility: private / internal.
- Hugging Face companion repos: private.
- `LICENSE_PLACEHOLDER.md` is a placeholder, not a licence grant. It does
  not confer any rights.
- `pyproject.toml` carries `license = { text = "OWNER_DEFERRED" }`. This
  string is not a recognised open-source licence under SPDX and should not
  be interpreted as one.
- GitHub may surface the placeholder as an `Other` licence in repo
  metadata. That is a side effect of the placeholder file's presence; it
  is not a licence grant.

What this means in practice:

1. External collaborators MUST NOT fork, mirror, redistribute, or derive
   from this repo until Zer0pa publishes a canonical `LICENSE` and updates
   this notice.
2. Internal collaborators work under existing Zer0pa employment,
   contractor, or confidentiality terms — not under any open-source
   licence grant.
3. AI agents (including agentic closeout runs) MUST NOT treat the
   placeholder as permission to publish code or artefacts externally.
4. Any legal / licensing questions that need to be resolved before a
   public release are catalogued in the Zer0pa closeout brief dated
   2026-04-24, section **Legal And Licensing Brief**.

Supersession:

This notice is superseded only by a canonical `LICENSE` file co-located
at repo root, accompanied by explicit removal of `LICENSE_PLACEHOLDER.md`
and an update to `pyproject.toml`'s `license` field with a valid SPDX
identifier. Either action without the other leaves this notice in force.

Owner: Zer0pa (`architects@zer0pa.ai`).
