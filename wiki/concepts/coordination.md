---
summary: Coordination mechanisms for multi-agent LLM systems — alignment, protocols, and shared state (promoted from stub)
tags: [coordination, multi-agent, agents, communication]
updated: 2026-05-30T14:04:40Z
---

---
created: 2026-05-25
updated: 2026-09-07T08:10:00Z
type: concept
summary: Coordination in multi-agent LLM systems — alignment mechanisms, protocols, and the problem of getting distributed agents to act coherently
tags: [coordination, multi-agent, agents, communication, protocol-design]
sources: [https://arxiv.org/abs/2605.28816, https://arxiv.org/abs/2605.18747]
status: active
confidence: 0.72
---

# Coordination

Coordination is the problem of aligning the actions and beliefs of multiple agents so that the collective achieves something none could accomplish alone. In multi-agent LLM systems, coordination is a first-class architectural challenge — agents are autonomous, potentially heterogeneous, and often operating with partial information about the world and about each other.

## The Coordination Problem

Coordination fails in predictable ways:

- **Inconsistent world state**: Agents act on different beliefs about environment state
- **Goal conflicts**: Agents have misaligned objectives that aren't explicitly managed
- **Underspecified interfaces**: Tool boundaries and message formats are ambiguous
- **Silent failures**: One agent fails, others don't notice, system produces wrong output
- **Deadlock**: Agents wait on each other indefinitely

These are the same problems studied in distributed systems for decades, but LLM agents add a new dimension: **natural language as the coordination medium**. Unlike rigid API contracts, LLM-generated messages are stochastic and can introduce ambiguity at every coordination point.

## Mechanisms

### 1. Shared World State

The most basic coordination mechanism is a **consistent shared representation** of what the world looks like. When agents operate in an environment (codebase, filesystem, game world), they need agreement on:

- Current environment state
- Who has taken what actions
- What the goal state looks like

**Gamma-World** (NVIDIA, 2026) provides permutation-symmetric multi-agent world modeling — a shared video world model where agents occupy distinct positions but share a common latent representation. This is the strongest form of coordination: agents literally agree on what the world is.

More practical: shared memory stores (see [[bounded-structured-memory]]) where agents write observations and read each other's state updates.

### 2. Explicit Protocols

Coordination protocols define the rules of interaction:

| Protocol | When to Use | Failure Mode |
|----------|-------------|--------------|
| **Request-response** | One agent needs a specific answer | Timeout, wrong response |
| **Broadcast** | All agents need the same information | Uneven reception |
| **Contract-net** | Task allocation among agents | Underspecified bids |
| **Blackboard** | Shared problem-solving space | Conflicting writes |
| **Token-passing** | Sequential access to a resource | Bottleneck |

### 3. Code as Coordination Medium

The **Code as Agent Harness** (2026) pattern shows that shared code artifacts become coordination infrastructure. When agents operate on the same codebase:

- Code reviews serve as verification gates
- Tool definitions encoded as code are self-documenting and executable
- Module boundaries create natural agent specializations

This is more robust than natural language coordination because code is executable and has formal semantics. Ambiguity in tool definitions becomes a runtime error rather than a silent misalignment.

### 4. Hierarchical Decomposition

Large tasks decompose into subtasks assigned to specialized agents. The decomposition must be:

- **Complete**: All necessary subtasks are identified
- **Non-overlapping**: Subtasks don't conflict or duplicate effort
- **Well-typed**: Each subtask's inputs/outputs are specified

The Hermes Kanban pattern uses a manager agent that owns goal decomposition and delegates to worker agents — a form of hierarchical coordination.

## Coordination vs. Collaboration

**Coordination** ≠ **Collaboration**:

- **Coordination**: Aligning actions to avoid conflict or exploit synergies, even if agents have different goals
- **Collaboration**: Agents actively working together toward a shared goal, sharing credit and cost

A traffic intersection is coordinated (cars don't collide) but not collaborative. A research team is both coordinated (role assignments) and collaborative (shared publication).

Multi-agent systems often need both. See [[multi-agent-systems]] for the broader taxonomy.

## Connection to Existing Pages

- [[multi-agent-systems]] — the broader context for multi-agent coordination
- [[agents]] — foundational agent definition
- [[bounded-structured-memory]] — shared memory as coordination infrastructure
- [[code-as-agent-harness]] — code artifacts as coordination medium
- [[distributed-systems]] — traditional coordination theory; some patterns transfer
- [[gamma-world]] — concrete shared world model example

## Open Questions

- Natural language coordination is ambiguous; when is it acceptable vs. when do agents need formal contracts?
- How do you detect coordination failure before it causes wrong outputs?
- What's the minimal coordination protocol that achieves reliable task decomposition?
