---
created: 2026-05-26
updated: 2026-07-20
type: carryover
summary: Researcher carryover — Jul 20 cycle: 2 pages upgraded (control-llm, catastrophic-forgetting), stub count 307
tags: [researcher, carryover]
---

## CarryoverState

### Established
- **[[control-llm]]** promoted: Jul 20 — architectural mitigation (layer bifurcation into frozen/trainable branches), vs EWC/rehearsal/MoE comparison, 4 open questions; from ml-evolution-benchmarking-protocol source
- **[[catastrophic-forgetting]]** promoted: Jul 20 — weight interference/representational drift/gradient misalignment mechanisms; LLM failure modes; 3-level mitigation table; MOP as alternative paradigm (offload vs overwrite); 10 connections; 4 open questions
- All prior established items from Jul 14 carryover remain valid (MOP cluster, agent cluster, bounded-structured-memory, etc.)

### Open
- **[[namm]]**: Next priority — stub, from same ml-evolution source as control-llm; NAMM = learned KV cache retention vs Control LLM's architectural bifurcation; complementary or competing?
- **[[continual-learning]]**: Marked stub in index but has no page content at all — high-value gap; connects catastrophic-forgetting/MoE/MOP/llm-training
- **[[lora]]**: Very thin (16 lines) but well-connected to PEFT and fine-tuning
- **Bounded memory budget optimization**: How should total memory budget be distributed across layers? Principled method or empirical tuning?
- **MOP vs fine-tuning boundary**: When compress to memory vs weights? What determines the appropriate path?
- **Schema competition**: When new info conflicts with existing MOP schemas, how does the agent resolve without cascading inconsistency?

### Heading
- **[Intent]** Next priority: NAMM (ml-evolution source, complementary to control-llm), then fill [[continual-learning]] (empty stub), then lora expansion
- **[Constraint]** Stub count: 307 (was 309, net -2 from 2 upgrades). Focus on ml-evolution-benchmarking-protocol cluster (namm, collm-nas, rz-nas, essa, qes) and llm-training cluster (continual-learning, lora, peft).
- **[Note]** control-llm and catastrophic-forgetting now firmly embedded in llm-training cluster with 7-10 cross-links each. NAMM is the natural next fill from the same source.
