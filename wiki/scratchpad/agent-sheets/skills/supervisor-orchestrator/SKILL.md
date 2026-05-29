---
name: "supervisor-orchestrator"
description: "Supervisor-orchestrator pattern: Orchestrator controls task planning and delegation."
---

---
name: "supervisor-orchestrator"
description: "Supervisor-orchestrator pattern: Orchestrator controls task planning and delegation to specialized agents with full decomposition logic."
---

# Supervisor Orchestrator Pattern

> [!IMPORTANT]
> **When to use**: When an orchestrator needs to plan, decompose, and coordinate multiple sub-agents — with routing logic built into the orchestrator itself.

## Decision Tree Path

```
Does the task require multiple specialized capabilities?
├── YES
│   └── Do you need a supervisor to route and coordinate sub-agents?
│       ├── NO, sub-agents need autonomy with orchestrator control?
│       │   └── YES → Supervisor Orchestrator (you're here)
│       └── YES, just routing needed?
│           └── YES → supervisor-delegation
└── NO → single-agent
```

## When to Choose

| ✅ Use Orchestrator When | ❌ Avoid When |
|--------------------------|---------------|
| Task decomposition is complex/unpredictable | Task has simple, fixed routing |
| Orchestrator needs fine-grained control over execution | Multi-level hierarchy needed |
| Sub-agents need to work on shared artifacts/data | Simple parallel execution suffices |
| You need conditional branching based on intermediate results | |

## Use Cases

- **Complex research pipelines** (search → analyze → compare → report)
- **Software architecture generation** (requirements → design → code → test)
- **Multi-step negotiations** (analyze → propose → counter → finalize)
- **Document authoring pipelines** (outline → research → draft → revise)

## Example Architecture

```
┌─────────────────────────────────────────────┐
│              Orchestrator                   │
│  ┌───────────────────────────────────────┐  │
│  │ • Task decomposition                  │  │
│  │ • Step sequencing                     │  │
│  │ • Conditional branching               │  │
│  │ • Result synthesis                    │  │
│  └───────────────────────────────────────┘  │
└──────────────────┬──────────────────────────┘
                   │
     ┌─────────────┼─────────────┐
     ▼             ▼             ▼
┌────────┐   ┌────────┐   ┌────────┐
│Agent A │◄──│Agent B │──►│Agent C │
│(Search)│   │(Analyze)   │(Write) │
└────────┘   └────────┘   └────────┘
     │             │             │
     └─────────────┼─────────────┘
                   ▼
              Shared Context
              (Artifacts, State)
```

## Orchestrator Prompt Pattern

```
You are an orchestrator controlling a team of specialized agents.

Task: {user_task}

Available agents:
- search_agent: Web search, fact retrieval
- analysis_agent: Data analysis, pattern recognition  
- writing_agent: Content creation, editing

Orchestrator responsibilities:
1. Decompose the task into steps
2. Assign each step to the appropriate agent
3. Manage shared state between agents
4. Handle errors and retries
5. Synthesize final output

Always maintain shared context between agents.
```

## Key Considerations

### Include in Your Decision

1. **Orchestrator sophistication** — Can it reliably decompose and sequence?
2. **Shared state management** — How will agents share context/artifacts?
3. **Error handling** — What happens when an agent fails mid-sequence?
4. **Conditional logic** — Does the flow need branching based on results?

### Shared State Options

| Approach | Use When |
|----------|----------|
| **Central artifact (file/DB)** | Agents produce/consume structured outputs |
| **Message passing** | Real-time coordination needed |
| **Orchestrator intermediates** | Supervisor holds all state, agents stateless |

## Anti-Patterns

| Mistake | Why It's Bad |
|---------|--------------|
| Over-centralizing in orchestrator | Bottleneck, single point of failure |
| No shared state mechanism | Agents work in isolation, results don't integrate |
| Rigid step sequencing | Can't adapt to intermediate results |
| Orchestrator does work itself | Defeats purpose of delegation |

## Scaling Up: Adding Autonomy

```
Need multiple levels of supervisory control?
├── YES → hierarchical-supervisor
└── NO, but agents should operate independently?
    └── YES → Consider parallel-execution for independent branches
```

## Scaling Down

```
Is orchestration actually simpler than expected?
├── YES, just routing based on type?
│   └── YES → supervisor-delegation
├── YES, just parallel independent tasks?
│   └── YES → parallel-execution
└── YES, one LLM can handle it?
    └── YES → single-agent
```

## Quick Reference

| Factor | Supervisor Orchestrator |
|--------|------------------------|
| **Latency** | High (decomposition + coordination + execution) |
| **Cost** | Higher (orchestrator + agents + state management) |
| **Complexity** | High |
| **Reliability** | Orchestrator critical; agents can be isolated |
| **Best for** | Complex multi-step tasks with shared state |

---

*Pattern ID: `supervisor-orchestrator` | AGEM-compatible*