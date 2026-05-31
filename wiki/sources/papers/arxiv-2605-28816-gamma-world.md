---
created: 2026-05-31
updated: 2026-05-31
type: source
summary: Gamma-World enables generative multi-agent video world modeling with permutation-symmetric agent encoding and sparse hub attention, scaling beyond two players.
tags: [paper, arxiv, research, world-model, multi-agent, video-generation]
---

# Gamma-World: Generative Multi-Agent World Modeling Beyond Two Players

**arXiv:** [2605.28816](https://arxiv.org/abs/2605.28816) | **Authors:** Liu et al. (NVIDIA, Tsinghua, U Toronto) | **Date:** 2026-05-27

## Overview

World models for interactive video generation have largely focused on single-agent settings. Gamma-World (γ-World) extends world modeling to multi-agent environments where multiple players, robots, or embodied agents act simultaneously within a shared space.

## Core Contribution: Simplex Rotary Agent Encoding

The key innovation is a parameter-free extension of 3D RoPE (Rotary Position Embedding) called **Simplex Rotary Agent Encoding**. Agents are represented as vertices of a regular simplex in rotary angle space, giving each agent a distinct phase while making all agents permutation-equivalent. This avoids learned per-slot identities or fixed agent ordering, enabling the model to scale from two to four players without retraining.

## Sparse Hub Attention

Dense all-to-all attention across agents scales quadratically. γ-World proposes **Sparse Hub Attention**, where learnable hub tokens mediate token-interaction across agents, reducing cross-agent attention cost from O(n²) to O(n).

## Causal Distillation for Real-Time Rollout

For real-time generation at 24 FPS, the full-context diffusion teacher is distilled into a causal student that generates temporal blocks sequentially with KV caching, enabling action-responsive generation.

## Key Results

- Improves video fidelity, action controllability, and inter-agent consistency over slot-based and dense-attention baselines
- Generalizes from 2 to 4 players without additional training

## Related

- [[world-models]] — general concept
- [[video-generation]] — generation pipeline background
- [[multi-agent-systems]] — coordination and interaction
- [[sparse-autoencoders]] — related to mechanistic interpretability tools mentioned in related work