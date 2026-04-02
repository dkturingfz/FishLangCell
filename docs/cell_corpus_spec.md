# Cell Corpus Specification (Scaffold v0.1)

## Purpose
Defines non-compute schema expectations for dataset/cell/gene metadata before any heavy preprocessing.

## Manifest-level required fields
Required for each row in manifest TSV files:
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

## Cell-level expected metadata (later standardization)
- `cell_id`
- `dataset_id`
- `species`
- `tissue`
- `label_original`
- `label_harmonized`
- `label_hierarchical`

## Gene-level expected metadata (later standardization)
- `gene_id`
- `gene_symbol`
- `gene_id_type`

## What is manual now vs compute later
- **Manual now**: curate dataset registry rows and governance decisions.
- **Compute later**: ingestion, matrix normalization, ID harmonization, and sequence/token generation.

## Out of scope in this scaffold round
- No training
- No heavy preprocessing
- No sequence generation
- No checkpoint downloads
