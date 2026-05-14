---
name: "agentic-planner"
description: "Planning pattern for structurally articulable tasks. Planner defines stages and dependencies upfront; ReAct handles local uncertainty within each step."
---

---
name: "agentic-planner"
description: "Planning pattern for structurally articulable tasks. Use when task stages and dependencies can be defined upfront, with ReAct execution inside each step."
---

# Agentic Planning Pattern

> [!TIP]
> **TL;DR**: Use this pattern when the task structure IS articulable before execution. The planner defines stages and dependencies; ReAct handles local uncertainty within each stage.
> **Key Principle**: "Planning exposes dependencies early and avoids mid-execution surprises."

## Pattern Overview

The **planning pattern** is based on two assumptions:
1. The **major structure of the task can be identified upfront**
2. Defining an **execution roadmap improves downstream reliability**

The agent first creates a plan, then executes it—typically using ReAct for each step to handle local uncertainty.

```
┌──────────────────────────────────────────────────────┐
│                   PLANNING PHASE                      │
│  ┌─────────────────────────────────────────────────┐ │
│  │  Task → Analyze → Identify Stages → Order      │ │
│  │        → Identify Dependencies → Create Plan   │ │
│  └─────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────┘
                          │
                          ▼
┌──────────────────────────────────────────────────────┐
│                  EXECUTION PHASE                      │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐          │
│  │ Stage 1 │───▶│ Stage 2 │───▶│ Stage 3 │          │
│  │ (ReAct) │    │ (ReAct) │    │ (ReAct) │          │
│  └─────────┘    └─────────┘    └─────────┘          │
│       │                                                   │
│       └── ReAct handles local uncertainty at each stage   │
└──────────────────────────────────────────────────────┘
```

## Decision Gate

**When to use**: Apply this pattern when:
- **Question 1** = NO: Solution path is unknown
- **Question 3** = YES: Task structure IS articulable before execution

**Good structure examples**:
- Building a feature: design → implement → test
- Provisioning systems: setup → configure → deploy → verify
- Research report: gather → synthesize → write
- Code review: parse → analyze → comment → resolve

## Two-Phase Design

### Phase 1: Planning

The agent must:
1. **Analyze** the task and identify main stages
2. **Order** stages based on dependencies
3. **Identify** what each stage expects as input
4. **Create** a structured plan with checkpoints

### Phase 2: ReAct Execution

Within each planned stage, use ReAct to:
- Handle local uncertainty
- Make step-by-step decisions
- Adapt to observed results

## Planning vs. ReAct Alone

| Aspect | ReAct Only | Planning + ReAct |
|--------|------------|-----------------|
| Dependency handling | Discovered late | Exposed early |
| Failure detection | After time spent | Before wasted effort |
| Flexibility | High | Medium (plan-aware) |
| Upfront cost | Low | Medium |
| Structure discovery | During execution | Before execution |

## Costs of Planning

Planning has real costs:

| Cost | Impact |
|------|--------|
| Upfront analysis | Extra step before execution |
| Plan quality dependence | Garbage in, garbage out |
| Reduced flexibility | Real-world differs from expectations |

**When NOT to use planning**:
- Structure only becomes clear through interaction
- Real-world conditions differ from expectations
- Tasks are exploratory by nature

## Failure Mode: Plan Abandonment

| Signal | What It Means | Suggested Fix |
|--------|---------------|---------------|
| Plan created but not followed | Execution keeps diverging | Task is less structured than assumed |
| Agent ignores plan steps | Plan quality issue OR agent prefers ReAct | Use lightweight planning + ReAct |
| Dependencies discovered late | Structure wasn't as clear as thought | Add more planning upfront OR switch to ReAct |

### Recommended Fix
```
If planning agent abandons plan → 
  Switch to: "Lightweight Planning + ReAct"
  Define only major stages, let ReAct handle within-stage decisions
```

## AGEM Integration

### Native Tools
- `run_agem_cycle` — Planning phase first, then execution
- `get_graph_topology` — Visualize dependency structure
- `detect_gaps` — Find missing dependencies in plan
- `generate_catalyst_questions` — Question the plan's assumptions

### MCP Server Usage
- **`mcp-logic`** — Prove dependency ordering constraints
- **`verifier-graph`** — Build causal DAG of the plan
- **`sheaf-consistency-enforcer`** — Track plan vs. execution consistency

### Workflow Template
```
1. PLANNING PHASE:
   a. run_agem_cycle with "Analyze task and create execution plan"
   b. List stages with dependencies
   c. Identify checkpoints
   d. Validate plan structure

2. EXECUTION PHASE:
   For each stage in plan order:
   a. Check prerequisites are met
   b. Run ReAct within stage
   c. Validate stage output
   d. Move to next stage or replan

3. ON PLAN ABANDONMENT:
   → Switch to lightweight planning + ReAct
```

## Quick-Start Template

```markdown
## Planning Task Definition

**Task**: [What needs to be done]
**Solution Path**: [UNKNOWN]
**Structure Articulable**: [YES]

### Plan Stages (ordered):
1. [Stage 1] → expects: [X], produces: [Y], depends_on: []
2. [Stage 2] → expects: [Y], produces: [Z], depends_on: [1]
3. [Stage N] → expects: [...], produces: [final], depends_on: [N-1]

### Checkpoints:
- [Validation point after Stage 1]
- [Validation point after Stage 2]

### ReAct Within Stages:
- Stage 1: [ReAct handles X]
- Stage 2: [ReAct handles Y]

### Escalation Triggers:
- [Plan abandoned] → lightweight planning
- [New dependencies found] → replan
```

## Pattern Combinations

| Base Pattern | + Planning | Result |
|--------------|------------|--------|
| ReAct | + Structure upfront | More reliable execution |
| Sequential | + Adaptive steps | Hybrid pattern |
| Multi-Agent | + Stage ownership | Coordinator defines plan, specialists execute |

---

## See Also

- [agentic-react](agentic-react) — Foundation for within-stage execution
- [agentic-sequential](agentic-sequential) — When stages become deterministic
- [agentic-multiagent](agentic-multiagent) — When stages need different specialists