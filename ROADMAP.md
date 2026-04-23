# Roadmap

## Active Priorities

| Priority | Item | Entry gate | Evidence needed | Status |
|---|---|---|---|---|
| P0 | Freeze source and consumer boundary | package transfer complete | updated `SOURCE_BOUNDARY.md` and `.gpd/STATE.md` | `NOT_STARTED` |
| P1 | Define minimal descriptor interface | P0 pass | interface note and tiny fixture plan | `BLOCKED_ON_P0` |
| P2 | Extract first runtime slice | P1 pass | package root, smoke path, path-rewrite ledger | `BLOCKED_ON_P1` |
| P3 | Run ablation against borrowed baselines | P2 pass | benchmark report | `BLOCKED_ON_P2` |

## Deferred Work

| Item | Reason | Unblock condition | Status |
|---|---|---|---|
| Public repo promotion | package boundary not earned | `package_boundary_earned` passes | `DEFERRED` |
| Commercial/library claims | no ablation or second consumer | benchmark proof exists | `DEFERRED` |
