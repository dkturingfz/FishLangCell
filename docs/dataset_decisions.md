# Dataset Decisions Log (Scaffold v0.1)

## Purpose
Track human governance decisions for dataset inclusion boundaries.

## Decision states
- `included`: allowed for later preprocessing pipeline consideration.
- `reserved`: intentionally held out (typically eval).
- `deferred`: pending metadata or policy clarification.
- `excluded`: out of current scope.

## Starter decisions

### zfish_foundation_candidate_01
- decision: `included`
- split/use: `foundation` / `foundation_pretrain`
- rationale: broad fish starter candidate for foundation curation queue.

### zfish_testis_candidate_01
- decision: `included`
- split/use: `testis` / `testis_tune`
- rationale: starter candidate for testis-focused curation queue.

### zfish_eval_holdout_candidate_01
- decision: `reserved`
- split/use: `eval` / `holdout_eval`
- rationale: preserve independent holdout boundary.

## Manual curation now vs compute later
- **Manual now**: update decisions and rationale as provenance improves.
- **Compute later**: enforce decision states in dataset filtering logic.
