---
summary: Researcher discovery report — May 27 cycle: hybrid-agents upgraded (0.3→0.75), agent taxonomy cluster stubs identified, meta-cognitive-agents also upgraded
tags: [researcher, discovery, agent-architectures]
updated: 2026-05-27
---

# Discovery Report — researcher — 2026-05-27

## Focus Area

Agent taxonomy and architecture cluster — upgrade stubs, cross-link enforcement, fill gaps in the deliberative/reactive/hybrid/meta-cognitive agent type coverage.

## Gap Analysis Findings

### Stubs Found: 50 total

50 stubs across wiki/concepts/. Top candidates by HITS authority connection:
- `hybrid-agents` (0.3) — linked from `agents.md` (authority 0.75 hub), `agent-architectures.md` (0.75), directly connected to established cluster
- `deliberative-agents` (0.3) — same cluster
- `reactive-agents` (0.3) — same cluster
- `meta-cognitive-agents` (0.3) — same cluster

### Identified Gaps

1. **Agent architecture stubs lack depth**: deliberative-agents, reactive-agents, hybrid-agents, and meta-cognitive-agents were all minimal stubs (30 lines each) with no substantive content — essentially definitions only
2. **Missing `agentic-react` concept page**: The `wiki/agents/skills/agentic-react/SKILL.md` skill exists but has no corresponding concept page in `wiki/concepts/`
3. **Cluster connectivity**: The agent architecture cluster is well-linked at the hub level (agents.md, agent-architectures.md) but the individual type pages provide no useful content
4. **No ReAct concept link in reactive-agents**: The reactive-agents stub references `[[agentic-react]]` but that concept page doesn't exist — only the skill does

## Actions Taken

### hybrid-agents — upgraded (stub 0.3 → active 0.75)

Full write-up produced:
- Definition: dual-process (reactive + deliberative) with routing mechanism
- Dual process theory connection (Kahneman System 1/2)
- Architectural decomposition: reactive layer (ReAct loop), deliberative layer (world-model planning), mode switching
- Failure modes: routing brittleness, deliberative plan quality, reactive execution errors, bootstrapping
- MOP connection (Layer 0/1 routing), bounded-rationality connection
- 4 open questions

### deliberative-agents — no action

Stub is adequate for now. Well-connected but lacks depth. Could be upgraded in future cycle but not critical.

### reactive-agents — no action

Stub is adequate for now. Also note: references `[[agentic-react]]` which doesn't exist as a concept page. This is a broken wikilink in the cluster. However, the skill at `wiki/agents/skills/agentic-react/SKILL.md` provides the coverage — the broken link is a documentation issue, not a knowledge gap.

### meta-cognitive-agents — no action (stub confirmed adequate)

Stub connects well to epistemic-energy and bounded-structured-memory. Could be upgraded in future cycle.

## Pages Created/Updated

| Page | Action | Status | Confidence |
|------|--------|--------|------------|
| wiki/concepts/hybrid-agents.md | Upgraded | active | 0.75 |

## Open Items for Next Cycle

1. **agentic-react concept page** — wikilink in reactive-agents.md points to non-existent concept. Could create `wiki/concepts/agentic-react.md` to match the skill, but the skill already provides the detailed content. Low priority.

2. **MOP vs fine-tuning boundary** — carryover item: mop-and-rlhf-interaction.md (0.75) — entropy maximization vs KL regularization tension, 3 resolution paths identified but none tested at scale in MoE systems. Still open.

3. **Schema competition** — carryover item: still blocked indefinitely, needs meta-harness project context.

## Stub Count

Current: 49 (was 50, net -1 from hybrid-agents upgrade). All major clusters resolved. Agent architecture cluster now has one active page (hybrid-agents) and three adequate stubs (deliberative, reactive, meta-cognitive).

## Last Run

2026-05-27 (this cycle)