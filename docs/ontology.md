# Ontology Mapping Guide (Scaffold v0.1)

## Purpose
`data/ontology/ontology_mapping.tsv` is the editable mapping table used to normalize dataset labels into Fish-LangCell training/eval labels.

## Required columns
The scaffold mapping table uses five required columns:
- `original_label`
- `harmonized_label`
- `hierarchical_label`
- `ontology_namespace`
- `notes`

## How it is used later
- **Manual curation now**: add and refine mappings row-by-row as datasets are reviewed.
- **Compute work later**: preprocessing will apply these mappings to convert source annotations into harmonized labels.

## Curation rules for this stage
- Keep labels conservative and broad where uncertain.
- Use `notes` to mark uncertainty (for example: `pending_curation`).
- Do not remove old source labels; add new rows for aliases/synonyms.

## Linkage
- Text corpus JSONL files should use `label_harmonized` and `label_hierarchical` values present in this mapping table.
- Dataset manifests should keep `label_original`/`label_harmonized` compatible with this mapping table.
