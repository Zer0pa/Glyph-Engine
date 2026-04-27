# Conventions

- Workspace root: this `05_repo_scaffold/` directory.
- Authority metric: `package_boundary_earned`.
- Public posture: no public repo, release, or package claim while the metric is
  `UNTESTED`.
- Build-vs-borrow rule: borrow commodity OSS layers; own only a descriptor or
  geometry contract that survives consumer pressure and ablation.
- Extraction rule: record every copied source path, rewritten import, fixture,
  and borrowed dependency in `SOURCE_BOUNDARY.md` before implementation.
- Reporting rule: no interim reporting unless a blocker cannot be answered
  from admitted evidence. Final report only at phase close.
- Remote rule: GitHub `Zer0pa/Glyph-Engine` is the canonical code remote
  (private). Hugging Face `Architect-Prime/glyph-engine-artefacts` is the artefact
  failover surface. Neither is public.
- Git hygiene: atomic commits per GPD sub-task; commit messages cite the
  authority metric and phase id; no force-push, no rebase of shared history.
- Environment rule: Phase 02+ compute runs on the RunPod host under
  `<RUNPOD_WORKSPACE>/gnosis-glyph-engine/` with a Python 3.13 venv; the Mac is the
  authoring surface only.
