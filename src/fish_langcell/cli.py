"""CLI entrypoints for Fish-LangCell scaffold workflows."""

from __future__ import annotations

import argparse
from pathlib import Path


def _require_existing_path(path_str: str, label: str) -> Path:
    path = Path(path_str)
    if not path.exists():
        raise FileNotFoundError(f"{label} does not exist: {path}")
    return path


def _print_todo(task: str) -> None:
    print(f"[TODO] {task}: implementation is scaffold-only in v0.1 initialization.")


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="fish-langcell", description="Fish-LangCell unified command interface")
    subparsers = parser.add_subparsers(dest="command", required=True)

    ingest = subparsers.add_parser("ingest-dataset", help="Ingest dataset into standardized project format")
    ingest.add_argument("--input", required=True, help="Input dataset path (h5ad/mtx/loom)")
    ingest.add_argument("--dataset-id", required=True, help="Unique dataset identifier")

    harmonize = subparsers.add_parser("harmonize-labels", help="Apply ontology-driven label harmonization")
    harmonize.add_argument("--inventory", default="data/data_inventory.tsv", help="Data inventory TSV path")
    harmonize.add_argument("--mapping", default="data/ontology/ontology_mapping.tsv", help="Ontology mapping TSV path")

    validate_inventory = subparsers.add_parser("validate-inventory", help="Validate dataset inventory governance artifact")
    validate_inventory.add_argument("--inventory", default="data/data_inventory.tsv", help="Data inventory TSV path")

    validate_ontology = subparsers.add_parser("validate-ontology", help="Validate ontology mapping governance artifact")
    validate_ontology.add_argument("--mapping", default="data/ontology/ontology_mapping.tsv", help="Ontology mapping TSV path")

    vocab = subparsers.add_parser("build-vocab", help="Build fish-native vocabulary artifacts")
    vocab.add_argument("--config", default="configs/vocab/zebrafish_vocab.yaml", help="Vocabulary config path")

    seq = subparsers.add_parser("build-sequences", help="Build ranked fish gene token sequences")
    seq.add_argument("--config", default="configs/train/pretrain_cell.yaml", help="Sequence build config path")

    cell = subparsers.add_parser("train-cell-encoder", help="Run fish-native cell encoder pretraining")
    cell.add_argument("--config", default="configs/train/pretrain_cell.yaml", help="Pretraining config path")

    mm = subparsers.add_parser("train-multimodal", help="Train multimodal cell-text alignment model")
    mm.add_argument("--config", default="configs/train/align_multimodal.yaml", help="Alignment config path")

    testis = subparsers.add_parser("tune-testis", help="Run fish testis domain tuning")
    testis.add_argument("--config", default="configs/train/tune_testis.yaml", help="Testis tuning config path")

    bench = subparsers.add_parser("run-benchmark", help="Run project benchmark suites")
    bench.add_argument("--config", default="configs/train/eval.yaml", help="Benchmark config path")

    export = subparsers.add_parser("export-model", help="Export model bundle and release metadata")
    export.add_argument("--checkpoint", required=True, help="Checkpoint path to export")
    export.add_argument("--output-dir", default="outputs/export", help="Output directory")

    return parser


def _run_command(args: argparse.Namespace) -> int:
    print(f"[Fish-LangCell] command start: {args.command}")

    if args.command == "ingest-dataset":
        _require_existing_path(args.input, "Input dataset")
        print(f"Ingestion request accepted for dataset '{args.dataset_id}' from: {args.input}")
        _print_todo("ingest-dataset")

    elif args.command == "harmonize-labels":
        _require_existing_path(args.inventory, "Inventory TSV")
        _require_existing_path(args.mapping, "Ontology mapping TSV")
        from fish_langcell.data import validate_inventory

        missing = validate_inventory(args.inventory)
        if missing:
            print(f"Inventory is missing required columns: {missing}")
            return 2
        print("Inventory metadata columns validated. Harmonization scaffold ready.")
        _print_todo("harmonize-labels")

    elif args.command == "validate-inventory":
        _require_existing_path(args.inventory, "Inventory TSV")
        from fish_langcell.data import validate_inventory_artifact

        report = validate_inventory_artifact(args.inventory)
        print(report.summary())
        for warning in report.warnings:
            print(f"WARNING: {warning}")
        for error in report.errors:
            print(f"ERROR: {error}")
        return 0 if report.ok else 2

    elif args.command == "validate-ontology":
        _require_existing_path(args.mapping, "Ontology mapping TSV")
        from fish_langcell.data import validate_ontology_artifact

        report = validate_ontology_artifact(args.mapping)
        print(report.summary())
        for warning in report.warnings:
            print(f"WARNING: {warning}")
        for error in report.errors:
            print(f"ERROR: {error}")
        return 0 if report.ok else 2

    elif args.command in {"build-vocab", "build-sequences", "train-cell-encoder", "train-multimodal", "tune-testis", "run-benchmark"}:
        _require_existing_path(args.config, "Config file")
        print(f"Command '{args.command}' using config: {args.config}")
        _print_todo(args.command)

    elif args.command == "export-model":
        _require_existing_path(args.checkpoint, "Checkpoint")
        output_dir = Path(args.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        print(f"Export request accepted for checkpoint: {args.checkpoint}")
        print(f"Output directory prepared: {output_dir}")
        _print_todo("export-model")

    else:
        raise ValueError(f"Unknown command: {args.command}")

    print(f"[Fish-LangCell] command complete: {args.command}")
    return 0


def main() -> int:
    parser = _build_parser()
    args = parser.parse_args()
    return _run_command(args)


if __name__ == "__main__":
    raise SystemExit(main())
