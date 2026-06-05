---
created: 2026-05-25
updated: 2026-07-14
type: concept
summary: Agents — LLM-based autonomous software entities that perceive, plan, and act; taxonomy and architectural foundations
tags: [agents, autonomous-agents, llm, planning]
sources: []
status: reference
confidence: 0.75
---

# Agents

## Definition

An *agent* (in the LLM context) is a software entity that uses a large language model as its reasoning engine to perceive an environment, formulate and execute plans, and take actions toward goals — operating with varying degrees of independence from continuous human direction.

The term "agent" is heavily overloaded. This page provides a unifying reference; see sub-pages for specific agent types.

## What Makes Something an Agent

Not every LLM-powered system is an agent. The key markers:

1. **Statefulness across time**: An agent maintains state that persists between LLM calls. A chatbot that starts fresh on each conversation turn is not an agent. A system that remembers what happened earlier in the session is.

2. **Goal-directedness**: The agent is pursuing an objective, not just responding to the current input. The goal may be user-specified or self-generated.

3. **Action capability**: The agent can affect the world (not just generate text) through tools, API calls, or environmental interaction.

4. **Operational independence**: The agent can take multiple steps toward a goal without requiring human direction at each step.

Systems that lack these properties are better described as *LLM applications* or *LLM-powered tools* rather than agents.

## Agent Taxonomy

The space of LLM agents can be organized along several axes:

### By Architecture
- [[deliberative-agents]]: Explicit planning and world-model reasoning
- [[reactive-agents]]: Direct stimulus-response mapping
- [[hybrid-agents]]: Combines deliberative and reactive layers
- [[meta-cognitive-agents]]: Explicit self-monitoring and self-regulation

See [[agent-architectures]] for the full comparison.

### By Autonomy Level
- **Tool-using assistants**: Human selects tool at each step
- **Sequential agents**: Agent chains tools, human monitors
- **Autonomous agents**: Agent pursues goals with limited oversight

See [[autonomous-agents]] for the full autonomy spectrum.

### By Scope
- **Single-agent systems**: One agent working on a task
- **Multi-agent systems**: Multiple agents with defined roles collaborating

See [[multi-agent-llm-systems]].

## The Minimal Agent Architecture

At minimum, an LLM agent requires:

```
Context (user input + memory)
    ↓
LLM (reasoning engine)
    ↓
Action (tool call, text response, state update)
    ↓
Memory update (new state)
    ↓
[loop until goal achieved or human intervenes]
```

The [[bounded-structured-memory]] pattern implements this loop with layered memory.

## Relationship to Non-LLM Agents

LLM agents differ from classical software agents (as in reinforcement learning or robotics) in important ways:

| Property | Classical Agents | LLM Agents |
|----------|-----------------|------------|
| Reasoning | Learned policy (RL) | Language model (statistical) |
| Transparency | Often opaque | Partially interpretable via CoT |
| Generalization | Domain-specific | Broad, zero-shot |
| Commonsense | Must be learned | Present in pretraining |
| Tool use | Custom integration | Natural language tool description |

## Connections

- [[agent-architectures]]: design patterns for agent organization
- [[autonomous-agents]]: agents that operate independently
- [[multi-agent-llm-systems]]: systems of multiple collaborating agents
- [[cognitive-world-models-for-llm-agents]]: world-model integration for agents
- [[agent-taxonomies]]: formal taxonomy of agent types

- [[agentic-design-picker]]
- [[multi-agent-systems]]

## See Also
- [[concepts/agents]]
- [[concepts/deliberative-agents]]
- [[concepts/agentic-design-picker]]
- [[concepts/reactive-agents]]
- [[log]]
- [[concepts/meta-cognitive-agents]]
- [[concepts/multi-agent-systems]]
- [[wiki/index]]
- [[concepts/agents]]

- [[agentic-planner]]: the planning capability within agents
- [[bounded-structured-memory]]: the memory layer for agent continuity
- [[markovian-carryover]]: the skill implementing forward-state memory
- [[hermes-agent]]: an LLM agent implementation using these patterns
