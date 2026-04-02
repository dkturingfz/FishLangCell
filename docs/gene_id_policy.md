# Gene ID Policy (Scaffold v0.1)

## Purpose
Define conservative rules for recording gene identifier types before any mapping or transformation work.

## Required fields to populate in inventory/manifests
- `gene_id_type`
- `species`
- `dataset_id`

## Current starter policy
- Zebrafish-first scaffold.
- Target canonical downstream ID family: Ensembl gene IDs.
- Do not assume IDs are already canonical unless explicitly verified.

## Allowed scaffold values for `gene_id_type`
- `Ensembl`
- `symbol`
- `Ensembl_or_symbol`
- `species_specific_or_mixed`
- `unknown`

## How this will be used later
- Drive ID harmonization checks and mapping reports.
- Gate dataset readiness before preprocessing.

## Manual curation now vs compute later
- **Manual now**: capture observed ID type conservatively.
- **Compute later**: perform actual mapping, conflict detection, and unmapped-ID reporting.
