---
summary: Concept page for neural long-term memory.
tags: [llm, memory, machine-learning]
updated: 2026-05-06T20:08:31Z
created: 2026-05-06T20:08:31Z
---

---
created: 2026-05-06T20:08:27Z
updated: 2026-05-06T20:08:27Z
type: concept
summary: A memory architecture where sequence-specific information is dynamically stored in the parameters of a neural network during inference.
tags: [llm, memory, machine-learning, titans]
sources: [[titans-test-time-memory]]
status: active
confidence: 1.0
---

# Neural Long-Term Memory

Neural Long-Term Memory (NLTM) is a paradigm in sequence modeling where the model "learns to memorize" at test time. Unlike static memory (KV caches) or persistent weights, NLTM dynamically updates a subset of weights during the forward pass to encode new information.

## Key Features
- **Meta In-Context Learning**: The model treats the sequence processing as a mini-training session, updating its "memory parameters" to reflect the current context.
- **Parametric Storage**: Information is stored in weights rather than an external database or an ever-growing cache, allowing for fixed-size memory representations.
- **Dynamic Forgetting**: Uses weight decay or gating to prioritize recent or important information over stale data.

## Implementation: The [[titans|Titans]] Model
In the Titans architecture, NLTM uses **surprise-based memorization**, where gradients of a local loss function indicate which tokens carry enough new information to justify a weight update.

## Connections
- Source: [[titans-test-time-memory|Titans: Learning to Memorize at Test Time]]
- Concept: [[surprise-based-learning]]
- Concept: [[in-context-learning]]
- Tool: [[mamba]]
