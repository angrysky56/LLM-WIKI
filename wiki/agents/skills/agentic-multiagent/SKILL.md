---
name: "agentic-multiagent"
description: "Multi-agent pattern for tasks requiring specialization or scale beyond single-agent capacity. Covers topology, routing, and coordination design."
---

---
name: "agentic-multiagent"
description: "Multi-agent pattern for tasks requiring specialization or scale beyond single-agent capacity. Use when task decomposition, parallel execution, or domain expertise provides clear benefits."
---

# Agentic Multi-Agent Pattern

> [!TIP]
> **TL;DR**: Use this pattern ONLY when clear specialization or scale problems exist that a single agent can't handle. Multi-agent adds coordination overhead—only use when benefits outweigh costs.
> **Key Principle**: "The trigger for multi-agent use should be a clear bottleneck that specialization or scale actually solves, not architectural preference."

## Pattern Overview

**Multi-agent systems** operate on the belief that a task benefits from **decomposition into specialized roles**, where parallel or modular execution outweighs the overhead of coordination.

Multi-agent systems are useful when:
- Tasks are too large for a single context window
- Different stages require different reasoning styles
- Parallel execution reduces overall time

```
┌─────────────────────────────────────────────────────────┐
│                   MULTI-AGENT TOPOLOGY                    │
│                                                          │
│  ┌─────────────┐                                        │
│  │ Coordinator │  (Task routing, orchestration)          │
│  └──────┬──────┘                                        │
│         │                                                 │
│    ┌────┴────┬────────────┐                             │
│    ▼         ▼            ▼                             │
│ ┌──────┐ ┌────────┐ ┌──────────┐                        │
│ │ Spec │ │ Spec B │ │ Spec C  │  (Parallel execution)   │
│ │  A   │ │        │ │          │                        │
│ └──────┘ └────────┘ └──────────┘                        │
│    │         │            │                             │
│    └─────────┴────────────┘                             │
│              │                                          │
│              ▼                                           │
│         [Result Aggregation / Synthesis]                 │
└─────────────────────────────────────────────────────────┘
```

## Decision Gate

**When to use**: Apply this pattern when:
- **Question 5** = YES: Task has specialization OR scale problem that one agent can't handle

**BOTH specialization AND scale must be evaluated first** using Questions 1-4.

## Two Core Triggers

### Trigger 1: Specialization Needs

| Task Component | Reasoning Style | Specialist Agent |
|----------------|----------------|------------------|
| Legal review | Formal, precise | Legal Specialist |
| Financial modeling | Numeric, analytical | Finance Specialist |
| Security auditing | Adversarial, cautious | Security Specialist |
| Code generation | Technical, systematic | Dev Specialist |
| Creative writing | Open, generative | Creative Specialist |

**Signal**: Clear domain boundaries in the task that need different reasoning styles.

### Trigger 2: Scale Problems

| Problem | Single Agent Issue | Multi-Agent Solution |
|---------|-------------------|---------------------|
| Context overflow | Task too large for window | Split across agents |
| Serial bottleneck | Sequential steps take too long | Parallel execution |
| Rate limiting | API limits slow processing | Distribute load |

**Signal**: Task CANNOT fit into one agent's capacity.

## Three Key Design Choices

### 1. Task Ownership

Who owns each task component?

| Option | When to Use | Example |
|--------|-------------|---------|
| **Dedicated specialist** | Clear domain expertise needed | Legal agent owns contract review |
| **Pooled workers** | Many similar subtasks | Multiple crawler agents |
| **Hierarchical** | Tasks have natural parent-child | Manager → Workers |

### 2. Routing Logic

How are tasks assigned to agents?

| Option | When to Use | Example |
|--------|-------------|---------|
| **Deterministic rules** | Predictable task types | If code → Dev Agent |
| **LLM routing** | Ambiguous task types | Router decides based on content |
| **Self-selection** | Agents know their capabilities | Agent claims suitable tasks |
| **Central coordinator** | Complex orchestration needs | Coordinator dispatches |

### 3. Topology

How do agents interact?

| Topology | Structure | Best For |
|----------|-----------|----------|
| **Sequential** | Output of A → Input of B | Pipeline dependencies |
| **Parallel** | All agents work simultaneously | Independent subtasks |
| **Debate** | Agents argue positions | Diverse perspectives |
| **Hierarchical** | Manager → Subordinates | Nested complexity |

```
Sequential:      Parallel:        Debate:

[Agent A]        ┌───────┐       [Agent A]
    │           │ Agent │       ↙      ↘
[Agent B]        ├───────┤      [Arbiter]
    │           │ Agent │       ↘      ↙
[Agent C]        ├───────┤       [Agent B]
               └───────┘
```

## Costs of Multi-Agent

Multi-agent systems add significant overhead:

