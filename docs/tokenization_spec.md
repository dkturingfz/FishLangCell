# Tokenization and Sequence-Building Specification (Template v0.1)

This document defines non-compute requirements for future zebrafish sequence building.

## Expected input matrix format

- Preferred format: AnnData `.h5ad` with raw counts available.
- Alternative format (future): Matrix Market bundles.
- Matrix requirements:
  - cells on observation axis (`obs`)
  - genes/features on variable axis (`var`)
  - explicit `count_layer` for raw counts

## Required metadata fields

Each cell record should provide at minimum:
- `cell_id`
- `dataset_id`
- `species`
- `tissue`
- `developmental_stage`
- `sex`
- `split`

Missing required metadata should block sequence export for that dataset split.

## Supported gene ID types

Sequence builders must accept these input ID types:
- `Ensembl`
- `Ensembl_or_symbol`
- `SymbolOnly` (requires mapping via `gene_symbol_to_ensembl.tsv`)

All IDs should be normalized to canonical gene IDs from `fish_gene_vocab_v0.1.tsv`.

## Output naming conventions

- Sequence file pattern: `{dataset_id}__{split}__rankseq_v{version}.parquet`
- Metadata file pattern: `{dataset_id}__{split}__rankmeta_v{version}.json`
- Output root: `data/sequences/zebrafish_v0_1/`

Naming should preserve split boundaries and dataset provenance to reduce leakage risk.

## Rank-based sequence parameters (placeholders)

The following fields are reserved and intentionally not executed in this round:
- rank method
- max genes per cell
- count thresholds
- tie-break strategy
- special token policy

These placeholders are defined in `configs/tokenization/zebrafish_sequence_builder.yaml` for future implementation.
