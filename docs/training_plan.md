# Training and Delivery Plan

## Phase 0 — Data Audit & Harmonization
Deliverables:
- foundation/testis/eval pool assignments
- data inventory table
- ontology draft v0.1

## Phase 1 — Vocabulary & Tokenization
Deliverables:
- fish-native vocabulary table
- orthogroup mapping table
- tokenization pipeline

## Phase 2 — Cell Encoder Pretraining
Deliverables:
- `fish-geneformer-small`
- `fish-geneformer-base`

## Phase 3 — Multimodal Base Alignment
Deliverables:
- fish text corpus
- fish cell-text pair dataset
- `fish-langcell-base`

## Phase 4 — Testis Tuning
Deliverables:
- `fish-langcell-testis`
- hard-negative training strategy for adjacent germ stages

## Phase 5 — Benchmark & Release
Deliverables:
- broad/testis benchmark reports
- model card
- release bundle

## Acceptance Highlights
- Reproducible checkpoints and scripts.
- Frozen benchmark definitions before v1 release.
- Complete provenance metadata.
