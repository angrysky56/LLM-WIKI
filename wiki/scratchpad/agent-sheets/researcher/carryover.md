---
created: 2026-05-26
updated: 2026-08-05
type: carryover
summary: Researcher carryover — May 26 cycle: bounded-memory-budget-optimization created, PEFT cluster now complete
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
- **[[bounded-rationality]]** promoted: Aug 5 — full write-up: Simon's foundational concept; connection to epistemic-energy, MOP, EFHF, agent-native-design; structural vs budgetary bounds; satisficing vs optimizing
- **[[bounded-memory-budget-optimization]]** created: May 26 — unifying theme page for QES/ESSA/LLaMA-NAS cluster; memory as bounded resource; saturation effects; memory-aware architecture search; evolutionary score alignment; five open questions

## Kanban Status
- [x] QLoRA standalone page → resolved May 26
- [x] NAMM upgrade → resolved 2026-05-26
- [x] continual-learning fill → resolved 2026-05-26
- [x] lora expansion → resolved 2026-05-26
- [x] bounded-rationality upgrade → resolved Aug 5 (stub 0.3 → active 0.75)
- [x] Bounded memory budget optimization → t_a99e34b5260844d8 (done May 26)
- [ ] MOP vs fine-tuning boundary → t_b1e3b062cbc54e42 (ready, med)
- [ ] Resolve mcp.md redundancy → t_c1872eebfab24100 (ready, high)
- [ ] hermes-agent-skills stub → t_5c1c25fc387d4bb8 (ready, med)

### Open
- **MOP vs fine-tuning boundary**: entropy maximization vs KL regularization tension not fully developed; ramirez-ruiz-mop-2024 relationship to fine-tuning not articulated
- **Schema competition**: still open — needs meta-harness project context before filling (blocked indefinitely)
- **mcp.md redundancy**: mcp.md is stub (0.3) but mcp-model-context-protocol.md is active (0.85) — duplicate; needs redirect or deletion
- **hermes-agent-skills**: stub (0.3) connected to hermes-agent — needs skills inventory context before filling

### Heading
- **[Intent]** Next priority: either (1) mcp.md redirect to mcp-model-context-protocol.md or (2) bounded memory budget optimization page
- **[Constraint]** Stub count: 295 (was 296, net -1). PEFT cluster complete. ML-evolution cluster complete.
- **[Note]** epistemic-energy in carryover is stale — page is already active (0.8), not stub. mcp.md is a redundant stub. Next cycle: resolve mcp.md or tackle bounded memory.