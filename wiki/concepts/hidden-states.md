---
created: 2026-04-18T03:57:00Z
updated: 2026-04-18T03:57:00Z
type: concept
summary: "The internal vector representations (activations) of data at each layer of a neural network, containing 'inner knowledge' and confidence signals."
tags: [llm-architecture, interpretability, activations, linear-representation]
status: active
confidence: 1.0
---

# Hidden States

Hidden states (or internal activations) are the intermediate vector representations produced by each layer of a neural network as it processes an input. In Transformer-based Large Language Models (LLMs), these states capture complex linguistic, logical, and factual information that is not directly visible in the final textual output.

## Inner Knowledge and Linear Representation

Research has shown that LLM hidden states contain "inner knowledge"—a representation of the model's own certainty or the likely correctness of a reasoning path. 

- **Linearity**: Surprisingly, these complex signals can often be extracted using simple linear probes or linear discriminant analysis (LDA). This suggests that the model's internal representation of truthfulness or confidence is structured in a relatively straightforward geometric way within the high-dimensional hidden space.
- **Layer-wise Information**: Different layers capture different levels of abstraction. Lower layers often handle syntactic structure, while higher layers encode semantic meaning and final answer confidence.

## Applications

- **Interpretability**: Analyzing hidden states helps researchers understand why a model makes certain predictions or errors.
- **Efficient Reward Modeling**: Instead of processing the entire textual output with a separate 7B+ parameter model, lightweight linear models like **[[reward-inside-model-elhsr|ELHSR]]** can predict correctness directly from the concatenated hidden states of the generator LLM.
- **OOD Detection**: Hidden states can be used to detect Out-of-Distribution (OOD) inputs or "hallucinations" by identifying activations that deviate from the training distribution (see [[causal-state-edm-ood-isomorphism]]).

## Connections

- **[[reward-modeling]]**: Hidden states provide the raw data for state-based reward signals.
- **[[causal-state-edm-ood-isomorphism]]**: Explores the isomorphism between internal causal states and external observable behaviors.
- **[[critical-analysis]]**: Scientific evaluation of LLMs increasingly relies on internal metrics (hidden states) rather than just external benchmark scores.
