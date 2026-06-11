---
summary: Official model card for DiffusionGemma, Google DeepMind's open diffusion language model — covering architecture (MoE, encoder-decoder), benchmark results, capabilities, data, and best practices.
tags: [diffusion-models, gemma, google-deepmind, model-card, moe]
updated: 2026-06-11T12:43:05Z
created: 2026-06-11T12:43:05Z
---

Source: [Google AI for Developers](https://ai.google.dev/gemma/docs/diffusiongemma/model_card)

## Model Overview

DiffusionGemma is Google DeepMind's open diffusion language model. It uses a **Mixture-of-Experts (MoE)** architecture with 8 active experts out of 128 total, providing strong reasoning while maintaining low memory footprint suitable for local execution.

## Architecture

- **Encoder-decoder** design: encoder processes prompt and generates KV cache (incremental prefill); decoder uses bidirectional attention over an input block ("canvas") of tokens via cross-attention.
- Supports **vision-language** tasks — processes images, video as frames (up to 60s at 1fps).
- Uses **Uniform State Diffusion**: random tokens replace original words rather than `[MASK]`, allowing corrections at every step.

## Capabilities

- Text generation with low-latency diffusion
- Multimodal: vision, language, audio understanding
- 140+ languages in training data
- Strong on reasoning, coding, and creative tasks

## Benchmark Results

Significant improvements over Gemma 3/3n in:
- Content safety across all categories
- Unjustified refusal rates (kept low while improving safety)
- Raw capabilities tested without safety filters

## Model Data

- Pre-training cutoff: January 2025
- Large-scale diverse collection: web documents, code, images, audio
- Sensitive data filtering applied

## Best Practices

- Standard `system`/`assistant`/`user` chat roles with thinking control tokens
- Image content placed **before** text in prompts for multimodal inputs
- Standardized sampling configuration recommended across all use cases

## Connections

- [[diffusiongemma]]
- [[gemma]]
- [[non-autoregressive-generation]]
- [[google-deepmind]]
