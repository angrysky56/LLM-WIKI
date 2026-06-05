---
created: 2026-05-25
updated: 2026-07-14
type: concept
summary: Autonomous agents — LLM-based agents that independently perceive environment, form plans, and execute actions toward goals
tags: [autonomous-agents, agents, llm, planning, tool-use]
sources: []
status: active
confidence: 0.7
---

# Autonomous Agents

## Definition

An autonomous agent is an LLM-based system that independently perceives its environment, forms and revises plans, and executes actions toward specified goals — without requiring step-by-step human instruction at runtime. The defining property is *operational independence*: the agent can pursue a goal across time, adapting to obstacles and changes, without the human needing to direct each step.

This distinguishes autonomous agents from:
- **Single-shot LLM calls**: Complete their response in one forward pass
- **Co-pilots**: Work alongside humans, not independently
- **Scripted bots**: Follow predetermined decision trees

## Defining Characteristics

### 1. Goal-Directed Behavior

The agent holds an internal representation of a goal state and takes actions intended to move toward that state. Goals can be:
- **Specified** (given by the user): "Research topic X and summarize findings"
- **Inferred** (derived from context): "The user's stated goal requires this prerequisite step"
- **Self-generated** (emergent): "I should verify this claim before including it in the response"

### 2. Planning Capability

The agent decomposes goals into sub-tasks and sequences them (see [[agentic-planner]]). Planning enables:
- Multi-step task completion
- Handling of obstacles through replanning
- Allocation of time and resources across sub-tasks

### 3. Tool Use and Environment Interaction

Autonomous agents interact with the world through tools — search, code execution, file operations, API calls. The tool interface defines what the agent can perceive and affect. See [[tool-use]] and [[mcp]] (Model Context Protocol) for standard interfaces.

### 4. Memory and Continuity

Genuine autonomy requires memory — the ability to retain information from earlier in a task or previous sessions. [[bounded-structured-memory]] and [[markovian-carryover]] provide the architectural substrate for this continuity.

### 5. Self-Monitoring and Self-Correction

Autonomous agents monitor their own progress and detect failures. Self-correction may involve:
- Replanning when an action fails to produce expected results
- Abandoning an approach that isn't working
- Escalating to the human when obstacles are unresolvable

## The Autonomy Spectrum

Autonomy is not binary — agents exist on a spectrum:

| Level | Description | Human involvement |
|-------|-------------|-------------------|
| 1 | Tool use | Human selects tools |
| 2 | Sequential tool use | Human monitors each step |
| 3 | Goal-directed with replanning | Human intervenes on failures |
| 4 | Session-level autonomy | Human sets goals, agent executes |
| 5 | Cross-session autonomy | Agent pursues multi-session goals |

Most deployed systems operate at Level 2-3. True session-level autonomy (Level 4) is the target for mature agentic systems.

## Autonomy and Reliability

The tension in autonomous agent design: **more autonomy creates more capability but higher risk of cascading failures**. An agent that can execute 100 steps without human oversight can accomplish things a 10-step agent cannot — but a failure at step 50 may not be detected until step 99.

[[agentic-oversight]] addresses this: mechanisms for monitoring agent behavior without defeating the purpose of autonomy.

## Connections
- [[concepts/autonomous-agents]]
- [[concepts/agent-design]]
- [[concepts/tool-use]]
- [[concepts/mcp-model-context-protocol]]
- [[concepts/markovian-carryover]]
- [[concepts/reinforcement-learning]]
- [[concepts/agent-architectures]]
- [[concepts/research-agent]]
- [[concepts/agentic-oversight]]
- [[concepts/llm-agents]]
- [[concepts/bounded-structured-memory]]
- [[wiki/index]]
- [[concepts/agents]]
- [[concepts/agentic-planner]]
- [[log]]
- [[scratchpad/agent-sheets/librarian/carryover]]
- [[concepts/autonomous-agents]]

- [[agent-architectures]]: the architectural patterns that enable autonomy
- [[agentic-planner]]: planning as the core autonomy capability
- [[bounded-structured-memory]]: memory architecture for continuous operation
- [[agentic-oversight]]: oversight mechanisms for autonomous agents
- [[reinforcement-learning]]: training paradigm for developing autonomous behaviors

- [[research-agent]]
- [[agents]]
- [[mcp-model-context-protocol]]
## Open Questions

1. **Autonomy calibration**: How autonomous should an agent be for a given task? What's the right level, and how do we determine it automatically?

2. **Failure cascading**: How do we detect and halt cascading failures in autonomous agents before they cause significant damage? Is there a reliable "failure surface area" metric?

3. **Goal stability**: When an agent pursues a goal over many steps, how do we ensure the goal remains stable? Do agents experience goal drift — gradual misalignment between the original goal and the current goal?

4. **Trust calibration**: How should human trust in autonomous agents evolve with demonstrated performance? Is there a principled trust calibration framework?
