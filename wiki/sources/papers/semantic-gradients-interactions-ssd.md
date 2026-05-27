---
updated: 2026-05-27T14:18:03Z
created: 2026-05-27T14:18:03Z
---

---
created: 2026-05-27T14:30:00Z
updated: 2026-05-27T14:30:00Z
type: source
summary: "Interaction SSD extends supervised semantic differential to model how semantic gradients in hate speech detection vary by annotator identity — moderation effect detection"
tags: [paper, arxiv, nlp, hate-speech-detection, semantic-differential, moderation-analysis, annotation-bias, embeddings]
sources: https://arxiv.org/abs/2605.27322
status: active
confidence: high
---

# Semantic Gradients Interactions in SSD: A Case Study in Racial Identity and Hate Speech

**arXiv:** [2605.27322](https://arxiv.org/abs/2605.27322) | **Authors:** Felix Ostrowicki, Hubert Plisiecki | **Published:** 2026-05-26

## Core Contribution

Interaction SSD extends Supervised Semantic Differential (SSD) to model how semantic meaning varies across moderators (groups, traits, conditions), making this variation testable and interpretable.

Standard SSD estimates a single semantic gradient for the full sample. Interaction SSD estimates:
- **Main semantic gradient** — shared semantic direction associated with outcome
- **Interaction gradient** — how the main direction changes as a function of moderator
- **Conditional gradients** — semantic gradients at specific moderator values (e.g., white / people-of-color)

## Case Study

Applied to UC Berkeley Measuring Hate Speech corpus — testing whether annotator racial identity moderates hate-speech judgments of comments targeting people of color.

**Finding**: Significant moderation effect. The shared gradient contrasts dehumanizing hostility with counter-speech. The interaction gradient reveals smaller group-linked differences in which semantic cues predict hate-speech ratings.

## Model

```
yi = α + β⊤x̃i + γmi + δ⊤(x̃imi) + εi
```

Where:
- β = baseline semantic association with outcome
- γ = non-semantic main effect of moderator
- δ = whether semantic association changes with moderator

All coefficient vectors are back-projected from PCA space into original embedding space for interpretability.

## Connections

- [[hate-speech-detection]] — annotation bias, demographic moderation in content moderation
- [[semantic-differential]] — SSD methodology
- [[annotation-bias]] — annotator identity moderating judgments; connects to [[demographic-information]] (2605.27313 from same batch)
- [[moderation-analysis]] — interaction effects in ML
- [[embedding-analysis]] — PCA, SIF-weighting, back-projection interpretation

## Notes

- Content warning: Contains hate speech examples for research purposes
- This paper pairs with 2605.27313 (When Does Demographic Information Help?) — both examine demographic/identity moderation in hate speech detection, from different methodological angles
- Methodological contribution: enables statistically testable moderated meaning-outcome relationships
- Connects to [[annotation-bias]] and [[demographic-parity]] in fairness literature
