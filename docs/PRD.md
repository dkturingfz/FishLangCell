# Fish-LangCell PRD (Draft)

## 1. Vision
Build a fish-native LangCell system for fish single-cell transcriptomics annotation.

## 2. Product Goals
- Broad fish cell-type representation.
- Testis/spermatogenesis specialized annotation.
- Text-cell joint embedding for zero-shot and few-shot usage.

## 3. Non-Goals (Phase 1)
- Spatial multi-omics joint training.
- scATAC direct co-encoder.
- Proteomics/CITE-seq joint training.

## 4. Deliverables
- `fish-geneformer-small`
- `fish-geneformer-base`
- `fish-langcell-base`
- `fish-langcell-testis`

## 5. Interfaces
- zero-shot annotation
- few-shot fine-tune
- reference mapping
- embedding export
