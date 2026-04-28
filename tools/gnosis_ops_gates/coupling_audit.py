#!/usr/bin/env python3
"""Coupling audit: scan installable package source for concrete operational
leakage patterns.

Replaces the original CI grep audit, which false-positived on legitimate
explanatory mentions of "ZPE-Cipher" inside docstrings and argparse help
text in `gnosis_ops_gates.preflight.check_repo_truth`. This scanner checks
for **concrete** operational leakage instead of bare substring overlap with
the legacy parent-monorepo brand name.

Forbidden patterns (any hit fails the audit):

- absolute macOS user-home paths
- parent-monorepo workspace paths
- the specific RunPod pod identifier and IPv4 endpoint known to the gates
- ssh invocations carrying an identity file
- common private-key filenames, including security-key variants
- AWS access-key-id shape: ``AKIA[0-9A-Z]{16}``
- Slack token shape
- OpenAI-style API token shape: ``sk-[A-Za-z0-9]{20,}``
- embedded PEM private-key markers

Acceptable (intentionally NOT flagged):

- bare ``ZPE-Cipher`` mentions in docstrings, comments, or argparse help
  text (explanatory legacy-profile terminology preserved by the
  ``--repo-profile parent-monorepo`` API)
- the literal ``parent-monorepo`` profile name
- the bare word ``workspace`` without parent-monorepo path context

Scope
-----

By default this scans every ``.py`` file under ``src`` (passable as
positional argument(s) for testing). Excludes generated metadata
directories (``*.egg-info/``, ``__pycache__``, ``.pytest_cache``,
``.mypy_cache``, ``build``, ``dist``) and virtualenv directories.

Exit code 0 if zero violations; 1 if any violation, with per-line
evidence printed to stdout for CI logs.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Iterable, Iterator, NamedTuple


class Violation(NamedTuple):
    path: str
    line_no: int
    pattern_label: str
    matched_text: str
    line: str


MACOS_USER_PATH = "/" + "Users" + "/"
PARENT_WORKSPACE_PATH = "/" + "workspace" + "/" + "ZPE-"
RUNPOD_POD_ID = "7k3riasg" + "lemecu"
RUNPOD_IPV4_PATTERN = r"38\." + r"80\." + r"152\." + r"147"
PRIVATE_KEY_ALGOS = ("ed25519", "rsa", "ecdsa", "dsa", "xmss")
PRIVATE_KEY_FILENAME_PATTERN = (
    r"\bid_(?:"
    + "|".join(PRIVATE_KEY_ALGOS)
    + r")(?:_sk)?\b"
)
PEM_PRIVATE_KEY_PATTERN = "-----BEGIN " + r"[A-Z ]*" + "PRIVATE KEY-----"

FORBIDDEN_PATTERNS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(re.escape(MACOS_USER_PATH)),                                "macOS user-local path"),
    (re.compile(re.escape(PARENT_WORKSPACE_PATH)),                          "parent-monorepo workspace path"),
    (re.compile(RUNPOD_POD_ID),                                             "specific RunPod pod id"),
    (re.compile(RUNPOD_IPV4_PATTERN),                                       "specific RunPod IPv4"),
    (re.compile(r"\bssh\s+-i\s"),                                           "ssh invocation with identity-file flag"),
    (re.compile(PRIVATE_KEY_FILENAME_PATTERN),                              "private-key filename"),
    (re.compile(r"\bAKIA[0-9A-Z]{16}\b"),                                   "AWS access-key-id shape"),
    (re.compile(r"\bxox[abp]-[A-Za-z0-9-]+"),                               "Slack token shape"),
    (re.compile(r"\bsk-[A-Za-z0-9]{20,}"),                                  "OpenAI-like API token shape"),
    (re.compile(PEM_PRIVATE_KEY_PATTERN),                                   "embedded private key"),
]

EXCLUDE_DIR_NAMES = frozenset({
    ".git",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".tox",
    ".eggs",
    "build",
    "dist",
    ".venv",
    "venv",
    "env",
    "node_modules",
})
EXCLUDE_DIR_SUFFIXES = (".egg-info",)
INCLUDE_FILE_SUFFIXES = (".py",)


def _is_excluded(path: Path) -> bool:
    """True if *path* lies within an excluded directory."""
    for parent in (*path.parents, path):
        if parent.name in EXCLUDE_DIR_NAMES:
            return True
        if any(parent.name.endswith(suffix) for suffix in EXCLUDE_DIR_SUFFIXES):
            return True
    return False


def iter_files(root: Path) -> Iterator[Path]:
    """Yield .py files under *root*, skipping excluded dirs."""
    if not root.exists():
        return
    if root.is_file():
        if root.suffix in INCLUDE_FILE_SUFFIXES and not _is_excluded(root):
            yield root
        return
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix not in INCLUDE_FILE_SUFFIXES:
            continue
        if _is_excluded(path):
            continue
        yield path


def scan(roots: Iterable[Path]) -> list[Violation]:
    """Return every Violation found across *roots*. Empty list = clean."""
    violations: list[Violation] = []
    for root in roots:
        for file_path in iter_files(root):
            try:
                text = file_path.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            for line_no, line in enumerate(text.splitlines(), start=1):
                for pattern, label in FORBIDDEN_PATTERNS:
                    match = pattern.search(line)
                    if match is not None:
                        violations.append(
                            Violation(
                                path=str(file_path),
                                line_no=line_no,
                                pattern_label=label,
                                matched_text=match.group(0),
                                line=line,
                            )
                        )
    return violations


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "roots",
        nargs="*",
        default=["src"],
        help="Files or directories to scan. Default: src.",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Print only the count, not per-line evidence.",
    )
    args = parser.parse_args(argv)
    paths = [Path(p) for p in args.roots]
    missing_paths = [path for path in paths if not path.exists()]
    if missing_paths:
        for path in missing_paths:
            print(f"coupling_audit: missing root: {path}", file=sys.stderr)
        return 1
    violations = scan(paths)
    if not violations:
        print(
            f"coupling_audit: 0 violations across {len(paths)} root(s): "
            + ", ".join(str(p) for p in paths)
        )
        return 0
    if not args.quiet:
        for v in violations:
            print(
                f"{v.path}:{v.line_no}: {v.pattern_label}: "
                f"{v.matched_text!r} in: {v.line.strip()!r}"
            )
    print(f"coupling_audit: {len(violations)} violation(s)")
    return 1


if __name__ == "__main__":
    sys.exit(main())
