---
name: "single-agent"
description: "Single-agent pattern: One LLM handles all tasks without sub-agent delegation."
---

---
name: "single-agent"
description: "Single-agent pattern: One LLM handles all tasks without sub-agent delegation. Use when simplicity beats sophistication."
---

# Single Agent Pattern

> [!IMPORTANT]
> **When to use**: When one LLM can reliably complete the entire task. Prioritize simplicity unless complexity demands delegation.

## Decision Tree Path

```
Does the task require multiple specialized capabilities?
├── NO → Single Agent (you're here)
└── YES → Consider delegation patterns
```

## When to Choose

| ✅ Use Single Agent When | ❌ Avoid When |
|--------------------------|---------------|
| Straightforward, linear tasks | Task has distinct specialized phases |
| Task fits in one LLM's context window | Multiple experts needed (legal + code + writing) |
| Speed/simplicity is paramount | One specialist failing shouldn't block others |
| Low task variance | Task might need independent retry logic |

## Use Cases

- **One-shot document generation** (draft → refine in one session)
- **Simple Q&A with web search**
- **Text classification / sentiment analysis**
- **Code snippet generation** (no multi-file architecture)

## Example Architecture

```
User Request
      │
      ▼
┌─────────────┐
│  Single LLM │ ← One model, one context
└─────────────┘
      │
      ▼
   Output
```

## Key Considerations

### Include in Your Decision

1. **Context window size** — Can the full task fit?
2. **Latency requirements** — Is multi-turn overhead acceptable?
3. **Error recovery** — Single point of failure; is that OK?
4. **Cost** — Sub-agents cost more per request

### Single Agent Prompts That Work

- Be explicit about output format
- Include all necessary context upfront
- Specify constraints and guardrails
- Break into steps within the prompt if needed (Chain-of-Thought)

## Anti-Patterns

| Mistake | Why It's Bad |
|---------|--------------|
| Forcing delegation into a simple task | Adds latency, cost, and complexity for no benefit |
| Ignoring when a task outgrows single agent | Leads to prompt engineering spaghetti |
| Using single agent for multi-domain expertise | LLM may "hallucinate" expertise it doesn't have |

## Scaling Up

When single agent isn't enough, follow the decision tree:

```
Need multiple specialized capabilities?
├── NO, just parallel independent tasks?
│   └── YES → parallel-execution
└── YES, but centralized control needed?
    └── YES → supervisor-delegation
    └── NO, agents need autonomy?
        └── YES → supervisor-orchestrator
```

## Quick Reference

| Factor | Single Agent |
|--------|--------------|
| **Latency** | Lowest |
| **Cost** | Lowest |
| **Complexity** | Minimal |
| **Reliability** | Single point of failure |
| **Best for** | Simple, linear tasks |

---

*Pattern ID: `single-agent` | Decision tree leaf | AGEM-compatible*