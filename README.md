# Fish-LangCell

Fish-LangCell is a fish-native multimodal single-cell annotation framework inspired by LangCell, with a zebrafish-first strategy and a later testis specialization phase.

## Current status (frozen schema preparation round)

This round is **non-compute only** and prepares schema-level training-input artifacts:
- frozen text corpus schema and starter JSONL files
- frozen cell corpus schema specification
- frozen gene vocabulary starter package + ID policy
- tokenization dependency spec + sequence-builder template
- lightweight validators and CLI hooks

Not in scope for this round: training, large-scale preprocessing, sequence generation, checkpoint downloads, or heavy gene mapping.

## Repository layout

- `manifests/`: frozen split manifests derived from governance inventory.
- `data/ontology/`: ontology source and mapping assets.
- `data/text_corpus/`: frozen text corpus starter JSONL assets.
- `data/vocab/`: frozen gene vocabulary starter TSV assets.
- `configs/vocab/`: canonical gene ID policy.
- `configs/tokenization/`: sequence-builder dependency template.
- `docs/`: frozen specifications and planning docs.
- `src/fish_langcell/`: Python package and CLI commands.

## Artifact categories

### 1) Text corpus artifacts (manually curated now)
- `docs/text_corpus_spec.md`
- `docs/text_corpus_review_guidelines.md`
- `data/text_corpus/fish_celltype_definitions.jsonl`
- `data/text_corpus/testis_celltype_definitions.jsonl`
- `data/text_corpus/marker_sentences.jsonl`
- `data/text_corpus/hierarchy_descriptions.jsonl`

### 2) Cell corpus schema artifacts (specification now, compute later)
- `docs/cell_corpus_spec.md`
- dataset governance manifests:
  - `manifests/foundation_datasets.tsv`
  - `manifests/testis_datasets.tsv`
  - `manifests/eval_datasets.tsv`

### 3) Vocabulary artifacts (starter package now)
- `docs/gene_vocab_spec.md`
- `configs/vocab/id_policy.yaml`
- `data/vocab/fish_gene_vocab_v0.1.tsv`
- `data/vocab/zebrafish_gene_reference.tsv`
- `data/vocab/gene_symbol_to_ensembl.tsv`
- `data/vocab/orthogroup_reference.tsv`

### 4) Tokenization dependency artifacts (templates now)
- `docs/tokenization_spec.md`
- `configs/tokenization/zebrafish_sequence_builder.yaml`

## CLI commands

Validation commands for this stage:
- `validate-inventory`
- `validate-ontology`
- `validate-manifests`
- `validate-text-corpus`
- `validate-vocab`
- `validate-tokenization-spec`

Workflow scaffold commands (placeholder-only in this round):
- `ingest-dataset`
- `harmonize-labels`
- `build-vocab`
- `build-sequences`
- `train-cell-encoder`
- `train-multimodal`
- `tune-testis`
- `run-benchmark`
- `export-model`

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
fish-langcell --help
```

## Typical validation checks

```bash
fish-langcell validate-manifests
fish-langcell validate-text-corpus
fish-langcell validate-vocab
fish-langcell validate-tokenization-spec
```

## Prerequisites for future training phases

Before future compute phases begin, the project expects these prerequisites to pass validation:
- text corpus starter files and schema consistency
- manifest governance consistency
- vocab schema and ID policy consistency
- tokenization dependency config presence and key checks
