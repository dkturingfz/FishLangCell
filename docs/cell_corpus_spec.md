# Cell Corpus Specification (Scaffold v0.1)

## Purpose
Define minimal metadata schemas for curating cell corpus sources before ingestion, normalization, or model training.

## Required dataset-manifest fields (TSV rows)
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

## Expected cell-level fields (future standardized metadata)
- `cell_id`
- `dataset_id`
- `species`
- `tissue`
- `label_original`
- `label_harmonized`
- `label_hierarchical`

## Expected gene-level fields (future standardized metadata)
- `gene_id`
- `gene_symbol`
- `gene_id_type`

## How this will be used later
- Drive ingestion plans from curated manifests.
- Enforce split boundaries for foundation/testis/eval stages.
- Feed future validation scripts for ID policy and ontology consistency.

## Manual curation now vs compute later
- **Manual now**: add conservative dataset metadata and split intent.
- **Compute later**: data loading, normalization, harmonization, tokenization, and sequence construction.

## Explicitly out of scope in scaffold round
- Training
- Heavy preprocessing
- Sequence generation
- Checkpoint download
