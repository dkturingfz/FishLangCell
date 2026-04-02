# Data Inventory Standard

## Goal
Track source provenance, biological metadata, technical metadata, annotation state, and project split assignment for all candidate datasets.

## Required Minimum Metadata
- `dataset_id`
- `species`
- `tissue`
- `stage`
- `sex`
- `assay`
- `source`
- `paper_id`
- `donor_id`
- `gene_id_type`
- `label_original`
- `label_harmonized`
- `split`

## Split Definitions
- `foundation`: broad representation pretraining pool.
- `testis`: testis domain tuning pool.
- `eval`: strict holdout evaluation pool.
- `undecided`: candidate pending audit.

## Provenance Policy
Each dataset should preserve source URL/accession, citation metadata, assay/platform, ID system, preprocessing notes, and inclusion decision rationale.

## Companion Artifacts
- `data/data_inventory.tsv`
- `data/ontology/ontology_mapping.tsv`
- `docs/gene_id_policy.md`
- `docs/dataset_decisions.md`
