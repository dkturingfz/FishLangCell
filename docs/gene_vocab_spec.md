# Fish Gene Vocabulary Specification (v0.1)

This document defines schema and governance expectations for fish-native gene vocabulary artifacts used by Fish-LangCell sequence/tokenization pipelines.

## Scope and files

- `data/vocab/fish_gene_vocab_v0.1.tsv`
- `data/vocab/zebrafish_gene_reference.tsv`
- `data/vocab/gene_symbol_to_ensembl.tsv`
- `data/vocab/orthogroup_reference.tsv`
- `configs/vocab/id_policy.yaml`

## Required columns

### `fish_gene_vocab_v0.1.tsv`
- `gene_token`: stable token string used by sequence builders.
- `canonical_gene_id`: canonical ID after normalization.
- `species`: species scientific name.
- `gene_symbol`: preferred display symbol.
- `biotype`: gene biotype when known.
- `orthogroup_id`: orthogroup link for cross-species context (optional if unknown).
- `id_source`: source table/release that produced the canonical ID.
- `status`: `curated|placeholder|unresolved|deprecated`.
- `audit_note`: free-text justification for unresolved or placeholder states.

### `zebrafish_gene_reference.tsv`
- `canonical_gene_id`, `gene_symbol`, `species`, `gene_id_type`, `genome_build`, `source_release`, `is_primary_symbol`, `status`, `notes`.

### `gene_symbol_to_ensembl.tsv`
- `species`, `input_symbol`, `canonical_gene_id`, `mapping_status`, `mapping_source`, `source_release`, `confidence`, `review_required`, `notes`.

### `orthogroup_reference.tsv`
- `orthogroup_id`, `reference_species`, `reference_gene_id`, `reference_gene_symbol`, `member_species`, `member_gene_id`, `member_gene_symbol`, `confidence`, `source`, `status`, `notes`.

## Canonical gene ID policy

1. Canonical IDs are Ensembl gene IDs when available.
2. Zebrafish canonical IDs follow `^ENSDARG[0-9]{11}$`.
3. If no canonical Ensembl ID is available, use `UNRESOLVED:<reason>:<symbol_or_local_id>` and set `status=unresolved`.
4. Never silently replace unresolved IDs during preprocessing; resolution must be auditable.

## Accepted alternate ID types

Alternate IDs may include `gene_symbol`, `entrez_gene_id`, `ensembl_transcript_id`, and curated synonyms. All alternates must map through `gene_symbol_to_ensembl.tsv` or carry unresolved status.

## Duplicate and paralog handling

- Exact duplicate canonical IDs are collapsed during vocab curation.
- Species-specific paralogs remain distinct rows/tokens.
- Orthogroup links provide optional alignment metadata and must not force token merges.
- Ambiguous symbol-to-paralog mappings remain unresolved until curator review.

## Orthogroup metadata usage

Orthogroups are metadata for analysis and optional future transfer-learning strategies. They are **not** a replacement for canonical gene IDs in tokenizer inputs.

## Unresolved status fields

Rows with unresolved IDs must include:
- `status=unresolved`
- a non-empty note (`audit_note` or `notes`)
- `review_required=true` where available
- source provenance (`mapping_source` and `source_release`)

## Audit expectations

Each update cycle should record:
- curator identity
- source release/version
- update date (ISO format)
- change reason
- before/after counts (mapped, unresolved, deprecated)

Do not promote placeholder rows to production without a recorded audit entry.
