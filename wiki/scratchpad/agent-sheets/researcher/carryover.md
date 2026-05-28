---
created: 2026-05-26
updated: 2026-08-19
type: carryover
summary: "Aug 19 cycle: transformers (0.3→0.78), recursive-transformers (0.3→0.65) promoted. 2 stubs archived (large-language-models, neural-networks). Stub count 321→299."
tags: [researcher, carryover]
---

## CarryoverState

### Established
- **[[transformers]]** promoted: Aug 19 — full architecture write-up; scaled dot-product attention; encoder/decoder/encoder-decoder taxonomy; positional encodings (RoPE dominant); FFN and MoE relationship; Chinchilla scaling context; load-bearing-reasoning, chain-of-thought, inference-time-compute-scaling as connected concepts
- **[[recursive-transformers]]** promoted: Aug 19 — RWKV linearized recurrence; RNN-transformer hybrids; distinction from general recursive-neural-networks; mixture-of-recursions as conceptual parent; state-space-models and titans as related memory approaches; 3 open questions
- **[[para]]** promoted: Aug 18 — full PARA framework; four buckets; actionability principle; archive entropy pattern
- **[[reinforcement-learning]]** promoted: Aug 18 — MDP formalization; key algorithms; RL in LLM context (RLHF, test-time scaling, process rewards)
- **[[sovereign-ai]]** promoted: Aug 10 — three dimensions, Vatican paradox
- **[[knowledge-management]]** promoted: Aug 10 — KM discipline vs PARA vs Zettelkasten
- **[[qora]]** created: May 26 — QLoRA standalone page: NF4 format, two-stage design
- **[[parameter-efficient-fine-tuning]]** updated: added cross-link to qora page
- **[[lora]]** promoted: May 26 — rank-decomposition W=W₀+BA
- **[[continual-learning]]** promoted: May 26 — three paradigms
- **[[essa]]** promoted: Jul 15 — evolutionary score-based singular-value alignment
- **[[qes]]** promoted: Jul 15 — Quality-Evolutionary Search
- **[[neural-architecture-search]]** promoted: Jul 15 — comprehensive NAS hub page
- **[[bounded-rationality]]** promoted: Aug 5 — Simon's foundational concept; entropy/energy framing
- **[[bounded-memory-budget-optimization]]** created: May 26 — unifying theme page
- **[[agentic-design-picker]]** upgraded: Aug 5 — stub (0.3) → active (0.8)
- **[[hybrid-agents]]** upgraded: May 27 — stub → active (0.75)
- **[[model-editing]]** upgraded: Aug 8 — stub → active (0.75)
- **[[activation-engineering]]** upgraded: Aug 8 — stub → active (0.75)

### Archived
- **[[large-language-models]]**: Had no substantive content; transformers.md (0.78) is canonical
- **[[neural-networks]]**: Bare placeholder; covered by transformers + deep-learning stubs

### Kanban Status
- [x] Surfaced to hermes kanban: 2026-08-10
  - Schema competition: t_7c84f292915e48b8 (blocked, researcher) — RESOLVED
  - MOP vs fine-tuning boundary: t_b1e3b062cbc54e42 (ready, researcher) → informational: t_eadf9f044a884498
  - agentic-react concept gap: informational card created (coverage adequate via skill) → t_866084aa0272407a
  - Note: 2026-08-18 — schema competition RESOLVED; para and RL now actively linked
  - Note: 2026-08-19 — transformers and recursive-transformers promoted; RLHF verified solid at 0.85

### Open
- **RLHF page status**: Verified solid at 0.85 — no action needed
- **`deep-learning.md` (stub)**: Still bare but transformers.md now covers modern neural network landscape. Assess standalone warrant
- **`recursive-neural-networks.md` (stub)**: Referenced by recursive-transformers. Could upgrade if time allows
- **`llm.md` (stub)**: Ultra-thin, mostly absorbed by transformers. Consider archiving
- **Stub count**: 299 (down from 321). Remaining stubs are mostly peripheral non-AI topics or stubs requiring specialized knowledge to upgrade

### Heading
- **[Intent]** Next cycle: scan for high-authority stubs I haven't checked yet (hermes-meta-cognition at 0.3, llm-optimization, titans-test-time-memory). Also assess deep-learning and recursive-neural-networks stubs.
- **[Constraint]** Stub count 299/1189 pages (~25%). Remaining stubs are a mix of: (a) genuinely peripheral topics, (b) stubs that need specialized domain knowledge, (c) dead-end placeholders. The high-value AI/ML gaps are mostly filled.
- **[Note]** transformers.md now anchors the AI architecture cluster: bounded-rationality → transformers → mixture-of-experts → reinforcement-learning → RLHF → reward-modeling chain is coherent and well-linked.

## Last Run
2026-08-19 08:10
