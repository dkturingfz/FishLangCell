# Text Corpus Specification (Scaffold v0.1)

## Purpose
Defines the lightweight JSONL schema for starter text artifacts used by Fish-LangCell.

## Files in scope
- `data/text_corpus/fish_celltype_definitions.jsonl`
- `data/text_corpus/testis_celltype_definitions.jsonl`
- `data/text_corpus/marker_sentences.jsonl`
- `data/text_corpus/hierarchy_descriptions.jsonl`

## Frozen common schema (all JSONL records)
Required fields:
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

## `text_type` values
- `definition`
- `marker_prompt`
- `hierarchy_description`
- `alias`

## `status` values
- `draft`
- `reviewed`
- `frozen`
- `deprecated`

## What is manual now vs compute later
- **Manual now**: write short, conservative definitions/prompts and align labels to ontology mapping.
- **Compute later**: use these records for prompt templates, weak supervision, and eval documentation generation.

## Editing guidance
- Keep entries short and curator-editable.
- Prefer broad placeholders over speculative biological detail.
- Keep harmonized/hierarchical labels synchronized with `data/ontology/ontology_mapping.tsv`.
