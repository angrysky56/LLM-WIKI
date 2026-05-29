---
created: 2026-05-23
updated: 2026-07-15
type: concept
summary: RZ-NAS — zero-cost proxy neural architecture search with reflection module; evaluates architecture quality without training candidate networks
tags: [neural-architecture-search, zero-cost-proxies, reflection-module, ml-evolution, architecture-discovery]
sources: wiki/sources/articles/ml-evolution-benchmarking-protocol.md
status: active
confidence: 0.75
---

# RZ-NAS (Zero-Cost Reflective NAS)

**Also known as:** RZ-NAS, Zero-Cost Reflective Neural Architecture Search, Rasteiro-Zhang NAS

## What It Is

RZ-NAS is a Neural Architecture Search method that combines zero-cost architecture quality proxies with a reflection module that evaluates proxy reliability. Unlike conventional NAS which trains candidate architectures (or inherits weights from a supernetwork), RZ-NAS evaluates architectures in a single forward pass using proxy metrics — then uses the reflection module to correct for proxy biases across the search trajectory.

The fundamental problem RZ-NAS addresses: architecture search is exponentially expensive because each candidate requires full training. Zero-cost proxies attempt to predict architecture quality without training by measuring proxy signals (activation patterns, gradient covariance, spectral properties). But these proxies are individually unreliable — they disagree about which architectures are best. The reflection module learns which proxy types are trustworthy for which architecture families, enabling proxy combination without sacrificing the zero-cost evaluation speed advantage.

## Zero-Cost Proxies

Standard zero-cost proxies evaluate architecture quality from a single forward pass:

| Proxy | Signal | Intuition |
|-------|---------|----------|
| **SNIC** | Activation trajectories | Networks with diverse activation patterns generalize better |
| **NASWOT** | Handshake graph properties | Connectivity structure predicts emergent computation |
| **GraDes** | Gradient covariance | Similar gradient dynamics indicate similar generalization |
| **Thermal** | Jacobian stability | Stable networks near criticality generalize |

All focus on properties that can be measured in one forward (or backward) pass — no weight training required. Each captures a different structural characteristic of the network.

## The Reflection Module

The reflection module is the key innovation in RZ-NAS. Rather than averaging all proxies equally (which introduces noise from unreliable proxy types), it learns to weight proxies based on their historical accuracy:

1. **Track proxy accuracy**: Record each proxy's predicted ranking vs actual fitness for past candidates
2. **Meta-learn weights**: Given a new architecture family (e.g., transformers with Flash Attention), learn which proxy types are most predictive
3. **Dynamic weighting**: Apply different proxy weightings for different architecture subspaces

This is analogous to [[mop-architecture]]'s approach to exploration: the reflection module maintains a model (of proxy reliability, just as MOP maintains a model of state visitation distribution) and uses it to weight future decisions.

## The Algorithm

1. **Sample architecture** from search space
2. **Compute zero-cost proxy scores** (all available proxy metrics in a single forward pass)
3. **Reflection weighting**: Reflection module applies learned proxy weights to produce aggregate score
4. **Check termination**: If confidence threshold met, output best architecture; else iterate
5. **Update reflection model**: After evaluation, update proxy accuracy tracking

## Why Not Just Use One Best Proxy?

Different architecture families have different proxy sensitivities:
- RNN-like architectures: GraDes more predictive (gradient dynamics are interpretable)
- Transformer variants: NASWOT/thermal more predictive (attention patterns are key)
- MoE architectures: Multi-proxy combinations fare best (routing structure varies)

The reflection module discovers these relationships from search experience without manual architecture family labeling.

## RZ-NAS vs Other NAS Methods

| Method | Evaluation Cost | Search Strategy | Proxy Use |
|--------|---------------|----------------|-----------|
| Random Search | High (full training) | Random | None |
| DARTS | Medium (gradient sharing) | Gradient-based | None |
| CoLLM-NAS | Medium (LLM proposals) | LLM-guided | Partial |
| **RZ-NAS** | **Low (forward pass)** | **Proxy + reflection** | **Full (multi-proxy)** |

RZ-NAS achieves the lowest evaluation cost (forward pass only) with the most sophisticated proxy combination mechanism.

## Connections
- [[log]]
- [[concepts/rz-nas]]
- [[scratchpad/jobs/reports/researcher/discovery-2026-08-03]]
- [[concepts/neural-architecture-search]]
- [[scratchpad/jobs/reports/researcher/discovery-2026-07-15]]
- [[scratchpad/jobs/reports/researcher/discovery-2026-07-20]]
- [[concepts/collm-nas]]
- [[sources/articles/ml-evolution-benchmarking-protocol]]
- [[concepts/ml-evolution]]
- [[scratchpad/agent-sheets/researcher/carryover]]
- [[wiki/index]]
- [[concepts/llama-nas]]
- [[rz-nas]]

- [[neural-architecture-search]] — RZ-NAS is a specific NAS method within the architecture search field
- [[ml-evolution-benchmarking-protocol]] — source reference for RZ-NAS
- [[ml-evolution]] — zero-cost proxy search is the extreme end of "cheap evaluation" in guided ML evolution
- [[collm-nas]] — complementary NAS method; CoLLM-NAS uses LLM guidance, RZ-NAS uses proxy-based evaluation
- [[evolutionary-strategies]] — RZ-NAS can be viewed as ES where the fitness function is the reflection-weighted proxy (not training loss)
- [[maximum-occupancy-principle]] — reflection module parallels MOP's exploration model; both maintain adaptive models of reliability
- [[essa]] — both RZ-NAS and ESSA aim for gradient-free search; RZ-NAS avoids training via proxies, ESSA avoids RLHF via singular value mutations
- [[namm]] — both use learnable "reflection" mechanisms to make black-box search tractable (proxy reliability for RZ-NAS, KV retention for NAMM)

- [[llama-nas]]
## Open Questions

1. Does RZ-NAS reflection module need to be retrained per architecture family or does it generalize across families?
2. Can the reflection module be distilled into a small meta-learner for faster inference during search?
3. RZ-NAS achieves efficient architecture evaluation — can this principle apply to other expensive evaluation settings (e.g., safety evaluation, capability evaluation)?
4. Does the reflection module overfit to proxy accuracy history, or does it generalize across architecture topology changes?
