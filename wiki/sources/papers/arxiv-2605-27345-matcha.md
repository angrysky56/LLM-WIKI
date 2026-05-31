---
created: 2026-05-31
updated: 2026-05-31
type: source
summary: "MATCHA: A semantic similarity metric using contrastive alignment with adversarial counterfactuals, outperforming ROUGE/BERTScore by up to 20% on TruthfulQA"
tags: [paper, arxiv, nlp, evaluation-metrics, llm]
---

# MATCHA: Matching Text via Contrastive Semantic Alignment

**Paper:** [arXiv:2605.27345](https://arxiv.org/abs/2605.27345)
**Authors:** Siran Li, Ece Sena Etoglu, Carsten Eickhoff, Seyed Ali Bahrainian (University of Tübingen)

## Overview

MATCHA is an automatic evaluation metric for LLM-generated text that jointly rewards semantic agreement with a reference and penalizes contradictions. It uses a dual-view approach:
1. **Proximity** to the gold/reference text
2. **Distance** from adversarially generated counterfactual contradictions

## Key Problem

Existing metrics (ROUGE, BERTScore) assign nearly identical scores to texts that directly contradict each other, masking fundamental errors in generation.

## Method

- Employs a dual-view perspective measuring proximity to gold text AND distance from adversarial counterfactuals
- Generates counterfactual contradictions to test whether metrics can distinguish correct from incorrect statements
- Compared against 23 embedding models

## Results

- Outperforms popular metrics on 8 public benchmarks (QA, image captioning, NLI, summarization, STS)
- On TruthfulQA: **+18.38% over ROUGE-L**, **+20.82% over BERTScore**
- Most accurate among 23 embedding models tested

## Tags
- evaluation-metrics
- semantic-similarity
- contrastive-learning
- llm-generation