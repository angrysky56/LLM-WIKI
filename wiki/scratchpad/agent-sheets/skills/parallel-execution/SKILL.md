---
name: "parallel-execution"
description: "Parallel execution pattern: Multiple agents work simultaneously on independent sub-tasks."
---

---
name: "parallel-execution"
description: "Parallel execution pattern: Multiple agents work simultaneously on independent sub-tasks. Best for embarrassingly parallel workloads."
---

# Parallel Execution Pattern

> [!IMPORTANT]
> **When to use**: When sub-tasks are independent and can be executed simultaneously. Maximizes throughput for parallelizable workloads.

## Decision Tree Path

```
Does the task require multiple specialized capabilities?
├── YES
│   └── Are subtasks independent (no shared state/collaboration)?
│       ├── YES → Parallel Execution (you're here)
│       └── NO, need shared context?
│           └── YES → supervisor-orchestrator
└── NO → single-agent
```

## When to Choose

| ✅ Use Parallel When | ❌ Avoid When |
|----------------------|---------------|
| Subtasks are truly independent | Subtasks share state/artifacts |
| You need maximum throughput | Order dependency exists |
| Each subtask is self-contained | Errors in one affect others |
| Subtasks are embarrassingly parallel | Result synthesis is complex |

## Use Cases

- **Batch document processing** (N docs, each processed independently)
- **A/B content generation** (multiple variants simultaneously)
- **Multi-source research** (search multiple sources at once)
- **Grid of evaluations** (test N configurations in parallel)
- **User research synthesis** (analyze N surveys simultaneously)

## Example Architecture

```
┌─────────────────────────────────────────────────────┐
│                    Dispatcher                       │
│         (Splits task, aggregates results)            │
└────────────────────┬───────────────────────────────┘
                     │
    ┌────────────────┼────────────────┐
    ▼                ▼                ▼
┌────────┐      ┌────────┐      ┌────────┐
│ Agent 1│      │ Agent 2│      │ Agent 3│  ← All simultaneous
│(Doc A) │      │(Doc B) │      │(Doc C) │
└────────┘      └────────┘      └────────┘
    │                │                │
    └────────────────┼────────────────┘
                     ▼
              ┌─────────────┐
              │  Aggregator  │
              │ (Synthesize) │
              └─────────────┘
                     │
                     ▼
                 Final Output
```

## Dispatcher Pattern

```
You are a dispatcher for parallel execution.

Task: {user_task}

1. Identify N independent subtasks
2. Launch all subtasks simultaneously
3. Wait for all completions
4. Aggregate results

Subtasks identified: {list}
```

## Key Considerations

### Include in Your Decision

1. **True independence** — Can any subtask fail without affecting others?
2. **Result aggregation** — How will results be combined?
3. **Load balancing** — Are subtasks similar in complexity?
4. **Error handling** — Partial failure vs. total failure?

### Independence Checklist

| Question | If NO, Use Another Pattern |
|----------|----------------------------|
| Do subtasks need shared state? | ❌ → supervisor-orchestrator |
| Do subtasks depend on each other's output? | ❌ → supervisor-orchestrator |
| Is there an execution order requirement? | ❌ → supervisor-orchestrator |
| Do subtasks need to collaborate? | ❌ → supervisor-orchestrator |

## Anti-Patterns

| Mistake | Why It's Bad |
|---------|--------------|
| Faking independence | Race conditions, corrupted outputs |
| No aggregation plan | Results pile up without synthesis |
| Uneven workload | Some agents idle, others overwhelmed |
| Ignoring partial failures | Incomplete results, wasted compute |

## Aggregation Strategies

| Strategy | Use When |
|----------|----------|
| **Simple concatenation** | Results are independent, list format OK |
| **Weighted scoring** | Some results more important than others |
| **Consensus voting** | Multiple perspectives on same question |
| **Hierarchical synthesis** | Results themselves need synthesis |

## Scaling Up: Adding Dependencies

```
Need some coordination between parallel tasks?
├── YES, light handoffs?
│   └── YES → supervisor-orchestrator (light version)
└── YES, hierarchical control?
    └── YES → hierarchical-supervisor
```

## Scaling Down

```
Is parallelism actually overkill?
├── YES, one LLM can handle it?
│   └── YES → single-agent
└── YES, simple routing by type?
    └── YES → supervisor-delegation
```

## Quick Reference

| Factor | Parallel Execution |
|--------|-------------------|
| **Latency** | Low (limited by slowest subtask) |
| **Cost** | Higher (N agents running) |
| **Complexity** | Low-Moderate |
| **Reliability** | Partial failure possible; others continue |
| **Best for** | Independent batch workloads |

---

*Pattern ID: `parallel-execution` | AGEM-compatible*