---
created: 2026-06-03
updated: 2026-06-09
type: concept
summary: Benchmark for measuring information leakage in LLM agents — specifically reconstruction attacks on shared KV-cache artifacts in multi-agent systems
tags: [benchmark, security, privacy, multi-agent-systems, kv-cache, adversarial]
sources: https://arxiv.org/abs/2605.22786 (LCGuard)
status: active
confidence: 0.85
---

# Agent Leak Benchmark

**Also known as:** AgentLeak benchmark, reconstruction attack benchmark

**Source:** LCGuard paper (arXiv:2605.22786) — Sadia Asif et al., IBM Research / RPI

## What It Is

AgentLeak is a benchmark for measuring information leakage in multi-agent LLM systems, specifically focusing on **reconstruction attacks** against shared KV-cache artifacts. The threat model: an adversary with access to communicated latent representations (KV caches) can train a decoder to reconstruct sensitive information that never appeared in any text output.

The benchmark measures:
- **ASR (Attack Success Rate)**: Accuracy of reconstructing agent-specific sensitive inputs from shared KV artifacts
- **Helpfulness**: Downstream task performance after mitigation
- **Privacy-Utility Tradeoff**: The fundamental tension between suppressing leakage and preserving utility

## Why It Matters

Multi-agent LLM systems often share KV caches as an efficient communication substrate — agents maintain shared working memory to avoid redundant computation. The LCGuard paper shows this creates a **reconstruction vulnerability**: sensitive context (user documents, retrieved private data, intermediate reasoning) can be extracted from the KV representations even when:

1. The sensitive content never appeared in any text output
2. The sharing is intentional and task-motivated (not a misconfiguration)
3. Standard output-level privacy checks pass

The ASR on vanilla KV sharing reaches **up to 0.900** on AgentLeak — meaning an adversary can reconstruct sensitive inputs with near-perfect accuracy for some agent configurations.

## Benchmark Components

### Threat Model
The benchmark assumes:
- **Adversary access**: Access to observed artifacts M_obs (shared KV caches)
- **Reconstruction decoder**: Trained to map M_obs → sensitive input s_i
- **Leakage metric**: Reconstruction loss gap from prior (how much more the decoder learns than it should)

### Evaluation Setting
- Multi-agent LLM systems with KV-based latent communication
- PrivacyLens benchmark suite for sensitive input domains
- Sequential multi-agent configurations (one agent shares with the next)

### Key Finding
Without protection, **ASR up to 0.900** on vanilla KV sharing across Qwen3-4B, Gemma-9B, and LLaMA-8B agent configurations.

## Connections
- [[concepts/agent-leak-benchmark]]
- [[concepts/autonomous-research]]
- [[scratchpad/jobs/reports/researcher/discovery-2026-06-09]]
- [[concepts/adversarial-training]]
- [[concepts/agent-onboarding]]
- [[log]]
- [[sources/papers/lcguard-kv-communication-guard-2026]]
- [[concepts/multi-agent-llm-systems]]
- [[index]]
- [[concepts/kv-cache]]
- [[agent-leak-benchmark]]

- [[multi-agent-llm-systems]] — the target domain where this leakage occurs
- [[kv-cache]] — the specific artifact being exploited
- [[lcguard]] — the mitigation framework evaluated on this benchmark
- [[latent-communication]] — the communication paradigm at risk
- [[adversarial-training]] — the mitigation methodology
- [[agent-onboarding]] — agent onboarding processes should address information leakage risks
- Concept: [[autonomous-research]]
