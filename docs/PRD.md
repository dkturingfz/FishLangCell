# Fish-LangCell Product Requirements (v0.1)

## Purpose
Fish-LangCell aims to deliver a **fish-native multimodal single-cell annotation system** inspired by LangCell. The core architectural change from prior work is replacing human-centered cell encoder initialization with a fish-native encoder and fish-native gene vocabulary.

## v1 Scope
- Zebrafish-first foundational training.
- Fish testis and spermatogenesis specialization.
- Zero-shot text-guided annotation, few-shot adaptation, and reference mapping.

## Primary Objectives
1. Train fish-native cell encoder from fish scRNA-seq.
2. Build fish ontology and fish cell-text corpus.
3. Train multimodal fish LangCell base model.
4. Fine-tune for testis domain and spermatogenesis stages.
5. Release broad/testis benchmark suite.

## Non-goals (v1)
- Spatial transcriptomics training.
- Direct multi-omic integration (ATAC/proteomics/imaging).
- Full universal fish ontology.
- Production GUI/web portal.

## Users
- Computational fish scRNA-seq researchers.
- Reproductive biology scientists studying spermatogenesis.
- Method developers building multimodal foundation models.

## Functional Requirements
System must support ingestion, metadata harmonization, fish-native vocab construction, sequence tokenization, encoder pretraining, multimodal alignment, testis adaptation, and reproducible benchmark evaluation.

## Non-functional Requirements
- Modular, config-driven, versioned system.
- Data and label provenance preservation.
- Reproducible preprocessing/training/eval.
- Expandable to additional teleost species.

## Frozen schema prerequisites (v0.1 non-compute round)

Before model training phases, these assets are required and versioned:
- text corpus spec + starter JSONL files
- cell corpus spec and manifest-aligned governance fields
- gene vocabulary spec + starter TSV package + ID policy
- tokenization dependency spec + sequence-builder template

This round does not run training or sequence generation; it freezes schema and validation contracts only.
