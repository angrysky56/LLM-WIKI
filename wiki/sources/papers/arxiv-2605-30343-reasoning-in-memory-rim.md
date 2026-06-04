---
created: 2026-06-04T00:00:00Z
updated: 2026-06-04T00:00:00Z
type: source
summary: "Reasoning in Memory (RiM) — Aichberger & Hochreiter (JKU/NXAI): replaces autoregressive chain-of-thought with fixed latent memory blocks that the model processes in a single forward pass, matching or beating Coconut and CoT at SFT-w/o-CoT latency."
tags: [arxiv, paper, latent-reasoning, working-memory, bounded-representation-capacity, hochreiter, agents, bounded-self-model]
sources: https://arxiv.org/abs/2605.30343
status: active
confidence: 0.85
---

# Reasoning in Memory (RiM) — Aichberger & Hochreiter (2026)

> **One-line:** Use fixed special-token "memory blocks" inside the forward pass as a working-memory workspace, then read the answer only from the last block. Latent reasoning at the speed of direct answer SFT.

**arXiv:** 2605.30343 · 21 pages · JKU Linz (ELLIS Unit) + NXAI · Lukas Aichberger & Sepp Hochreiter (the LSTM inventor).

## Problem

Test-time-compute reasoning currently *requires* autoregressive token generation. Chain-of-thought, Coconut's continuous thoughts, and DART all pay latency proportional to the number of intermediate "steps". This couples **internal computation to external communication** — the model is forced to "think out loud" in natural language, which is optimized for transmission, not for manipulation. Human cognition has a separate channel (working memory) that holds and manipulates information internally. RiM asks: can an LLM learn to *use* such a working memory if we give it a latent workspace that doesn't require generation?

## Method

1. **Memory blocks.** Interleave fixed sequences of a single special token (`<m>`) between the question and answer. These tokens are *not generated* — they are part of the input, processed in a single forward pass, and discarded at decode time.
2. **Two-stage curriculum.**
   - **Stage 1 — grounding.** After each memory block, predict an explicit reasoning step. The blocks learn to *carry* intermediate computation by being forced to do so supervisedly.
   - **Stage 2 — refinement.** Discard step-level supervision. Keep only a final-answer loss applied after every block. The model is iteratively pushed to compress the intermediate reasoning into the block-internal hidden state.
3. **Inference.** At deployment, the answer is read from the *last* memory block. Compute cost is one forward pass over `(question, m₁, m₂, …, mₖ, answer)` — identical latency to SFT w/o CoT.

The key technical claim is that LLMs already have a working-memory capacity sitting dormant in their residual stream; RiM just unlocks it by giving the optimizer a place to *put* intermediate computation that doesn't have to be communicated.

## Results

| Model | Method | TTFT (ms) | GSM8K greedy | GSM-Hard (OOD) greedy |
|-------|--------|-----------|--------------|------------------------|
| GPT-2 | SFT w/o CoT | 7.6 | 15.4 | 3.5 |
| GPT-2 | Coconut | 53.4 | 31.1 | 7.1 |
| **GPT-2** | **RiM (final block)** | **7.6** | **33.6** | **7.8** |
| Llama-3.2-1B | SFT w/o CoT | 16.1 | 23.9 | 5.3 |
| Llama-3.2-1B | Coconut | 108.3 | 36.9 | 8.5 |
| **Llama-3.2-1B** | **RiM (final block)** | **16.1** | **42.1** | **10.5** |
| Llama-3.2-3B | SFT w/o CoT | 27.9 | 36.2 | 8.5 |
| Llama-3.2-3B | Coconut | 188.8 | 41.3 | — |
| **Llama-3.2-3B** | **RiM (final block)** | **27.9** | **~43** | **~12** |

**Latency parity (Table 7, GSM8K, Llama-3.2-1B):**
- SFT w/o CoT: 3.1 tokens, 126.0 ms
- SFT w/ CoT: 36.7 tokens, 1108.7 ms (+982.7)
- Coconut: 3.1 tokens, 304.7 ms (+178.7)
- **RiM: 3.1 tokens, 126.5 ms (+0.5)** — essentially free vs. direct SFT.