| Cost | Impact |
|------|--------|
| **Coordination complexity** | Who assigns tasks? Who resolves conflicts? |
| **Shared state management** | How do agents share context? |
| **Failure propagation** | One agent failure can cascade |
| **Communication overhead** | Extra latency for messaging |
| **Debugging difficulty** | Harder to trace execution paths |

**Rule**: If a single strong agent can handle the task, use one. The overhead of multiple agents outweighs the benefit.

## Failure Modes

### Failure Mode 1: Routing Failures

| Signal | Cause | Fix |
|--------|-------|-----|
| Wrong specialist selection | Routing logic issue | Use deterministic rules for predictable cases |
| Outputs don't combine well | Integration problem | Define clear output contracts |
| Deadlock | Circular dependencies | Add timeout + fallback |

### Fix Template
```
If routing failures → 
  Analyze: Is routing deterministic? YES → debug rules
                           NO → consider deterministic routing
```

### Failure Mode 2: Coordination Overhead

| Signal | Cause | Fix |
|--------|-------|-----|
| Slower than single agent | Too much coordination | Reduce agent count OR simplify topology |
| Complex state sharing | Shared state management | Use structured state with clear ownership |

## AGEM Integration

### Native Tools
- `spawn_agem_agent` — Create specialist agents with personas
- `get_cohomology` — Check cross-agent consistency (H¹ should be 0)
- `sheaf-consistency-enforcer` — Cross-agent state management
- `reset_agem_engine` — Clean state between runs

### MCP Server Usage
- **`sheaf-consistency-enforcer`** — **Critical**: Track state consistency across agents
- **`hipai-montague`** — Belief tracking per agent
- **`verifier-graph`** — Build causal chains across agent outputs
- **`conscience-servitor`** — Ethical evaluation of combined decisions

### Workflow Template
```
1. DECOMPOSE:
   a. Identify specialization boundaries
   b. Identify scale bottlenecks
   c. Define task ownership

2. ARCHITECT:
   a. Choose topology (sequential/parallel/debate)
   b. Define routing logic
   c. Define output contracts

3. EXECUTE:
   a. Spawn specialist agents
   b. Register each in sheaf-consistency-enforcer
   c. Route tasks per logic
   d. Aggregate results

4. VALIDATE:
   a. Check H¹ = 0 (agreement across agents)
   b. If H¹ > 0 → spawn_agem_agent for resolution
   c. Verify combined output quality
```

## Quick-Start Template

```markdown
## Multi-Agent Task Definition

**Task**: [What needs to be done]
**Specialization Triggers**:
  - [Domain boundary 1] → [Specialist A]
  - [Domain boundary 2] → [Specialist B]

**Scale Triggers**:
  - [Bottleneck] → [Solution]

### Topology: [sequential/parallel/debate/hierarchical]
### Routing Logic: [deterministic/LLM/self-select/coordinator]

### Agents:
┌─────────────────┬────────────────┬─────────────────┐
│ Specialist A    │ [Persona]      │ [Tasks owned]   │
├─────────────────┼────────────────┼─────────────────┤
│ Specialist B    │ [Persona]      │ [Tasks owned]   │
└─────────────────┴────────────────┴─────────────────┘

### Output Contracts:
  - Specialist A → produces: [X], format: [Y]
  - Specialist B → produces: [Z], format: [W]

### State Management:
  - Shared state: [what's shared, how]
  - Agent-local state: [what's private]

### Failure Handling:
  - Agent failure: [fallback strategy]
  - Routing failure: [fallback strategy]
  - Consensus failure (H¹ > 0): [resolution strategy]
```

## AGEM Spawn Patterns

For different topologies:

```python
# Parallel specialists (debate-style)
spawn_agem_agent(persona="Advocate") # Argues position A
spawn_agem_agent(persona="Challenger") # Argues position B
spawn_agem_agent(persona="Arbiter")    # Resolves debate

# Sequential pipeline
spawn_agem_agent(persona="Collector")  # Gathers data
spawn_agem_agent(persona="Analyzer")   # Processes data
spawn_agem_agent(persona="Reporter")    # Generates output

# Hierarchical
spawn_agem_agent(persona="Manager")     # Coordinates
spawn_agem_agent(persona="Worker_A")    # Subordinate
spawn_agem_agent(persona="Worker_B")    # Subordinate
```

## Decision Summary

| Question | Answer | Use Multi-Agent? |
|----------|--------|------------------|
| Questions 1-4 resolved? | YES | Required before considering multi-agent |
| Clear specialization need? | YES | ✓ Consider |
| Clear scale need? | YES | ✓ Consider |
| Either trigger present? | YES | → Use Multi-Agent |
| No clear trigger? | NO | → Single agent sufficient |

---

## See Also

- [agentic-sequential](agentic-sequential) — For pipeline-style decomposition
- [agentic-react](agentic-react) — Each specialist may use ReAct
- [agentic-planner](agentic-planner) — Coordinator may use planning
- [agentic-reflection](agentic-reflection) — Specialists may use reflection for quality