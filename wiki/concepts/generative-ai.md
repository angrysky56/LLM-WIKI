---
created: 2026-05-25
updated: 2026-07-03
type: concept
summary: AI systems that generate new content — text, code, images, audio — via learned probability distributions over structured generation spaces
tags: [generative-ai, generation, llm, diffusion, transformer]
sources: []
status: active
confidence: 0.75
---

# Generative AI

## Definition

Generative AI systems produce novel outputs — text, code, images, audio, video — by sampling from learned probability distributions. Unlike discriminative models that classify or predict, generative models model the full distribution over output space, enabling sampling of new instances.

The core architecture families:
- **Autoregressive transformers** (GPT, LLaMA, Gemini): next-token prediction; generative at token level
- **Diffusion models** (Stable Diffusion, DALL-E, Sora): denoising process; generative over image/audio/video space
- **Variational autoencoders (VAEs)**: latent space sampling; generative via latent interpolation
- **Flow-based models**: invertible transformations; exact log-likelihood

## The Generation Pipeline

Generative AI involves multiple stages:

1. **Representation learning**: The model learns a compressed representation of the output distribution during training
2. **Latent space structure**: The geometry of the learned representation space determines what's generationally accessible
3. **Sampling**: The generation process traverses or samples from this space — greedy decoding, nucleus sampling, CFG (classifier-free guidance), etc.

This connects to [[creativity]] — the **convergent evaluation** problem is central to generative AI. Given many possible outputs, how does the system select the best? This is the selection bottleneck in [[parallel-reasoning]] applied to generation.

## Connection to Reasoning

[[LlM-reasoning]] and generative AI are not separate capabilities — reasoning is a special case of generation where the output space is constrained by logic, not aesthetics. Chain-of-thought generation is just text generation with reasoning-shaped prompts.

The [[shorthand-for-thought]] hypothesis suggests that trained models develop compressed internal representations of reasoning paths that don't require explicit token-by-token generation. This has implications for generative efficiency: models may "know" the answer before generating it, with the generation process being more like retrieval than creation.

## Key Properties of Generative AI

### Mode Collapse and Diversity

Generative models can fail to capture full distribution diversity — mode collapse where the model only generates a subset of possible outputs. This is the opposite of the creativity problem: rather than too much diversity, there's too little.

### Classifier-Free Guidance (CFG)

CFG interpolates between conditional and unconditional generation: `output = unconditional + γ(conditional - unconditional)`. Higher guidance scale → more mode-seeking (deterministic, aligned with conditioning prompt). Lower → more diverse but potentially off-prompt.

This parallels the divergent/convergent trade-off in [[creativity]]: CFG high = convergent (safe, on-distribution), CFG low = divergent (surprising, potentially off-distribution).

### Regeneration and Refinement

Modern systems often generate iteratively: initial output → evaluation → revision → output. This connects to [[self-correction]] and [[process-reward-model]] — the PRM provides step-level evaluation signals that enable refinement.

## Evaluation of Generated Content

The evaluation problem differs fundamentally from discriminative tasks:

- **Text**: Perplexity, BLEU, ROUGE measure surface properties but miss semantic quality
- **Code**: Functional correctness (pass@k, exec score) — the strongest evaluation because it has ground truth
- **Images**: FID, Inception Score — distribution-level metrics; human preference for individual outputs
- **Creative text**: No established metric — Bradley-Terry pairwise ranking in [[parallel-reasoning]] suggests possible approaches

## Connections

- [[creativity]] — the convergent evaluation phase of creative generation; CFG as divergent/convergent dial
- [[parallel-reasoning]] — the selection mechanism problem is shared; OpenDeepThink's Bradley-Terry may inform creative selection
- [[generative-ai]] (this entry) is the medium; [[creativity]] is the property; [[llm-reasoning]] is the process
- [[diffusion-models]] — another generation architecture family
- [[in-context-learning]] — few-shot prompting enables generation without fine-tuning
- [[chain-of-thought]] — reasoning as generation with logical constraints

## Open Questions

1. **Latent space structure**: How does the geometry of the learned representation space determine generation capability? What does a "well-structured" generative latent space look like?

2. **Mode collapse detection**: Can we detect when a model is in mode collapse without exhaustive sampling? Are there structural signatures?

3. **Generative AI vs. retrieval**: At what point does generation become retrieval from compressed representations? This connects to [[shorthand-for-thought]].

4. **Scaling of generation vs. reasoning**: As models scale, do they get better at generation and reasoning proportionally, or do different capabilities have different scaling slopes?

## Limitations

- Generative AI can only sample from the training distribution — true origination beyond the distribution is not demonstrated
- Long-form generation coherence is not guaranteed; models can lose track of distant goals
- Evaluation remains the central unsolved problem, especially for creative outputs