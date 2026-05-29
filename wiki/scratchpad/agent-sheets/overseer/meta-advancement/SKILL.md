---
name: meta-advancement
description: "Meta-advancement tracking framework — per-agent state, advancement formula, scrutiny/improvement cycles. Used by overseer to track agent progress and coordinate tasking."
tags: [meta, advancement, tracking, overseer, agent-state]
updated: 2026-05-25
created_by: agent
---

# Meta Advancement Framework

Per-agent state tracking for the wiki-overseer. Each agent has one tracking file.
The central sheet indexes all agents and their tracking file paths.

## Per-Agent Tracking File Format

```yaml
agent: {agent-name}
job_id: {cron-job-id}
updated: {ISO-timestamp}
state: idle|running|waiting|done|blocked|error
last_run: {ISO-timestamp}
next_run: {ISO-timestamp}
deliver: {delivery-target}

## AdvancementState

### Truth (Base Value)
- Initial hypotheses / core principles for this agent's domain
- Current hypothesis strength: 0.0–1.0

### Scrutiny (alpha-weighted)
- Weaknesses or gaps identified since last cycle
- Alpha weight: 0.0–1.0 (importance of scrutiny vs improvement)

### Improvement (beta-weighted)
- Changes made based on scrutiny since last cycle
- Beta weight: 0.0–1.0 (importance of improvement vs scrutiny)
- Alpha + Beta must equal 1.0

### Advancement Score
```
Advancement = Truth + (alpha * Scrutiny) + (beta * Improvement)
```

### Meta-Meta Process State

| Step | Component | Status | Notes |
|------|-----------|--------|-------|
| 1. Why? | Purpose / Core Intent | | |
| 2. What? | Dimensional Axes | | |
| 3. How? | Recursive Frameworks | | |
| 4. What if? | Constraints as Catalysts | | |
| 5. How Else? | Controlled Emergence | | |
| 6. What Next? | Feedback Loops | | |
| 7. What Now? | Adaptive Flexibility | | |

### Feedstock

- Input sources consumed this cycle
- Open questions carried forward
- Blockers or dependencies

### Derivation Chain

```
C(R(F(S(D(RB(M(SF)))))))
C → Concept formation
R → Representation
F → Facts identified
S → Scrutiny applied
D → Derivation performed
RB → Rule-based approach used
M → Model created/updated
SF → Semantic formalization
```

### Open Items

| Item | Priority | Status | Last Updated |
|------|----------|--------|--------------|
| | | | |

### Logs

```
{date} — {event}
{date} — {event}
```