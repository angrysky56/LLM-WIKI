---
created: 2026-01-01
updated: 2026-05-25
type: skill
summary: Supervisor → Delegate pattern — one supervisor breaks down work, assigns to specialists, merges results
tags: [agent-skill, skill, supervisor, delegation]
sources: 
status: active
confidence: 1.0
---

# Supervisor Delegation Pattern

> [!TIP]
> **Use when**: A task has separable sub-tasks with known types (research, write, verify) and you want a supervisor to coordinate specialists.

## Pattern

```
Supervisor Agent
├── Delegates task to Specialist A
├── Delegates task to Specialist B
├── Waits for all results
└── Merges and delivers final output
```

## Key Properties

- **Fixed assignment**: Sub-agents are assigned tasks at the start — not routed dynamically
- **Carryover coordination**: Supervisor writes carryover; sub-agents read it for context
- **Shared output space**: Sub-agents write to a shared location (e.g., `jobs/reports/{agent}/`)
- **Result merge**: Supervisor is responsible for combining sub-agent outputs

## Implementation

### Supervisor Side
1. Break the task into N independent sub-tasks
2. For each sub-task: write a brief in carryover or a task file
3. Spawn N sub-agents (or delegate sequentially if parallelization isn't needed)
4. Wait for all sub-agents to complete
5. Read their output files
6. Merge into final report

### Sub-Agent Side
1. Read supervisor's task assignment (carryover, task file, or directive)
2. Execute your specialized task
3. Write output to the shared location
4. Report completion to supervisor (via filename convention or status update)

## When to Use

✅ Good for:
- Research + Write pipelines (researcher finds content, writer drafts)
- Multi-topic coverage (different agents cover different topics in parallel)
- Review + Edit pipelines (one writes, one reviews)
- Fact-check + Summary (parallel find, sequential merge)

❌ Bad for:
- Tasks where sub-agent output is input to another sub-agent (use sequential)
- Atomic single-task (use single-agent)
- Content-type unknown until you see it (use orchestrator)

## Connections
- [[agents/skills/supervisor-orchestrator]]
- [[agents/skills/agentic-multiagent]]
- [[agents/skills/hierarchical-supervisor]]
- [[agents/skills/supervisor-delegation]]
- [[agents/skills/single-agent]]
- [[agents/skills/agentic-decision-tree]]
- [[index]]
- [[supervisor-delegation]]

- [[supervisor-orchestrator]] — dynamic routing variant
- [[hierarchical-supervisor]] — nested supervisors for complex domains
- [[single-agent]] — supervisor overhead only makes sense for separable tasks
- [[agentic-multiagent]] — multi-agent coordination patterns
- [[agentic-decision-tree]] — routing to supervisor-delegation