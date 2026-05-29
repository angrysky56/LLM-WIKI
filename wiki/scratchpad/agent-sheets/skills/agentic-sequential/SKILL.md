---
name: "agentic-sequential"
description: "Sequential workflow pattern for deterministic, fixed-path tasks. Use when solution steps are known upfront and follow a stable repeatable sequence."
---

---
name: "agentic-sequential"
description: "Sequential workflow pattern for deterministic, fixed-path agentic tasks. Use when solution steps are known upfront and the process follows a stable, repeatable sequence."
---

# Agentic Sequential Workflow Pattern

> [!TIP]
> **TL;DR**: Use this pattern when the full step-by-step process is known before execution. Best for deterministic workflows like invoice processing, employee onboarding, or data pipelines.
> **Key Principle**: "If the process is deterministic, the agent should execute — not decide."

## Pattern Overview

The **sequential workflow pattern** handles tasks with a **known solution path**. The agent follows explicit steps in order, passing outputs from one stage to the next until completion.

```
┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
│ Step 1  │───▶│ Step 2  │───▶│ Step 3  │───▶│ Step N  │
│ Output  │    │ Output  │    │ Output  │    │ Final   │
└─────────┘    └─────────┘    └─────────┘    └─────────┘
```

## Decision Gate

**When to use**: Apply this pattern when the answer to **Question 1** is YES:
- "Is the solution path known in advance?"

**Good fit examples**:
- Invoice processing: extract fields → validate → store → confirm
- Employee onboarding: create accounts → send welcome email → assign manager → schedule orientation
- Document processing: parse → extract → transform → load

## Critical Design Choice

| What to use | Where to use it |
| ----------- | --------------- |
| **LLM/Agent** | Interpretation, generation, complex decisions |
| **Deterministic code** | Routing, data transformation, storage, validation |

**Rationale**: This separation keeps systems **fast, predictable, and cost-efficient**. The agent handles ambiguity; code handles repetition.

## Failure Mode: Over-Engineering

The main failure signal is **adding ReAct-style reasoning where every step is already defined**.

### ❌ Over-Engineered Example
```
Agent decides: "Now I should validate the email format..."
Agent decides: "Now I should check if the email exists..."
Agent decides: "Now I should send the welcome..."
```

### ✅ Correct Approach
```python
# Deterministic code handles the workflow
for step in ["validate_email", "check_existence", "send_welcome"]:
    execute_step(step)
# Agent only called for steps requiring judgment
if step.requires_ai():
    agent.execute(step)
```

## AGEM Integration

### Native Tools
- `run_agem_cycle` — Execute each step in sequence
- `get_agem_state` — Monitor step completion
- `spawn_agem_agent` — Use specialized agents for steps requiring different reasoning styles

### MCP Server Usage
- **`mcp-logic`** — Prove step dependencies and ordering constraints
- **`sheaf-consistency-enforcer`** — Register each step's output as agent state for consistency tracking

### Workflow Template
```
1. Define ordered step list with clear inputs/outputs
2. For each step:
   a. Check if deterministic → execute with code
   b. Check if requires AI → run_agem_cycle for that step
   c. Validate output before proceeding
3. On edge case failure → escalate to Question 2b pattern
```

## Escalation to Other Patterns

When to **escalate to other patterns**:

| Signal | Next Pattern |
|--------|-------------|
| Steps require external data | → Add Tool Use |
| Edge cases emerge requiring new steps | → → Question 2b (adaptive) |
| Different steps need different reasoning | → → Multi-Agent |

## Quick-Start Template

```markdown
## Sequential Workflow Definition

**Task**: [Task name]
**Path Known**: [YES/NO - if NO, use other pattern]

### Steps (ordered):
1. [Step 1] → expects: [X], produces: [Y]
2. [Step 2] → expects: [Y], produces: [Z]
3. [Step N] → expects: [...], produces: [final]

### AI Steps: [Which steps need agent reasoning]
### Code Steps: [Which steps are deterministic]

### Escalation Triggers:
- [Edge case condition] → escalate to [pattern]
```

---

## See Also

- [agentic-react](agentic-react.md) — For adaptive step-by-step reasoning
- [agentic-planner](wiki/concepts/agentic-planner.md) — For tasks with upfront planning needs
- [agentic-multiagent](agentic-multiagent.md) — For multi-stage tasks with specialization