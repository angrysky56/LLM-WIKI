---
summary: Concept page for compressed reasoning tokens.
tags: [llm, tokenization, compression]
updated: 2026-05-06T20:07:43Z
created: 2026-05-06T20:07:43Z
---

---
created: 2026-05-06T20:07:39Z
updated: 2026-05-06T20:07:39Z
type: concept
summary: High-level vocabulary entries created by merging multi-token sequences (often structural phrases) into a single token for efficiency and interpretability.
tags: [llm, tokenization, compression, nlp]
sources: [[shorthand-for-thought]]
status: active
confidence: 1.0
---

# Supertokens

Supertokens are an advanced form of tokenization where recurring, low-entropy sequences—typically structural phrases in [[chain-of-thought|Chain-of-Thought]] reasoning—are merged into a single entry in the model's vocabulary.

## Mechanics
- **Creation**: Identified using algorithms like [[superbpe]] which allow merging across whitespace.
- **Embedding**: Initialized by averaging the embeddings of the constituent tokens to preserve semantic context.
- **Utility**: Reduces the length of output sequences (lowering latency and cost) while serving as "diagnostic signposts" for model behavior.

## Categories in Reasoning
- **Verification**: "Let's check this," "Let us verify."
- **Backtracking**: "Wait, hold on," "Let me restart."
- **Strategy Shift**: "Alternatively," "Let's try a different approach."

## Connections
- Source: [[shorthand-for-thought|Shorthand for Thought: Compressing LLM Reasoning]]
- Concept: [[chain-of-thought]]
- Concept: [[entropy-guided-compression]]
