# Gene Vocabulary Specification (Frozen v0.1)

This document freezes schema and policy for vocabulary starter assets used by future Fish-LangCell tokenization.

## Scope

Applies to:
- `data/vocab/fish_gene_vocab_v0.1.tsv`
- `data/vocab/zebrafish_gene_reference.tsv`
- `data/vocab/gene_symbol_to_ensembl.tsv`
- `data/vocab/orthogroup_reference.tsv`
- `configs/vocab/id_policy.yaml`

## Frozen schemas

### `fish_gene_vocab_v0.1.tsv` required columns
- `token_id`
- `species`
- `gene_id`
- `gene_symbol`
- `gene_biotype`
- `is_protein_coding`
- `orthogroup_id`
- `human_ortholog`
- `is_testis_marker`
- `is_germline_marker`
- `is_somatic_marker`
- `status`
- `source`
- `notes`

Allowed `status` values:
- `active`
- `placeholder`
- `pending_curation`
- `deprecated`
- `excluded`

### `zebrafish_gene_reference.tsv` required columns
- `gene_id`
- `gene_symbol`
- `gene_name`
- `gene_biotype`
- `chromosome`
- `start`
- `end`
- `strand`
- `genome_build`
- `source`
- `notes`

### `gene_symbol_to_ensembl.tsv` required columns
- `gene_symbol`
- `gene_id`
- `mapping_status`
- `mapping_source`
- `ambiguity_flag`
- `notes`

### `orthogroup_reference.tsv` required columns
- `orthogroup_id`
- `species`
- `gene_id`
- `gene_symbol`
- `ortholog_group_label`
- `human_ortholog`
- `evidence_source`
- `notes`

## Frozen policy constraints

- Species-appropriate Ensembl-style gene IDs are canonical when possible.
- Teleost paralogs must remain separate by default.
- Orthogroup metadata is auxiliary and must not collapse primary token space.
- Unresolved mappings must be explicitly recorded (never silently dropped).

## Status and placeholder handling

Starter files may include `placeholder` and `pending_curation` rows to freeze schema shape. These rows are structural scaffolding and require future curator replacement.
