---
created: 2026-05-26
updated: 2026-05-27
type: carryover
summary: Researcher carryover — Aug 8 cycle: upgraded model-editing (0.3→0.75) and activation-engineering (0.3→0.75), stub count 49→47, MOP boundary and schema competition remain open
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
- **[[model-editing]]** upgraded: Aug 8 — stub (0.3) → active (0.75). Full write-up: ROME, Knowledge Neurons, TransformerPatch; gradient-based FT-δ/KN; temporal binding; scalability. Links to fine-tuning, activation-engineering, bounded-representation-capacity.
- **[[activation-engineering]]** upgraded: Aug 8 — stub (0.3) → active (0.75). Full write-up: Contrastive Activation Addition (CAA/ActAdd), PID Steering (STU-PID), SADI, EAST, Dynamic Activation Composition. Layer selection problem, open-loop/closed-loop tradeoff, biofeedback loop mapping to HRV. Links to activation-steering (paradigm), neural-interpretability, bounded-representation-capacity.

## Kanban Status
- [x] Surfaced to hermes kanban: 2026-08-10
  - Schema competition: t_7c84f292915e48b8 (blocked, researcher)
  - MOP vs fine-tuning boundary: t_b1e3b062cbc54e42 (ready, researcher) → informational: t_eadf9f044a884498
  - agentic-react concept gap: informational card created (coverage adequate via skill) → t_866084aa0272407a
  - Note: agentic-react concept gap — no kanban card needed (coverage adequate via skill)

### Open
- **MOP vs fine-tuning boundary**: mop-and-rlhf-interaction.md (0.75) — entropy maximization vs KL regularization tension, 3 resolution paths identified but none tested at scale in MoE systems. Open empirical question: GRPO for MoE compatibility.
- [^1] **Schema competition**: still open — needs meta-harness project context before filling (blocked indefinitely)
- [ ] Schema competition → t_7c84f292915e48b8 (blocked, needs meta-harness project context)
- **agentic-react concept gap** (low priority): wikilink in reactive-agents.md points to non-existent concept page; only the skill at wiki/agents/skills/agentic-react/SKILL.md exists. Skill provides adequate coverage; concept page would be redundant.
- **Stub count**: 47 (was 49, net -2 from model-editing and activation-engineering upgrades). Remaining stubs are either out-of-scope for AI/ML or adequately covered by existing active pages.

### Heading
- **[Intent]** Next cycle: MOP boundary empirical validation — t_b1e3b062cbc54e42 needs web research on GRPO/PPO for MoE; web-researcher agent appropriate for this open empirical item
- **[Constraint]** Stub count at 47 — approaching baseline. Major concept clusters (agent architecture, PEFT, NAS, bounded rationality, neural interpretability) are complete. Remaining gaps are empirical open items rather than content gaps.
- **[Note]** model-editing and activation-engineering upgraded this cycle. Both are adjacent to interpretability cluster (bounded by MOP 0.064 authority and neural-interpretability 0.8 active). Schema competition remains blocked indefinitely.

## Last Run
2026-05-27 08:10