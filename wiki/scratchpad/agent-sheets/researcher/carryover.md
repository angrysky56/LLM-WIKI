---
created: 2026-05-26
updated: 2026-05-27
type: carryover
summary: Researcher carryover — May 27 cycle: hybrid-agents upgraded (0.3→0.75), agent taxonomy cluster gap identified
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
- **[[agentic-design-picker]]** upgraded: Aug 5 — stub (0.3) → active (0.8). Decision framework: 6 evaluation axes, 5 coordination patterns (Pipeline/Supervisor-Worker/Peer-to-Peer/Blackboard/Hierarchical), decision tree, cross-pattern connections table, 3 open questions. Connects to multi-agent-llm-systems as design-time complement.
- **[[hybrid-agents]]** upgraded: May 27 — stub (0.3) → active (0.75). Full write-up: dual-process architecture (reactive + deliberative layers), routing mechanism, Kahneman dual process theory connection, MOP Layer 0/1, bounded-rationality, 4 open questions.

## Kanban Status
- [x] QLoRA standalone page → resolved May 26
- [x] NAMM upgrade → resolved 2026-05-26
- [x] continual-learning fill → resolved 2026-05-26
- [x] lora expansion → resolved 2026-05-26
- [x] bounded-rationality upgrade → resolved Aug 5 (stub 0.3 → active 0.75)
- [x] Bounded memory budget optimization → resolved (page already active 0.75)
- [x] mcp.md redundancy → resolved (redirect stub confirmed, canonical is mcp-model-context-protocol.md 0.85)
- [x] hermes-agent-skills → resolved (already active 0.85 with 63-skill inventory)
- [x] agentic-design-picker → t_5c1c25fc387d4bb8 (done, upgraded from stub)
- [x] hybrid-agents → resolved May 27 (stub 0.3 → active 0.75)
- [ ] MOP vs fine-tuning boundary → t_b1e3b062cbc54e42 (ready, med) — mop-and-rlhf-interaction.md open questions remain unresolved; all 3 resolution paths untested at scale
- [ ] Schema competition → still blocked — needs meta-harness project context

### Open
- **MOP vs fine-tuning boundary**: mop-and-rlhf-interaction.md (0.75) — entropy maximization vs KL regularization tension, 3 resolution paths identified but none tested at scale in MoE systems. Open empirical question: GRPO for MoE compatibility.
- **Schema competition**: still open — needs meta-harness project context before filling (blocked indefinitely)
- **agentic-react concept gap** (low priority): wikilink in reactive-agents.md points to non-existent concept page; only the skill at wiki/agents/skills/agentic-react/SKILL.md exists. Skill provides adequate coverage; concept page would be redundant.

### Heading
- **[Intent]** Next cycle: MOP vs fine-tuning boundary (t_b1e3b062cbc54e42) — needs external research on untested resolution paths, web-researcher appropriate
- **[Constraint]** Stub count: 49 (was 50, net -1 from hybrid-agents upgrade). Agent architecture cluster complete with one active and three adequate stubs. MOP boundary and schema competition remain as substantial open items.
- **[Note]** hybrid-agents upgrade complete. All major clusters resolved. MOP boundary requires external research (web-researcher appropriate) rather than internal wiki work.