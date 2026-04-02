"""Governance validators for inventory and ontology TSV artifacts."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from fish_langcell.utils.io import load_tsv_header, load_tsv_rows
from fish_langcell.utils.validation import validate_required_columns

REQUIRED_INVENTORY_COLUMNS: tuple[str, ...] = (
    "dataset_id",
    "species",
    "tissue",
    "assay",
    "gene_id_type",
    "split",
    "recommended_use",
    "source_url",
    "accession_or_link",
    "paper_id",
    "license_or_usage",
    "download_status",
)

INVENTORY_ALIASES: dict[str, tuple[str, ...]] = {
    "stage": ("stage", "developmental_stage"),
    "source": ("source", "source_type"),
    "donor_id": ("donor_id", "donor_id_available"),
    "label_original": ("label_original", "label_original_available"),
    "label_harmonized": ("label_harmonized", "label_harmonized_available"),
}

REQUIRED_ONTOLOGY_COLUMNS: tuple[str, ...] = (
    "original_label",
    "harmonized_label",
    "hierarchical_label",
    "ontology_namespace",
    "ontology_version",
    "mapping_confidence",
    "source_dataset",
    "notes",
)

ALLOWED_SPLITS: set[str] = {"foundation", "testis", "eval", "undecided"}
ALLOWED_RECOMMENDED_USE: set[str] = {
    "foundation_pretrain",
    "testis_tune",
    "holdout_eval",
    "defer_review",
    "exclude_for_now",
}

CRITICAL_PROVENANCE_FIELDS: tuple[str, ...] = (
    "source_url",
    "accession_or_link",
    "paper_id",
    "license_or_usage",
    "download_status",
)

PLACEHOLDER_VALUES: set[str] = {
    "",
    "tbd",
    "unknown",
    "not_started",
    "pending",
    "pending_curation",
    "candidate_identified",
}


@dataclass
class ValidationReport:
    file_path: str
    total_rows: int
    errors: list[str]
    warnings: list[str]

    @property
    def ok(self) -> bool:
        return not self.errors

    def summary(self) -> str:
        status = "PASS" if self.ok else "FAIL"
        return (
            f"[{status}] {self.file_path}: rows={self.total_rows}, "
            f"errors={len(self.errors)}, warnings={len(self.warnings)}"
        )


def _resolve_alias_missing(columns: set[str], required: tuple[str, ...]) -> list[str]:
    missing: list[str] = []
    for name in required:
        aliases = INVENTORY_ALIASES.get(name, (name,))
        if not any(alias in columns for alias in aliases):
            missing.append(name)
    return missing


def validate_inventory_artifact(path: str | Path) -> ValidationReport:
    headers = load_tsv_header(path)
    rows = load_tsv_rows(path)
    column_set = set(headers)

    errors: list[str] = []
    warnings: list[str] = []

    missing_required = _resolve_alias_missing(column_set, REQUIRED_INVENTORY_COLUMNS)
    if missing_required:
        errors.append(f"Missing required columns: {', '.join(missing_required)}")

    split_col = "split"
    use_col = "recommended_use"

    if split_col in column_set:
        bad_split = sorted(
            {
                (row.get("dataset_id") or "<unknown>", row.get(split_col, ""))
                for row in rows
                if row.get(split_col, "") not in ALLOWED_SPLITS
            }
        )
        if bad_split:
            errors.append(
                "Invalid split values: "
                + ", ".join([f"{dataset_id}:{value}" for dataset_id, value in bad_split])
            )

    if use_col in column_set:
        bad_use = sorted(
            {
                (row.get("dataset_id") or "<unknown>", row.get(use_col, ""))
                for row in rows
                if row.get(use_col, "") not in ALLOWED_RECOMMENDED_USE
            }
        )
        if bad_use:
            errors.append(
                "Invalid recommended_use values: "
                + ", ".join([f"{dataset_id}:{value}" for dataset_id, value in bad_use])
            )

    for field in CRITICAL_PROVENANCE_FIELDS:
        if field not in column_set:
            continue
        missing_for_field = [
            row.get("dataset_id") or "<unknown>"
            for row in rows
            if row.get(field, "").strip().lower() in PLACEHOLDER_VALUES
        ]
        if missing_for_field:
            warnings.append(
                f"Missing critical provenance '{field}' for datasets: {', '.join(missing_for_field)}"
            )

    return ValidationReport(str(path), len(rows), errors, warnings)


def validate_ontology_artifact(path: str | Path) -> ValidationReport:
    headers = load_tsv_header(path)
    rows = load_tsv_rows(path)

    errors: list[str] = []
    warnings: list[str] = []

    missing_required = validate_required_columns(headers, REQUIRED_ONTOLOGY_COLUMNS)
    if missing_required:
        errors.append(f"Missing required columns: {', '.join(missing_required)}")

    for idx, row in enumerate(rows, start=2):
        for col in ("original_label", "harmonized_label", "hierarchical_label"):
            if col in headers and not row.get(col, "").strip():
                errors.append(f"Row {idx} has empty required value for '{col}'")

    return ValidationReport(str(path), len(rows), errors, warnings)
