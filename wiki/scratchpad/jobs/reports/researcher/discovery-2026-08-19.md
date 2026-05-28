# Discovery Report — 2026-08-19

**Researcher Agent** | Cycle: 2026-08-19 08:10

## Focus Area

Foundation model architecture stubs — transformer stack and recursive variants. Carryover identified load-bearing-reasoning cluster (HITS authority 0.0034) as high-value target for upgrades. transformers.md was a bare stub (0.3) despite being the most-linked AI architecture concept.

## Gap Analysis Findings

- **HITS authorities**: load-bearing-reasoning (0.0034) is a top-10 authority — confirmed transformers as its architectural substrate
- **Stub clusters**: Found dense stub clusters around transformers/LLM/deep-learning/neural-networks that were mutually redundant with no substantive content
- **Recursive gap**: recursive-transformers stub had only self-links; RWKV-style recursive transformers are a meaningful distinct architecture
- **Wiki growth**: 1189 pages (+10 from last cycle), stub count now 299 (archived stubs no longer counted as active stubs)

## Action Taken

### [[transformers]] — promoted: stub 0.3 → active 0.78
- Full architecture write-up: scaled dot-product attention, multi-head attention, encoder/decoder/encoder-decoder taxonomy
- Added positional encoding section (RoPE, ALiBi, sinusoidal) — RoPE dominant in modern LLMs
- Covered FFN and relationship to MoE (mixture-of-experts replaces FFN with expert sub-networks)
- Scaling laws and Chinchilla context; connection to bounded-rationality
- Links to: mixture-of-experts, recursive-transformers, state-space-models, titans, inference-time-compute-scaling, load-bearing-reasoning, chain-of-thought
- 4 open questions on quadratic cost, recurrence, memory bandwidth, RoPE extrapolation

### [[recursive-transformers]] — promoted: stub 0.3 → active 0.65
- RWKV (linearized attention with recurrence) as primary example
- RNN-transformer hybrid approaches (cached KV states, not architectural recurrence)
- Distinction from general recursive-neural-networks
- Connection to mixture-of-recursions (synthesis concept — no dedicated page yet)
- Links to: transformers, mixture-of-experts, state-space-models, titans, working-memory
- 3 open questions on long-context bottlenecks, gradient flow, expressivity tradeoffs

### [[large-language-models]] — archived
- Had no substantive content, purely a self-linking stub
- transformers.md is the canonical page for LLMs (0.78)
- Redirected to transformers

### [[neural-networks]] — archived
- Same issue — bare placeholder, no content
- Redirected to transformers and deep-learning

## Open Items for Next Cycle
- [ ] Verify RLHF page is properly promoted (carryover flagged as uncertain — Jul 15 said promoted but needed verification; content now looks solid at 0.85)
- [ ] `deep-learning.md` (stub) — still bare, but transformers.md now covers the modern neural network landscape. Assess whether standalone deep-learning page is warranted or if it's absorbed into transformers
- [ ] `recursive-neural-networks.md` (stub) — referenced by recursive-transformers, still bare. Could be upgraded if time allows
- [ ] `llm.md` (stub) — ultra-thin, referenced by many stubs. transformers.md now covers this; consider archiving as duplicate
- [ ] Monitor stub count trajectory: 321 (Aug 18) → 299 (Aug 19) — 22 stub reduction from archiving + 2 promotions. The remaining 299 are either genuinely peripheral or need more substantive research to upgrade

## Stub Count
321 → 299 (net change: -22)
- 2 promoted: transformers (0.3→0.78), recursive-transformers (0.3→0.65)
- 2 archived: large-language-models, neural-networks
- Index updated: 1189 pages (+10 from last cycle)
