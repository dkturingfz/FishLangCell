# Tokenization Dependency Specification (Frozen v0.1)

This document freezes dependencies and structural requirements for future sequence generation. No sequence generation is performed in this stage.

## Expected matrix orientation

- Canonical orientation: cells as rows, genes as columns.
- If an input uses a different orientation, it must declare and normalize orientation before sequence output.

## Accepted input containers / file types

- AnnData: `.h5ad`
- Matrix Market bundle: `.mtx` + barcode/cell metadata + gene/features metadata
- Loom: `.loom` (accepted as optional legacy input)

## Required cell metadata fields

- `cell_id`
- `dataset_id`
- `species`
- `tissue`
- `label_original`
- `label_harmonized`
- `label_hierarchical`
- `donor_id` (if available)
- `batch_id` (if available)

## Required gene metadata fields

- `gene_id`
- `gene_symbol`
- `gene_id_type`

## Accepted gene ID types

- `ensembl_gene_id`
- `gene_symbol`
- `ensembl_or_symbol_mixed`

Canonicalization behavior must follow `configs/vocab/id_policy.yaml`.

## Dependency linkage

- `configs/vocab/id_policy.yaml`: canonical ID type, accepted input types, unresolved handling, and audit fields.
- `data/vocab/fish_gene_vocab_v0.1.tsv`: primary token space and token IDs.
- `data/vocab/gene_symbol_to_ensembl.tsv`: explicit symbol-to-gene_id mapping support.

## Raw count policy

Raw counts are preferred and treated as canonical future tokenization input. Normalized matrices are supplementary and cannot silently replace raw counts when raw counts exist.

## Future output naming conventions

Future sequence outputs should use a stable pattern:
- sequence: `{dataset_id}__{split}__rankseq_v{version}.parquet`
- metadata: `{dataset_id}__{split}__rankmeta_v{version}.json`

The split token in filenames is required to preserve evaluation boundary clarity.
