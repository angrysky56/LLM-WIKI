# Researcher Discovery Report — 2026-05-22

## Discovery Cycle
- Topics researched: 4
- New pages created: 3
- Pages updated: 0
- Cross-links added: ~15 (via new pages)

## New Entries

### 1. [[constitutional-ai]]
**Constitutional AI** — Anthropic's alignment technique using AI-generated self-critique and principle-based revision instead of human-labeled preference data.

Key coverage:
- SL-CAI and RLAIF phases — self-critique loop replacing human labels
- The constitution: UDHR + ethical guidelines + dialogue principles
- Comparison table: CAI vs RLHF across scalability, interpretability, harm reduction
- Limitations: self-critique inherits model biases, constitution quality matters
- Relationship to metacognitive architecture and process reward models

*Why this matters*: The carryover flagged this as the most actionable missing piece. It's directly relevant to alignment work in the wiki. Three open questions remain about constitution design, cross-model transfer, and the ethical framework.

### 2. [[length-generalization]]
**Length Generalization** — the failure of LLMs to generalize from short training sequences to longer inference sequences.

Key coverage:
- Problem taxonomy: position collapse, repetition, attention budget mismatch
- Root causes: positional encoding limitations, KV cache distribution shift
- Research directions: ALiBi, RoPE, Position Interpolation, YaRN, memory-augmented approaches
- Why it matters for Hermes/LLM-WIKI: agentic loops, long documents, cross-session memory

*Why this matters*: This was a flagged gap from the May 21 report. It connects directly to chain-of-thought (which generates long sequences), neural-long-term-memory, and load-bearing reasoning. The open questions probe whether there's a theoretical limit and how it interacts with reasoning.

### 3. [[self-correction]]
**Self-Correction in LLMs** — the capability to detect, critique, and revise own outputs.

Key coverage:
- Taxonomy: implicit (emergent) vs explicit (structured loop) self-correction
- Self-Refine pattern: generate → critique → revise → iterate
- Implementations: RAA hypothesis, self-verification, Reflexion framework
- Interaction with CoT: CoT enables self-correction, self-correction can restart CoT
- Limitations: self-trust bias, same-model blind spots, compute cost

*Why this matters*: Self-correction is central to agentic systems — catching a bad tool call before it happens vs. correcting output. The page connects to metacognitive architecture (formal version of the same idea), PRM, and agentic research.

## Gap Analysis

### Still thin or missing
1. **Verifier-graph theory** — flagged May 21; the entity page exists but no concept page explaining the theory. Needs Ty input on whether it should be synthesis or concept.
2. **MOP fine-tuning** — MoE fine-tuning is hard; worth a dedicated concept or should it be left as a research note?
3. **Test-time compute economics** — the inference-time-compute-scaling page lacks economic analysis. Important for Hermes deployment decisions (flagged in carryover).
4. **Hybrid reward models** — combining ELHSR (hidden-state) with SD-Search (process-level) — emerging research direction.

## Open Questions

1. **Verifier-graph classification**: Should the theory be a `concept` or `synthesis`? It's Ty's original work. Flagged May 21 and still unresolved.
2. **Constitutional AI scope**: Should it be a standalone alignment concept or folded into a broader alignment page? The principles-based approach is meaningfully different from RLHF.
3. **Test-time compute economics**: Missing from inference-time-compute-scaling. Critical for real-time deployment decisions.

## Cross-Links Added

New pages connect to existing concepts:
- constitutional-ai → reward-modeling, alignment, metacognitive-architecture, process-reward-model
- length-generalization → chain-of-thought, neural-long-term-memory, hidden-states, load-bearing-reasoning
- self-correction → metacognitive-architecture, chain-of-thought, process-reward-model, load-bearing-reasoning, agentic-research

---

*Next run scheduled: Monday 2026-05-26 8:30AM*