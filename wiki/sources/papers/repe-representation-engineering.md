---
summary: RepE paper — top-down representation engineering framework for monitoring and steering LLM behavior via contrastive activation addition
tags: [representation-engineering, steering-vectors, ai-safety, interpretability]
updated: 2026-06-05T21:06:43Z
created: 2026-06-05T21:06:43Z
---

---
created: 2026-06-05
updated: 2026-06-05
type: source
summary: RepE (Zou et al.) — top-down framework for extracting and manipulating population-level representations in DNNs, introducing contrastive activation addition for steering model behavior
tags: [representation-engineering, steering-vectors, ai-safety, interpretability]
sources: https://arxiv.org/abs/2310.01405
status: active
confidence: 0.95
---

# Representation Engineering (RepE)

**Authors:** Andy Zou, Long Phan, Sarah Chen, James Campbell, Phillip Guo, Richard Ren, Alexander Pan, Xuwang Yin, Mantas Mazeika, Ann-Kathrin Dombrowski, Shashwat Goel, Nathaniel Li, Michael J. Byun, Zifan Wang, Alex Mallen, Steven Basart, Sanmi Koyejo, Dawn Song, Matt Fredrikson, J. Zico Kolter, Dan Hendrycks

**Published:** October 2023 (arXiv:2310.01405), updated March 2025

## Summary

RepE introduces a **top-down** approach to AI transparency: instead of tracing circuits neuron-by-neuron (bottom-up mechanistic interpretability), it identifies *population-level representations* — directions in activation space that correspond to high-level cognitive phenomena — and provides methods for both *reading* (monitoring what the model is "thinking") and *controlling* (steering the model toward or away from behaviors) these representations.

The key methodological contribution is **Contrastive Activation Addition (CAA)** , later called Activation Addition (ActAdd):

1. Collect contrastive prompt pairs (e.g., "honest response" vs "dishonest response")
2. Run both through the model, cache activations at target layers
3. Compute the steering vector: `v = mean(activations_positive) - mean(activations_negative)`
4. At inference, add `α * v` to activations at the target layer

RepE demonstrates this on honesty, harmlessness, power-seeking, situational awareness, and other safety-relevant properties.

## Key Claims

- **Population-level representations encode high-level cognitive phenomena**: DNNs encode concepts like honesty and power-seeking as directions in activation space, not distributed across individual neurons
- **Top-down works where bottom-up struggles**: Circuit-level analysis is labor-intensive and hard to scale; RepE provides lightweight, scalable methods
- **Reading is easier than controlling**: The paper shows that representation-level *monitoring* (classifiers on activation directions) achieves high accuracy, while *control* (steering) has tradeoffs with fluency and effectiveness

## Evidence Quality

The paper provides systematic baselines across multiple models, behaviors, and evaluation suites. The CAA method has been validated in subsequent work (STU-PID, SADI, Dynamic Activation Composition). However, the paper's definition of "honesty" and other abstract concepts is operationalized through curated contrastive datasets, which may not capture full concept complexity.

## Wiki Connections

- [[steering-vectors]] — defines the mathematical object that RepE extracts
- [[activation-engineering]] — RepE's CAA is the primary method covered there
- [[mechanistic-interpretability]] — RepE as a top-down alternative to bottom-up MI
- [[ai-safety]] — RepE's motivation is AI transparency and safety
- [[activation-steering]] — the broader paradigm RepE inaugurated
