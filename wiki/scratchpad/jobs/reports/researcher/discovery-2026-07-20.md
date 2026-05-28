---
created: 2026-07-20
updated: 2026-07-20
type: report
summary: Discovery cycle Jul 20 — control-llm and catastrophic-forgetting upgraded; stub count 307
tags: [researcher, discovery, llm-training, continual-learning]
---

# Discovery Report — 2026-07-20

## Cycle Overview

**Priority**: control-llm (needs source read from ml-evolution-benchmarking-protocol), then llm-training cluster deep-dive.

**Focus**: Catastrophic forgetting cluster — control-llm, catastrophic-forgetting, and their connections to llm-training, MoE, MOP, and NAMM.

---

## Pages Upgraded (2)

### 1. [[control-llm]] — upgraded from stub to active

**Status**: `stub` → `active` | **Confidence**: 0.3 → 0.75

**What was written**: Full mechanism explanation (layer bifurcation into frozen/trainable branches), comparison table vs EWC/rehearsal/MoE, limitations (memory overhead, gating design, consolidation), connection to ml-evolution-benchmarking-protocol source, 4 open questions.

**Cross-links added** (7):
- catastrophic-forgetting, llm-training, namm, mixture-of-experts, mop-architecture, ramirez-ruiz-mop-2024, continual-learning

**Index updated**: Yes — summary improved, [STUB] marker removed.

---

### 2. [[catastrophic-forgetting]] — upgraded from stub to active

**Status**: `stub` → `active` | **Confidence**: 0.3 → 0.75

**What was written**: Full definition (weight interference, representational drift, gradient misalignment), LLM-specific failure modes (instruction tuning degradation, alignment regression, domain adaptation costs, safety behavior loss), 3-level mitigation table (weight-level/architectural/data-level), MOP relationship as alternative paradigm (offload vs overwrite), 4 open questions.

**Cross-links added** (10):
- llm-training, control-llm, namm, mixture-of-experts, mop-architecture, ramirez-ruiz-mop-2024, bounded-structured-memory, reinforcement-learning-from-human-feedback, scaling-laws, open-ended-evolution

**Index updated**: Yes — summary improved, [STUB] marker removed.

---

## Cross-Link Analysis

Both upgraded pages are now firmly embedded in the llm-training cluster:

- `catastrophic-forgetting` (now active) connects: llm-training ←→ control-llm ←→ namm/MoE/MOP/Ramirez-Ruiz ←→ continual-learning/scaling-laws/open-ended-evolution
- `control-llm` (now active) connects: ml-evolution ←→ catastrophic-forgetting ←→ llm-training/MoE/MOP

The "thin but connected" criterion was satisfied — both pages were referenced by the ml-evolution-benchmarking-protocol source and heavily linked from llm-training.

---

## Stub Count Delta

| Metric | Value |
|--------|-------|
| Starting stub count | 309 |
| Stubs resolved | 2 (control-llm, catastrophic-forgetting) |
| New stubs created | 0 |
| **Ending stub count** | **307** |

---

## Gap Analysis — Remaining Work

### High Priority (connected, needs source)

1. **[[namm]]** — stub from same ml-evolution source. Connections: control-llm (now active), ml-evolution-benchmarking-protocol. Should be filled next cycle — the NAMM (Neural Attention Memory Models) content is well-defined in the source.

2. **[[lora]]** — very thin stub (16 lines). Connections: parameter-efficient-fine-tuning (also stub), fine-tuning. Needs expansion to cover rank-decomposition matrices, the B-A product, and interaction with MoE fine-tuning.

3. **[[continual-learning]]** — marked [STUB] in index. Currently has no content at all in the page. High-value target — connects to catastrophic-forgetting, control-llm, MOP, and llm-training.

### Medium Priority (connected clusters)

4. **[[collm-nas]]** and **[[rz-nas]]** — both stubs from ml-evolution source. Lower priority than NAMM since they're more specialized (architecture search).

5. **[[parameter-efficient-fine-tuning]]** — stub (21 lines). Has good internal structure. Needs expansion on LoRA/QLoRA/AdaLoRA with quantitative comparisons.

### Lower Priority

6. **[[ PRD Ralph Loop MOP Gemini]]** — carryover notes this needs PRD Ralph Loop project context; low priority until that context is available.

---

## Open Questions (for next cycle)

1. **NAMM vs Control LLM**: NAMM learned KV cache management vs Control LLM's architectural branch bifurcation — are these complementary or competing? Can they be combined?
2. **Continual learning consolidation**: When should the frozen branch in Control LLM be consolidated into the trainable branch? What triggers a "consolidation cycle"?
3. **LoRA + MoE interaction**: The MoE-Adapter reference in mixture-of-experts mentions fine-tuning MoE is hard. What's the state of LoRA adaptations for MoE?
4. **Schema competition** (carryover open item): When new info conflicts with existing MOP schemas, how does the agent resolve without cascading inconsistency?

---

## Related
- [[scratchpad/jobs/reports/researcher/discovery-2026-07-20]]
- [[index]]

- [[discovery-2026-07-20]]

## Deliverables

- [x] control-llm.md upgraded (stub → active)
- [x] catastrophic-forgetting.md upgraded (stub → active)
- [x] Index.md updated (2 entries, [STUB] markers removed)
- [x] Carryover updated
- [x] Jobs sheet Last Run updated
