---
created: 2026-05-25
updated: 2026-07-14
type: concept
summary: Agent architectures — design patterns for organizing LLM-based autonomous agents: deliberative, reactive, hybrid, and meta-cognitive
tags: [agents, architecture, agent-design, deliberative, reactive, hybrid]
sources: []
status: active
confidence: 0.75
---

# Agent Architectures

## Definition

Agent architecture refers to the organizational structure and operational patterns that govern how an LLM-based autonomous agent perceives, decides, and acts. The architecture determines what reasoning processes the agent can perform, how it maintains state across time, and how it interacts with external tools and environments.

The choice of architecture is the primary determinant of an agent's capabilities and limitations. Different architectures make different tradeoffs between speed, reliability, flexibility, and transparency.

## Architecture Families

### Deliberative Architecture

Deliberative agents maintain an explicit representation of goals, plans, and world state, and use symbolic reasoning to select actions. The LLM serves as a reasoning engine over a structured state representation.

**Properties**:
- Transparent reasoning — can inspect the plan
- Handles complex, multi-step goals well
- Can reason about hypotheticals and counterfactuals
- Slower than reactive systems (requires reasoning overhead)
- Brittle if world model diverges from reality

**Implementation**: The agent maintains a task hierarchy (see [[agentic-planner]]) and reasons backward from goals to subgoals. The world-model provides predictions of action outcomes.

### Reactive Architecture

Reactive agents map sensor inputs (observations) directly to actions via a learned or programmed policy, without explicit plan representation. The LLM generates actions directly from context.

**Properties**:
- Fast — no reasoning overhead
- Good for routine, well-understood tasks
- Opaque — cannot easily inspect why a specific action was chosen
- Struggles with novel situations or long-horizon goals

**Implementation**: Simple reactive agents use a single LLM call per action. More sophisticated variants use action templates or tool-calling policies learned during training.

### Hybrid Architecture

Hybrid agents combine deliberative and reactive layers — a deliberative layer for high-level goal reasoning, a reactive layer for low-level action execution.

**Properties**:
- Balances planning capability with execution speed
- Can replan at high level without blocking on low-level execution
- More complex to implement and debug
- The interface between layers (when to delegate down, when to escalate) is a critical design decision

**Implementation**: The [[hierarchical-supervisor]] pattern is a common form — a supervisor agent decomposes goals and delegates to reactive worker agents.

### Meta-Cognitive Architecture

Meta-cognitive agents explicitly monitor and regulate their own cognition. They maintain a self-model — beliefs about their own reasoning processes — and use this to calibrate confidence, detect failures, and allocate cognitive resources.

**Properties**:
- Can recognize when they don't know something
- Can self-correct before cascading failures
- More robust in novel situations
- Highest implementation complexity

**Implementation**: The [[cognitive-architecture]] MCM framework provides the theoretical basis. The [[bounded-structured-memory]] layer maintains the self-model across sessions.

## Architectural Comparison

| Property | Deliberative | Reactive | Hybrid | Meta-Cognitive |
|----------|--------------|----------|--------|----------------|
| Planning depth | Deep | Shallow | Deep | Deep |
| Execution speed | Slow | Fast | Medium | Medium |
| Novel situation handling | Moderate | Poor | Good | Good |
| Transparency | High | Low | Medium | High |
| Self-correction | Explicit replanning | None | Partial | Explicit |
| Implementation complexity | Medium | Low | High | Very High |

## Connection to Agent Design

[[agent-design]] principles determine how these architectural patterns are instantiated in practice:

- **Modularity**: Each architectural layer should be independently replaceable
- **Observability**: The agent's reasoning should be inspectable at each layer
- **Graceful degradation**: When one layer fails, the system should fail safely rather than catastrophically

## Connections

- [[agent-design]]: principles for designing agents using these architectures
- [[autonomous-agents]]: the class of agents these architectures enable
- [[agentic-planner]]: the deliberative planning capability within agents
- [[hierarchical-supervisor]]: a common hybrid architecture pattern
- [[cognitive-architecture]]: meta-cognitive layer design
- [[multi-agent-llm-systems]]: architectures for systems of multiple agents

## Open Questions

1. **Architecture selection**: Given a new task, how do we determine which architecture is appropriate? Is there a decision framework, or must it be determined empirically?

2. **Architecture evolution**: Can an agent's architecture change over time as it learns? Can a reactive agent develop deliberative capability, or vice versa?

3. **Cross-architecture communication**: When multiple agents with different architectures collaborate, what communication protocols bridge them?
