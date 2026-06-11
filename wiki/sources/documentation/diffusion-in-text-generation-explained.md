---
summary: Google DeepMind explains how text-based diffusion works in DiffusionGemma — covering masked diffusion, uniform state diffusion, self-conditioning, and multi-canvas sampling for non-autoregressive generation.
tags: [diffusion-models, gemma, google-deepmind, text-generation, non-autoregressive]
updated: 2026-06-11T12:39:59Z
created: 2026-06-11T12:39:59Z
---

Source: [Google AI for Developers](https://ai.google.dev/gemma/docs/diffusiongemma/explained)

## Overview

This article explains why DiffusionGemma moves away from traditional autoregressive generation and how text diffusion works under the hood.

## Key Concepts

- **Autoregressive bottleneck**: Standard LLMs generate one token at a time, creating a latency bottleneck. While batching masks this at the system level, individual users see no speedup.
- **Memory-bound problem**: For smaller batch sizes, hardware spends most time waiting on memory transfers rather than computation — a core inefficiency addressed by diffusion-based generation.

## Diffusion Methods

- **Masked Diffusion**: Tokens are replaced with `[MASK]` tokens and progressively denoised. Limitation: once replaced, tokens cannot be corrected in later steps.
- **Uniform State Diffusion**: Instead of masking, tokens are replaced with **random tokens** from the vocabulary. This allows corrections at every step since no token is permanently locked.

## Architecture

- **Incremental Prefill**: The encoder processes the prompt and generates the KV cache.
- **Bidirectional Attention**: The decoder processes an entire block ("canvas") of tokens simultaneously, accessing context via cross-attention.

## Inference Frameworks

- **Self-Conditioning**: The model uses its own intermediate predictions as input for the next denoising step.
- **Multi-Canvas Sampling (Block Diffusion)**: Multiple independent canvases are denoised in parallel and stitched together, enabling efficient batch generation.

## Connections

- [[diffusiongemma]]
- [[gemma]]
- [[non-autoregressive-generation]]
