# Cell Corpus Specification (Frozen v0.1)

This specification freezes schema requirements for future standardized cell-corpus inputs, without running compute pipelines.

## Scope

This document defines:
1. dataset-level governance requirements
2. cell-level standardized metadata requirements
3. gene-level standardized metadata requirements
4. count-matrix policy for future tokenization

## Dataset-level requirements (manifest-aligned)

All training-eligible datasets must be traceable in manifests and include at minimum:
- `dataset_id`
- `species`
- `tissue`
- `assay`
- `source`
- `gene_id_type`
- `label_original`
- `label_harmonized`
- `split`
- `recommended_use`
- `source_url`
- `paper_id`

Primary manifest files:
- `manifests/foundation_datasets.tsv`
- `manifests/testis_datasets.tsv`
- `manifests/eval_datasets.tsv`

## Cell-level standard input requirements

Before future tokenization, each standardized cell record must provide:
- `cell_id`
- `dataset_id`
- `species`
- `tissue`
- `label_original`
- `label_harmonized`
- `label_hierarchical`
- `donor_id` (if available)
- `batch_id` (if available)

## Gene-level standard input requirements

Before future tokenization, each standardized gene record must provide:
- `gene_id`
- `gene_symbol`
- `gene_id_type`

## Frozen count-matrix policy

- Raw counts are preferred and are canonical future tokenization inputs.
- Normalized matrices may be retained as supplementary artifacts.
- Normalized matrices must not silently replace raw counts when raw counts exist.
- If only normalized matrices exist, that condition must be explicitly documented in manifests or dataset decisions.

## Linkage to other artifacts

- **Manifests**: dataset governance and split boundaries.
- **Ontology mappings**: `label_harmonized` and `label_hierarchical` consistency via `data/ontology/ontology_mapping.tsv`.
- **Vocab assets**: gene IDs must be compatible with `configs/vocab/id_policy.yaml` and `data/vocab/fish_gene_vocab_v0.1.tsv`.
- **Tokenization spec**: downstream structural requirements are defined in `docs/tokenization_spec.md` and `configs/tokenization/zebrafish_sequence_builder.yaml`.

## Out of scope for this stage

No training, no large-scale preprocessing, and no sequence generation are performed in this round.
