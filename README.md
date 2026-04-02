# Fish-LangCell

Fish-LangCell is a **fish-native** multimodal single-cell annotation framework inspired by LangCell, with a zebrafish-first v1 plan and testis specialization track.

## Current status

This repository is initialized as a **scaffold + planning implementation**:
- modular package layout
- versioned configs
- data inventory and ontology templates
- placeholder CLI commands for end-to-end workflow orchestration

Model training logic remains intentionally minimal in this round.

## Repository layout

- `configs/`: versioned configuration templates for data, vocab, models, and training/eval stages
- `data/`: inventory and ontology mapping artifacts
- `docs/`: PRD-derived project documentation
- `src/fish_langcell/`: importable Python package modules
- `scripts/`: helper scripts (future)
- `benchmarks/`: benchmark assets and reports (future)
- `outputs/`: generated outputs and exports

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
fish-langcell --help
```

## CLI commands (scaffold)

- `ingest-dataset`
- `harmonize-labels`
- `build-vocab`
- `build-sequences`
- `train-cell-encoder`
- `train-multimodal`
- `tune-testis`
- `run-benchmark`
- `export-model`

Each command validates key inputs, prints status, and leaves clear TODO markers for future implementation.
