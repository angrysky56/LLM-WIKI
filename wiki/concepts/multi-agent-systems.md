---
summary: Multi-agent LLM systems taxonomy, coordination patterns, and architectural foundations (promoted from stub)
tags: [multi-agent, agents, coordination, agent-architecture]
updated: 2026-05-30T14:04:05Z
---

---
created: 2026-05-25
updated: 2026-09-07T08:10:00Z
type: concept
summary: Multi-agent LLM systems — taxonomy, coordination patterns, and architectural foundations for multiple agents cooperating or competing
tags: [multi-agent, agents, coordination, agent-architecture, tool-use]
sources: [https://arxiv.org/abs/2605.28816, https://arxiv.org/abs/2605.18747]
status: active
confidence: 0.72
---

# Multi-Agent Systems

Multi-agent LLM systems involve multiple autonomous LLM-based agents that interact, cooperate, or compete to solve problems. Unlike single-agent systems where one agent works alone, multi-agent systems introduce coordination overhead, communication protocols, and emergent collective behaviors that are distinct design challenges.

## Definition

A multi-agent LLM system is a collection of LLM-based agents (see [[agents]]), each with its own reasoning engine, memory, and tool access, that coordinate through explicit protocols to accomplish goals that exceed any single agent's capability or knowledge horizon.

Key distinction from single-agent: **agency is distributed**. No single agent has complete information or capability. Success depends on how agents share state, divide labor, and resolve conflicts.

## Taxonomy

### By Coordination Structure

| Structure | Description | Examples |
|-----------|-------------|----------|
| **Sequential delegation** | One agent assigns subtasks to others, waits for results | Chain-of-thought with tool use |
| **Hierarchical** | Manager agent decomposes goals, worker agents execute in parallel | Hermes Kanban pattern |
| **Peer-to-peer** | Agents negotiate directly, no fixed hierarchy | Gamma-World shared world model |
| **Debate/panel** | Multiple agents argue positions, synthesis agent decides | Research council pattern |
| **Market/auction** | Agents bid on tasks, self-organize around incentive signals | Task market systems |

### By Communication Pattern

- **Synchronous**: Agents wait for responses before proceeding (blocking calls)
- **Asynchronous**: Agents post to shared state, others read when ready (message passing)
- **Broadcast**: One agent publishes, all relevant agents receive (event-driven)
- **Contract-net**: Agent publishes task, others bid, owner selects contractor

### By Goal Structure

- **Cooperative**: All agents share the same goal; coordination maximizes collective utility
- **Competitive**: Agents have opposing objectives; coordination manages conflict
- **Mixed-motive**: Shared and opposing incentives coexist (e.g., negotiation scenarios)

## Key Dimensions

### 1. World Model Sharing

When agents operate in a shared environment, they need a **consistent world model** — a shared representation of environment state that all agents can read and update.

**Gamma-World** (NVIDIA, 2026) demonstrates multi-agent video world modeling with permutation-symmetric agent encoding. Agents occupy distinct positions in a shared latent space while maintaining individual identity. This enables real-time 24 FPS multiplayer simulation with linear cross-agent attention cost (instead of quadratic).

Key insight: shared world models prevent agents from acting on contradictory environment state, which is a common failure mode in ad-hoc multi-agent setups.

### 2. Coordination Through Code Artifacts

**Code as Agent Harness** (2026 survey) shows that shared code artifacts become the coordination substrate in production multi-agent systems. When multiple agents operate on the same codebase or share tool definitions encoded as code, the code itself becomes the coordination medium:

- **Code review as verification**: One agent writes code, another reviews it — the review is a tool call
- **Shared execution state**: Code that one agent writes, another can execute and observe
- **Role-specialized agents**: Different agents own different modules; coordination happens through module interfaces

### 3. Communication Protocols

LLM agents communicate through several channels:

- **Direct messaging**: Structured text passed between agent contexts
- **Shared memory**: Agents read/write to a common memory store (see [[bounded-structured-memory]])
- **Tool-mediated**: One agent calls another's tools as if they were environment APIs
- **Artifact/filesystem**: Agents write files that other agents read later

### 4. Conflict Resolution

When agents have conflicting goals or contradictory beliefs about the world:

- **Voting/consensus**: Multiple agents propose, majority wins
- **Authority hierarchy**: Predefined priority ordering resolves conflicts
- **Negotiation**: Agents bargain using explicit utility signals
- ** Arbitration**: A separate "judge" agent resolves disputes

## Relationship to Single-Agent Architecture

Multi-agent systems layer additional complexity on top of single-agent architecture:

| Layer | Single-Agent | Multi-Agent |
|-------|--------------|-------------|
| Reasoning | LLM only | LLM + coordination protocol |
| Memory | Agent-private | Private + shared |
| Tools | Agent-owned | May be shared or exclusive |
| State | Centralized | May be distributed |
| Failure modes | Hallucination, tool misuse | additionally: coordination failure, inconsistent world state, deadlock |

The [[llm-agent-architecture]] pattern addresses single-agent runtime architecture. Multi-agent systems inherit those patterns and add coordination as a new architectural dimension.

## Connections to Existing Pages

- [[agents]] — foundational agent taxonomy
- [[coordination]] — the mechanisms by which agents align their actions
- [[multi-agent-llm-systems]] — related concept page
- [[bounded-structured-memory]] — shared memory as coordination substrate
- [[code-as-agent-harness]] — code artifacts as coordination medium
- [[gamma-world]] — concrete example of shared world modeling
- [[entities/tools/hermes-agent]] — example of agent system with coordination patterns

## Open Questions

- How do multi-agent systems handle **adversarial others** (agents that intentionally mislead)?
- What is the minimal coordination protocol for reliable task decomposition?
- How does agent role specialization emerge vs. being explicitly defined?
- When does adding more agents hurt vs. help (coordination overhead vs. capability scaling)?
