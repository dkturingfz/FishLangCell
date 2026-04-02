# Gene ID Policy (Scaffold v0.1)

## Purpose
Set conservative rules for recording gene identifiers before compute pipelines are run.

## Current canonical policy
- v0.1 is zebrafish-first.
- Canonical target ID type for downstream processing is Ensembl gene ID.
- Source ID type must always be recorded in manifest/inventory fields (`gene_id_type`).

## Allowed input states for scaffold curation
- `Ensembl`
- `symbol`
- `Ensembl_or_symbol`
- `species_specific_or_mixed`

## Manual now vs compute later
- **Manual now**: accurately mark observed ID type and unresolved ambiguity.
- **Compute later**: perform explicit ID mapping audits and produce mapped/unmapped reports.

## Guardrails
- Never silently coerce unknown IDs.
- Keep unresolved cases visible (`unknown`, `pending_curation`).
