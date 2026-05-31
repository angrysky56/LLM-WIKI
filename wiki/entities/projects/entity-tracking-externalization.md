---
created: 2026-05-30T00:00:00Z
updated: 2026-05-30T00:00:00Z
type: entity
subtype: project
summary: Test harness probing whether externalizing entity-state into tokens lets small local models solve harder state-tracking problems — answer is yes, and completeness beats brevity for REMOVE.
tags: [entity-tracking, state-tracking, externalization, competence-frontier, small-models, prompting-strategies]
related:
  - concepts/length-generalization
  - concepts/shorthand-for-thought
  - concepts/attractor-dynamics
  - synthesis/test-time-sampling-vs-retraining-ood
---

# Entity-Tracking Externalization (ete/)

**Repository:** `~/Repositories/ai_workspace/entity-tracking-externalization/`

A self-contained probe into the recombination-OOD question: when a model's `direct` answer fails on structured state-tracking, can a prompting scaffold recover the latent computation by forcing it into explicit tokens — without fine-tuning?

## The question

Does making a model write its working out — in the right format — let it solve longer, harder state-tracking problems than it can natively?

The specific failure targeted is the **ghost error** — a `REMOVE` operation that the model's global-suppression mechanism silently fails to register, so a removed object is reported as still present. The question is whether externalizing state into tokens **routes around** this fragility (recombination-OOD: capability latent, scaffold recovers it) or whether the operation is genuinely absent (capability-OOD: only retraining helps).

## Core finding: +20+ steps, completeness beats brevity

On `granite4.1:3b` (3.4B, non-reasoning), three prompt formats tested across ladder 8..36 ops:

| Condition | Frontier (n_ops @ ≥60%) | vs direct |
|---|---|---|
| `direct` | 16 | — |
| `delta` (track queried object only) | 36 | +20, ghost 0.15 |
| `externalized` (full state every step) | **36+ (never broke)** | **+20, ghost 0.00** |

`externalized` never broke across the full ladder — its true frontier is past 36. The **+20 is a floor, not the effect size.**

Critical contrast: `delta` (Turing-Program style, minimal edits) reintroduced ghost errors (~0.15–0.35 rate) because discarding other objects' state means there's no written record that a REMOVE happened. **To fix REMOVE, externalize the removal itself.**

## Key architectural insight

The fix is not "show your work" — it is **maintain a complete, typed world-state and re-emit ALL of it after every operation**. Removed entities go to an explicit `nowhere` slot, never erased.

This invariant is baked into `ete/agent/core.py`'s `TrackingAgent`:
- Forces full re-emission each step
- Completeness check: no entity from the prior step may vanish
- `repair_incomplete` re-adds any dropped entity to `nowhere`

This makes ghosts structurally impossible to hide, independent of model capability.

## Relevant to

- **[[synthesis/test-time-sampling-vs-retraining-ood]]** — this project is the behavioral probe for the recombination-OOD vs capability-OOD boundary
- **[[concepts/length-generalization]]** — synthetic state-trackers are the standard probe class here
- **[[concepts/shorthand-for-thought]]** — inverts the "minimal edits generalize better" prior for the REMOVE failure mode
- **[[concepts/attractor-dynamics]]** — the suppression mechanism failure may be an attractor basin issue

## Components

| File | Role |
|---|---|
| `ete/tasks.py` | Task generation, ground truth, similar-name stressor |
| `ete/prompts.py` | Three conditions: `direct`, `delta`, `externalized` |
| `ete/backends.py` | Ollama + MiniMax (Anthropic-compatible endpoint) |
| `ete/grading.py` | Answer extraction, trace salvage, error-type classification |
| `ete/agent/core.py` | Domain-independent `TrackingAgent` |
| `ete/agent/domain.py` | `Domain` Protocol + `ContainerDomain` / `VariableDomain` |
| `frontier.py` | Primary: competence-frontier sweep (headline metric) |
| `sweep.py` | Fixed-ladder difficulty staircase |
| `twobytwo.py` | Reasoning {on,off} × prompt {direct,externalized} grid |

## Run it

```bash
# Verify deterministic core (no model needed)
uv run --extra dev pytest

# Headline experiment
uv run python frontier.py --backend ollama --model granite4.1:3b \
    --conditions direct,delta,externalized --ladder 8,12,16,24,36 \
    --n-tasks 20 --max-tokens 2048

# Live agent smoke test
uv run python -m ete.agent.smoke --model granite4.1:3b
```

## Scaling conjecture (untested)

The mechanism is governed by the gap between task demand and model's *internal* capacity, not by model size. Predictions:
- Bigger models get the same repair but only on harder tasks that put *them* near their ceiling
- On tasks below a model's ceiling, gain → 0 and can go negative (wasted tokens, artifacts) — confirmed with MiniMax-M2.7
- Reasoning models benefit least: their thinking channel already externalizes internally
- Capability-OOD (operation absent) is unfixable by externalization; needs retraining

## Connection to meta-harness

The `ete/agent/` module is the generalization of the finding — a domain-independent tracking engine. Adding a new domain means implementing the `Domain` Protocol; `core.py` stays unchanged. Clean seam between model and code.

The `verify=True` mode (compare every step to `reduce()` ground truth) produces **clean traces** — the fine-tuning corpus for the recursive self-training loop.