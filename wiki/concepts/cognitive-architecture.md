---
created: 2026-05-25T00:27:20Z
updated: 2026-05-25T00:27:20Z
type: concept
summary: Hub page on cognitive architecture, MCM framework, and metacognitive self-models
tags: [meta-cognition, cognitive-architecture, AI-frameworks]
sources: []
status: active
confidence: 0.9
---

# Cognitive Architecture

**Cognitive architecture** refers to the organizational structure of an intelligent system's knowledge, reasoning processes, and meta-cognitive control mechanisms. It defines how a system represents itself, models its own cognition, and exercises control over its own operations.

## Definition

A cognitive architecture comprises:

1. **Knowledge structures** — How domain knowledge is represented
2. **Reasoning mechanisms** — How inference and decision-making are performed
3. **Meta-cognitive layer** — How the system monitors and controls its own cognition

## The Metacognitive Control Model (MCM)

The MCM framework proposes that intelligent agents maintain **two distinct self-models**:

### Knowledge Self-Model

The **knowledge self-model** contains the agent's beliefs about its own competencies, limitations, and domain expertise:

- What the agent knows and doesn't know
- Task completion histories and success rates
- Confidence in specific knowledge domains

This is the "naive" self-model — the agent's folk understanding of its own capabilities.

### Meta-Cognitive Self-Model

The **meta-cognitive self-model** contains the agent's beliefs about its own cognitive processes:

- How it generates options
- How it allocates attention
- How it updates beliefs
- The dynamics of its own reasoning

This is the "engineered" self-model — a formal specification of cognitive operations.

> **MCM Proposal**: The meta-cognitive self-model is **not identical** to the knowledge self-model. An agent may have accurate knowledge of what it knows while remaining oblivious to how it thinks. MCM argues that true metacognition requires the agent to model its own cognitive machinery explicitly.

## Relationship to oMCD

The [[oMCD]] (online Metacognitive Control of Decisions) framework provides the formal, operationalized instantiation of MCM's control layer. MCM defines *what* must be modeled; oMCD defines *how* the computation proceeds.

## Agent Architectures

Different agent architectures implement MCM in different ways:

- **Deliberative agents** — Explicit symbolic reasoning; slow but transparent
- **Reactive agents** — Direct stimulus-response mapping; fast but opaque
- **Hybrid agents** — Combine deliberative and reactive layers
- **Meta-cognitive agents** — Explicit self-monitoring and self-regulation (see [[agent-taxonomies]])

## See Also

- [[oMCD]] — Operational MCM implementation
- [[agent-taxonomies]] — Agent archetype taxonomy
- [[hermes-meta-cognition]] — Hermes as MCM implementation

## Notes

- The cognitive architecture concept originates in classical AI (Newell, Simon, SOAR, ACT-R)
- Modern large language models implicitly implement aspects of cognitive architecture through in-context learning
- Explicit meta-cognitive self-modeling remains an open research area