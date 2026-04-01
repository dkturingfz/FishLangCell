# Training Plan (Phase-based)

## Phase 0: Data audit
- Build `foundation_pool`, `testis_pool`, `eval_pool`.
- Run QC reports for cells/genes/label coverage.

## Phase 1: Vocab + tokenization
- Freeze gene ID conversion policy.
- Build fish-native vocab + orthogroup metadata.
- Target: >=95% tokenization success on foundation cells.

## Phase 2: Cell encoder pretraining
- Train small/base fish-Geneformer variants.
- Validate broad lineage separability and neighborhood purity.

## Phase 3: Multimodal alignment
- Build fish cell-text pairs.
- Train fish-langcell-base using contrastive + matching losses.

## Phase 4: Testis domain tuning
- Continued pretraining on testis pool.
- Hard negatives for adjacent spermatogenesis stages.

## Phase 5: Benchmark + release
- Benchmarks: broad_fish, testis_coarse, testis_fine.
- Package model cards, reports, and inference utilities.
