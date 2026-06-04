---
summary: Gate protocol for onboarding new agents into a system
tags: [agentic-ai, onboarding, multi-agent, safety]
updated: 2026-05-28T00:25:05Z
---

---
created: 2026-05-27
updated: 2026-08-10T06:00:00Z
type: concept
summary: Gate protocol for onboarding new agents into a system — capability verification, safety constraints, and trust bootstrapping
tags: ['agentic-ai', 'onboarding', 'multi-agent', 'safety']
sources: 
status: active
confidence: 0.7
---

# Agent Onboarding

Agent onboarding is the gate protocol for introducing a new agent (whether AI or human) into a running system. The onboarding process must verify the agent's capabilities, establish safety constraints, and bootstrap trust before granting access to system resources.

## The Onboarding Problem

When a new agent enters a system, several risks emerge:
- **Capability mismatch**: The agent claims capabilities it doesn't have
- **Safety blind spots**: The agent doesn't understand system-specific safety constraints
- **Trust deficit**: Existing agents don't know what the new agent will do
- **Coordination disruption**: Uncoordinated onboarding disrupts existing agent workflows

The onboarding protocol solves these by providing a structured, verifiable introduction.

## Components of Agent Onboarding

### 1. Capability Verification
Before onboarding, the system must verify the agent's stated capabilities. For AI agents, this typically means:
- Running capability benchmarks (e.g., [[swe-bench]] for coding agents)
- Testing safety-relevant behaviors in a sandbox
- Verifying tool access patterns

For human agents, this might mean authentication, training completion, or certification.

### 2. Safety Constraint Injection
The agent must learn the system's safety rules. This includes:
- **Capability bounds**: What the agent can and cannot do
- **Escalation protocols**: When to defer to human operators
- **Information barriers**: What the agent can and cannot access
- **Constitutional constraints**: The principles governing agent behavior (cf. [[constitutional-ai]])

In the Hermes framework, safety constraints are injected via the agent's soul configuration and the `constrained` flag in `delegate_task`.

### 3. Trust Bootstrap
Existing agents need a trust model for the new agent. Onboarding establishes:
- **Identity**: How to identify and reference the new agent
- **Role**: What function the agent serves in the system
- **Authority**: What decisions the agent can make autonomously
- **Audit trail**: What actions the agent takes (for accountability)

### 4. Resource Allocation
The agent needs access to resources (context, tools, memory) to function. Onboarding allocates:
- **Context budget**: Maximum context window the agent can use
- **Tool access**: Which tools the agent can invoke
- **Memory access**: Which memory systems the agent can read/write
- **Delegation rights**: Whether the agent can spawn sub-agents

## The Hermes Onboarding Flow

In the Hermes framework (per `hermes-agent` architecture):
1. **Spawn**: `delegate_task()` creates the agent with `constrained` flag
2. **Soul injection**: Agent reads its soul.md for identity and principles
3. **Capability test**: Agent runs a capability probe (e.g., "solve this benchmark problem")
4. **Constraint acceptance**: Agent confirms understanding of safety constraints
5. **Active state**: Agent joins the agent pool and can receive tasks

## Open Questions

- **Onboarding scalability**: How do you onboard 100+ agents without bottlenecking on a single orchestrator?
- **Dynamic re-onboarding**: When an agent's capabilities change (upgrade/downgrade), does onboarding need to repeat?
- **Cross-system onboarding**: When agents move between systems, does prior onboarding transfer?

## Connections
- [[concepts/swe-bench]]
- [[concepts/agent-leak-benchmark]]
- [[concepts/delegation]]
- [[research/index]]
- [[concepts/agentic-hierarchy]]
- [[concepts/agent-onboarding]]
- [[concepts/domain-onboarding-standards]]
- [[concepts/adversarial-training]]
- [[concepts/constitutional-ai]]
- [[wiki/index]]
- [[concepts/llm-training]]
- [[agents/skills/librarian-agent/skill]]
- [[log]]
- [[scratchpad/agent-sheets/librarian/carryover]]
- [[concepts/agent-onboarding]]
- [[entities/projects/project-synapse]] — the underlying MCP framework for agent onboarding infrastructure

- [[delegation]] — the mechanism for assigning tasks to agents
- [[agentic-hierarchy]] — the structure of agent relationships
- [[project-synapse]] — the underlying MCP framework
- [[constitutional-ai]] — the constraint framework for agent behavior
- [[agent-leak-benchmark]] — measuring information leakage during onboarding
- Concept: [[adversarial-training]]

- [[llm-training]]