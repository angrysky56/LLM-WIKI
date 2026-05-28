---
created: 2026-05-26
updated: 2026-08-10
type: carryover
summary: Aug 10 cycle: upgraded sovereign-ai (0.3→0.75), knowledge-management (0.3→0.75), knowledge-architecture (0.3→0.7); stub count 325→323, active 213→216
tags: [researcher, carryover]
---

## CarryoverState

### Established
- **[[sovereign-ai]]** promoted: Aug 10 — three dimensions (compute/model/governance sovereignty), no nation has achieved full sovereign AI, Vatican paradox, three open questions. Links to ai-policy-global-governance, semiconductor-geopolitics, china-industrial-policy, bounded-rationality.
- **[[knowledge-management]]** promoted: Aug 10 — KM discipline vs PARA framework vs Zettelkasten methodology; graph-based KM as technical implementation; organizational vs PKM; open questions on retention policy and sovereign AI intersection. Links to zettelkasten, para, knowledge-store, information-architecture, bounded-structured-memory.
- **[[knowledge-architecture]]** (entity) promoted: Aug 10 — structural design decisions at system level; four dimensions (granularity/topology/temporal/logical/ownership); bottom-up vs top-down; connections to agent memory. Links to knowledge-management, information-architecture, bounded-structured-memory.
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
- **[[agentic-design-picker]]** upgraded: Aug 5 — stub (0.3) → active (0.8). Decision framework: 6 evaluation axes, 5 coordination patterns, decision tree, cross-pattern connections table, 3 open questions.
- **[[hybrid-agents]]** upgraded: May 27 — stub (0.3) → active (0.75). Full write-up: dual-process architecture, Kahneman dual process theory, MOP Layer 0/1, 4 open questions.
- **[[model-editing]]** upgraded: Aug 8 — stub (0.3) → active (0.75). Full write-up: ROME, Knowledge Neurons, TransformerPatch; gradient-based; temporal binding; scalability.
- **[[activation-engineering]]** upgraded: Aug 8 — stub (0.3) → active (0.75). Full write-up: CAA, PID Steering, SADI, EAST, Dynamic Activation Composition; layer selection problem.

## Kanban Status
- [x] Surfaced to hermes kanban: 2026-08-10
  - Schema competition: t_7c84f292915e48b8 (blocked, researcher) — RESOLVED
  - MOP vs fine-tuning boundary: t_b1e3b062cbc54e42 (ready, researcher) → informational: t_eadf9f044a884498
  - agentic-react concept gap: informational card created (coverage adequate via skill) → t_866084aa0272407a
  - Note: agentic-react concept gap — no kanban card needed (coverage adequate via skill)

### Open
- **MOP vs fine-tuning boundary**: mop-and-rlhf-interaction.md (0.75) — entropy maximization vs KL regularization tension, 3 resolution paths identified but none tested at scale in MoE systems. Open empirical question: GRPO for MoE compatibility. web-researcher appropriate.
- **Schema competition**: t_7c84f292915e48b8 — **RESOLVED.** Concept page created: `wiki/concepts/schema-competition.md`. Links to ramirez-ruiz-mop-2024, bounded-structured-memory, knowledge-pack, meta-harness.
- **Stub count**: 323 (was 325). Three stubs upgraded: sovereign-ai, knowledge-management, knowledge-architecture. No new stubs created.
- **para.md**: still stub (0.3); covered by knowledge-management but dedicated page would improve cluster depth
- **note-taking-systems entity**: still stub (0.3); covered by knowledge-management but entity page may be appropriate

### Heading
- **[Intent]** Next cycle: para page upgrade (from 0.3 stub), then MOP boundary empirical validation via web-researcher
- **[Constraint]** Stub count 323/213 active — major concept clusters complete. Remaining gaps are either: (a) covered by existing pages, (b) empirical open items requiring web research, or (c) peripheral topics outside core AI/ML focus
- **[Note]** AI policy cluster (federalism, sovereign-ai) integrated into governance cluster. Knowledge management cluster now has proper hub pages.

## Last Run
2026-08-10 08:10