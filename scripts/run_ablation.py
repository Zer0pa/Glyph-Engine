"""Thin shim so `python scripts/run_ablation.py` works from a checked-out
repo root. The real implementation lives at
``gnosis_glyph_engine.scripts.run_ablation``; the console entry point
``glyph-engine-ablation`` (see ``pyproject.toml``) also routes there.
"""

from __future__ import annotations

from gnosis_glyph_engine.scripts.run_ablation import main


if __name__ == "__main__":
    raise SystemExit(main())
