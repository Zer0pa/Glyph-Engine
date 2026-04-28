# Roadmap

## Active Priorities

| Priority | Item | Entry gate | Evidence needed | Status |
|---|---|---|---|---|
| P0 | Freeze source and consumer boundary | package transfer complete | `SOURCE_BOUNDARY.md`, Phase 01 decisions | `DONE` |
| P1 | Define minimal descriptor interface | P0 pass | `Descriptor`, `LearnedDescriptor`, `manifest_builder` | `DONE` |
| P2 | Extract borrowed-baseline runtime slice | P1 pass | package root, smoke path, path-rewrite ledger | `DONE` |
| P3 | Run borrowed-baseline ablation and robustness | P2 pass | Phase 02a + 02c artefacts | `DONE` |
| P4 | Keep Ops-Gates hygiene load-bearing | CI edit | coupling audit in `.github/workflows/ci.yml` | `DONE` |
| P5 | Run owned-arm ablation | D-06 source retrieval | owned-arm metrics versus Phase 02c ceiling | `BLOCKED_ON_D-06` |
| P6 | Package-boundary review | P5 complete | `package_boundary_earned` declaration | `PENDING` |

## Deferred Work

| Item | Reason | Unblock condition | Status |
|---|---|---|---|
| Public repo promotion | package boundary not earned | Phase 03 declares the boundary earned and operator approves visibility | `DEFERRED` |
| Commercial/library claims | owned arms untested | Phase 02b + Phase 03 evidence | `DEFERRED` |
| Cross-corpus claims | no rights-cleared real-glyph fixture | rights-cleared fixture + new evidence | `DEFERRED` |

## Stop Conditions

- Owned arms fail to beat the multi-seed ORB ceiling by the D-04 rule.
- Extraction requires broad Indus or cuneiform domain logic rather than a
  constrained descriptor slice.
- The repo begins presenting Apache/CC licensing as public-readiness proof.
