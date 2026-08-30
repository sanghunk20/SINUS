"""The one place that answers "where is the repository root".

Every module that has to reach outside the package — feature caches, splits, model
directories, the reconstructed per-structure targets — resolves its paths against
``REPO``.  Relative paths in the configs are read as relative to it.

The layout is ``<REPO>/toothfairy/paths.py``, so the root is one level up from the
package.  Keeping this in a single module means moving the package needs one edit,
not one per file.
"""
from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def resolve(p: str | Path) -> Path:
    """Absolute paths are used as they are; relative ones hang off the repository root."""
    p = Path(p)
    return p if p.is_absolute() else REPO / p
