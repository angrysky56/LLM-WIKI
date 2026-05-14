---
name: "agentic-reflection"
description: "Reflection pattern for quality-critical outputs using generate-critique-refine cycles. Requires clear evaluation criteria and acceptable latency."
---

---
name: "agentic-reflection"
description: "Reflection pattern for quality-critical outputs. Use generate-critique-refine cycles when evaluation criteria are clear and error cost justifies extra latency."
---

# Agentic Reflection Pattern

> [!TIP]
> **TL;DR**: Use this pattern when output quality matters more than response speed, AND evaluation criteria are clear. The agent generates, critiques, and refines until quality thresholds are met.
> **Key Principle**: "Critic independence is critical. If the critic mirrors the generator too closely, it tends to agree rather than evaluate."

## Pattern Overview

The **reflection pattern** is grounded in the expectation that **first-pass outputs are often incomplete or flawed**, and that iterative self-critique and refinement improves final quality enough to justify the added cost.

```
┌─────────────────────────────────────────────────────┐
│              REFLECTION CYCLE                        │
│                                                      │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐         │
│  │ Generate│───▶│ Critique│───▶│ Refine  │         │
│  │ "First │    │ "What's │    │ "Fixed  │         │
│  │ draft" │    │ wrong?" │    │ version"│         │
│  └─────────┘    └─────────┘    └─────────┘         │
│       │              │              │               │
│       ◀──────────────┴──────────────┘               │
│              (iterate until quality met)            │
└─────────────────────────────────────────────────────┘
```

## Decision Gate

**When to use**: Apply this pattern when:
- **Question 4** = YES: Output quality matters more than response speed
- **Question 4** = YES: Clear quality criteria exist for evaluation

**BOTH conditions must be met.**

## Two Required Conditions

### Condition 1: Clear Evaluation Criteria

| Good Criteria | Bad Criteria |
|---------------|--------------|
| "Valid SQL query that returns expected columns" | "Good code" |
| "Contract with all required fields filled" | "Professional document" |
| "Passes linting + unit tests + integration tests" | "Clean output" |
| "Mathematically equivalent to specification" | "Correct answer" |

**Without clear criteria**, the critic produces vague or misleading feedback.

### Condition 2: High Error Cost

| High Error Cost (use reflection) | Low Error Cost (skip reflection) |
|----------------------------------|----------------------------------|
| Deployed production code | Development exploration |
| Client-facing documents | Internal scratchpads |
| Regulatory submissions | Drafts for internal review |
| Financial transactions | High-throughput batch processing |

## Critical Design: Critic Independence

This is the **most important design choice** in reflection patterns:

### ❌ Weak Reflection (Low Independence)
```
Generator: GPT-4
Critic: Same GPT-4, slightly different prompt
→ Tendency: Agree rather than evaluate
→ Result: Minimal improvement, wasted cycles
```

### ✅ Strong Reflection (High Independence)
```
Generator: GPT-4
Critic: Different model (e.g., Claude), OR
        Same model but different framing/context, OR
        Rule-based validator for specific criteria

→ Result: Genuine evaluation, meaningful improvement
```

## Reflection Loop Design

```
MAX_ITERATIONS = 3  # Prevent infinite loops

For iteration in 1..MAX_ITERATIONS:
    1. Generate output
    2. Evaluate against criteria
    3. If PASSED → return output
    4. If FAILED → generate critique
    5. Refine based on critique
    6. Loop

If MAX_ITERATIONS reached without PASS:
    → return best effort OR escalate to human
```

## Failure Modes

### Failure Mode 1: No Improvement

| Signal | Cause | Fix |
|--------|-------|-----|
| Critique cycles don't improve output | Evaluation criteria unclear | Define sharper, verifiable criteria |
| Critique cycles don't improve output | Critic too aligned with generator | Use different model/framing for critic |
| Same errors persist | Critique not actionable | Make critique specific to criteria |

### Failure Mode 2: Infinite Loop

| Signal | Cause | Fix |
|--------|-------|-----|
| Cycles continue without end | No stopping condition | Define max iterations |
| Quality doesn't improve | Criteria not achievable | Revise criteria or accept current state |

### Fix Template
```python
def reflection_loop(generator, critic, criteria, max_iterations=3):
    best_output = None
    best_score = -1
    
    for i in range(max_iterations):
        output = generator.generate()
        score = critic.evaluate(output, criteria)
        
        if score > best_score:
            best_output = output
            best_score = score
        
        if score >= threshold:
            return output  # Quality met
        
        critique = critic.critique(output, criteria)
        generator.refine(critique)
    
    return best_output  # Best effort after max iterations
```

## Reflection Combinations

Reflection adds well to other patterns:

| Base Pattern | + Reflection | Use When |
|--------------|-------------|----------|
| ReAct | + Quality at each step | Quality critical at each stage |
| Planning | + Checkpoint validation | Quality gates between stages |
| Multi-Agent | + Specialist critique | Domain-specific quality checks |

## AGEM Integration

### Native Tools
- `run_agem_cycle` — Generation phase
- `get_cohomology` — Check generator/critic alignment (should be LOW for independence)
- `spawn_agem_agent` — Spawn independent critic agent

### MCP Server Usage
- **`advanced-reasoning`** — Deep critique reasoning
- **`mcp-logic`** — Formal verification of generated outputs
- **`hipai-montague`** — Track belief evolution through refinement
- **`conscience-servitor`** — Ethical evaluation for sensitive outputs

### Workflow Template
```
1. Define quality criteria (must be verifiable)
2. Set max reflection iterations (typically 2-3)
3. Initialize generator and critic (ensure independence)
4. LOOP:
   a. Generate output
   b. Evaluate against criteria
   c. If PASSED → return
   d. If FAILED → critique
   e. Refine generator based on critique
   f. If max iterations → return best effort
```

## Quick-Start Template

```markdown
## Reflection Task Definition

**Task**: [What needs to be generated]
**Quality Matters**: [YES/NO]
**Speed Matters**: [YES/NO - if YES, don't use reflection]
**Latency Acceptable**: [YES/NO]

### Quality Criteria (verifiable):
1. [Criterion 1] - [how to verify]
2. [Criterion 2] - [how to verify]
3. [Criterion N] - [how to verify]

### Generator: [model/prompt]
### Critic: [different model/framing for independence]

### Max Iterations: [N]
### Pass Threshold: [score/value]

### Escalation Triggers:
- [Max iterations reached] → human review OR accept best effort
- [Criteria impossible to meet] → revise criteria
```

## Decision Summary

| Question | Answer | Use Reflection? |
|----------|--------|----------------|
| Quality matters more than speed? | YES | ✓ |
| Clear evaluation criteria exist? | YES | ✓ |
| Both conditions met? | YES | → Use Reflection |
| Either condition NO? | NO | → Skip Reflection |

---

## See Also

- [agentic-react](agentic-react) — Often the generator's base pattern
- [agentic-planner](agentic-planner) — Checkpoint reflection between stages
- [agentic-multiagent](agentic-multiagent) — Specialist critics for domain quality