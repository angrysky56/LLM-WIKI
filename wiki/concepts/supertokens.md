---
created: 2026-05-06T20:07:39Z
updated: 2026-05-06T21:50:50Z
type: concept
summary: High-level vocabulary entries created by merging multi-token sequences (structural phrases) into single units, functioning as operators in a problem-space search.
tags: [llm, cognitive-architecture, process-modeling, superbpe]
sources: [[shorthand-for-thought]]
status: active
confidence: 1.0
---

# Supertokens

Supertokens are an advanced form of tokenization where recurring structural sequences in reasoning traces are merged into single vocabulary entries. 

## Theoretical Lineage: Cognitive Architectures
While supertokens are an LLM optimization, they function as high-level **operators** in a **Problem Space Hypothesis** (Newell, 1980). They align with the tradition of **Classical Cognitive Architectures** (Soar, ACT-R) and **GOMS-style operator analysis**, where reasoning is viewed as a sequence of discrete functional moves rather than a continuous stream.

### Operators in Reasoning
In this framework, supertokens represent discrete cognitive steps:
- **Strategy Shift**: A move to a different branch of the search tree.
- **Verification**: A consistency check on a previously emitted state.
- **Backtracking**: Returning to a prior node in the problem space.

## Interpretability: Causal Mediation
Instead of viewing transitions between supertokens as "Wolfram-style physics," they are better analyzed as a **Causal Network of Intent**. By measuring which supertoken transitions are **load-bearing** (affecting the final conclusion) vs. **scaffolding** (statistical noise reduction), we can perform **Causal Mediation Analysis** (Pearl-flavored) on the model's internal "monologue."

## Connections
- Source: [[shorthand-for-thought|Shorthand for Thought]]
- Concept: [[load-bearing-reasoning]]
- Concept: [[chain-of-thought]]
- Tool: [[superbpe]]
