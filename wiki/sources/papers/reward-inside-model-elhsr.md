---
created: 2026-04-18T03:55:00Z
updated: 2026-04-18T03:55:00Z
type: source
summary: "Efficient Linear Hidden State Reward (ELHSR): A lightweight reward model (<0.005% parameters) using internal LLM hidden states for Best-of-N sampling."
tags: [reward-modeling, hidden-states, efficiency, reasoning, best-of-n]
sources: https://arxiv.org/html/2505.12225v1
status: active
confidence: 0.95
---

# Reward Inside the Model: A Lightweight Hidden-State Reward Model for LLM’s Best-of-N sampling

The paper introduces **ELHSR** (Efficient Linear Hidden State Reward), a novel reward modeling approach that leverages the internal hidden states of an LLM to provide high-quality reward signals with extreme parameter and computational efficiency.

## Key Contributions

- **ELHSR Architecture**: A token-level linear reward model that uses concatenated hidden states across all layers.
- **Extreme Efficiency**: Uses less than 0.005% of the parameters of traditional reward models (e.g., 270K vs 7B+).
- **Data Efficiency**: Competitive performance with only 6,000 training samples.
- **Versatility**: Supports logit-only training for closed-source models and hybrid integration with external reward models.

## Methodology: ELHSR Architecture

The core of ELHSR is its simplicity and reliance on the "inner knowledge" of the LLM.

1.  **Input**: For each token $t$, hidden states from all $L$ layers are concatenated and flattened into $h_t \in \mathbb{R}^{Ld}$.
2.  **Projection**: A linear transformation maps $h_t$ to a gating value $\tilde{g}_t$ and a token-level reward $r_t$.
    $$\begin{pmatrix}\tilde{g}_{t}\\r_{t}\end{pmatrix}=W_{ELHSR}h_{t}+b_{ELHSR}$$
3.  **Gating**: A sigmoid activation is applied to $\tilde{g}_t$ to produce $g_t$.
4.  **Aggregation**: The final reward $R$ is a weighted average of token-level rewards:
    $$R=\frac{\sum_{t=1}^{T}(g_{t}\cdot r_{t})}{\max\left(\sum_{t=1}^{T}g_{t},\epsilon\right)}$$

## Performance Results

ELHSR was evaluated on MATH, GSM8K, and AQuA_RAT using Llama-3 (3B/8B) and Ministral-8B.

| Dataset | Metric | ELHSR (Avg) | Baseline Best (Avg) |
| :--- | :--- | :--- | :--- |
| MATH | BoN Accuracy | **57.5** | 52.9 (Skywork) |
| GSM8K | BoN Accuracy | **89.0** | 88.2 (FT-Eurus) |
| AQuA_RAT | BoN Accuracy | **72.8** | 70.2 (Skywork) |

### Efficiency Comparison
- **Parameters**: ~0.2M (ELHSR) vs 7B-13B (Baselines).
- **Inference Cost**: Orders of magnitude lower FLOPs and time per sample compared to textual reward models.

## Critical Review Analysis

Applying the [[critical-analysis]] framework to this study:

### Methodological Strengths
- **Theoretical Grounding**: Builds on existing evidence that LLM hidden states contain linear representations of confidence/truthfulness.
- **Robust Baselines**: Compares against state-of-the-art open-source reward models (Eurus, Skywork, Starling).
- **Ablation Studies**: Effectively demonstrates the necessity of the gating mechanism and evaluates various loss functions (CE, Hinge, DPO).

### Limitations & Caveats
- **Closed-Source Access**: While logit training is offered as a fallback, full hidden-state access (which provides the best results) is restricted in API-only models.
- **Task Specificity**: Evaluated primarily on mathematical and code reasoning. Performance on creative writing or subjective preference (RLHF) is less clear.
- **Model Dependency**: The reward model is tied to the hidden state distribution of the specific generator LLM.

## Connections

- **[[reward-modeling]]**: A significant shift from text-based to state-based reward evaluation.
- **[[hidden-states]]**: Demonstrates the high information density of internal representations for self-evaluation.
- **[[reasoning]]**: Enhances Best-of-N sampling, a core technique for scaling test-time compute.
- **[[critical-analysis]]**: This summary serves as a materialized instance of the scientific review process.

## Activity Log
- **2026-04-18**: Ingested and summarized research findings. Integrated with scientific communication concepts.
