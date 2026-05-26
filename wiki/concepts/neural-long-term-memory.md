---
created: 2026-05-06T20:08:27Z
updated: 2026-05-29
type: concept
summary: Neural network architectures that explicitly separate working memory from long-term memory stores, enabling persistent information across very long contexts
sources: []
status: active
confidence: 0.8
tags: [llm, memory, machine-learning, neural-memory]
---

# Neural Long-Term Memory

Neural Long-Term Memory (NLTM) is a paradigm in sequence modeling where the model "learns to memorize" at test time. Unlike static memory (KV caches) or persistent weights, NLTM dynamically updates a subset of weights during the forward pass to encode new information.

## Key Features

- **Meta In-Context Learning**: The model treats the sequence processing as a mini-training session, updating its "memory parameters" to reflect the current context.
- **Parametric Storage**: Information is stored in weights rather than an external database or an ever-growing cache, allowing for fixed-size memory representations.
- **Dynamic Forgetting**: Uses weight decay or gating to prioritize recent or important information over stale data.

## Implementation: The [[titans-test-time-memory]] Model

In the Titans architecture, NLTM uses **surprise-based memorization**, where gradients of a local loss function indicate which tokens carry enough new information to justify a weight update.

## Connections

- Source: [[titans-test-time-memory]]
- Concept: [[mamba]]
- Concept: 
- Tool: [[mamba]]
- Concept: [[length-generalization]]
- Concept: [[ml-evolution]]
- Concept: [[surprise-based-learning]]
- Concept: [[titans]]

