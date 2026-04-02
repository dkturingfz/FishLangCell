"""Governance validators for inventory, manifests, ontology, and starter artifacts."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import yaml

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

REQUIRED_MANIFEST_COLUMNS: tuple[str, ...] = REQUIRED_INVENTORY_COLUMNS

INVENTORY_ALIASES: dict[str, tuple[str, ...]] = {
    "source": ("source", "source_type"),
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

REQUIRED_VOCAB_COLUMNS: dict[str, tuple[str, ...]] = {
    "data/vocab/fish_gene_vocab_v0.1.tsv": (
        "token_id",
        "species",
        "gene_id",
        "gene_symbol",
        "gene_biotype",
        "is_protein_coding",
        "orthogroup_id",
        "human_ortholog",
        "is_testis_marker",
        "is_germline_marker",
        "is_somatic_marker",
        "status",
        "source",
        "notes",
    ),
    "data/vocab/zebrafish_gene_reference.tsv": (
        "gene_id",
        "gene_symbol",
        "gene_name",
        "gene_biotype",
        "chromosome",
        "start",
        "end",
        "strand",
        "genome_build",
        "source",
        "notes",
    ),
    "data/vocab/gene_symbol_to_ensembl.tsv": (
        "gene_symbol",
        "gene_id",
        "mapping_status",
        "mapping_source",
        "ambiguity_flag",
        "notes",
    ),
    "data/vocab/orthogroup_reference.tsv": (
        "orthogroup_id",
        "species",
        "gene_id",
        "gene_symbol",
        "ortholog_group_label",
        "human_ortholog",
        "evidence_source",
        "notes",
    ),
}

ALLOWED_VOCAB_STATUS: set[str] = {
    "active",
    "placeholder",
    "pending_curation",
    "deprecated",
    "excluded",
}

REQUIRED_TEXT_CORPUS_FILES: tuple[str, ...] = (
    "data/text_corpus/fish_celltype_definitions.jsonl",
    "data/text_corpus/testis_celltype_definitions.jsonl",
    "data/text_corpus/marker_sentences.jsonl",
    "data/text_corpus/hierarchy_descriptions.jsonl",
)

REQUIRED_TEXT_CORPUS_FIELDS: tuple[str, ...] = (
    "id",
    "species_scope",
    "tissue_scope",
    "ontology_namespace",
    "label_original",
    "label_harmonized",
    "label_hierarchical",
    "text_type",
    "text",
    "markers",
    "source",
    "status",
    "notes",
)

ALLOWED_TEXT_TYPE: set[str] = {
    "definition",
    "marker_prompt",
    "hierarchy_description",
    "alias",
}

ALLOWED_TEXT_STATUS: set[str] = {
    "draft",
    "reviewed",
    "frozen",
    "deprecated",
}

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


def _validate_split_and_use(rows: list[dict[str, str]], errors: list[str]) -> None:
    bad_split = sorted(
        {
            (row.get("dataset_id") or "<unknown>", row.get("split", ""))
            for row in rows
            if row.get("split", "") not in ALLOWED_SPLITS
        }
    )
    if bad_split:
        errors.append(
            "Invalid split values: " + ", ".join([f"{dataset_id}:{value}" for dataset_id, value in bad_split])
        )

    bad_use = sorted(
        {
            (row.get("dataset_id") or "<unknown>", row.get("recommended_use", ""))
            for row in rows
            if row.get("recommended_use", "") not in ALLOWED_RECOMMENDED_USE
        }
    )
    if bad_use:
        errors.append(
            "Invalid recommended_use values: "
            + ", ".join([f"{dataset_id}:{value}" for dataset_id, value in bad_use])
        )


def _validate_provenance_placeholders(rows: list[dict[str, str]], column_set: set[str], warnings: list[str]) -> None:
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


def validate_inventory_artifact(path: str | Path) -> ValidationReport:
    headers = load_tsv_header(path)
    rows = load_tsv_rows(path)
    column_set = set(headers)

    errors: list[str] = []
    warnings: list[str] = []

    missing_required = _resolve_alias_missing(column_set, REQUIRED_INVENTORY_COLUMNS)
    if missing_required:
        errors.append(f"Missing required columns: {', '.join(missing_required)}")

    _validate_split_and_use(rows, errors)
    _validate_provenance_placeholders(rows, column_set, warnings)

    return ValidationReport(str(path), len(rows), errors, warnings)


def validate_manifest_artifact(path: str | Path) -> ValidationReport:
    headers = load_tsv_header(path)
    rows = load_tsv_rows(path)
    column_set = set(headers)

    errors: list[str] = []
    warnings: list[str] = []

    missing_required = _resolve_alias_missing(column_set, REQUIRED_MANIFEST_COLUMNS)
    if missing_required:
        errors.append(f"Missing required columns: {', '.join(missing_required)}")

    _validate_split_and_use(rows, errors)
    _validate_provenance_placeholders(rows, column_set, warnings)

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


def validate_vocab_artifacts(base_dir: str | Path = ".") -> ValidationReport:
    base = Path(base_dir)
    errors: list[str] = []
    warnings: list[str] = []
    total_rows = 0

    for rel_path, required_cols in REQUIRED_VOCAB_COLUMNS.items():
        path = base / rel_path
        if not path.exists():
            errors.append(f"Missing vocab file: {rel_path}")
            continue
        headers = load_tsv_header(path)
        rows = load_tsv_rows(path)
        total_rows += len(rows)
        missing = validate_required_columns(headers, required_cols)
        if missing:
            errors.append(f"{rel_path} missing required columns: {', '.join(missing)}")

        if rel_path.endswith("fish_gene_vocab_v0.1.tsv") and "status" in headers:
            for idx, row in enumerate(rows, start=2):
                status = row.get("status", "")
                if status not in ALLOWED_VOCAB_STATUS:
                    errors.append(
                        f"{rel_path}:{idx} invalid status '{status}'. "
                        f"Allowed: {', '.join(sorted(ALLOWED_VOCAB_STATUS))}"
                    )

    return ValidationReport("vocab_artifacts", total_rows, errors, warnings)


def validate_text_corpus_artifacts(base_dir: str | Path = ".") -> ValidationReport:
    base = Path(base_dir)
    errors: list[str] = []
    warnings: list[str] = []
    total_rows = 0

    for rel_path in REQUIRED_TEXT_CORPUS_FILES:
        path = base / rel_path
        if not path.exists():
            errors.append(f"Missing text corpus file: {rel_path}")
            continue

        with path.open("r", encoding="utf-8") as handle:
            for line_number, raw in enumerate(handle, start=1):
                line = raw.strip()
                if not line:
                    continue
                total_rows += 1
                try:
                    payload = json.loads(line)
                except json.JSONDecodeError as exc:
                    errors.append(f"{rel_path}:{line_number} invalid JSON: {exc.msg}")
                    continue

                missing = [f for f in REQUIRED_TEXT_CORPUS_FIELDS if f not in payload]
                if missing:
                    errors.append(f"{rel_path}:{line_number} missing required fields: {', '.join(missing)}")
                    continue

                if payload.get("text_type") not in ALLOWED_TEXT_TYPE:
                    errors.append(
                        f"{rel_path}:{line_number} invalid text_type '{payload.get('text_type')}'. "
                        f"Allowed: {', '.join(sorted(ALLOWED_TEXT_TYPE))}"
                    )

                if payload.get("status") not in ALLOWED_TEXT_STATUS:
                    errors.append(
                        f"{rel_path}:{line_number} invalid status '{payload.get('status')}'. "
                        f"Allowed: {', '.join(sorted(ALLOWED_TEXT_STATUS))}"
                    )

                if not isinstance(payload.get("markers"), list):
                    errors.append(f"{rel_path}:{line_number} field 'markers' must be a JSON array")

    return ValidationReport("text_corpus_artifacts", total_rows, errors, warnings)


def validate_tokenization_spec(
    path: str | Path = "configs/tokenization/zebrafish_sequence_builder.yaml",
) -> ValidationReport:
    errors: list[str] = []
    warnings: list[str] = []

    required_files = (
        "docs/tokenization_spec.md",
        "configs/vocab/id_policy.yaml",
        "data/vocab/fish_gene_vocab_v0.1.tsv",
        str(path),
    )

    for req in required_files:
        if not Path(req).exists():
            errors.append(f"Missing required tokenization dependency file: {req}")

    path_obj = Path(path)
    if path_obj.exists():
        content = path_obj.read_text(encoding="utf-8")
        required_keys = (
            "input_dataset_paths:",
            "input_metadata_paths:",
            "canonical_id_type:",
            "matrix_orientation:",
            "raw_count_preference_policy:",
            "future_sequence_output_directory:",
            "rank_tokenization_placeholders:",
        )
        for key in required_keys:
            if key not in content:
                errors.append(f"Missing tokenization config key: {key.rstrip(':')}")

        try:
            yaml.safe_load(content)
        except yaml.YAMLError as exc:
            errors.append(f"Invalid YAML in {path_obj}: {exc}")

    return ValidationReport("tokenization_spec_dependencies", 1, errors, warnings)
