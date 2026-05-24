---
created: 2026-06-03
updated: 2026-06-08
type: concept
summary: System design patterns where AI capabilities are architecturally native rather than retrofitted — designing agents with intrinsic motivation, bounded rationality, and epistemic energy management from the ground up
tags: [agent-design, architecture, MOP, intrinsic-motivation, bounded-rationality, epistemic-energy, EFHF]
sources: [[ramirez-ruiz-mop-2024]], [[mop-edm-cognitive-architecture]]
status: active
confidence: 0.8
---

# Agent Native Design

Agent native design refers to system architectures where AI capabilities are architecturally intrinsic — built into the foundational structure — rather than retrofitted onto general-purpose models. The term implies that genuinely capable, safe, and aligned AI systems require design choices that are native to agency: intrinsic motivation, bounded rationality, epistemic energy management, and absorbing-state awareness from the ground up.

This contrasts with the dominant paradigm: take a transformer language model, fine-tune it with RLHF, add tool use and memory systems, and call it an "agent." Agent native design says the architectural primitives must change first.

## The Core Problem: Retrofitting Is Inefficient

A transformer pretrained on next-token prediction is fundamentally reactive — it generates the most likely continuation given the context. An agent needs to be proactive: it needs motivation that isn't derived from the next-token objective, epistemic energy management that prevents reckless exploration, and absorbing-state detection that stops it from continuing into contradiction.

These properties can't be fully retrofitted onto a reactive base. You can approximate them with RLHF (reward shaping), constitutional constraints (external filter), andCoT prompting (internal coherence), but the underlying architecture remains reactive.

Agent native design proposes changing the architecture:

1. **Replace reactive next-token generation with proactive path-entropy maximization** (MOP as Layer 0)
2. **Replace KL-regularized RLHF with absorbing-state constraints** (no reinforcement needed)
3. **Replace token-level coherence with epistemic energy tracking** (depletion before contradictions)

## Key Design Principles

### 1. Intrinsic Motivation from Birth

The [[maximum-occupancy-principle]] provides the theoretical foundation: agents should maximize action-state path entropy rather than reward. This means behavioral diversity is the primary objective, with survival (avoiding absorbing states) as the constraint.

In an agent native system, this means:
- The base policy is trained to maximize entropy over reachable states
- Absorbing states are architecturally defined (not learned)
- Reward signals are secondary to occupancy diversity

### 2. Bounded Rationality Is Structural, Not Budgetary

LLM agents are typically made "bounded" via context window limits and token budgets. Agent native design says bounded rationality should be structural — the agent's reasoning itself should exhibit diminishing returns and coherence degradation as it approaches its epistemic limits.

This is where [[mop-edm-cognitive-architecture]] connects:
- Epistemic energy `E` depletes as reasoning progresses
- Coherence degrades as `E` approaches zero
- High-Δ events (novel territory) accelerate depletion
- Absorbing states (contradiction) are terminal — no further exploration possible

### 3. Verification Before Action

The EFHF architecture implements verification at every layer (L3: mcp-logic, L5: sheaf-consistency-enforcer). Agent native design makes this structural — the agent cannot commit to an action without passing the verification stack.

This contrasts with reactive models where the output is generated first and then checked (if at all). Agent native means:
- Hypothesis generation (L1) → world model encoding (L2) → verification (L3) → coherence tracking (L4) → persistence enforcement (L5)
- No skipping verification to save time

### 4. Epistemic Energy as First-Class Resource

In LLM systems, "context" is treated as a container to be filled. Agent native design treats epistemic energy as a limited resource that must be managed:
- [[persistent-knowledge-compilation]] (PKC) predicts which knowledge will be needed and precompiles it into rapidly accessible form
- MOP's energy reservoir analogy maps physical energy (food sources) to epistemic energy (information retrieval)
- The agent stops exploring when energy is depleted — not when tokens run out

## Architectural Patterns

### The MOP-EFHF Layer Stack

Agent native design maps to the MOP-EDM cognitive architecture:
- **Layer 0 (MOP)**: Path entropy maximization → intrinsic motivation
- **L1 (Hypothesis)**: Generate from MOP's exploration target
- **L2 (World model)**: Encode hypotheses in the world model
- **L3 (Verification)**: mcp-logic checks for absorbing states, contradictions
- **L4 (Coherence)**: Track epistemic energy, detect degradation
- **L5 (Persistence)**: sheaf-consistency-enforcer maintains global consistency
- **L5+ (Ethics)**: conscience-servitor screens for deontological violations

### Agentic Hierarchy Integration

Agent native design works naturally with [[agentic-hierarchy]]:
- Supervisors are left-adjoint to workers (adjunction structure)
- Authority delegation is functorial (specification → implementation)
- Each agent in the hierarchy has its own MOP-EFHF stack
- Absorbing states are shared across the hierarchy (global consistency)

## Connections

- [[maximum-occupancy-principle]] — the intrinsic motivation foundation
- [[mop-edm-cognitive-architecture]] — the full architectural synthesis
- [[efhf]] — the verification and consistency enforcement backbone
- [[agentic-hierarchy]] — hierarchical agent organization as native pattern
- [[epistemic-energy]] — the first-class resource for bounded rationality
- [[bounded-rationality]] — structural bounds on reasoning, not just budgetary

## Open Questions

1. **Can MOP be trained into a transformer from scratch?** Current MOP results are in RL agents. Can the path entropy objective be applied to next-token prediction training?

2. **Absorbing states in language models** — physical death is a clear absorbing state in biological agents. What is the equivalent for a language model? Contradiction is one candidate, but what counts as "no further coherent continuation"?

3. **Epistemic energy measurement** — how do you measure the depletion of an LLM's epistemic energy in real time? Context utilization? Attention entropy? Perplexity on known facts?

4. **Agent-to-agent transfer** — if two agents both implement the MOP-EFHF stack, what's the minimal interface for them to coordinate? (This connects to the MCP protocol design.)