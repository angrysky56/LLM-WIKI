---
created: 2026-05-21 08:33:00+00:00
updated: 2026-05-25 00:00:00+00:00
type: concept
summary: The capability and architectures of LLMs to detect, critique, and revise their own outputs — distinct from explicit CoT or formal metacognitive control
tags: [self-correction, reflection, metacognition, agentic, self-refine, reasoning, llm]
sources: ['https://arxiv.org/abs/2303.11391', 'https://arxiv.org/abs/2212.07060']
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

## Relationship to oMCD

Self-correction is the *behavioral output* of the [[oMCD]] (online Metacognitive Control of Decisions) framework. In oMCD terms:

- The **Epsilon** agent archetype (assumption validation) implements the detection phase of self-correction
- The **Beta** agent archetype (option optimization) computes the revised action
- The 9-step oMCD loop's "Adapt" step (step 9) corresponds to the self-correction update

See [[cognitive-architecture]] for how self-correction fits into the broader MCM framework.

## Why It Matters

Self-correction reduces the brittleness of LLM outputs. Without it, errors propagate unchecked. With it, the model can catch:
- Logical inconsistencies
- Factual contradictions
- Hallucinations before emission
- Style or tone mismatches

For agentic systems, self-correction at the action level prevents cascading failures — catching a bad tool call before it happens is better than correcting the output.

## Connections
- [[concepts/load-bearing-reasoning]]
- [[concepts/engineering-internal-awareness]]
- [[concepts/process-reward-model]]
- [[concepts/agent-taxonomies]]
- [[concepts/generative-ai]]
- [[scratchpad/jobs/reports/librarian/audit-2026-05-21]]
- [[concepts/chain-of-thought]]
- [[concepts/imagination]]
- [[concepts/cognitive-architecture]]
- [[concepts/agentic-reasoning]]
- [[concepts/parallel-reasoning]]
- [[concepts/llm-reasoning]]
- [[concepts/reward-hacking]]
- [[concepts/agentic-research]]
- [[wiki/index]]
- [[concepts/metacognitive-architecture-closed-loop-self-regulation]]
- [[scratchpad/jobs/reports/researcher/discovery-2026-05-22]]
- [[concepts/multi-agent-reasoning]]
- [[concepts/self-correction]]
- [[log]]
- [[self-correction]]

- [[metacognitive-architecture-closed-loop-self-regulation]] — The formal control-theory version; self-correction can be seen as the behavioral output of metacognitive monitoring
- [[oMCD]] — The formal framework for metacognitive control; Epsilon and Beta archetypes implement self-correction
- [[cognitive-architecture]] — MCM framework where self-correction is the control output
- [[chain-of-thought]] — CoT provides the substrate for implicit self-correction; explicit CoT often includes self-correction as a step
- [[process-reward-model]] — Both PRM and self-correction involve evaluating intermediate steps; PRM provides a learned reward signal, self-correction uses the model's own judgment
- [[load-bearing-reasoning]] — Identifies which reasoning steps are essential vs. scaffolding; self-correction often removes or revises scaffolding steps
- [[agent-taxonomies]] — The Epsilon archetype specifically implements assumption validation and self-correction triggers
- [[agentic-research]] — Self-correction is essential for agentic research loops to handle implementation drift
- Concept: [[engineering-internal-awareness]]
- Concept: [[reward-hacking]]


- [[parallel-reasoning]]
- [[llm-reasoning]]
- [[imagination]]
- [[multi-agent-reasoning]]
- [[generative-ai]]
- [[agentic-reasoning]]
## Limitations

- **Self-trust bias**: Models often fail to catch errors they are capable of catching if the error is on a topic where the model is overconfident
- **Same-model limitation**: A model critiquing itself shares the same blind spots as the original generator
- **Compute cost**: Self-correction multiplies inference compute by the number of revision iterations
- **Not guaranteed**: Self-correction is probabilistic, not deterministic — it may or may not trigger on any given error

## Open Questions

1. **When does implicit self-correction fail most?** Is there a pattern to the errors models catch vs. miss in single-pass generation?
2. **Can self-correction be reliably elicited?** Prompting strategies (e.g., "Double-check your work") help but aren't reliable — what's the mechanism?
3. **Self-correction vs. self-consistency**: Should we ensemble multiple generation paths rather than revise a single path?
4. **oMCD integration**: Can explicit meta-cognitive control (via [[oMCD]]) improve self-correction reliability beyond prompt-based elicitation?