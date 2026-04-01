# Fish-LangCell

Fish-LangCell is a fish-native multimodal annotation project for single-cell transcriptomics.

## Scope (Phase 1)

- Scaffold a zebrafish-first fish-native LangCell codebase.
- Standardize data inventory, ontology, and configuration layout.
- Provide CLI entrypoints for ingestion, vocab, sequence building, training orchestration, and benchmarking.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
fish-langcell --help
```

## Core principles

- Fish-native cell encoder as the mainline.
- Human ortholog mapping baseline allowed only as a comparison track.
- Reuse biomedical text encoders (BiomedBERT / PubMedBERT) rather than training from scratch.
- Ontology and label governance first, then multimodal alignment.
