---
created: 2026-05-29
updated: 2026-05-29
type: concept
summary: Delegation — the act of assigning authority and task responsibility from one agent to another within an agentic hierarchy
tags: [delegation, agentic-ai, hierarchy, task-assignment]
sources: 
status: active
confidence: 0.8
---



# Delegation

## Definition

Delegation is the mechanism by which an agent assigns task authority to another agent, transferring responsibility for some portion of work while retaining overall accountability. In agentic systems, delegation is the primary tool for decomposing complex goals across hierarchy levels.

Delegation is distinct from mere tool-calling. A tool call is a stateless request for a specific function (get the weather, run this query). Delegation implies the receiving agent has agency — it can make sub-decisions, request clarification, handle failures, and adapt its approach. The delegating agent specifies *what* outcome to achieve and *constraints* on how to achieve it; the delegated agent determines *how*.

## Why It Matters

Without delegation, every agent system is a flat single-agent architecture — capable but bounded by the context window and model capacity of a single agent. Delegation is what enables:

1. **Parallelization**: Multiple sub-tasks can be executed simultaneously, reducing end-to-end latency.
2. **Specialization**: Different agents can develop expertise in different domains without contaminating each other's context.
3. **Scale**: The system can handle tasks whose complexity exceeds any single agent's context or capability.
4. **Robustness**: Failure of a delegated sub-task doesn't necessarily fail the entire system — the delegating agent can retry, reassign, or adapt.

In the Hermes agent framework, `delegate_task` is the primary delegation primitive — spawning isolated child agents with their own context and tool sets for parallel workstreams.

## Delegation Mechanics

### What Gets Delegated

When an agent delegates, it transfers:
- **Goal specification**: What outcome is needed, not how to achieve it
- **Constraint specification**: Budget, deadline, quality bar, or other boundaries
- **Authority**: The right to make sub-decisions within those boundaries
- **Accountability** (partial): The delegating agent remains ultimately responsible for the outcome

What stays with the delegator:
- **Context**: The high-level task context and planning state
- **Coordination**: Ensuring sub-tasks fit together into a coherent whole
- **Validation**: Accepting or rejecting the delegated result

### Delegation Patterns in Hermes

In Hermes, delegation happens via `delegate_task`:
```
delegate_task(
  task="analyze this codebase",
  agent_type="coder",
  model="claude-sonnet",
  tools=["read_file", "search_files"],
  delivery=discord_channel
)
```

Key properties:
- **Isolated context**: Each child gets a fresh conversation context
- **Restricted toolsets**: Delegator controls what tools the child can use
- **Parallel execution**: Up to 3 concurrent children
- **Non-durable**: Interrupt cancels children (use cron jobs for durable delegation)

The [[entities/tools/hermes-agent]] entity page has full details on `delegate_task` mechanics.

### Levels of Delegation

1. **Flat delegation** (default): One level of children, no nesting. Simple, predictable, bounded cost.
2. **Hierarchical delegation**: Child agents can further delegate to their own children. Enables recursive task decomposition but with exponential context growth risk.
3. **Market-based delegation**: Tasks are broadcast and agents bid for them based on capability matching. More flexible but requires coordination infrastructure.

## Delegation vs. Planning

The key distinction:

| | Delegation | Planning |
|
|
|
|
| **Who acts** | Another agent | Same agent |
| **Context** | Isolated | Shared |
| **Adaptivity** | Agent decides how | Prompt decides how |
| **Failure scope** | Bounded to sub-task | Full task |

A system with delegation but no planning gets sub-tasks done but may produce incoherent results. A system with planning but no delegation can adapt but is bounded by single-agent context limits. The combination — delegation with a coordinator that plans — enables scalable complex task execution.

## Connections
- [[concepts/agentic-oversight]]
- [[concepts/subagent-delegation]]
- [[sources/articles/choosing-right-agentic-design-pattern]]
- [[wiki/index]]
- [[concepts/delegation]]
- [[log]]
- [[sources/documentation/create-custom-subagents]]
- [[concepts/multi-agent-coordination]]
- [[concepts/agentic-hierarchy]]
- [[concepts/agent-onboarding]]
- [[sources/documentation/subagent-delegation-hermes-agent]]
- [[concepts/markovian-carryover]]
- [[concepts/multi-agent-llm-systems]]
- [[concepts/delegation]]

- [[agentic-hierarchy]] — organizational structures that make delegation structured and systematic; delegation is the mechanism that moves work down hierarchy levels
- [[entities/tools/hermes-agent]] — framework with native `delegate_task` support for delegation primitives
- [[subagent-delegation]] — mechanics of Hermes's delegate_task spawning
- [[bounded-structured-memory]] — layered memory that preserves context across delegation boundaries
- [[multi-agent-llm-systems]] — systems where delegation is the primary composition primitive
- [[markovian-carryover]] — forward-state mechanism for maintaining continuity across delegation sessions
- Concept: [[agent-onboarding]]
- Concept: [[agentic-oversight]]
- Concept: [[multi-agent-coordination]]


## Open Questions

1. **Optimal delegation granularity**: How fine-grained should delegation be? Too fine creates coordination overhead; too coarse limits parallelism. Is there a theoretical optimal?

2. **Delegation cost-benefit**: When does delegation overhead (serialization, communication, context isolation) exceed the parallelism benefit? This depends on task structure and is not well understood.

3. **Trust and verification**: How much should a delegator trust the delegated result? Full trust risks cascading errors; full verification negates the parallelism benefit. What's the right balance?

4. **Cross-model delegation**: If model capabilities differ, should the delegator use a stronger or weaker model for sub-tasks? Does this create a principal-agent problem where the sub-agent optimizes for its own objectives instead of the delegator's?

## Limitations

- **Context loss**: Each delegation boundary loses some context. Deep delegation chains can lose critical information between levels.
- **Non-determinism**: Same delegation may produce different results depending on child agent's internal state. Hard to reproduce.
- **Overhead**: Delegation has non-trivial overhead (context creation, toolset setup, result serialization). Not worth it for simple tasks.
- **Debugging**: When a delegated task fails, determining whether the failure was in the delegation spec, the sub-agent execution, or the result interpretation is non-trivial.