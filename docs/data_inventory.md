# Data Inventory Guide (Scaffold v0.1)

## Purpose
`data/data_inventory.tsv` is the governance source of truth for candidate datasets considered by Fish-LangCell.

## Required fields
At minimum, each row must include:
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

## How this will be used later
- Build inclusion/exclusion lists for pipeline runs.
- Track provenance, policy compliance, and split governance.
- Feed future automated checks for completeness and consistency.

## Manual curation now vs compute later
- **Manual now**: record candidate datasets and uncertainty with `TBD` / `pending_curation`.
- **Compute later**: generate ingestion manifests and preprocess scheduling outputs.
