<!-- Template: contribution discipline for truthful live repo work. -->

# Contributing

## First Rule

Contribute only what this repo can honestly support. Do not import claims,
metrics, or release language from another Zer0pa repo.

## Before You Start

1. Read `README.md` for the current public truth.
2. Read `GOVERNANCE.md` for status and claim rules.
3. Read `docs/ARCHITECTURE.md` for the actual component map.
4. Use an issue or documented task as the source of change intent.

## Contribution Rules

- Keep scope tight. One change should have one coherent reason.
- If you add or change a public claim, update the evidence path with it.
- If you cannot verify a statement, mark it `UNKNOWN`, `UNVERIFIED`,
  `INFERRED`, or `OWNER_DEFERRED`.
- Do not widen roadmap or legal language opportunistically.
- Keep docs, code, and release semantics in sync.

## Pull Requests

Every PR should state:

- what changed
- why it changed
- what evidence or test supports it
- what docs were updated
- what remains unknown or deferred

Use the PR template. If the change affects public truth, update the relevant doc
surface in the same PR.

## Boundaries

- Security-sensitive issues belong in `SECURITY.md`, not in a public exploit
  write-up.
- Evidence disputes belong in the evidence dispute template.
- Questions that do not require a code change should use the question template.
