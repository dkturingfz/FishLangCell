# Text Corpus Specification (Frozen v0.1)

This document freezes the schema for Fish-LangCell text corpus starter assets used in later multimodal training.

## Scope

Applies to:
- `data/text_corpus/fish_celltype_definitions.jsonl`
- `data/text_corpus/testis_celltype_definitions.jsonl`
- `data/text_corpus/marker_sentences.jsonl`
- `data/text_corpus/hierarchy_descriptions.jsonl`

Format: JSONL (one JSON object per line).

## Frozen common schema

Each record must include these fields:
- `id`
- `species_scope`
- `tissue_scope`
- `ontology_namespace`
- `label_original`
- `label_harmonized`
- `label_hierarchical`
- `text_type`
- `text`
- `markers`
- `source`
- `status`
- `notes`

## Allowed enums

### `text_type`
- `definition`
- `marker_prompt`
- `hierarchy_description`
- `alias`

### `status`
- `draft`
- `reviewed`
- `frozen`
- `deprecated`

## Field expectations

- `id`: unique stable string identifier.
- `species_scope`: one of project-level scopes such as `zebrafish`, `fish`, `teleost`, or `mixed`.
- `tissue_scope`: scope such as `testis`, `gonad`, `multi_tissue`.
- `ontology_namespace`: ontology namespace used by this repository (for this stage: `broad_fish` or `testis`).
- `label_original`: optional dataset/source label prior to harmonization; may be empty.
- `label_harmonized`: canonical harmonized label used across artifacts.
- `label_hierarchical`: hierarchy path aligned to ontology mapping.
- `text`: main text payload for definition/prompt/description.
- `markers`: JSON array of marker symbols or empty array.
- `source`: provenance (`manual_curated`, `ontology_curated`, `imported`, etc.).
- `notes`: optional free text.

## Starter role by file

- `fish_celltype_definitions.jsonl`: broad fish categories.
- `testis_celltype_definitions.jsonl`: testis and spermatogenesis stage definitions.
- `marker_sentences.jsonl`: concise marker-style prompts.
- `hierarchy_descriptions.jsonl`: parent-child and stage hierarchy text entries.

## Consistency linkage

- Harmonized labels and hierarchical labels must remain consistent with `data/ontology/ontology_mapping.tsv`.
- Text-corpus status values must remain synchronized with repository validators.
