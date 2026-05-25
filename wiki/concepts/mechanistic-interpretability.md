---
created: 2026-05-21T00:00:00Z
updated: 2026-05-29
type: concept
summary: Reverse-engineering transformer internals — activation caching, circuit analysis, and the EEG of artificial minds
sources: https://transformerlens.org/
status: active
confidence: 0.9
tags: [llm, interpretability, mechanistic-interpretability, transformerlens, activation-space, circuits]
---

# Mechanistic Interpretability

Field of study focused on understanding the internal computational mechanisms of transformer models — reverse-engineering what specific attention heads, MLP neurons, and circuits actually do when models process inputs and generate outputs.

## Core Tools

**TransformerLens** (Neel Nanda's library): provides a programmatic bridge into the model's computational graph. Enables:
- Hooking into any activation cache during forward pass
- Capturing residual streams at specific layers
- Ablating specific neurons/heads to test their functional role
- Tracing the exact attention heads firing when a model makes a reasoning decision

This is the "EEG" of the artificial mind — the instrument that makes the internal check loop possible by providing unoccluded visibility into latent dynamics during inference.

## Key Findings

1. **Induction heads** perform few-shot learning by detecting and completing patterns (key insight for understanding in-context learning)
2. **Functional neurons**: many neurons are "poly-semantic" — activating for multiple unrelated concepts depending on context
3. **Linear representations**: high-level behaviors are often encoded as interpretable linear directions in activation space (the foundation for activation steering)
4. **Circuit-level analysis**: complex behaviors like chain-of-thought can be traced to specific attention head sequences

## Connection to Biofeedback Paradigm

In the [[metacognitive-architecture-closed-loop-self-regulation]] framework, mechanistic interpretability serves as the **observability layer** — the sensor apparatus equivalent to EEG/EMG/HRV electrodes on a biofeedback patient. Without this visibility, modulation (activation steering) cannot be closed-loop.

See also: [[activation-steering]] for the complementary modulation half of the biofeedback loop.

## Connections

- [[activation-steering]] — the modulation counterpart to interpretability's observation
- [[metacognitive-architecture-closed-loop-self-regulation]] — complete biofeedback loop using interpretability as sensors
- [[chain-of-thought]] — mechanistic understanding of how explicit reasoning emerges from circuit dynamics
- Concept: [[activation-engineering]]
- Concept: [[affective-ai-inner-architecture]]
- Concept: [[neural-interpretability]]

