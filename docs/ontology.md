# Ontology Plan (v0.1)

## Broad Fish Ontology
Initial top-level categories for foundation annotation:
- germ cell
- epithelial cell
- stromal cell
- endothelial cell
- immune cell
- neural cell
- blood cell
- muscle-like cell

## Testis Ontology
Hierarchy for testis specialization:
- testis cell
  - germ cell
    - spermatogonia (undifferentiated, differentiating)
    - spermatocyte (preleptotene, leptotene, zygotene, pachytene, diplotene, late meiotic)
    - spermatid (early, intermediate, late)
  - somatic cell
    - Sertoli
    - Leydig
    - macrophage
    - endothelial
    - myoid / vascular smooth muscle-like
    - stromal

## Label Preservation Policy
Every cell must preserve:
- `label_original`
- `label_harmonized`
- `label_hierarchical`

## Versioning
- Ontology resources are versioned artifacts.
- Mapping changes should be tracked in change logs and benchmark freeze points.
