# Release Checklist (Scaffold v0.1)

## Purpose
Define minimum governance and schema checks required before releasing scaffold or curated artifacts.

## Governance checks
- [ ] `data/data_inventory.tsv` rows reviewed for provenance and policy fields.
- [ ] `docs/dataset_decisions.md` consistent with split assignments in manifests.
- [ ] `data/ontology/ontology_mapping.tsv` reviewed for active label coverage.
- [ ] `docs/gene_id_policy.md` version and assumptions documented.

## Schema checks
- [ ] Text corpus JSONL records include all required fields.
- [ ] Manifest TSVs include required headers and conservative row values.
- [ ] Placeholder values are clearly marked (`TBD`, `pending_curation`, or notes).

## Compute boundary checks
- [ ] No training run in this phase.
- [ ] No heavy preprocessing run in this phase.
- [ ] No sequence generation run in this phase.
- [ ] No checkpoint downloads performed in this phase.
