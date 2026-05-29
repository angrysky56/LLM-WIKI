---
name: "hierarchical-supervisor"
description: "Hierarchical supervisor pattern: Multi-level supervisor chains."
---

---
name: "hierarchical-supervisor"
description: "Hierarchical supervisor pattern: Multi-level supervisor chains where supervisors delegate to supervisors who delegate to workers."
---

# Hierarchical Supervisor Pattern

> [!IMPORTANT]
> **When to use**: When you need multiple levels of supervisory control — a supervisor delegates to supervisors who manage worker agents.

## Decision Tree Path

```
Does the task require multiple specialized capabilities?
├── YES
│   └── Do you need multiple levels of supervisory control?
│       ├── YES → Hierarchical Supervisor (you're here)
│       └── NO, single level of control?
│           ├── YES, centralized routing?
│           │   └── YES → supervisor-delegation
│           └── YES, orchestrator control?
│               └── YES → supervisor-orchestrator
└── NO → single-agent
```

## When to Choose

| ✅ Use Hierarchical When | ❌ Avoid When |
|--------------------------|---------------|
| Large organization-scale tasks | Simple routing with fixed paths |
| Clear domain/team boundaries needing management | Shallow task decomposition |
| Middle managers needed for domain expertise | Single supervisor suffices |
| Coordination at multiple abstraction levels | Overhead exceeds benefit |

## Use Cases

- **Enterprise automation** (VP → Manager → Team Lead → Worker)
- **Multi-domain research** (Research Director → Domain Leads → Specialists)
- **Complex manufacturing** (Plant Manager → Line Supervisors → Workers)
- **Large-scale content production** (Editor → Section Editors → Writers)

## Example Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Executive Supervisor                  │
│              (High-level task understanding)            │
└─────────────────────────────┬───────────────────────────┘
                              │
         ┌───────────────────┼───────────────────┐
         ▼                   ▼                   ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│  Domain Lead A  │ │  Domain Lead B  │ │  Domain Lead C  │
│ (Technical Mgmt)│ │ (Creative Mgmt) │ │ (Legal Mgmt)    │
└────────┬────────┘ └────────┬────────┘ └────────┬────────┘
         │                   │                   │
    ┌────┴────┐        ┌────┴────┐        ┌────┴────┐
    ▼    ▼    ▼        ▼    ▼    ▼        ▼    ▼    ▼
┌──── ┌──── ┌──── ┌──── ┌──── ┌──── ┌──── ┌──── ┌────
│Wrkr │Wrkr │Wrkr │Wrkr │Wrkr │Wrkr │Wrkr │Wrkr │Wrkr
└──── └──── └──── └──── └──── └──── └──── └──── └────
```

## Level Definitions

| Level | Role | Responsibility |
|-------|------|----------------|
| **Executive** | Task interpretation | Convert user request to domain tasks |
| **Domain Lead** | Domain coordination | Manage specialists within domain |
| **Specialist** | Execution | Perform actual work |

## Key Considerations

### Include in Your Decision

1. **Level count** — How many levels truly needed? (Prefer ≤3)
2. **Handoff clarity** — Clear contracts between levels
3. **Information loss** — Does context survive multi-level handoffs?
4. **Latency** — Each level adds latency

### Design Principles

| Principle | Why It Matters |
|-----------|----------------|
| **3 levels max** | More adds latency, loses context |
| **Semantic handoffs** | Each level adds its own interpretation |
| **Clear domain boundaries** | Reduces cross-level confusion |
| **Aggregated feedback** | Lower levels report up; upper levels synthesize |

## Anti-Patterns

| Mistake | Why It's Bad |
|---------|--------------|
| Too many levels | Context collapse, latency explosion |
| Unclear level responsibilities | Work falls through cracks |
| Top does work | Middle management is overhead |
| Bottom reports directly to top | Bypasses domain expertise |

## Scaling Down

```
Is hierarchy actually simpler than expected?
├── NO, just single level routing?
│   └── YES → supervisor-delegation
├── NO, just orchestration control?
│   └── YES → supervisor-orchestrator
└── Task is embarrassingly parallel?
    └── YES → parallel-execution
```

## Quick Reference

| Factor | Hierarchical Supervisor |
|--------|--------------------------|
| **Latency** | Highest (multiple levels) |
| **Cost** | Highest (multiple supervisors) |
| **Complexity** | Very High |
| **Reliability** | Distributed; domain leads isolate failures |
| **Best for** | Large-scale multi-domain tasks |

---

*Pattern ID: `hierarchical-supervisor` | AGEM-compatible*