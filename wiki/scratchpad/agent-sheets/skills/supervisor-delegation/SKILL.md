---
name: "supervisor-delegation"
description: "Supervisor delegation pattern: One supervisor LLM routes tasks to specialized sub-agents."
---

---
name: "supervisor-delegation"
description: "Supervisor delegation pattern: One supervisor LLM routes tasks to specialized sub-agents. Best for multi-capability routing."
---

# Supervisor Delegation Pattern

> [!IMPORTANT]
> **When to use**: When one supervisor LLM routes to multiple specialized LLMs. Best for tasks with distinct capability requirements.

## Decision Tree Path

```
Does the task require multiple specialized capabilities?
├── YES
│   └── Do you need a supervisor to route and coordinate sub-agents?
│       ├── YES → Supervisor Delegation (you're here)
│       └── NO, sub-agents need more autonomy?
│           └── YES → supervisor-orchestrator
└── NO → single-agent
```

## When to Choose

| ✅ Use Supervisor Delegation When | ❌ Avoid When |
|----------------------------------|--------------|
| Task has distinct phases needing different expertise | Sub-agents need to collaborate on shared context |
| You want centralized control/logic in supervisor | Task decomposition is complex/unpredictable |
| Sub-agents are largely independent workers | You need multi-level handoffs |

## Use Cases

- **Customer support routing** (billing → tech → refunds)
- **Multi-document processing** (analyze → summarize → respond)
- **Research pipelines** (search → extract → synthesize)
- **Code review with multiple specialties** (security → performance → style)

## Example Architecture

```
           ┌─────────────┐
           │  Supervisor │ ← Routes based on task type
           │     LLM     │
           └──────┬──────┘
                  │
       ┌──────────┼──────────┐
       ▼          ▼          ▼
  ┌────────┐ ┌────────┐ ┌────────┐
  │ Code   │ │ Legal  │ │Research│
  │ Expert │ │ Expert │ │ Expert │
  └────────┘ └────────┘ └────────┘
       │          │          │
       └──────────┼──────────┘
                  ▼
            Synthesize
```

## Supervisor Prompt Pattern

```
You are a supervisor router. Given a user task:
1. Identify the required capabilities
2. Route to the appropriate specialist agent
3. Synthesize results if multiple agents respond

Agents available:
- code_expert: Python, JavaScript, debugging
- legal_expert: contracts, compliance, privacy
- research_expert: web search, citations, analysis

Respond with your routing decision and reasoning.
```

## Key Considerations

### Include in Your Decision

1. **Supervisor capability** — Does the supervisor LLM reliably understand routing?
2. **Sub-agent scope** — Are sub-agents clearly defined with limited scope?
3. **Handoff clarity** — Is it clear how sub-agents return results to supervisor?
4. **Error boundaries** — Does one sub-agent failure affect others?

### Specialist Definition Best Practices

| Aspect | Recommendation |
|--------|----------------|
| **Scope** | Narrow, well-defined capabilities |
| **Interface** | Consistent input/output format |
| **Fallback** | Default response if task doesn't fit specialty |
| **Independence** | Each specialist should be independently usable |

## Anti-Patterns

| Mistake | Why It's Bad |
|---------|--------------|
| Vague specialist definitions | Supervisor can't route reliably |
| Overloading supervisor | Supervisor becomes a bottleneck |
| No synthesis layer | User gets fragmented outputs |
| Sub-agents that need shared context | Creates coordination nightmares |

## Scaling Up: Multi-Level Routing

```
Need multiple levels of supervision?
├── YES → hierarchical-supervisor
│       (Supervisor → Supervisor → Workers)
└── NO, but agents need to collaborate?
    └── YES → supervisor-orchestrator
```

## Scaling Down

```
Is the task actually simpler than expected?
├── YES, just parallel independent tasks?
│   └── YES → parallel-execution
└── YES, one LLM can handle it?
    └── YES → single-agent
```

## Quick Reference

| Factor | Supervisor Delegation |
|--------|----------------------|
| **Latency** | Medium (routing + sub-agent) |
| **Cost** | Medium (supervisor + specialists) |
| **Complexity** | Moderate |
| **Reliability** | Sub-agents isolated, supervisor is single point |
| **Best for** | Multi-capability routing with central control |

---

*Pattern ID: `supervisor-delegation` | AGEM-compatible*