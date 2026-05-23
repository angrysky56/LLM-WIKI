---
created: 2026-05-21T08:30:00Z
updated: 2026-05-21T08:30:00Z
type: concept
summary: Sparse conditional computation via expert routing — activating only subnetworks per token, enabling massive parameter counts without proportional FLOPs
tags: [llm-architecture, mixture-of-experts, sparse-computation, conditional-computation, scaling-law]
status: active
confidence: 0.88
sources: https://arxiv.org/abs/2102.12166, https://arxiv.org/abs/2309.02427
---



# Mixture of Experts

A neural network architecture that divides parameters into discrete "expert" sub-networks and activates only a subset per forward pass — enabling massive parameter counts with a fraction of the FLOP cost per token.

## Definition

In a Mixture of Experts (MoE) architecture, the feedforward layers in a transformer are replaced by **N expert networks** (typically FFN layers), each with its own weights. A **router** (a learned linear layer) decides which expert(s) to activate for each token. Only the activated experts compute; the rest are idle.

The key equation for a sparse MoE layer:
```
y = Σ_{i=1}^{N} g_i · E_i(x)
```
where E_i is expert i's feedforward network, and g_i is the routing weight (typically top-k, meaning only the k highest-scoring experts activate per token).

**Key parameters:**
- **N**: Number of experts in the layer
- **k**: Number of active experts per token (e.g., k=2 in Mixtral 8x7B)
- **Capacity factor**: Limits the maximum tokens any expert can process per batch, preventing load imbalance

## Why It Matters

MoE represents a fundamental tradeoff in the scaling tradeoff:

| Architecture | Parameters | FLOPs/token | Memory |
|
-|
--|
-|
--|
| Dense (e.g., Llama 3 70B) | 70B | 140B FLOPs | Must load all weights |
| MoE (e.g., Mixtral 8x7B) | 46.7B total, 12.9B active | ~12.9B FLOPs | Must load all weights, but only compute active |

The 46.7B figure is **total parameters** — weights stored in memory. The **active parameters** per token are ~12.9B (two experts of 7B each). This means MoE achieves dense-model quality at a fraction of the per-token compute cost, but doesn't save memory bandwidth.

Mixtral 8x7B (8 experts, 2 active) achieves Llama 2 70B quality at ~5x lower per-token compute — but requires the same memory footprint as a 70B model since all experts must remain in RAM.

## Architectural Variants

### Soft MoE (Pseudo-aggregated)

Instead of hard routing to discrete experts, compute a weighted average of all expert outputs using soft probabilities. This is closer to a standard feedforward layer but loses the conditional computation benefit. Used in early work (Fedus et al., 2022) and some multimodal models.

### Hash Layer (Legend)

Use a learned hash function to deterministically assign tokens to experts — no routing overhead, no load balancing loss. Used in the Google Legend family (Hash Layer, HashiRouter). Advantages: trivial to implement, no auxiliary losses, scales well. Disadvantages: cannot learn optimal routing, tokens with similar content may land in different experts.

### Token-Choice Routing

Each token independently chooses its top-k experts. This is the standard approach in Mixtral, Grok-1, and most production MoE systems. Challenges include:
- **Load imbalance**: Some experts receive many more tokens than others
- **Expert collapse**: Early training can lead to a few experts dominating
- **Communication overhead**: In distributed settings, activating experts across different GPUs requires all-to-all collective operations

### Expert Choice Routing

Experts choose which tokens to process instead of tokens choosing experts. Guarantees perfect load balancing but allows variable expert coverage per token — some tokens may be processed by more experts than others. More complex to implement in distributed settings.

## Frontier Systems

### Mixtral 8x7B (Mistral AI, Dec 2023)
- 8 experts per layer, 2 active
- Total: 46.7B parameters; 12.9B active per token
- Achieved GPT-3.5 quality at 5x lower compute
- First widely deployed sparse MoE

### Grok-1 (xAI, 2024)
- 8 experts, 2 active
- 314B total parameters (larger than Mixtral)
- Open-sourced with sparse MoE weights

### DBRX (Databricks, 2024)
- 16 experts, 4 active
- 132B total parameters
- Fine-grained routing with higher active parameter count

### MegaBlocks (Dao et al., 2022)
- Framework for efficient MoE training with arbitrary expert sizes
- Addresses "expert imbalance" problem where some experts receive most tokens
- Enables dynamic expert count per batch, avoiding the waste of standard padding

## Expert Routing Dynamics

The routing decision is learned via a simple linear layer + softmax:
```
g = softmax(W_r · x)
```
Top-k selection picks the k highest-scoring experts. The routing weights are computed per-token and determine the mixture.

**Problems that emerge:**

1. **Expert imbalance**: Early in training, some experts may consistently receive high scores and dominate. Without intervention, other experts receive little signal and become useless ("expert collapse").

   *Mitigation*: Auxiliary load balancing loss — penalizes concentration of routing mass.

2. **Router locality**: The router learns to route tokens to experts based on surface features (e.g., punctuation, code keywords). This can create "expert silos" where different domains dominate different experts, reducing the model's ability to share knowledge across the full parameter space.

3. **Communication bottleneck**: In distributed training, different experts reside on different GPUs. If tokens activate experts on remote GPUs, all-to-all communication becomes a bottleneck. Systems like DeepSpeed-MoE and Megatron-Linearly offer tensor-parallel variants that minimize this.

## Open Questions

1. **Optimal expert count**: What is the right number of experts? More experts means sparser activation per token (lower compute) but harder routing learning and less expert sharing. Mixtral uses 8; some research suggests 32–64 may be better for large models.

2. **Expert specialization vs sharing**: How do we design MoE to encourage complementary expertise rather than silos? Current approaches rely on load-balancing losses; more sophisticated approaches are an open research area.

3. **Memory vs compute tradeoff**: MoE saves compute but not memory. For deployment on memory-constrained devices (mobile, edge), dense models may still be preferred. Can we design "small MoE" variants that maintain quality at lower memory footprint?

4. **Fine-tuning MoE**: MoE models are notoriously hard to fine-tune — the sparse activation pattern makes gradient updates noisy. LoRA adaptations need to account for routing; methods like MoE-Adapter address this.

5. **Integration with test-time compute**: Can we combine MoE's sparse compute with inference-time compute techniques (BoN, PRM-guided search)? The per-token activation is already low; BoN would multiply that cost by N candidates.

## Connections

- [[inference-time-compute-scaling]] — MoE provides architectural basis for efficient test-time compute; the two techniques are complementary
- [[reward-modeling]] — reward models for BoN selection can exploit MoE structure
- [[ml-evolution]] — MoE challenges the scaling law by separating parameter count from FLOPs per token

## Related Papers

- Shazeer et al. (2017): "Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer" — foundational work
- Fedus et al. (2022): "Switch Transformers: Scaling to Trillion Parameter Models with Sparse Sparsity"
- Du et al. (2022): "Hash Layer Routing in MegaBlocks"
- Ryotin et al. (2023): "Mixtral 8x7B: A Sparse Mixture of Experts"