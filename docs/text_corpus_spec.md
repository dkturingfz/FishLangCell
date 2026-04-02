# Text Corpus Specification (Scaffold v0.1)

## Purpose
Define the editable JSONL schema for Fish-LangCell text corpus curation before any compute pipeline runs.

## Files in scope
- `data/text_corpus/fish_celltype_definitions.jsonl`
- `data/text_corpus/testis_celltype_definitions.jsonl`
- `data/text_corpus/marker_sentences.jsonl`
- `data/text_corpus/hierarchy_descriptions.jsonl`

## Required fields (all JSONL records)
- `id`
- `species_scope`
- `tissue_scope`
- `ontology_namespace`
- `label_original`
- `label_harmonized`
- `label_hierarchical`
- `text_type`
- `text`
- `markers` (JSON array)
- `source`
- `status`
- `notes`

## Allowed starter values
- `text_type`: `definition`, `marker_prompt`, `hierarchy_description`, `alias`
- `status`: `draft`, `reviewed`, `frozen`, `deprecated`

## How this will be used later
- Generate curation reports and review queues.
- Provide aligned text artifacts for later prompt templates and weak supervision experiments.
- Support traceable linkage from text entries to ontology mappings.

## Manual curation now vs compute later
- **Manual now**: create conservative, human-editable records and keep label fields synchronized with ontology mapping.
- **Compute later**: schema validation, dataset-linked text retrieval, and downstream text/cell alignment features.
