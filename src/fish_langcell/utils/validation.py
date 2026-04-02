"""Validation utilities for metadata and tabular project artifacts."""

from __future__ import annotations

from typing import Iterable, Sequence


REQUIRED_METADATA_COLUMNS: tuple[str, ...] = (
    "dataset_id",
    "species",
    "tissue",
    "stage",
    "sex",
    "assay",
    "source",
    "paper_id",
    "donor_id",
    "gene_id_type",
    "label_original",
    "label_harmonized",
    "split",
)


def validate_required_columns(columns: Sequence[str], required: Iterable[str]) -> list[str]:
    """Return missing columns from *required* that are absent in *columns*."""
    column_set = set(columns)
    return [column for column in required if column not in column_set]
