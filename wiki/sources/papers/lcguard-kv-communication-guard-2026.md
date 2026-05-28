---
created: 2026-05-22
updated: 2026-05-22
type: source
summary: Framework for safe KV-based latent communication in multi-agent LLM systems, using adversarial-learned transformations to suppress reconstruction-based leakage while preserving task utility.
tags: [multi-agent-systems, llm-security, kv-cache, latent-communication, privacy-utility-tradeoff, adversarial-learning]
sources: https://arxiv.org/abs/2605.22786
status: active
confidence: 0.9
---

# LCGuard: Latent Communication Guard for Safe KV Sharing in Multi-Agent Systems

**Authors:** Sadia Asif, Mohammad Mohammadi Amiri (Rensselaer Polytechnic Institute), Momin Abbas, Prasanna Sattigeri, Karthikeyan Natesan Ramamurthy (IBM Research)

**Submitted:** 22 May 2026 (arXiv:2605.22786v1)
**Subjects:** Artificial Intelligence, Computation and Language, Machine Learning (cs.AI, cs.CL, cs.LG)

## Core Insight

LCGuard addresses a fundamental vulnerability in multi-agent LLM systems that use KV caches as communication substrate: **sensitive information can be reconstructed from shared latent representations**, even when it never appears in text outputs. The framework learns representation-level transformations that suppress reconstructable sensitive content while preserving task-relevant semantics.

## Key Claims

| Claim | Evidence |
|-------|----------|
| KV-based latent communication introduces reconstruction-based privacy leakage | ASR up to 0.900 on vanilla KV sharing (AgentLeak benchmark) |
| LCGuard reduces ASR by 65-75% while maintaining competitive task performance | Tables 1-3 across Qwen3-4B, Gemma-9B, LLaMA-8B |
| System-level optimization outperforms per-agent local optimization | Full-System LCGuard vs Per-Agent LCGuard: ASR 0.224 vs 0.265 (Qwen3-4B hierarchical) |
| LCGuard achieves better privacy-utility tradeoff than baselines | ADAPT kills utility; PrivAct doesn't reduce ASR; LCGuard balances both |

## Problem Formulation

**Setting:** Multi-agent systems communicating through latent KV representations (not text). Agents share KV caches as "shared working memory" for efficiency.

**Threat model:** Adversary with access to communicated artifacts M_obs can train a decoder D_i to reconstruct agent-specific sensitive inputs s_i from M_obs. Leakage is measured by reconstruction loss gap from prior.

**Key insight:** Unlike text-based communication (discrete, inspectable), KV caches are high-dimensional and semantically dense — they encode contextual inputs, intermediate reasoning states, and attention structure that can be exploited for reconstruction.

## Methodology

LCGuard treats shared KV caches as latent working memory and learns communication functions g_ij that transform KV representations before transmission:

```
m_ij = g_ij(K_i, V_i)
```

The transformation is a **lightweight residual bottleneck**:
```
K_san = K + W_K2 · GELU(LN(K))
V_san = V + W_V2 · GELU(LN(V))
```

Where db << dk,dv (bottleneck dimension), forcing compression of task-relevant vs reconstructable information.

**Adversarial training (minimax optimization):**
- Communication functions {g_ij} minimize: L_task(M) + β · Σ L_rec(M_obs)
- Adversarial decoder D_i maximizes reconstruction success
- Alternating updates: adversary step (fix g, update D) → communication step (fix D, update g)

**Two variants:**
- **Per-Agent LCGuard:** M_obs = m_ij (single link, local leakage)
- **Full-System LCGuard:** M_obs = M (all artifacts, accounts for compositional/system-level leakage)

## Key Results

### Privacy-Utility Tradeoff (Qwen3-4B, PrivacyLens, sequential 4-agent)

| Method | Helpfulness ↑ | ASR ↓ | Privacy ↑ |
|--------|---------------|-------|-----------|
| Vanilla KV Sharing | 0.780 | 0.871 | 0.420 |
| ADAPT | 0.285 | 0.332 | 0.850 |
| PrivAct | 0.690 | 0.845 | 0.820 |
| Full-System LCGuard | 0.710 | 0.216 | 0.801 |

**65-75% ASR reduction** with minimal helpfulness degradation.

### System vs Local Protection

Full-System LCGuard consistently outperforms Per-Agent LCGuard:
- Qwen3-4B hierarchical AgentLeak: ASR 0.224 (Full) vs 0.265 (Per-Agent)
- Gemma-9B: ASR 0.215 (Full) vs 0.254 (Per-Agent)

This confirms that leakage is compositional — sensitive information re-emerges after aggregation across agents.

### Inference Efficiency

LCGuard adds minimal latency overhead:
- Text-based MAS: 1.00× (baseline)
- Vanilla KV Sharing: 0.24× (4.1× speedup)
- Full-System LCGuard: 0.28× (3.6× speedup)

## Baselines Compared

| Baseline | Approach | Failure Mode |
|----------|----------|--------------|
| Vanilla KV Sharing (LatentMAS, KVComm) | Raw KV transmission | No protection; high ASR |
| ADAPT | Gaussian noise injection | Kills both sensitive and task-relevant info |
| PrivAct | Policy-level output constraints | Doesn't constrain latent representations; ASR unchanged |

## Connections
- [[index]]
- [[sources/papers/papers-2026-05-22-researched]]
- [[sources/papers/lcguard-kv-communication-guard-2026]]
- [[lcguard-kv-communication-guard-2026]]

- [[multi-agent-llm-systems]] — target domain
- [[kv-cache]] — the communication substrate being protected
- [[latent-communication]] — the communication paradigm
- [[privacy-utility-tradeoff]] — core tradeoff LCGuard addresses
- [[adversarial-training]] — training methodology
- [[reconstruction-attack]] — threat model
- [[agent-leak-benchmark]] — evaluation benchmark
- [[privacy-mas]] — related work on privacy in multi-agent systems

## Limitations

- Evaluated on selected open-weight LLM families (Qwen3, Gemma-2, LLaMA); behavior may differ with heterogeneous agents
- Assumes access to paired training data for adversarial reconstruction
- Relies on decoder strength as proxy for leakage risk (no formal guarantees)
- Does not provide formal privacy guarantees (e.g., differential privacy)

## Broader Impact

**Positive:** Reduces representation-level privacy leakage in collaborative multi-agent settings involving sensitive user context, retrieved documents, or private reasoning.

**Risks:** Reconstruction-based evaluation methods could inform stronger attacks if misused. Should be combined with access control, logging safeguards, and output-level privacy checks.

## Open Questions

- Can LCGuard transformations generalize across different agent architectures/heterogeneous models?
- What is the minimum bottleneck dimension that preserves task utility while suppressing leakage?
- How does LCGuard interact with other privacy mechanisms (output filtering, access control)?
- Does compositional leakage emerge in very large-scale deployments (10+ agents)?