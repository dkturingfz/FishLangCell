# Data Inventory

## Purpose
Track all candidate datasets for foundation, testis domain tuning, and evaluation pools.

## Inventory template

| dataset_id | species | tissue | stage | assay | source | cell_count | gene_id_type | label_original | label_harmonized | split | notes |
|---|---|---|---|---|---|---:|---|---|---|---|---|
| example_zf_atlas_001 | danio_rerio | multi_tissue | larval+adult | scRNA-seq | DOI/URL | 0 | ensembl | yes | partial | foundation | fill in after ingestion |

## Required checks
- Metadata completeness for required fields.
- Label coverage and harmonization status.
- Candidate split assignment (`foundation`, `testis`, `eval`).
