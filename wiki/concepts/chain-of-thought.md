---
summary: Concept page for Chain-of-Thought.
tags: [llm, reasoning, cot]
updated: 2026-05-06T20:09:26Z
created: 2026-05-06T20:09:26Z
---

---
created: 2026-05-06T20:09:21Z
updated: 2026-05-06T20:09:21Z
type: concept
summary: A prompting technique and internal process where LLMs generate intermediate reasoning steps before providing a final answer.
tags: [llm, reasoning, prompting, cot]
sources: [Wei et al. 2022]
status: active
confidence: 1.0
---

# Chain-of-Thought

Chain-of-Thought (CoT) is a paradigm in Large Language Models where the model is encouraged (or naturally exhibits) the generation of "thinking steps" in a hidden or visible reasoning trace.

## Variants
- **Implicit CoT**: Reasoning occurs within the model's latent space.
- **Explicit CoT**: Reasoning is output as text tokens, allowing for better accuracy and interpretability.

## Optimization
- **[[supertokens]]**: Compressing CoT traces by merging structural phrases.
- **[[titans]]**: Using neural long-term memory to handle long-context reasoning.

## Connections
- Source: [[shorthand-for-thought]]
- Concept: [[reasoning]]
- Concept: [[supertokens]]
