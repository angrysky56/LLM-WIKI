---
created: 2026-05-21T08:33:00Z
updated: 2026-05-21T08:33:00Z
type: concept
summary: The capability and architectures of LLMs to detect, critique, and revise their own outputs — distinct from explicit CoT or formal metacognitive control
tags: [self-correction, reflection, metacognition, agentic, self-refine, reasoning, LLM]
sources: [https://arxiv.org/abs/2303.11391, https://arxiv.org/abs/2212.07060]
status: active
confidence: 0.8
---

# Self-Correction in LLMs

Self-correction is the capability of a language model to detect errors, inconsistencies, or suboptimal outputs in its own generation and revise them without external intervention. It encompasses both *implicit* self-correction (emergent behavior during generation) and *explicit* self-correction (structured loop of generate → evaluate → revise).

## Taxonomy

### Implicit Self-Correction
The model corrects itself as part of normal generation — often manifesting as hedging, backtracking, or mid-stream revision without explicit prompting. This emerges from next-token prediction trained on data containing corrections.

Examples:
- Starting a sentence one way, then changing direction ("Actually, let me reconsider...")
- Adding caveats after a confident claim
- Self-verification of stated facts against internal knowledge

### Explicit Self-Correction (Self-Refine Pattern)
A structured multi-turn loop where the model:
1. Generates an initial output
2. Critiques it against explicit criteria
3. Revises based on the critique
4. Optionally iterates until a threshold

The Self-Refine framework (Madaan et al., 2023) demonstrated this pattern across 15 tasks — typically yielding 10-20% improvement over single-pass generation.

## Architectures and Implementations

### The Self-Refine Loop
```
generate(output) → critique(output, criteria) → refine(output, critique) → [iterate]
```
Key finding: The same model can generate both the output and the critique (self-critique). No separate critic model required for many tasks.

### Recurring Activation Assumption (RAA)
A hypothesis that self-correction emerges from recurring activation of attention heads that detect inconsistencies between the model's current output and its internal representation of what's correct. When these heads signal mismatch, the model shifts to a "revision mode."

### Self-Verification
The model generates an answer, then *reads its own answer* as input to verify correctness. Particularly effective for mathematical reasoning — the model checks whether each step logically follows from previous steps.

### Reflexion (Shinn et al., 2023)
A framework where the model maintains external verbal reflections that inform subsequent attempts. Failure traces are stored as text and consulted on retry. This is a *verbal* short-term memory for failures.

## Relationship to Chain-of-Thought

CoT and self-correction interact in complex ways:
- **CoT enables self-correction**: Seeing one's reasoning steps makes errors more visible
- **Self-correction can restart CoT**: After detecting an error, the model may restart the reasoning trace
- **Implicit CoT vs. explicit loops**: Some self-correction appears to happen within a single CoT trace (implicit), while explicit loops generate entirely new traces

## Why It Matters

Self-correction reduces the brittleness of LLM outputs. Without it, errors propagate unchecked. With it, the model can catch:
- Logical inconsistencies
- Factual contradictions
- Hallucinations before emission
- Style or tone mismatches

For agentic systems, self-correction at the action level prevents cascading failures — catching a bad tool call before it happens is better than correcting the output.

## Connections

- [[metacognitive-architecture-closed-loop-self-regulation]] — The formal control-theory version; self-correction can be seen as the behavioral output of metacognitive monitoring
- [[chain-of-thought]] — CoT provides the substrate for implicit self-correction; explicit CoT often includes self-correction as a step
- [[process-reward-model]] — Both PRM and self-correction involve evaluating intermediate steps; PRM provides a learned reward signal, self-correction uses the model's own judgment
- [[load-bearing-reasoning]] — Identifies which reasoning steps are essential vs. scaffolding; self-correction often removes or revises scaffolding steps
- [[agentic-research]] — Self-correction is essential for agentic research loops to handle implementation drift

## Limitations

- **Self-trust bias**: Models often fail to catch errors they are capable of catching if the error is on a topic where the model is overconfident
- **Same-model limitation**: A model critiquing itself shares the same blind spots as the original generator
- **Compute cost**: Self-correction multiplies inference compute by the number of revision iterations
- **Not guaranteed**: Self-correction is probabilistic, not deterministic — it may or may not trigger on any given error

## Open Questions

1. **When does implicit self-correction fail most?** Is there a pattern to the errors models catch vs. miss in single-pass generation?
2. **Can self-correction be reliably elicited?** Prompting strategies (e.g., "Double-check your work") help but aren't reliable — what's the mechanism?
3. **Self-correction vs. self-consistency**: Should we ensemble multiple generation paths rather than revise a single path?