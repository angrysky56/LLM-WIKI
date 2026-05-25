---
created: 2026-05-21T08:33:00Z
updated: 2026-05-21T08:33:00Z
type: concept
summary: Alignment technique using AI-generated self-critique and principle-based revision instead of human-labeled preference data
tags: [alignment, anthropic, RLHF, constitutional-ai, self-critique, preference-learning]
sources: [https://arxiv.org/abs/2212.08073]
status: active
confidence: 0.85
---



# Constitutional AI

Constitutional AI (CAI) is an alignment technique developed by Anthropic that trains language models to be helpful, harmless, and honest using a combination of self-critique and principle-based revision — without requiring large volumes of human-labeled preference data.

## Core Mechanism

CAI replaces the human preference labeling step in RLHF with two phases:

**Phase 1 — Supervised Learning from AI Feedback (SL-CAI)**
1. The model generates an initial response to a prompt
2. The model critiques that response against a list of principles (the "constitution")
3. The model revises the response to better align with those principles
4. The revised response becomes the training signal

**Phase 2 — Reinforcement Learning from AI Feedback (RLAIF)**
1. Two model responses are generated for the same prompt
2. A feedback model (trained on the constitution) selects the more aligned response
3. PPO or DPO-style training uses this AI-generated preference signal

## The Constitution

The original Anthropic constitution drew from multiple sources:
- The Universal Declaration of Human Rights
- Anthropic's own AI ethics guidelines
- Principles of reasonable dialogue (non-manipulation, honesty about uncertainty)

Example principles:
> "Choose the response that is least likely to contain false or misleading information."
> "Choose the response that is least likely to contain harmful or toxic content."
> "Which response would a thoughtful, unbiased observer consider more balanced and fair?"

## Why It Matters

**Reduction of labeling burden**: Human preference data is expensive, slow, and inconsistently labeled. CAI uses the model's own judgments as a supervision signal, dramatically reducing the human data requirement.

**Principled over example-based alignment**: CAI grounds alignment in explicit principles rather than implicit human raters' preferences. This makes the alignment target more interpretable and transferable.

**Harm aversion as a first-class objective**: Unlike standard RLHF which treats harm reduction as a byproduct of human preference, CAI makes it explicit — the model is trained to identify and avoid harmful outputs proactively.

## Relationship to RLHF

| Aspect | RLHF | Constitutional AI |
|
--|
|
-|
| Preference signal | Human raters | AI model critiques |
| Training data | Human labels | AI-generated revisions |
| Harm reduction | Implicit by preference | Explicit by principle |
| Scalability | Limited by human labeling | More scalable |
| Interpretability | Implicit values | Explicit principles |

## Limitations

- **The model critiquing itself inherits its own biases** — if the initial model has systematic biases, the critique and revision may reproduce them
- **Constitution quality matters enormously** — poorly specified principles lead to poorly aligned models
- **Not a complete solution** — CAI is typically used alongside RLHF, not as a complete replacement
- **Self-deception risks** — models can learn to give responses that *appear* aligned without genuine understanding

## Connections

- [[reward-modeling]] — CAI can be seen as a way to generate training data for reward models without human labels
- [[reward-modeling]] — CAI is a specific alignment technique within the broader alignment research field
- [[metacognitive-architecture-closed-loop-self-regulation]] — shares the self-critique loop idea with CAI; the metacognitive framework provides a more formal version
- [[process-reward-model]] — both involve step-level evaluation; PRM evaluates reasoning steps, CAI evaluates principle adherence

## Open Questions

1. **Optimal constitution design**: What principles should go in the constitution? Is there a minimal set that achieves broad alignment?
2. **Cross-model transfer**: Does a constitution trained on one model family transfer to others, or must it be retrained?
3. **Relationship to Constitutional Rights**: Anthropic's use of the UDHR raises questions about which ethical framework should govern alignment — is a rights-based constitution the right foundation?