# Data Inventory Standard

## Purpose
`data/data_inventory.tsv` is the single editable registry for candidate datasets and their governance status. It is used by curation, preprocessing, and training configuration generation.

## Primary editors
- Data curation owners
- Benchmark/evaluation owners
- Preprocessing maintainers (for QC and provenance completion)

## Required governance behavior
- One row per dataset candidate (`dataset_id` unique).
- Preserve uncertainty explicitly (`TBD`, `unknown`, `pending_*`) rather than guessing.
- Keep split and recommended use aligned with decision log in `docs/dataset_decisions.md`.

## Required/validated fields
Validation enforces required columns and constrained value sets:
- Required metadata columns (with alias support for `stage`, `source`, `donor_id`, `label_original`, `label_harmonized`).
- `split` must be one of: `foundation`, `testis`, `eval`, `undecided`.
- `recommended_use` must be one of: `foundation_pretrain`, `testis_tune`, `holdout_eval`, `defer_review`, `exclude_for_now`.
- Critical provenance fields are checked for missing placeholders: `source_url`, `accession_or_link`, `paper_id`, `license_or_usage`, `download_status`.

## How this feeds preprocessing/training
- Preprocessing should only promote rows that pass schema checks and required provenance thresholds.
- Foundation/testis/eval data pools are generated from `split` + `recommended_use`.
- Holdout evaluation datasets remain out of training by policy.

## Companion artifacts
- `data/data_inventory.tsv`
- `docs/dataset_decisions.md`
- `data/ontology/ontology_mapping.tsv`
- `docs/gene_id_policy.md`

## Validation command
```bash
fish-langcell validate-inventory --inventory data/data_inventory.tsv
```
