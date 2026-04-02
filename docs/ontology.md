# Ontology Mapping Guide (Scaffold v0.1)

## Purpose
Define how source labels map to harmonized and hierarchical labels in `data/ontology/ontology_mapping.tsv`.

## Required fields
- `original_label`
- `harmonized_label`
- `hierarchical_label`
- `ontology_namespace`
- `notes`

## How this will be used later
- Normalize heterogeneous dataset labels into a shared project label space.
- Keep text corpus labels and cell corpus labels aligned.
- Provide a stable target for later preprocessing validation.

## Manual curation now vs compute later
- **Manual now**: add conservative mappings, preserve ambiguity in `notes`, avoid speculative granularity.
- **Compute later**: apply mappings programmatically during metadata harmonization.

## Curation guidance
- Prefer broad, defensible labels when uncertain.
- Add alias/source labels as new rows instead of replacing existing mappings.
- Mark unresolved cases as `pending_curation`.
