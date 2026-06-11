---
created: 2026-06-11T00:00:00Z
updated: 2026-06-11T00:00:00Z
type: source
summary: Recoverable Visual Token Routing for Vision-Language Models — rethinking visual token reduction as a routing problem with recovery, instead of irreversible removal
tags: [vision-language-model, vlm, token-routing, visual-tokens, kv-cache, multimodal, efficiency]
sources: https://arxiv.org/abs/2606.12412
status: active
confidence: 0.85
---

# Reroute, Don't Remove: Recoverable Visual Token Routing for Vision-Language Models

> Yang, C-Y., Lo, S-Y., Liu, Y-L. (2026). Reroute, Don't Remove: Recoverable Visual Token Routing for Vision-Language Models. arXiv:2606.12412.

## Problem

Vision-language models (VLMs) project images into hundreds to thousands of visual tokens, making decoder inference expensive in both attention computation and KV-cache memory. Existing visual-token reduction methods follow a **rank-and-remove** paradigm: they score visual tokens by importance, keep a compact subset, and permanently discard the rest.

The critical flaw: **visual-token importance changes across decoder depth**. A token ranked low in early layers may become highly relevant in later layers as the model builds context. But irreversible removal means these tokens are gone forever. This fragility means current methods either (a) keep too many tokens (reducing efficiency gain) or (b) discard potentially useful information (reducing quality).

## Method

**Recoverable Visual Token Routing** reframes token reduction as a routing problem instead of a destruction problem:

1. **Token scoring**: At each decoder layer, a lightweight scoring module evaluates the importance of each visual token given the current context.

2. **Active vs. standby routing**: Instead of discarding low-scoring tokens, the system maintains two groups:
   - **Active tokens**: Participate in full attention computation (keeps the compute budget low).
   - **Standby tokens**: Compressed representation stored in a compact form (not discarded — just paused).

3. **Recovery mechanism**: A routing gate at each layer decides which standby tokens should be reactivated based on the evolving context. Tokens are moved between active and standby pools dynamically across layers.

4. **Compression during standby**: Standby tokens are compressed via lightweight linear projection to minimize memory footprint, but retain enough information for meaningful recovery when reactivated.

This creates a **recoverable routing** mechanism where the model naturally learns which visual information to prioritize at each stage of decoding, without permanent information loss.

## Key Results

- **KV-cache reduction**: Achieves comparable or better VLM quality while using 40-60% fewer visual tokens in the active set.
- **Quality preservation**: Matches or exceeds full-token baselines on VQA, captioning, and multimodal reasoning benchmarks — outperforms rank-and-remove methods that discard the same number of tokens permanently.
- **Adaptive routing**: Analysis shows the recovery mechanism is actively used — tokens routinely move between active and standby pools across layers, confirming the paper's premise that token importance is depth-dependent.
- **Inference speedup**: 1.5-2x wall-clock speedup in decoder inference due to reduced attention computation at each layer.

## Key Quote

> "Visual-token importance changes across decoder depth; tokens ranked low at one stage may become relevant later."

## Limitations

- Requires a routing gate and scoring module at each layer — adds architectural complexity.
- Standby token compression introduces minor quality loss (though much less than permanent removal).
- Routing overhead partially offsets compute gains from reduced attention — net gain is significant but less than naive token-count reduction would suggest.
- Evaluated on VLM architectures with visual encoders (CLIP-style) — applicability to other multimodal architectures (e.g., tokenized video, audio) unverified.
- Recovery mechanism's computational overhead per layer means the approach is most beneficial for models with many decoder layers (depth > 16).

## Connections

- [[vision-language-model]] — The target architecture
- [[kv-cache]] — Key-value cache, the primary memory bottleneck being addressed
- [[multi-modal-llm]] — Broader class of models benefiting from this approach
- [[attention-efficiency]] — Related work on sparse attention, token pruning
- [[llm-inference-optimization]] — Practical deployment concern
- **Theme connection**: VToken Routing imposes **structured information flow** (active/standby routing with recovery) — the third paper in this cycle showing that structured inductive biases (MPI's geometric alignment, APPO's procedural credit, VToken's recoverable routing) outperform unstructured or irreversible approaches

## Related Work

| Approach | Difference |
|----------|-----------|
| Token pruning (e.g., ToMe, EViT) | Irreversible removal — no recovery mechanism |
| Sparse attention (Kitaev et al., 2020) | Reduces attention computation differently — doesn't address visual token count |
| Cross-attention compression | Compresses at encoder level — doesn't adapt across decoder layers |
| Multi-resolution VLMs | Different input strategy — doesn't address per-layer routing |
| Adaptive computation (Mixtral-style MoE for vision) | Expert-level rather than token-level routing |