RiM matches or beats Coconut on all four comparable settings *while matching SFT-w/o-CoT latency*. The gap to CoT remains in absolute accuracy, but CoT pays for that accuracy with 9× latency.

## Limitations

- The latent workspace is bounded by the residual stream's working-memory capacity — there is a wall the method cannot push past, evidenced by Stage 2's refinement plateau. The paper does not characterize that wall.
- Training is two-stage and the curriculum schedule is a hyperparameter; the paper sweeps but does not give a principled derivation.
- The memory blocks are uninterpretable — they are not the same as interpretable scratchpads. Any safety/audit story is harder.
- All evaluations on math (GSM8K, GSM-Hard). Generalization to non-math reasoning, code, or open-ended generation is not yet demonstrated.

## Wiki Connections

- **[[bounded-self-model]]** (current theme): RiM is the *compute-side* counterpart to last cycle's three memory papers. Where [[sleep-self-modify-consolidate-2026]] adds capacity for *storage*, [[faithful-confidence-lrm-2026]] quantifies the model's gap on *knowing what it knows*, and [[skill-rm-2026]] externalises evaluation as a resource — RiM shows the model can be *trained to use* the bounded working-memory capacity it already has, for computation rather than storage. The unifying claim: the residual stream is a bounded workspace; everything is about how to *allocate* it.
- [[bounded-representation-capacity]]: RiM is a clean example of the same total budget, used differently. Coconut spends the budget on generated continuous thoughts; RiM spends it on input-side fixed blocks. Both use ~equal capacity; RiM is far cheaper at inference.
- [[latent-reasoning]] / [[coconut]] / [[continuous-thoughts]]: direct lineage. RiM is the first to show the compute saving is achievable *without* paying a generation cost per step.
- [[markovian-thinker]] (from Synapse memories): both pursue *linear compute in thinking tokens, constant memory by design*. RiM achieves it via fixed blocks, Markovian Thinker via chunked state. Two engineering paths to the same theoretical point.
- [[hochreiter]] (Sepp Hochreiter = LSTM inventor): his continued advocacy of *bounded recurrent state* is the throughline from the 1997 LSTM constant-error-carousel to this 2026 working-memory block.
- [[metacognition-llm]]: a method for "thinking without speaking" is exactly the kind of metacognitive control the bounded-self-model theme predicts is necessary.
- **Future synthesis candidate:** "Working memory in LLMs" — covers RiM (compute), Sleep/CMR (storage), the 1997 LSTM constant-error-carousel (historical lineage), Markovian Thinker (state-bounded), and the bounded-self-model cross-cycle thread.

## Key Quote

> "These results demonstrate that large language models can be trained to use working memory as an effective mechanism for latent reasoning." — Aichberger & Hochreiter, abstract

### Cross-cycle (2026-06-03 batch)
- **RiM ↔ [[sleep-self-modify-consolidate-2026]]:** Sleep adds parameter capacity (memory blocks *grow* the model). RiM trains the model to *use* the existing residual-stream working memory. Sleep's `expert_block` is a parameter-space analogue of RiM's `m`-token memory block. The unifying claim: the residual stream is a bounded workspace; Sleep grows the budget, RiM allocates it.
- **RiM ↔ [[skill-rm-2026]]:** Skill-RM externalises evaluation as a multi-step evidence trace. RiM internalises reasoning as fixed memory blocks. Two opposite moves on the same "internalise-vs-externalise" axis.
- **RiM ↔ [[faithful-confidence-lrm-2026]]:** FC shows LRMs are unfaithful in expressing their intrinsic confidence. RiM removes the *externalised* reasoning trace entirely. If you combine the two — a latent-reasoning model that uses RiM-style memory blocks — the FC problem gets *worse*, because the intermediate steps (and any signal about their confidence) are now invisible.
