# Fish-LangCell

Fish-LangCell is a **fish-native** multimodal single-cell annotation framework inspired by LangCell, with a zebrafish-first strategy and a later testis specialization phase.

## Current status (artifact preparation round)

This round prepares schema-complete training-input artifacts only:
- frozen dataset manifests
- fish gene vocabulary templates and ID policy
- text corpus starter JSONL files
- tokenization and sequence-building specs
- train/eval configuration templates
- lightweight artifact validators

No training, large preprocessing, or checkpoint downloads are performed in this stage.

## Repository layout

- `manifests/`: frozen split manifests derived from governance inventory.
- `data/`: governance (`data_inventory`, ontology), vocabulary TSVs, and text corpus JSONL artifacts.
- `configs/tokenization/`: sequence-builder template configs.
- `configs/train/`: pretrain/alignment/tuning/eval templates.
- `docs/`: governance, vocabulary, tokenization, and planning documentation.
- `src/fish_langcell/`: Python package and CLI commands.

## Artifact categories

### 1) Governance artifacts
- `data/data_inventory.tsv`
- `docs/dataset_decisions.md`
- `data/ontology/ontology_mapping.tsv`

### 2) Vocabulary artifacts
- `data/vocab/fish_gene_vocab_v0.1.tsv`
- `data/vocab/zebrafish_gene_reference.tsv`
- `data/vocab/gene_symbol_to_ensembl.tsv`
- `data/vocab/orthogroup_reference.tsv`
- `configs/vocab/id_policy.yaml`
- `docs/gene_vocab_spec.md`

### 3) Text corpus artifacts
- `data/text_corpus/fish_celltype_definitions.jsonl`
- `data/text_corpus/testis_celltype_definitions.jsonl`
- `data/text_corpus/marker_sentences.jsonl`
- `data/text_corpus/hierarchy_descriptions.jsonl`

### 4) Tokenization specs
- `configs/tokenization/zebrafish_sequence_builder.yaml`
- `docs/tokenization_spec.md`

### 5) Train/eval config templates
- `configs/train/pretrain_cell.yaml`
- `configs/train/align_multimodal.yaml`
- `configs/train/tune_testis.yaml`
- `configs/train/eval.yaml`

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

Validation commands:
- `validate-inventory`
- `validate-ontology`
- `validate-manifests`
- `validate-vocab`
- `validate-text-corpus`
- `validate-tokenization-config`

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
fish-langcell --help
```

## Typical validation checks

```bash
fish-langcell validate-inventory --inventory data/data_inventory.tsv
fish-langcell validate-manifests
fish-langcell validate-vocab
fish-langcell validate-text-corpus
fish-langcell validate-tokenization-config
```
