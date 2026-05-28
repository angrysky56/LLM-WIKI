---
summary: Decision framework for matching task profiles to multi-agent coordination patterns
tags: [agentic-design-picker, multi-agent, coordination, agent-design, design-patterns]
updated: 2026-05-27T06:21:22Z
---

---
created: 2026-06-16
updated: 2026-08-05
type: concept
summary: Decision framework for matching task characteristics to the right multi-agent coordination pattern
tags: [agentic-design-picker, multi-agent, coordination, agent-design, design-patterns]
sources: []
status: active
confidence: 0.8
---

# Agentic Design Picker

A decision framework for selecting the right multi-agent coordination pattern given task characteristics. Given a task description, the picker evaluates tradeoffs along six axes and recommends a coordination architecture.

## The Six Evaluation Axes

| Axis | What It Measures | Low → High |
|------|-----------------|-------------|
| **Task Decomposability** | Can the task be cleanly split into independent subtasks? | Monolithic → Decomposable |
| **Expertise Segregation** | Do subtasks require distinct capabilities/knowledge? | Homogeneous → Heterogeneous |
| **Coordination Criticality** | How costly are agent-to-agent conflicts or duplication? | Low → High |
| **Latency Budget** | How much time is available before first meaningful output? | Tight → Generous |
| **Context Window Pressure** | How large is the working state relative to context limits? | Low → High |
| **Failure Severity** | What happens when the system fails mid-execution? | Minor → Catastrophic |

## The Five Patterns (from Multi-Agent LLM Systems)

The picker matches task profiles to these five coordination architectures:

### 1. Pipeline / Sequential
**Best for**: Tasks that are naturally decomposable into a strict sequence of stages where each stage's output feeds the next. Order matters; backtracking is rare or impossible.

**Task profile**: Low decomposability (clear linear flow), low coordination criticality, moderate latency budget
**Avoid when**: Tasks have significant branching or when late-stage information should inform early stages

**Signal phrase**: "first do X, then Y, then Z" or "assembly line"

### 2. Supervisor-Worker (Hierarchical)
**Best for**: Tasks where a manager can accurately decompose work and assign to specialists without needing to see all worker outputs simultaneously. The supervisor is the bottleneck — only use when supervisor overhead is acceptable.

**Task profile**: High decomposability, high expertise segregation, moderate coordination criticality, some failure severity tolerance
**Avoid when**: Supervisor becomes the bottleneck (high parallelism needs) or workers need real-time cross-communication

**Signal phrase**: "one agent directs, others execute" or "specialist agents"

### 3. Peer-to-Peer (Debate / Negotiation)
**Best for**: Tasks where multiple perspectives must be evaluated and the final answer benefits from adversarial pressure. Agents challenge each other's outputs; consensus (or voting) produces the final result.

**Task profile**: High coordination criticality, moderate decomposability, high failure severity (errors are visible and contestable)
**Avoid when**: Tasks are sequential (debate doesn't help if order matters) or when one agent clearly has more domain expertise (peer structure gives equal weight to unequal agents)

**Signal phrase**: "agents argue and the best answer wins" or "adversarial refinement"

### 4. Blackboard / Shared State
**Best for**: Tasks where many agents contribute partial observations to a shared picture and no single agent has the full context. Useful when task state is larger than any single agent's context window.

**Task profile**: High context window pressure, moderate decomposability, high coordination criticality
**Avoid when**: Semantic conflicts are likely (agents interpret shared data differently) or when consensus on shared state is hard to define

**Signal phrase**: "shared memory" or "agents write what they find to a board"

### 5. Hierarchical with Memory
**Best for**: Complex, long-horizon tasks with nested subtask clusters. Manager decomposes into workstreams, sub-managers handle clusters in parallel, cross-level memory allows coordination without constant supervisor involvement.

**Task profile**: High decomposability, high expertise segregation, high coordination criticality, generous latency budget
**Avoid when**: Latency is tight (nested hierarchy adds overhead) or task doesn't have clear subtask clustering

**Signal phrase**: "parallel workstreams coordinated at higher levels"

## Decision Tree

```
Task decomposed cleanly?
├── No → Pipeline (if strict order matters) or Blackboard (if state is large)
└── Yes → Distinct expertise needed?
    ├── No → Supervisor-Worker (flat, many workers)
    └── Yes → Coordination criticality?
        ├── Low → Supervisor-Worker
        └── High → Parallelism needed?
            ├── No → Supervisor-Worker (sequential decomposition)
            └── Yes → Failure severity high?
                ├── No → Peer-to-Peer (debate)
                └── Yes → Hierarchical with Memory
```

## Cross-Pattern Connections

| Pattern | Uses | Conflicts With |
|---------|------|----------------|
| Pipeline | Sequential stage processing | Peer-to-Peer (no clear ordering) |
| Supervisor-Worker | Manager-driven decomposition | Peer-to-Peer (no manager) |
| Peer-to-Peer | Adversarial refinement | Pipeline (no agent-to-agent debate) |
| Blackboard | Shared state aggregation | Supervisor-Worker (centralized) |
| Hierarchical | Nested parallel workstreams | Pipeline (nested vs linear) |

## Connections
- [[concepts/spiral-architecture]]
- [[log]]
- [[concepts/multi-agent-llm-systems]]
- [[sources/articles/choosing-right-agentic-design-pattern]]
- [[scratchpad/agent-sheets/researcher/carryover]]
- [[concepts/agentic-research]]
- [[index]]
- [[sources/articles/designing-agentic-design-picker]]
- [[agents/skills/librarian-agent/skill]]
- [[concepts/agentic-design-picker]]
- [[agentic-design-picker]]

- [[multi-agent-llm-systems]] — the five patterns this picker selects among
- [[agentic-planner]] — planning is the cognitive function that drives decomposition in supervisor and hierarchical patterns
- [[agentic-hierarchy]] — hierarchical organizational structure for multi-agent systems
- [[agents]] — parent concept for agent taxonomy

- [[agentic-research]]
## Open Questions

1. **Can a task change coordination pattern mid-execution?** Most systems fix the pattern at design time, but a truly adaptive agent might promote from Pipeline → Supervisor-Worker when decomposition reveals structure. No established pattern for dynamic migration.

2. **How do you choose between Peer-to-Peer and Supervisor-Worker for adversarial tasks?** Peer-to-Peer gives all agents equal standing; Supervisor-Worker lets the manager arbitrate. If some agents have reliably better judgment (domain experts), supervisor structure may outperform peer debate even in adversarial settings.

3. **What is the latency overhead of each pattern at different scales?** Pipeline has minimal overhead; Hierarchical has maximal. But the relationship is not linear — Supervisor-Worker overhead scales with worker count only if the supervisor is the bottleneck. Empirical characterization missing.
