"""CLI entrypoints for Fish-LangCell scaffolding workflows."""

from __future__ import annotations

import argparse


def _print_stub(task: str, args: argparse.Namespace) -> int:
    print(f"[Fish-LangCell] {task} invoked")
    print(f"Arguments: {args}")
    return 0


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="fish-langcell", description="Fish-LangCell unified command interface.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    ingest = subparsers.add_parser("ingest-dataset", help="Ingest dataset into standardized format.")
    ingest.add_argument("--input", required=False, help="Input dataset path (h5ad/mtx/loom).")
    ingest.add_argument("--dataset-id", required=False, help="Unique dataset identifier.")

    vocab = subparsers.add_parser("build-vocab", help="Build fish-native gene vocabulary artifacts.")
    vocab.add_argument("--config", default="configs/vocab/zebrafish_vocab.yaml", help="Vocabulary config path.")

    seq = subparsers.add_parser("build-sequences", help="Build ranked gene token sequences.")
    seq.add_argument("--config", default="configs/train/pretrain_cell.yaml", help="Sequence build config path.")

    cell = subparsers.add_parser("train-cell-encoder", help="Run fish-native cell encoder pretraining.")
    cell.add_argument("--config", default="configs/train/pretrain_cell.yaml", help="Training config path.")

    mm = subparsers.add_parser("train-multimodal", help="Train multimodal cell-text alignment model.")
    mm.add_argument("--config", default="configs/train/align_multimodal.yaml", help="Training config path.")

    testis = subparsers.add_parser("tune-testis", help="Run testis domain tuning.")
    testis.add_argument("--config", default="configs/train/tune_testis.yaml", help="Training config path.")

    bench = subparsers.add_parser("run-benchmark", help="Run benchmark suites.")
    bench.add_argument("--config", default="configs/train/eval.yaml", help="Benchmark config path.")

    return parser


def _run_command(args: argparse.Namespace) -> int:
    return _print_stub(args.command, args)


def main() -> int:
    parser = _build_parser()
    args = parser.parse_args()
    return _run_command(args)


def _standalone(cmd: str, argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args([cmd, *(argv or [])])
    return _run_command(args)


def ingest_dataset() -> int:
    return _standalone("ingest-dataset")


def build_vocab() -> int:
    return _standalone("build-vocab")


def build_sequences() -> int:
    return _standalone("build-sequences")


def train_cell_encoder() -> int:
    return _standalone("train-cell-encoder")


def train_multimodal() -> int:
    return _standalone("train-multimodal")


def tune_testis() -> int:
    return _standalone("tune-testis")


def run_benchmark() -> int:
    return _standalone("run-benchmark")


if __name__ == "__main__":
    raise SystemExit(main())
