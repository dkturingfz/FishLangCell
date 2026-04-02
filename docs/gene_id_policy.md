# Gene Identifier Policy (v1 Governance Baseline)

## Scope
This policy governs how Fish-LangCell stores, converts, and audits gene identifiers across inventory, preprocessing, vocabulary construction, and model training. It is zebrafish-first for v1 and designed to expand safely to additional teleost species.

## 1) Canonical identifier for v1
- **Canonical gene ID for v1:** Ensembl stable gene ID as provided by the project-approved zebrafish reference release.
- Inventory rows should record the observed input type in `gene_id_type` (e.g., `Ensembl`, `symbol`, `mixed`, `Ensembl_or_symbol`).
- Canonicalized outputs used by preprocessing/training must carry canonical Ensembl IDs as primary token IDs.

## 2) Accepted alternate input ID types
Accepted upstream ID types for ingestion (before canonicalization):
- Ensembl gene IDs (preferred input)
- Gene symbols
- Mixed Ensembl + symbol datasets
- Species-specific IDs for future teleost expansion (tracked as `species_specific_or_mixed` until mapping is curated)

Any unsupported/unknown type must be explicitly flagged and never silently coerced.

## 3) Conversion strategy
1. Preserve raw identifiers exactly as received in ingestion artifacts.
2. Apply a **versioned mapping table** to derive canonical Ensembl IDs.
3. Emit conversion outcome fields at minimum:
   - `input_gene_id`
   - `canonical_gene_id`
   - `mapping_status` (`mapped`, `unmapped`, `ambiguous`, `retired_id`, `manual_override`)
   - `mapping_reference_version`
4. Never drop unmapped IDs silently; record counts and examples in preprocessing logs.

## 4) Duplicate IDs and teleost paralogs
- **Do not collapse teleost paralogs by default.**
- Fish-native modeling requires preserving duplicated genes as distinct biological tokens unless a task-specific exception is formally approved.
- If duplicate identifiers occur inside a dataset after normalization, resolve with deterministic rules (e.g., aggregate counts by exact canonical ID) and log the rule/version.

## 5) Orthogroup metadata policy
- Orthogroups are allowed as **auxiliary metadata only**.
- Orthogroup labels must not replace canonical gene IDs in training token space.
- Cross-species analyses may reference orthogroups for reporting/transfer diagnostics, but model inputs remain gene-level unless explicitly re-scoped in a future policy version.

## 6) Unsupported or ambiguous IDs
- Unsupported formats, ambiguous mappings, or multi-target symbol mappings are assigned `mapping_status=ambiguous` or `unmapped`.
- These rows remain in audit outputs for curator review.
- Dataset promotion into training pools is blocked if unresolved ID rate exceeds project thresholds (thresholds TBD in preprocessing policy).

## 7) Species expansion policy
- v1 is zebrafish-first; additional teleost species are onboarded only after:
  - approved species reference build,
  - versioned ID mapping table,
  - documented unresolved/ambiguous rate,
  - curator sign-off in `docs/dataset_decisions.md`.
- Species-specific paralog structure must be preserved; no human-centric one-to-one collapse assumptions.

## 8) Audit trail requirements
Each preprocessing run must produce an audit artifact containing:
- dataset_id and processing timestamp,
- mapping resource version(s),
- input ID type distribution,
- mapped/unmapped/ambiguous counts and percentages,
- manual override records with rationale,
- hash or version tag of the conversion code.

## 9) Change management
- Any policy or mapping change that can alter vocabulary membership or token identity requires:
  - a documented change note,
  - reproducible rerun instructions,
  - benchmark impact check before model release.
