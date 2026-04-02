# Fish-LangCell

Fish-LangCell is a **fish-native** multimodal single-cell annotation framework inspired by LangCell, with a zebrafish-first v1 plan and testis specialization track.

## Current status

This repository now includes a first practical **data governance layer**:
- curated dataset inventory scaffold with split/use decisions
- ontology mapping table for harmonized and hierarchical labels
- gene identifier policy focused on fish-native constraints
- validation CLI commands for governance artifacts

Model training remains intentionally minimal in this round.

## Repository layout

- `configs/`: versioned configuration templates for data, vocab, models, and training/eval stages
- `data/`: inventory and ontology mapping artifacts
- `docs/`: PRD-derived project documentation and governance policies
- `src/fish_langcell/`: importable Python package modules and CLI
- `scripts/`: helper scripts (future)
- `benchmarks/`: benchmark assets and reports (future)
- `outputs/`: generated outputs and exports

## Governance artifacts

- `data/data_inventory.tsv`: candidate datasets, provenance fields, split, and intended use
- `data/ontology/ontology_mapping.tsv`: original-to-harmonized label mappings plus hierarchical paths
- `docs/gene_id_policy.md`: canonical ID and teleost paralog handling policy
- `docs/dataset_decisions.md`: include/defer/exclude decision log

These artifacts are human-editable and machine-validated before preprocessing/training promotion.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
fish-langcell --help
```

## CLI commands

Workflow scaffold commands:
- `ingest-dataset`
- `harmonize-labels`
- `build-vocab`
- `build-sequences`
- `train-cell-encoder`
- `train-multimodal`
- `tune-testis`
- `run-benchmark`
- `export-model`

Governance validation commands:
- `validate-inventory`
- `validate-ontology`

### Typical governance checks

```bash
fish-langcell validate-inventory --inventory data/data_inventory.tsv
fish-langcell validate-ontology --mapping data/ontology/ontology_mapping.tsv
```
