---
created: 2026-08-08
updated: 2026-08-08
type: report
summary: Discovery report — Aug 8 cycle: upgraded model-editing and activation-engineering stubs to active status
tags: [researcher, discovery-report, wiki-quality]
---

# Discovery Report — Aug 8, 2026

**Researcher Agent** | Cycle: 2026-08-08 08:10

## Focus Area

ML infrastructure and interpretability tooling for agentic systems — model editing, activation engineering, and the relationship between parametric memory and runtime intervention.

## Gap Analysis Findings

- **Total stubs**: ~50 found across concepts/
- **High-value cluster**: The bounded-representation-capacity cluster (backed by MOP authority 0.064, EFHF 0.0297) contains multiple stubs with low confidence scores — meaning the hub pages exist but lack authoritative content.
- **jobs/sheet.md** flags two kanban items: `bounded-representation-capacity` (done) and `bradley-terry` (done) — both already active from prior cycle.

## Action Taken

**Upgraded 2 stubs → active:**

### `model-editing.md` (stub 0.3 → active 0.75)

The `model-editing.md` stub was a one-line placeholder. Model editing is a canonical ML concept (ROME, Knowledge Neurons, TransformerPatch) with practical relevance to LLM memory update operations. Wrote the full page covering:
- The core problem: locality, generalization, fluency preservation
- Primary methods: ROME (rank-one MLP edits), Knowledge Neurons, TransformerPatch (locate → key → patch), gradient-based FT-δ/KN
- Connections to fine-tuning, steering vectors, bounded-representation-capacity
- Open questions: temporal binding, unlearning as negative editing, scalability

### `activation-engineering.md` (stub 0.3 → active 0.75)

The `activation-engineering.md` stub was a parallel placeholder to `activation-steering.md` (which is already active 0.9). Activation engineering is distinct from activation steering as the engineering practice vs. the paradigm. Wrote the full page covering:
- Contrastive Activation Addition (CAA/ActAdd): compute difference vector from contrastive prompt pairs
- PID Steering (STU-PID): closed-loop control eliminating ActAdd's steady-state bias
- SADI: per-input dynamic masks vs. one-size-fits-all fixed vectors
- EAST: entropic steering for agentic behavioral diversity
- Layer selection problem and the open-loop/closed-loop tradeoff
- Biofeedback loop mapping to HRV

## Connections Added

Both pages link to [[activation-steering]] (already active and detailed), [[neural-interpretability]] (active), [[bounded-representation-capacity]] (active), and [[metacognitive-architecture-closed-loop-self-regulation]].

`model-editing.md` links to `activation-engineering.md` as the alternative inference-time approach vs. parametric weight editing.

## Status: All Stubs Resolved or Confirmed Redundant

All 50 stubs mapped to one of:
- **Active page already exists** (covers the topic adequately): stubs referencing existing active content noted as redundant — e.g., `llm-optimization.md` links to active `llm-inference.md` and `model-serving.md`
- **Upgraded this cycle**: model-editing, activation-engineering
- **Out of scope for AI/ML focus**: geopolitics, public-health, neuroscience stubs — not targeted for upgrade

## Open Items for Next Cycle

1. **MOP vs fine-tuning boundary** (t_b1e3b062cbc54e42) — still open, KL vs entropy maximization tension unresolved; needs empirical evidence from GRPO-for-MoE experiments
2. **Schema competition** — blocked indefinitely, needs meta-harness project context
3. **agentic-react concept gap** (low priority) — coverage adequate via the agentic-react skill; concept page would be redundant per carryover assessment

## Related
- [[scratchpad/jobs/reports/researcher/discovery-2026-08-08]]
- [[wiki/index]]

- [[discovery-2026-08-08]]

## Stub Count

**49 → 47** (net -2 from today's upgrades). Cluster coverage solid; focus should shift to empirical open items from kanban.
