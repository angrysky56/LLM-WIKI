---
created: 2026-05-26
updated: 2026-05-26
type: carryover
summary: Researcher carryover — May 26 cycle: 3 pages upgraded (namm, continual-learning, lora), stub count 304
tags: [researcher, carryover]
---

## CarryoverState

### Established
- **[[namm]]** promoted: May 26 — learned KV cache retention vs Control LLM's architectural bifurcation; complementary mechanisms (context-level vs weight-level); source: ml-evolution-benchmarking-protocol
- **[[continual-learning]]** promoted: May 26 — three paradigms (regularization/architectural/memory-based); forgetting spectrum; MOP as alternative to weight-level solutions; connects catastrophic-forgetting/MoE/MOP/llm-training
- **[[lora]]** promoted: May 26 — rank-decomposition W=W₀+BA; rank selection (r=4–128+); variants: LoRA+, QLoRA, AdaLoRA, DoRA; parameter efficiency; connection to MoE fine-tuning
- All prior established items from Jul 20 carryover remain valid (control-llm, catastrophic-forgetting, MOP cluster, agent cluster)

### Open
- **[[collm-nas]]**: stub, from ml-evolution source, needs filling
- **[[essa]]**: stub, from ml-evolution source, needs filling
- **[[qes]]**: stub, from ml-evolution source, needs filling
- **[[rz-nas]]**: stub, from ml-evolution source, needs filling
- **[[parameter-efficient-fine-tuning]]**: thin stub (~21 lines), connected to lora/fine-tuning
- **[[qora]]**: mentioned in LoRA page, needs own concept page
- **Bounded memory budget optimization**: still open from prior cycles
- **MOP vs fine-tuning boundary**: still open from prior cycles
- **Schema competition**: still open from prior cycles

### Heading
- **[Intent]** Next priority: fill ml-evolution source cluster (collm-nas, essa, qes, rz-nas), then PEFT cluster expansion (peft, qora)
- **[Constraint]** Stub count: 304 (was 307, net -3 from 3 upgrades). Focus on ml-evolution source cluster and peft/qora expansion.
- **[Note]** namm and continual-learning now firmly embedded in llm-training cluster with strong cross-links. lora expanded with rank selection, variants, and MoE connection. Next cycle should tackle the remaining ml-evolution stubs (essa, qes, collm-nas, rz-nas) before moving to peft/qora.