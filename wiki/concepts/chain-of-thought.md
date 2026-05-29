---
created: 2026-05-06
updated: 2026-05-29
type: concept
summary: A prompting technique and internal process where LLMs generate intermediate reasoning steps before providing a final answer
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
- **[[titans-test-time-memory|Titans]]**: Using neural long-term memory to handle long-context reasoning.

## Connections
- [[concepts/generative-ai]]
- [[concepts/benchmark]]
- [[concepts/molecular-reasoning]]
- [[synthesis/self-prompting-via-production-stage-architecture]]
- [[concepts/self-correction]]
- [[synthesis/bounded-structured-memory]]
- [[concepts/supertokens]]
- [[log]]
- [[sources/papers/production-llm-agent-runtime-architecture-patterns]]
- [[concepts/parallel-reasoning]]
- [[concepts/opendeepthink-parallel-reasoning]]
- [[concepts/mechanistic-interpretability]]
- [[concepts/in-context-learning]]
- [[sources/papers/decoupling-perception-reasoning-vlm-post-training]]
- [[concepts/chain-of-thought]]
- [[synthesis/verifiable-graph-context-protocol]]
- [[concepts/activation-steering]]
- [[sources/news/2026/engineering-internal-awareness-and-closed-loop-self-regulation-in-large-language-models]]
- [[concepts/length-generalization]]
- [[concepts/agentic-reasoning]]
- [[sources/papers/ma-sd-search-2026]]
- [[concepts/activation-engineering]]
- [[concepts/multi-agent-reasoning]]
- [[concepts/latent-reasoning]]
- [[sources/articles/shorthand-for-thought]]
- [[sources/papers/chen-molecular-cot-2026]]
- [[concepts/load-bearing-reasoning]]
- [[concepts/evaluation]]
- [[concepts/emergence]]
- [[concepts/shorthand-for-thought]]
- [[concepts/inference-time-compute-scaling]]
- [[concepts/process-reward-model]]
- [[wiki/index]]
- [[chain-of-thought]]

- Source: [[shorthand-for-thought]]
- Concept: [[load-bearing-reasoning]]
- Concept: [[supertokens]]
- Concept: [[activation-steering]]
- Concept: [[benchmark]]
- Concept: [[bounded-structured-memory]]
- Concept: [[emergence]]
- Concept: [[evaluation]]
- Concept: [[in-context-learning]]
- Concept: [[inference-time-compute-scaling]]
- Concept: [[length-generalization]]
- Concept: [[llm-reasoning]]
- Concept: [[mechanistic-interpretability]]
- Concept: [[molecular-reasoning]]
- Concept: [[parallel-reasoning]]
- Concept: [[process-reward-model]]
- Concept: [[self-correction]]


- [[activation-engineering]]
- [[multi-agent-reasoning]]
- [[generative-ai]]
- [[latent-reasoning]]
- [[agentic-reasoning]]