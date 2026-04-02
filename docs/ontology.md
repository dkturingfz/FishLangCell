# Ontology Plan (v1 Governance Baseline)

## Purpose
`data/ontology/ontology_mapping.tsv` maps dataset-specific labels into a practical harmonized hierarchy for fish-centric training and evaluation.

## Editing policy
Primary editors are ontology curators and domain scientists. Preprocessing engineers may add provisional mappings but should flag them with lower confidence for curator review.

## Required label layers
Each mapping row preserves:
- `original_label` (as observed in source dataset)
- `harmonized_label` (project-standard flat label)
- `hierarchical_label` (training-oriented hierarchy path)

This distinction is mandatory for reproducibility and reversible label audits.

## Required mapping columns
Validation enforces the following columns:
- `original_label`
- `harmonized_label`
- `hierarchical_label`
- `ontology_namespace`
- `ontology_version`
- `mapping_confidence`
- `source_dataset`
- `notes`

## Practical v1 ontology scope
- Broad fish categories for foundation tasks.
- Testis somatic classes.
- Germline hierarchy and spermatogenesis stage labels.
- Dataset-specific synonym/abbreviation mapping examples.

## How this feeds preprocessing/training
- Harmonization transforms source labels into standardized training targets.
- Hierarchy paths support coarse-to-fine task definitions.
- Confidence flags (`curated`, `provisional`, `review_needed`) guide whether mappings can be auto-applied.

## Validation command
```bash
fish-langcell validate-ontology --mapping data/ontology/ontology_mapping.tsv
```
