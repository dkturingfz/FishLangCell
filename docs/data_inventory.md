# Data Inventory Guide (Scaffold v0.1)

## Purpose
`data/data_inventory.tsv` is the source-of-truth registry for candidate datasets and governance status.

## What each row represents
One candidate dataset with enough metadata to track provenance, split assignment, and readiness.

## Minimum required fields
- `dataset_id`
- `species`
- `tissue`
- `assay`
- `gene_id_type`
- `split`
- `recommended_use`
- `source_url`
- `accession_or_link`
- `paper_id`
- `license_or_usage`
- `download_status`

## Manual now vs compute later
- **Manual now**: fill provenance fields, assign split/use, and document uncertainty as `TBD`/`pending_curation`.
- **Compute later**: auto-generate inclusion lists and preprocessing plans from curated rows.

## Companion files
- `docs/dataset_decisions.md`
- `manifests/foundation_datasets.tsv`
- `manifests/testis_datasets.tsv`
- `manifests/eval_datasets.tsv`
