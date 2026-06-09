---
summary: "Evaluation Cards: standardized interpretive layer for AI evaluation reporting across 5,816 models and 101,955 results"
tags: [arxiv, paper, ai-evaluation, reproducibility, benchmarking, model-cards, evaluation]
updated: 2026-06-09T08:45:50Z
created: 2026-06-09T08:45:50Z
---

# Evaluation Cards: An Interpretive Layer for AI Evaluation Reporting

> **EVALUATION CARDS** — Ghosh, Reuel, Chim et al. (48 authors from Stanford, MLCommons, HuggingFace, EleutherAI, and 30+ organizations), June 2026. arXiv: 2606.09809

## Problem

AI evaluation results are produced at massive scale but reported inconsistently across leaderboards, model cards, benchmark papers, and company blogs. The cost is interpretive: readers cannot reliably compare results across sources, identify what a report omits, or trace an aggregate claim to its underlying evidence. Existing efforts address isolated components but leave three gaps:

1. **Coverage gap**: They cover narrow slices of the evaluation lifecycle and don't compose into a single interpretable record
2. **Audience gap**: They specify static representations that don't differentiate the questions different stakeholders bring to the same evidence
3. **Adoption gap**: They remain proposals on paper, lacking the extraction infrastructure required for adoption at scale

## Method

The paper proposes **EVALUATION CARDS**, an operational reporting layer that composes benchmark metadata, evaluation run data, and model metadata into a unified record. The system has four components:

1. **Reporting schema**: Derived from a structured review of 52 papers and 10 stakeholder interviews, covering fields for reproducibility, documentation completeness, provenance/risk, and score comparability
2. **Interpretive signals** (four computed per result):
   - *Reproducibility* — are minimal reproduction fields present? (code, hyperparameters, hardware, seed)
   - *Documentation completeness* — how well does the benchmark or model document itself?
   - *Provenance and risk* — who conducted the evaluation, on what version of the model, under what conditions?
   - *Score comparability* — can two results on different benchmarks be meaningfully compared?
3. **Reader modes**: Calibrated to research and non-research audiences — researchers see the full technical record; policymakers and practitioners see a distilled risk/reliability summary
4. **Monitoring tool**: Automated infrastructure that scrapes, validates, and indexes evaluation reports from 30+ sources

## Results

Deployed across **5,816 models, 635 benchmarks (62 families + 10 composites), and 101,955 results** from 30 organizations:

- **Finding 1 (Reproducibility)**: 96.5% of (model, benchmark, metric-path) triples lack at least one minimal reproducibility field
- **Finding 2 (Documentation)**: Median per-benchmark completeness against the operationalized schema is **10.7%** across all 635 benchmarks
- **Finding 3 (Multi-source divergence)**: Multi-source reporting is rare, and when it occurs, results frequently diverge across sources for the same (model, benchmark, metric) triple
- **Systematic gaps**: The tool surfaces that most AI evaluation lacks the infrastructure for even basic reproduction, let alone cross-source validation

## Limitations

- The corpus is limited to publicly reported evaluations — internal/closed evaluations are not captured
- The schema and signals are derived from current practice, which may embed existing reporting norms rather than ideal ones
- Reader modes are prototypes; real-world user studies on their interpretability are not yet conducted
- Automated extraction may miss nuanced reporting patterns or produce false negatives on completeness

## Connections

- Related to [[model-cards|Model Cards]] (Mitchell et al., 2019) and [[data-sheets|Data Sheets for Datasets]] (Gebru et al., 2021) — extends the card paradigm from model/data documentation to evaluation reporting
- Complements [[system-cards|System Cards]] and [[ai-standards|AI standards efforts]] (NIST AI RMF, EU AI Act)
- [[olmes|Olmes/HELM]] standard for LM evaluations addresses similar fragmentation at a smaller scale
- The 96.5% reproducibility gap echoes findings from the broader reproducibility crisis in ML (Pineau et al., 2021)

## Key Quote

> "AI evaluation results are produced at scale but reported inconsistently across leaderboards, model cards, benchmark papers, and company blogs. The cost is interpretive: readers cannot reliably compare results across sources, identify what a report omits, or trace an aggregate claim to its underlying evidence."

## Links

- arXiv: [2606.09809](https://arxiv.org/abs/2606.09809)
