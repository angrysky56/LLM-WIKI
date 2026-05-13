---
created: 2026-05-13
type: concept
summary: How to write bounded forward-state carryover at agent/session boundaries using structured templates
tags: [markovian, carryover, session-management, bounded-memory, skill]
status: draft
confidence: 0.8
sources:
  - https://arxiv.org/abs/2510.06557 (Markovian Thinker)
---

# Markovian Carryover: Structured Forward-State for Agent Sessions

**Type:** Skill / Prompt Template  
**Model:** MiniMax (any model that supports structured output)  
**Bounded size:** ~512 tokens max per carryover  

---

## The Problem

Markovian Thinker (2510.06557) shows that agents can learn to write a *textual carryover state* sufficient to continue reasoning after a context reset. Instead of storing full transcripts (expensive, garbage-heavy), we store a structured forward-state that:

1. Encodes what was established (facts, decisions, commitments)
2. Marks what is still open (questions, risks, pending choices)
3. Predicts where the session is going (intended next steps)

This decoupling means **reasoning length is linear in compute, not context length** — constant memory footprint regardless of session length.

---

## Carryover Template

At session or iteration boundary, the agent writes this into `carryover.md` (or returns it as structured output):

```markdown
## CarryoverState

### Established
- **[Entity/Fact]** Description of what was confirmed or decided
- ...

### Open
- **[Question]** What remains unresolved
- **[Risk]** What could go wrong with current approach
- ...

### Heading
- **[Intent]** What the next session/turn should prioritize
- **[Constraint]** Any constraints or boundaries to respect
```

### Established
- What was confirmed, decided, or completed in this session
- One bullet per discrete fact or decision
- Cite sources if applicable: `source: [[page]]`

### Open
- Unresolved questions with enough context to resume
- Risks or failure modes identified but not resolved
- Dependencies: "waiting on X before Y can proceed"

### Heading
- Top 1-3 priorities for the next session
- Any hard constraints (budget, time, scope limits)
- Direction: what outcome is success for this workstream?

---

## Size Bound

Hard cap: **~512 tokens** (~2000 characters). If the carryover exceeds this:

1. Prioritize **Open** items (they're the hardest to re-derive)
2. Truncate **Established** to top 5 most consequential items
3. Drop **Heading** only if absolutely necessary
4. Never exceed ~512 tokens total

The discipline of the cap forces prioritization. Garbage gets left behind.

---

## Integration with Hermes delegate_task

When spawning a subagent via `delegate_task`, the parent injects carryover as context:

```
context="""## Current Carryover State
{servitor_carryover}

## Your Task
{goal}

## Constraints
- MiniMax API budget: ~1500 calls/5hrs (don't spawn unbounded workers)
- Check for existing carryover in your vault before starting fresh
- Write your own carryover to vault/agents/{agent-name}/carryover.md before returning
"""
```

The subagent:
1. Reads its `carryover.md` (if exists) to understand prior state
2. Executes the assigned task
3. Writes updated `carryover.md` before returning its summary
4. Manager reads all carryovers and synthesizes into project `now.md`

---

## Vault Layout for Carryover

```
LLM-WIKI/
├── now.md                    # Root: overall system state (manager synthesizes)
├── soul.md                   # Root: identity, principles
├── user.md                   # Root: user profile, preferences
├── agents.md                 # Root: agent registry, roles
│
├── agents/                   # Agent-specific vaults
│   ├── ha-agent/             # Hermes Agent's own vault
│   │   ├── carryover.md      # Markovian forward-state
│   │   ├── vault.md          # Current working context
│   │   └── workspace/        # Scratch notes, temp files
│   ├── librarian-agent/
│   │   ├── carryover.md
│   │   ├── vault.md
│   │   └── workspace/
│   └── researcher-agent/
│       ├── carryover.md
│       ├── vault.md
│       └── workspace/
│
└── projects/                 # Shared project folders
    ├── meta-harness/
    │   ├── now.md            # Project current state
    │   ├── carryover.md      # Cross-agent carryover aggregation
    │   └── workspace/
    ├── synapse/
    │   ├── now.md
    │   └── workspace/
    └── domain-graph-orchestrator/
        ├── now.md
        └── workspace/
```

### Per-Agent Responsibilities

| Agent | Reads | Writes | Frequency |
|---|---|---|---|
| Manager (HA) | All agent carryovers + project now.md | Root now.md + own carryover | Every session |
| Servitor (worker) | Project now.md + own carryover | Own carryover | Every delegation turn |
| Librarian | Root now.md + project now.md | Entity notes, project now.md updates | On ingestion/retrieval |

---

## Open Questions

1. **Who writes project now.md?** Manager synthesizes from all carryovers, but is the synthesis automatic (prompt template) or a separate LLM call?
2. **Carryover window size** — 512 tokens is the Markovian paper's bound, but should servitors get a larger window for complex tasks?
3. **Carryover vs. full retrieval** — for known facts, should the agent retrieve from Neo4j instead of relying on carryover? (Probably yes for factual grounding, carryover for session continuity)
4. **TTL on carryover** — should carryover expire after N sessions if not refreshed? Markovian paper doesn't address staleness.

---

## Related

- [[bounded-structured-memory]] — the full architectural synthesis
- [[synapse-retrieval-architecture]] — retrieval pipeline this integrates with
- [[persistent-knowledge-compilation]] — why durable artifacts beat re-derivation
