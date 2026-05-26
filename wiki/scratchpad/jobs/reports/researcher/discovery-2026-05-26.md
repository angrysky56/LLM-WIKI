# Researcher Discovery Report — 2026-05-26

## Discovery Cycle
- Topics researched: 3
- New pages created: 0
- Pages updated: 3 (namm, continual-learning, lora — all upgraded from stub to active)
- Cross-links added: ~30+

## New/Updated Entries

### NAMM (upgraded stub → active)
- Read ml-evolution-benchmarking-protocol source
- Wrote full concept page covering: definition, mechanism, Control LLM comparison table, training signals, limitations
- Connections: kv-cache, llm-inference, catastrophic-forgetting, control-llm, namm, maximum-occupancy-principle, bounded-structured-memory
- 4 open questions on learned vs heuristic tradeoffs, cross-task transfer, combining with Control LLM

### Continual Learning (upgraded empty stub → active)
- Wrote comprehensive concept page: three paradigms (regularization, architectural, memory-based), the forgetting spectrum, MOP relationship, LLM training connections
- 5 open questions on task boundary detection, compositional generalization, compress vs freeze, interference-structure relationship, selective forgetting
- Connections: catastrophic-forgetting, control-llm, namm, llm-training, mop-architecture, ramirez-ruiz-mop-2024, bounded-structured-memory, mixture-of-experts, parameter-efficient-fine-tuning

### LoRA (upgraded thin stub → active)
- Wrote full concept page: definition, mechanism (W=W₀+BA decomposition), rank selection table, LoRA+ / QLoRA / AdaLoRA / DoRA variants, PEFT comparison
- Connections: parameter-efficient-fine-tuning, fine-tuning, qora, mixture-of-experts, catastrophic-forgetting, llm-training, control-llm, continual-learning

## Gap Analysis

**ml-evolution source cluster** (from carryover):
- namm ✅ DONE this cycle
- collm-nas — still stub, referenced in ml-evolution source
- essa — still stub
- qes — still stub
- rz-nas — still stub (LLaMA-NAS reference in source may not have a wiki page)

**llm-training cluster** (from carryover):
- continual-learning ✅ DONE this cycle
- lora ✅ DONE this cycle
- peft/parameter-efficient-fine-tuning — still thin stub (~21 lines)
- fine-tuning — moderate coverage, could use expansion
- qora — mentioned in LoRA page, needs actual concept page

**Remaining thin pages from prior cycles**:
- Control-llm and catastrophic-forgetting are firmly established (Jul 20)
- Bounded-structured-memory, mop-architecture well-developed

## Open Questions
- PEFT cluster (peft, qora) — next priority after ml-evolution cluster
- rlhf/grpo relationship to forgetting — not deeply covered
- Schema competition in MOP — unresolved from prior cycles

## Index Updates
- continual-learning: [STUB] removed, summary updated
- lora: blank summary filled, [STUB] removed  
- namm: summary updated to reflect active status

## Stub Count
- Start: 307 (from carryover)
- End: 304 (net -3 from 3 upgrades)
- Note: 3 pages upgraded from stub to active this cycle