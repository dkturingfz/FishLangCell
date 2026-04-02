# Gene Identifier Policy (Draft v0.1)

## Canonical Identifier
- Zebrafish-first core identifier: **Ensembl gene ID**.

## Conversion Rules (Placeholder)
1. Preserve original ID columns in raw metadata.
2. Convert to canonical Ensembl IDs using versioned mapping tables.
3. Keep unresolved IDs flagged for manual curation (no silent drops).

## Duplicate / Paralog Handling
- Teleost duplicated genes **remain separate tokens**.
- Orthogroup labels are auxiliary metadata only.
- No token-space merge by orthogroup.

## Unsupported or Mixed ID Inputs
- Mark as `mixed` in inventory until resolved.
- Record conversion workflow and failure rates in preprocessing logs.

## TODO
- Finalize authoritative mapping source(s).
- Define conflict precedence when multiple mappings disagree.
