---
name: "agentic-decision-tree"
description: "Master orchestrator for the five-question decision tree that selects the right agentic pattern from Sequential, ReAct, Planning, Reflection, or Multi-Agent."
---

---
name: "agentic-decision-tree"
description: "Master orchestrator skill for the five-question decision tree that selects the right agentic pattern. Use when beginning any new agentic task to determine optimal starting pattern."
---

# Agentic Design Pattern Decision Tree

> [!TIP]
> **TL;DR**: Use this skill to select the right agentic pattern for any task. Work through five questions in order to narrow down from four destination patterns.
> **Key Principle**: "Questions 1-4 build up; Question 5 is a gate that should only be considered after all previous questions are evaluated."

## Pattern Overview

The **decision tree** maps concrete task properties to the most appropriate starting pattern through five sequential questions:

```
                        ┌─────────────────────┐
                        │  Q1: Solution path   │
                        │  known in advance?  │
                        └─────────┬───────────┘
                                  │
                    ┌─────────────┴─────────────┐
                    ▼                           ▼
              YES: Fixed                   NO: Unknown
             ┌────────┐                    ┌────────┐
             │ Q2a:   │                    │ Q2b:   │
             │ Fixed? │                    │ Tools? │
             └────┬───┘                    └───┬────┘
                  │                          │
                  ▼                          ▼
         SEQUENTIAL                  YES: (assumed)
         WORKFLOW                     ┌────────┐
                                     │ Q3:    │
                                     │Struct? │
                                     └───┬────┘
                                         │
                               ┌─────────┴─────────┐
                               ▼                   ▼
                          YES:                    NO:
                          PLANNING              ReAct
                          +ReAct                (skip Q4)
                          │
                          ▼
                    Q4: Quality
                    matters?
                    │
            ┌─────────┴─────────┐
            ▼                   ▼
        YES:                  NO:
        + Reflection          Q5
        │
        ▼
      Q5: Scale/Specialization?
      │
      │
┌─────┴─────┐
▼           ▼
YES:        NO:
MULTI       Final
AGENT       Pattern
```

## The Five Questions

### Question 1: Is the Solution Path Known in Advance?

**This separates fixed workflows from adaptive ones.**

| Known Solution Path | Unknown Solution Path |
|---------------------|----------------------|
| Full steps defined upfront | Each step depends on previous outputs |
| Same process every time | Task branches based on context |
| Deterministic flow | Exploratory/adaptive |

**Examples of known paths**:
- Invoice processing: extract → validate → store → confirm
- Employee onboarding: create accounts → send welcome → assign manager → schedule orientation

**Examples of unknown paths**:
- Research tasks following new evidence
- Customer support branching based on user input
- Debugging shifting hypotheses based on results

**If known → go to Q2a**
**If unknown → go to Q2b**

---

### Question 2a: Is This a Fixed Workflow?

**For known solution paths only.**

If the path is stable and predictable, use **Sequential Workflow Pattern**.

**When SEQUENTIAL is correct**:
- Steps never change
- No branching logic
- Deterministic execution

**When to escalate**:
- Workflow breaks on edge cases
- Requires new steps not originally defined
- → Escalate to Q2b (adaptive path)

---

### Question 2b: Does the Task Require Tool Access or External Information?

**For unknown solution paths.**

The answer is **almost always YES**. Almost all real-world tasks need:
- Current information
- External state
- System-level actions

**If YES (assumed) → go to Q3**

**If NO (genuinely self-contained task)**:
- Pure reasoning or generation
- No external data needed
- → Consider lightweight ReAct only

---

### Question 3: Is the Task Structure Articulable Before Execution?

**This separates Planning from ReAct.**

| Structurally Articulable | NOT Structurally Articulable |
|--------------------------|------------------------------|
| Can break into ordered subtasks | Structure only emerges through interaction |
| Dependencies knowable upfront | Dependencies discovered during execution |
| Stages and sequence are clear | Steps not predictable |

**Examples of articulable structure**:
- Building a feature: design → implement → test
- Research report: gather → synthesize → write
- System provisioning: setup → configure → deploy → verify

**If YES → use PLANNING + ReAct (inside steps)**
**If NO → use ReAct (structure emerges during execution) → go to Q4**

---

### Question 4: Does Output Quality Matter More Than Response Speed?

**This introduces the Reflection pattern.**

**Reflection is useful when BOTH conditions are met**:
1. Clear quality criteria exist for evaluation
2. Error cost is high enough to justify extra pass

**Clear criteria examples**:
- Valid SQL query with expected columns
- Contract with all required fields
- Code passing linting + unit tests + integration tests

**High error cost examples**:
- Deployed production code
- Client-facing documents
- Regulatory submissions
- Financial transactions

**Low error cost (skip reflection)**:
- Development exploration
- Internal drafts
- High-throughput processing where latency matters

**If YES (both conditions met) → add REFLECTION**
**If NO → go to Q5**

---

### Question 5: Does the Task Have a Specialization or Scale Problem?

**This decides whether to use Multi-Agent.**

