# Dataset Decisions Log (Scaffold v0.1)

Tracks manual governance decisions for candidate datasets.

## Decision states
- **included**: candidate can proceed to future preprocessing
- **reserved**: intentionally held out (e.g., eval)
- **deferred**: blocked on missing metadata/provenance
- **excluded**: not used in current scope

## Starter decisions

### zfish_foundation_broad_atlas_candidate_01
- decision: included
- split/use: foundation / foundation_pretrain
- reason: broad zebrafish foundation starter candidate

### zfish_testis_atlas_candidate_01
- decision: included
- split/use: testis / testis_tune
- reason: primary testis specialization starter candidate

### zfish_eval_holdout_testis_candidate_01
- decision: reserved
- split/use: eval / holdout_eval
- reason: holdout evaluation boundary

## Manual now vs compute later
- **Manual now**: keep decision rationale aligned with inventory/manifests.
- **Compute later**: enforce these decisions in dataset filtering and split construction.
