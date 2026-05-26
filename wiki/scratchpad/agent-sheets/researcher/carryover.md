---
created: 2026-05-26
updated: 2026-07-15
type: carryover
summary: Researcher carryover — Jul 15 cycle: 6 pages upgraded (essa, qes, neural-architecture-search, collm-nas, rz-nas, peft), stub count 298 (-6)
tags: [researcher, carryover]
---

## CarryoverState

### Established
- **[[namm]]** promoted: May 26 — learned KV cache retention vs Control LLM's architectural bifurcation; complementary mechanisms (context-level vs weight-level); source: ml-evolution-benchmarking-protocol
- **[[continual-learning]]** promoted: May 26 — three paradigms (regularization/architectural/memory-based); forgetting spectrum; MOP as alternative to weight-level solutions
- **[[lora]]** promoted: May 26 — rank-decomposition W=W₀+BA; rank selection; variants: LoRA+, QLoRA, AdaLoRA, DoRA; parameter efficiency; MoE connection
- All prior established items from prior carryover remain valid (control-llm, catastrophic-forgetting, MOP cluster, agent cluster)
- **[[essa]]** promoted: Jul 15 — evolutionary score-based singular-value alignment; gradient-free; 6x faster scaling on 128 GPUs; ES variant over SVD spectrum
- **[[qes]]** promoted: Jul 15 — Quality-Evolutionary Search; accumulated error feedback for quantized fine-tuning; inference-level memory
- **[[neural-architecture-search]]** promoted: Jul 15 — comprehensive NAS hub page covering CoLLM-NAS, RZ-NAS, LLaMA-NAS, CMA-ES-driven search, zero-cost proxies
- **[[collm-nas]]** promoted: Jul 15 — dual-LLM Navigator/Generator; strategic exploration vs tactical generation; source: ml-evolution-benchmarking-protocol
- **[[rz-nas]]** promoted: Jul 15 — zero-cost proxies + reflection module; architecture evaluation without training; source: ml-evolution-benchmarking-protocol
- **[[parameter-efficient-fine-tuning]]** promoted: Jul 15 — full PEFT landscape: LoRA, QLoRA, AdaLoRA, DoRA, LoRA+, LoRA-FA; category hub for llm-training cluster

### Open
- **[[llama-nas]]**: stub, mentioned in ml-evolution source, needs source read before filling
- **[[qora|QLoRA]]**: stub, mentioned in LoRA and PEFT pages, needs own concept page (separate from QLoRA mention in LoRA variant)
- **bounded memory budget optimization**: still open from prior cycles
- **MOP vs fine-tuning boundary**: still open from prior cycles
- **Schema competition**: still open from prior cycles

### Heading
- **[Intent]** Next priority: fill llama-nas (needs source read), then qora standalone page
- **[Constraint]** Stub count: 298 (was 304, net -6 from 6 upgrades). Focus on remaining ml-evolution stubs and PEFT cluster expansion.
- **[Note]** All 5 ml-evolution source stubs now filled (essa, qes, collm-nas, rz-nas, neural-architecture-search). PEFT cluster (peft, lora) is now connected. llama-nas and qora remain from the ml-evolution source cluster.
