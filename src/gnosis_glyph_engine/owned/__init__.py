"""Owned-arm descriptors. Blocked on Phase 01 decision D-06.

Importing any symbol from this module raises ``SourceRetrievalPending`` until
the two source files named in D-06 are retrieved and the path-rewrite ledger
is recorded in ``SOURCE_BOUNDARY.md``:

- ``scripts/indus/stroke_native_encoding.py`` → ``owned.stroke_compass``
- ``scripts/indus/phase3_common.py`` → ``owned.topology``

Phase 02b will populate this subpackage.
"""

from __future__ import annotations

from ..protocols import SourceRetrievalPending


def stroke_compass(*_args, **_kwargs):  # pragma: no cover - intentionally unimplemented
    raise SourceRetrievalPending(
        "owned.stroke_compass is blocked on Phase 01 D-06: retrieve "
        "scripts/indus/stroke_native_encoding.py from the live monorepo "
        "before Phase 02b."
    )


def topology(*_args, **_kwargs):  # pragma: no cover - intentionally unimplemented
    raise SourceRetrievalPending(
        "owned.topology is blocked on Phase 01 D-06: retrieve "
        "scripts/indus/phase3_common.py from the live monorepo "
        "before Phase 02b."
    )