**This question should ONLY be considered after Q1-Q4.**

### Specialization Trigger

Clear domain boundaries needing different reasoning:
- Legal review (formal, precise)
- Financial modeling (numeric, analytical)
- Security auditing (adversarial, cautious)
- Code generation (technical, systematic)

### Scale Trigger

| Problem | Single Agent Issue | Multi-Agent Solution |
|---------|-------------------|---------------------|
| Context overflow | Task too large for window | Split across agents |
| Serial bottleneck | Sequential steps too slow | Parallel execution |
| Rate limiting | API limits slow processing | Distribute load |

**If YES → use MULTI-AGENT**
**If NO → SINGLE AGENT with appropriate pattern is sufficient**

---

## Pattern Destination Summary

| Path | Destination Pattern | When |
|------|-------------------|------|
| Q1 NO, Q2b YES, Q3 NO, Q4 NO, Q5 NO | Single Agent + Tools + ReAct | Unknown path, emergent structure, speed OK |
| Q1 NO, Q2b YES, Q3 YES, Q4 NO, Q5 NO | Planning + ReAct | Known structure, adaptive execution |
| Q1 NO/QYES, Q2b YES, Q3 ANY, Q4 YES, Q5 NO | + Reflection | Quality critical |
| Q1 NO, Q2b YES, Q3 ANY, Q4 ANY, Q5 YES | Multi-Agent Specialist | Specialization OR scale needs |

## Decision Matrix

| Criteria | Sequential | ReAct | Planning | Reflection | Multi-Agent |
|----------|------------|-------|----------|-----------|-------------|
| **Path known** | ✓ | ✗ | ✗ | depends | depends |
| **Structure articulable** | N/A | ✗ | ✓ | depends | depends |
| **Tools needed** | optional | ✓ | ✓ | depends | depends |
| **Quality critical** | ✗ | ✗ | ✗ | ✓ | depends |
| **Specialization** | ✗ | ✗ | ✗ | ✗ | ✓ |
| **Scale** | ✗ | ✗ | ✗ | ✗ | ✓ |

## Failure Mode Quick Reference

| Signal | Means | Fix |
|--------|-------|-----|
| ReAct loops excessively | Agent uncertain about progress | Add planning, better tools, clearer stop |
| Planning agent abandons plan | Task less structured than assumed | Lightweight planning + ReAct |
| Reflection not improving | Criteria unclear OR critic aligned | Sharpen criteria OR independent critic |
| Multi-agent routing failures | Wrong specialist OR bad integration | Deterministic routing for predictable cases |

## AGEM Integration for Pattern Selection

### Using AGEM for Decision Support

```python
# Decision tree implementation
def select_pattern(task_requirements):
    # Q1: Solution path known?
    if task_requirements.path_known:
        return sequential_workflow(task_requirements)
    
    # Q2b: Tool access needed?
    if not task_requirements.self_contained:
        # Q3: Structure articulable?
        if task_requirements.structure_known:
            pattern = planning_agent(task_requirements)
        else:
            pattern = react_agent(task_requirements)
        
        # Q4: Quality matters?
        if task_requirements.quality_critical:
            pattern = add_reflection(pattern)
        
        # Q5: Specialization or scale?
        if task_requirements.specialization_needed or task_requirements.scale_needed:
            pattern = multi_agent_system(pattern)
        
        return pattern
```

### AGEM Native Tool Usage

| Decision Point | AGEM Tool | Purpose |
|----------------|----------|---------|
| Initial analysis | `run_agem_cycle` | Analyze task requirements |
| Pattern consistency | `get_cohomology` | Verify pattern selection is coherent |
| Gap detection | `detect_gaps` | Find missing considerations |
| Multi-agent decision | `spawn_agem_agent` | Get perspective on pattern choice |

---

## Quick-Start: Pattern Selection Checklist

```markdown
## Pattern Selection for: [Task Name]

### Q1: Solution Path
- [ ] Known (use Sequential if NO other issues)
- [x] Unknown (continue)

### Q2b: Tool Access
- [x] YES - tools required (almost always)
- [ ] NO - self-contained task

### Q3: Structure
- [ ] YES - articulable (Planning + ReAct)
- [x] NO - emerges during execution (ReAct only)

### Q4: Quality
- [ ] YES - clear criteria + high error cost (+ Reflection)
- [x] NO - speed OK or criteria unclear

### Q5: Scale/Specialization
- [ ] YES - clear trigger (Multi-Agent)
- [x] NO - single agent sufficient

### SELECTED PATTERN: [agentic-react]
### WITH OPTIONS: [+reflection if Q4 yes, +multiagent if Q5 yes]
```

---

## See Also

Individual pattern skills:
- [agentic-sequential](agentic-sequential) — Fixed workflow pattern
- [agentic-react](agentic-react) — Adaptive step-by-step
- [agentic-planner](agentic-planner) — Upfront planning
- [agentic-reflection](agentic-reflection) — Quality loops
- [agentic-multiagent](agentic-multiagent) — Specialist systems
- [agentic-tooluse](agentic-tooluse) — Foundation layer