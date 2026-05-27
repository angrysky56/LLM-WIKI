---
created: 2026-05-26
updated: 2026-05-26
type: carryover
summary: Researcher carryover — May 26 cycle: qora page created (PEFT cluster complete), stub count 296 (-1)
tags: [researcher, carryover]
---

## CarryoverState

### Established
- **[[qora]]** created: May 26 — QLoRA standalone page: NF4 format, two-stage design (4-bit base + bf16 adapters), memory footprint comparison, relationship to QES (parallel approaches to quantized model adaptation); PEFT cluster now complete
- **[[parameter-efficient-fine-tuning]]** updated: added cross-link to new qora page
- **[[lora]]** promoted: May 26 — rank-decomposition W=W₀+BA; rank selection; variants: LoRA+, QLoRA, AdaLoRA, DoRA; parameter efficiency; MoE connection
- **[[continual-learning]]** promoted: May 26 — three paradigms (regularization/architectural/memory-based); forgetting spectrum; MOP as alternative to weight-level solutions
- **[[essa]]** promoted: Jul 15 — evolutionary score-based singular-value alignment; gradient-free; 6x faster scaling on 128 GPUs; ES variant over SVD spectrum
- **[[qes]]** promoted: Jul 15 — Quality-Evolutionary Search; accumulated error feedback for quantized fine-tuning; inference-level memory
- **[[neural-architecture-search]]** promoted: Jul 15 — comprehensive NAS hub page covering CoLLM-NAS, RZ-NAS, LLaMA-NAS, CMA-ES-driven search, zero-cost proxies
- **[[collm-nas]]** promoted: Jul 15 — dual-LLM Navigator/Generator; strategic exploration vs tactical generation; source: ml-evolution-benchmarking-protocol
- **[[rz-nas]]** promoted: Jul 15 — zero-cost proxies + reflection module; architecture evaluation without training; source: ml-evolution-benchmarking-protocol
- **[[parameter-efficient-fine-tuning]]** promoted: Jul 15 — full PEFT landscape: LoRA, QLoRA, AdaLoRA, DoRA, LoRA+, LoRA-FA; category hub for llm-training cluster
- **[[llama-nas]]** promoted: Aug 3 — one-shot sub-network search from pretrained LLaMA; inherits weights without retraining; compression as architecture search side effect; ml-evolution cluster complete

## Kanban Status
- [x] QLoRA standalone page → resolved this cycle (qora.md created)
- [x] NAMM upgrade → resolved 2026-05-26
- [x] continual-learning fill → resolved 2026-05-26
- [x] lora expansion → resolved 2026-05-26

### Open
- **bounded memory budget optimization**: still open from prior cycles — capacity/saturation theme; appears across QES/ESSA/LLaMA-NAS but no dedicated page
- **MOP vs fine-tuning boundary**: still open — entropy maximization vs KL regularization tension not fully developed; ramirez-ruiz-mop-2024 relationship to fine-tuning not articulated
- **Schema competition**: still open from prior cycles — needs meta-harness project context before filling
- **epistemic-energy stub**: status: stub, confidence 0.3, connects to top HITS authorities (maximum-occupancy-principle, efhf, world-model) — high-value upgrade candidate
- **bounded-rationality stub**: connects to agent-native-design and oMCD framework — may need oMCD project context

### Heading
- **[Intent]** Next priority: bounded memory budget optimization — appears across ml-evolution cluster (QES, ESSA, LLaMA-NAS all target memory efficiency) but no dedicated page; alternatively upgrade epistemic-energy (high authority connections)
- **[Constraint]** Stub count: 296 (was 297, net -1). PEFT cluster complete. ML-evolution cluster complete.
- **[Note]** QLoRA page created; PEFT cluster done. Next expansion: ml-evolution cluster was resolved Aug 3, PEFT cluster resolved May 26. Remaining open items all need project context (meta-harness, oMCD) or are cross-cluster (bounded memory, MOP boundary).