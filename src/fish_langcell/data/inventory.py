"""Helpers for dataset inventory artifacts."""

from __future__ import annotations

from pathlib import Path

from fish_langcell.utils.io import load_tsv_header
from fish_langcell.utils.validation import REQUIRED_METADATA_COLUMNS

ALIASES: dict[str, tuple[str, ...]] = {
    "stage": ("stage", "developmental_stage"),
    "source": ("source", "source_type"),
    "donor_id": ("donor_id", "donor_id_available"),
    "label_original": ("label_original", "label_original_available"),
    "label_harmonized": ("label_harmonized", "label_harmonized_available"),
}


def validate_inventory(path: str | Path) -> list[str]:
    """Validate metadata-standard columns in a dataset inventory TSV.

    Allows known alias columns from the full PRD template.
    """
    columns = set(load_tsv_header(path))
    missing: list[str] = []

    for required in REQUIRED_METADATA_COLUMNS:
        candidates = ALIASES.get(required, (required,))
        if not any(candidate in columns for candidate in candidates):
            missing.append(required)

    return missing
