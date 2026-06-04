---
created: 2026-06-14
updated: 2026-08-05
type: concept
summary: Decision-making under finite cognitive resources — Herbert Simon's foundational concept now driving architectural design in LLM agents where bounded rationality is first-class, not retrofitted
tags: [bounded-rationality, cognition, decision-making, agent-design, MOP, epistemic-energy, information-theory]
sources: [Herbert Simon (1950s), agent-native-design]
status: active
confidence: 0.75
---

# Bounded Rationality

Bounded rationality is Herbert Simon's foundational observation that decision-making agents — biological or artificial — operate under finite cognitive resources. They cannot optimize globally, enumerate all options, or compute perfect expected utility. Instead, they satisfice: find options that are "good enough" given their structural and informational constraints.

The concept originated in economics and cognitive psychology in the 1950s. In the LLM-WIKI context, it has become architecturally first-class: a design principle, not just a description of limitation.

## Core Definition

A bounded rational agent:

1. **Has limited information**: Cannot know all relevant facts about the world or all consequences of its actions
2. **Has limited computation**: Cannot fully enumerate or evaluate all options within available time or tokens
3. **Has limited memory**: Cannot retain all relevant context or retrieve it perfectly
4. **Must act before certainty is achieved**: Stopping rules are as important as search rules

The key insight: bounded rationality is not a bug to fix with faster hardware. It is a structural property that shapes what kind of reasoning is possible at all.

## Bounded Rationality in AI Systems

### Token and Context Limits as Hard Bounds

LLMs have fixed context windows (8K, 128K, 1M tokens). These are hard architectural bounds — not softened by better hardware. When an agent's context fills up, it must make decisions about what to retain and what to discard. This is the computational equivalent of Simon's satisficing threshold.

### Attention as a Degrading Resource

Transformer attention is not uniform over long contexts. Attention heads track dependencies with diminishing strength over distance. Long sequences degrade the signal-to-noise ratio — a form of computational bounded rationality where more context does not proportionally improve reasoning quality.

### Epistemic Energy Depletion

The [[epistemic-energy]] concept extends bounded rationality from information/computation to a resource-theoretic framework:

- Energy depletes as reasoning progresses
- High-Δ events (novel territory) accelerate depletion
- Depleted energy produces incoherent output — the agent's "bounded" limit reached
- The stopping condition is epistemic energy, not token budget

This maps to physical foraging: an animal stops searching not when it has exhausted all possible food sources, but when the energy cost of continued search exceeds the expected energy gain.

### Memory Constraints and Retrieval Decisions

The [[bounded-structured-memory]] pattern implements bounded rationality as a layered memory architecture:
- Working memory: high-bandwidth but volatile
- Episodic memory: medium-term, selective retention
- Semantic memory: long-term, compressed knowledge

The agent must decide at each layer what is worth retaining — an inherently lossy, satisficing operation.

## Agent Native Design: Bounded Rationality as First-Class

The [[agent-native-design]] framework argues that bounded rationality in LLM agents should be **structural** — built into the architecture from the ground up — not retrofitted onto general-purpose models.

Traditional approach (retrofitted):
- Take a transformer (unbounded next-token optimizer)
- Add token budget limits (hard stop)
- Add RLHF reward shaping (steer away from catastrophic outputs)
- Add constitutional constraints (external filter)

Agent native approach:
- Path entropy maximization as intrinsic motivation (Layer 0)
- Epistemic energy tracking as the primary resource
- Absorbing-state detection as the stopping condition
- Verification before action (EFHF layers)

The difference: in the retrofitted case, bounded rationality is a constraint applied externally. In the agent native case, it is the core organizing principle.

## Connection to MOP/EFHF Framework

### MOP (Maximum Occupancy Principle)

MOP replaces reward maximization with action-state path entropy maximization. The agent is not trying to reach a specific "optimal" state — it is trying to maximize behavioral diversity while avoiding absorbing states. Bounded rationality is the constraint that makes this objective meaningful: without limited resources, entropy maximization has no stopping condition.

### EFHF Architecture

The EFHF five-layer architecture implements bounded rationality structurally:
- L1 (Hypothesis): Generates candidates within the agent's current epistemic bounds
- L2 (World model): Encodes hypotheses given limited representational capacity
- L3 (Verification): Checks consistency — but verification itself is bounded by time/compute
- L4 (Coherence): Explicitly tracks epistemic energy depletion
- L5 (Persistence): Enforces consistency within bounded computational resources

## Connections
- [[concepts/epistemic-energy]]
- [[concepts/working-memory]]
- [[scratchpad/agent-sheets/researcher/carryover]]
- [[wiki/index]]
- [[concepts/bounded-rationality]]
- [[log]]
- [[concepts/adaptive-computation]]
- [[concepts/hybrid-agents]]
- [[concepts/agent-native-design]]
- [[concepts/cognitive-world-models-for-llm-agents]]
- [[bounded-rationality]]

- [[agent-native-design]] — the architectural framework that makes bounded rationality first-class
- [[epistemic-energy]] — the quantitative resource form of bounded rationality in agentic systems
- [[concepts/maximum-occupancy-principle]] — path entropy maximization as bounded exploration
- [[efhf]] — Layer 4 explicitly tracks bounded reasoning resources
- [[bounded-structured-memory]] — memory architecture implementing bounded retention decisions
- [[working-memory]] — the substrate most directly subject to bounded rationality constraints
- [[cognitive-world-models-for-llm-agents]] — how world models compensate for bounded context- [[concepts/sovereign-ai.md]]


- [[adaptive-computation]]
- [[sovereign-ai]]
- [[hybrid-agents]]
## Open Questions

1. **Information-theoretic formulation**: Can bounded rationality be fully expressed as a rate-distortion or compression problem? The agent minimizes distortion subject to a bounded representation budget — is this equivalent to bounded rational decision-making?

2. **Architectural vs budgetary bounds**: Is there a qualitative difference between agents designed with structural bounded rationality vs agents with externally imposed budget limits? Does the architectural approach yield qualitatively different emergent properties?

3. **Bounded rationality transfer**: Do reasoning patterns developed under one set of bounded constraints (e.g., a specific context window) transfer to different constraint profiles? How does an agent's internal bounded-rationality heuristic adapt to novel resource environments?

4. **Satisficing vs optimizing**: Simon argued that humans satisfice (find good-enough options) rather than optimize. Does the same apply to LLM agents? Is the "next most likely token" inherently a satisficing strategy?