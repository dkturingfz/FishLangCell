"""Helpers for dataset inventory artifacts."""

from __future__ import annotations

from pathlib import Path

from fish_langcell.data.governance import INVENTORY_ALIASES
from fish_langcell.utils.io import load_tsv_header
from fish_langcell.utils.validation import REQUIRED_METADATA_COLUMNS


def validate_inventory(path: str | Path) -> list[str]:
    """Validate metadata-standard columns in a dataset inventory TSV.

    Allows known alias columns from the full PRD template.
    """
    columns = set(load_tsv_header(path))
    missing: list[str] = []

    for required in REQUIRED_METADATA_COLUMNS:
        candidates = INVENTORY_ALIASES.get(required, (required,))
        if not any(candidate in columns for candidate in candidates):
            missing.append(required)

    return missing
