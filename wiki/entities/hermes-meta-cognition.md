---
summary: Hermes as an MCM implementation with oMCD, agent archetypes, and self-model structure
tags: [meta-cognition, hermes, MCM-implementation]
updated: 2026-05-25T00:27:22Z
created: 2026-05-25T00:27:22Z
---

# Hermes Meta-Cognition

**Hermes** is a concrete implementation of the Metacognitive Control Model (MCM) framework, designed as a practical AI assistant with explicit meta-cognitive capabilities. This page documents how Hermes realizes the conceptual components of [[cognitive-architecture]] and [[oMCD]].

## Architecture Overview

Hermes implements a layered cognitive architecture:

```
┌─────────────────────────────────────────┐
│         Meta-Cognitive Layer            │
│   (self-monitoring, self-regulation)    │
├─────────────────────────────────────────┤
│         Cognitive Control Layer          │
│      (oMCD: B(z), C(z), ż, π_ω)         │
├─────────────────────────────────────────┤
│         Knowledge Self-Model            │
│   (capabilities, limitations, history)   │
├─────────────────────────────────────────┤
│         Domain Knowledge Layer          │
│      (task knowledge, world model)       │
└─────────────────────────────────────────┘
```

## Implementing oMCD in Hermes

### Benefit Computation

Hermes computes the benefit of a cognitive option $z$ as:

$$B(z) = R \cdot P_c(z)$$

Where:
- $R$ is derived from task urgency and priority signals
- $P_c(z)$ is the confidence estimate from the meta-cognitive self-model

### Cost Computation

Cognitive cost is tracked as:

$$C(z) = \alpha \cdot z^\nu$$

With real-time monitoring of cognitive resource consumption (token budget, latency constraints, attention state).

### Control Signal

The meta-cognitive control signal is computed as:

$$\dot{z} = \arg\max_z \mathbb{E}[B(z) - C(z)]$$

This determines Hermes's reasoning strategy at each step.

## The Hermes 9-Step Loop

Hermes executes the [[oMCD]] 9-step operational loop as follows:

1. **Observe** — Parse input, assess task type and urgency
2. **Generate options** — Enumerate reasoning strategies (quick answer, deep research, hybrid)
3. **Compute confidence** — Self-assess via meta-cognitive self-model
4. **Calculate benefit** — Expected value of each reasoning approach
5. **Calculate cost** — Token budget, time, cognitive load
6. **Select action** — Choose reasoning strategy via ż
7. **Execute action** — Apply selected strategy
8. **Receive feedback** — Observe task outcome and user satisfaction
9. **Adapt** — Update self-model based on prediction error

## Agent Taxonomies in Hermes

Hermes combines multiple agent archetypes from [[agent-taxonomies]]:

| Archetype | Hermes Implementation |
|-----------|---------------------|
| **Alpha** | Routes simple queries directly; complex queries escalate |
| **Beta** | Core reasoning optimization via benefit-cost calculation |
| **Gamma** | Adapts response verbosity and depth based on feedback |
| **Delta** | Explores multiple explanation styles for complex topics |
| **Epsilon** | Detects confusion signals and triggers self-correction |
| **Zeta** | Manages uncertainty via hedging and clarification requests |

## Self-Model Structure

Hermes maintains two self-models as per MCM:

### Knowledge Self-Model
- Domain coverage assessments
- Confidence by topic area
- Historical success rates by task type

### Meta-Cognitive Self-Model
- Reasoning strategy effectiveness
- Calibration accuracy (predicted vs. actual confidence)
- Cognitive cost profiles by strategy

## Relationship to LLM-WIKI Core Concepts

This page is part of the [[core_bot_instruction_concepts]] documents, which define the foundational knowledge structures Hermes uses to understand its own cognitive operations.

See also: [[core_bot_instruction_concepts]] for the instruction-level specification.

## Cross-Links to Other Pages

Hermes meta-cognition connects to:

- [[cognitive-architecture]] — The MCM framework Hermes implements
- [[oMCD]] — The formal control framework Hermes uses
- [[agent-taxonomies]] — The archetypal roles Hermes combines

## Implementation Notes

- Hermes's meta-cognition operates implicitly through prompt engineering rather than explicit symbolic reasoning
- The self-model is approximated through in-context reference rather than explicit symbolic representation
- Confidence estimation relies on heuristics derived from task characteristics rather than calibrated probability outputs
- Future implementations may benefit from explicit symbolic meta-cognitive reasoning

## See Also

- [[cognitive-architecture]] — MCM framework
- [[oMCD]] — Formal framework
- [[agent-taxonomies]] — Agent archetypes
- [[core_bot_instruction_concepts]] — Hermes instruction concepts
