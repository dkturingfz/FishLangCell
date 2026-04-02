# Dataset Decisions Log

This log captures governance decisions for dataset promotion into Fish-LangCell pools. Keep this synchronized with `data/data_inventory.tsv`.

## Decision states
- **Included**: eligible for next preprocessing stage.
- **Reserved**: intentionally held out from training.
- **Deferred**: candidate retained but blocked on missing metadata/QC/provenance.
- **Excluded**: not used in current scope.

---

## Included in foundation candidates

### `zfish_foundation_broad_atlas_candidate_01`
- **Decision**: included
- **Date**: 2026-04-02
- **Split / use**: `foundation` / `foundation_pretrain`
- **Rationale**:
  - Aligns with zebrafish-first broad representation requirement.
  - Expected to provide diverse cell states for cell encoder pretraining.
- **Metadata needed before ingestion execution**:
  - concrete accession/link,
  - license terms,
  - confirmed gene ID type and genome build,
  - raw counts availability verification.

### `zfish_foundation_developmental_atlas_candidate_01`
- **Decision**: included
- **Date**: 2026-04-02
- **Split / use**: `foundation` / `foundation_pretrain`
- **Rationale**:
  - Adds developmental context diversity needed by PRD scope.
- **Metadata needed before ingestion execution**:
  - explicit developmental coverage,
  - assay/platform details,
  - provenance accession and citation IDs.

## Included in testis candidates

### `zfish_testis_atlas_candidate_01`
- **Decision**: included
- **Date**: 2026-04-02
- **Split / use**: `testis` / `testis_tune`
- **Rationale**:
  - Core testis specialization dataset class.
  - Supports germline/somatic ontology anchoring.
- **Metadata needed before ingestion execution**:
  - accession/link,
  - confirmed stage labels,
  - donor/batch metadata completeness.

### `zfish_testis_qian2022`
- **Decision**: included (provisional)
- **Date**: 2026-04-02
- **Split / use**: `testis` / `testis_tune`
- **Rationale**:
  - Existing scaffold candidate with explicit testis relevance.
- **Metadata needed before promotion beyond provisional**:
  - paper identifier normalization,
  - accession URL,
  - gene ID conversion audit,
  - QC status update from `pending`.

## Reserved for evaluation

### `zfish_eval_holdout_testis_candidate_01`
- **Decision**: reserved
- **Date**: 2026-04-02
- **Split / use**: `eval` / `holdout_eval`
- **Rationale**:
  - Maintains strict holdout set to avoid leakage into training/tuning.
- **Metadata needed before benchmark freeze**:
  - accession and license,
  - annotation depth and quality confirmation,
  - overlap/leakage check against training datasets.

## Deferred pending metadata

### `zfish_testis_aging_spermatogenesis_candidate_01`
- **Decision**: deferred
- **Date**: 2026-04-02
- **Split / use**: `testis` / `testis_tune`
- **Rationale**:
  - High biological relevance for stage-resolved spermatogenesis.
  - Deferred due to unresolved provenance and uncertainty around age/condition annotations.
- **Required to promote**:
  - validated accession/provenance,
  - clear age bins and condition labels,
  - review for compatibility with ontology stage granularity.

### `teleost_future_expansion_candidate_01`
- **Decision**: deferred
- **Date**: 2026-04-02
- **Split / use**: `undecided` / `defer_review`
- **Rationale**:
  - Intentionally retained for post-v1 multi-species expansion.
- **Required to promote**:
  - species assignment,
  - canonical gene ID policy mapping path,
  - cross-species governance review.

## Excluded for now
- No dataset is hard-excluded in this round.
- Add rows here when a candidate is rejected for licensing, irreproducibility, incompatible modality, or severe annotation/provenance issues.
