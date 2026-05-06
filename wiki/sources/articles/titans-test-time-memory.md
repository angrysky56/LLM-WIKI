---
summary: Titans: Learning to Memorize at Test Time summary.
tags: [llm, memory, titans]
updated: 2026-05-06T20:08:27Z
created: 2026-05-06T20:08:27Z
---

---
created: 2026-05-06T20:08:19Z
updated: 2026-05-06T20:08:19Z
type: source
summary: Google Research paper introducing Titans, an architecture that combines attention with a neural long-term memory module that learns to memorize at test time.
tags: [llm, memory, long-context, titans, neural-memory, machine-learning]
sources: https://www.alphaxiv.org/overview/2501.00663
status: active
confidence: 1.0
---

# Titans: Learning to Memorize at Test Time

Research by Google Research (Behrouz, Zhong, Mirrokni) introducing a cognitive-inspired memory architecture for sequence modeling.

## Summary

Titans addresses the trade-off between the expressive power of Transformers (quadratic complexity) and the efficiency of linear recurrent models. It proposes a three-tier memory system.

### Three Memory Components
1. **Short-term Memory**: Standard attention focused on local windows.
2. **Long-term Memory**: A neural network that dynamically updates its parameters $\theta$ during inference to store sequence-specific information.
3. **Persistent Memory**: Data-independent parameters representing static knowledge acquired during training.

### Mechanisms
- **Surprise-Based Memorization**: Uses a gradient-based surprise metric $\nabla_\theta L$ to identify which inputs are worth storing in the long-term memory.
- **Memory Decay**: A generalized forgetting mechanism to prevent parameter saturation over extremely long sequences.
- **Parallelization**: Uses tensorized mini-batch gradient descent for efficient training of the memory module.

### Architectural Variants
- **MAC (Memory as Context)**: Memory output is concatenated with the input sequence. Best for long-term dependencies.
- **MAL (Memory as Layer)**: Memory acts as a hierarchical layer before attention.
- **MAG (Memory as Gate)**: Memory output is combined with the main branch via a gating mechanism.

### Key Results
- **Context Length**: Maintains 70% accuracy at $10^7$ (10 million) tokens on needle-in-haystack tasks, significantly outperforming GPT-4 and Mamba.
- **Efficiency**: Achieves linear scaling with respect to sequence length while maintaining constant throughput.

## Connections
- Concept: [[neural-long-term-memory]]
- Concept: [[in-context-learning]]
- Concept: [[surprise-based-learning]]
- Entity: [[google-research]]
- Tool: [[mamba]]
