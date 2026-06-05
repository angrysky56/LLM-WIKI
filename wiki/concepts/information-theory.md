---
summary: Information theory — Shannon's mathematical theory of communication, entropy, channel capacity, and its application to LLM capacity, scaling laws, and path-entropy objectives
tags: [information-theory, shannon, entropy, channel-capacity, scaling-laws, compression]
updated: 2026-06-05T09:49:57Z
---

---
created: 2026-05-25
updated: 2026-06-05
type: concept
summary: Information theory — Shannon's mathematical theory of communication, entropy, channel capacity, and its application to LLM capacity, scaling laws, and path-entropy objectives
tags: [information-theory, shannon, entropy, channel-capacity, scaling-laws, compression]
sources: ['https://arxiv.org/abs/2605.23901']
status: active
confidence: 0.72
---

# Information Theory

Claude Shannon's 1948 mathematical theory of communication provides the language for quantifying information, capacity, and uncertainty — and in the 2026 LLM landscape, it's become unexpectedly literal: models are noisy channels, training is information transmission, and the capacity ceiling is finite.

## Core Quantities

### Entropy (H)

The fundamental measure of uncertainty in a random variable. For a discrete distribution p(x):

```
H(X) = −∑ p(x) log₂ p(x)     (bits)
```

Entropy is the minimum number of bits needed to encode a sample from the distribution on average. In LLM terms, the cross-entropy loss **is** a bound on the number of bits needed to predict the next token — which is why perplexity (2^H) is the canonical training metric.

### Mutual Information (I)

The reduction in uncertainty about one variable given knowledge of another:

```
I(X; Y) = H(X) − H(X|Y) = KL(p(x,y) ‖ p(x)p(y))
```

Mutual information quantifies how much knowing Y tells us about X. In representation learning, it's the objective of InfoNCE and related contrastive methods. In RL, it measures the information flow between agent state and environment.

### KL Divergence

The extra bits needed to encode samples from p using a code optimized for q:

```
KL(p ‖ q) = ∑ p(x) log₂(p(x)/q(x))
```

This is the training objective of supervised LLM pretraining in expectation: minimize KL(data ‖ model). It also appears in the ELBO (VAEs), reward-modeling divergences, and as the natural distance for model distillation.

### Channel Capacity (C)

The maximum mutual information achievable over a noisy channel, given by the Shannon-Hartley theorem for continuous channels with bandwidth B, signal S, and noise N:

```
C = B · log₂(1 + S/N)
```

This is the central equation of the [[sources/papers/shannon-scaling-law-2026|Shannon Scaling Law]] — where model parameters map to bandwidth, training tokens to signal power, and sources of noise (data quality, quantization, architectural limitations) collectively bound the model's effective capacity.

## Application to LLMs

### The Noisy-Channel View of LLM Training

The [[sources/papers/shannon-scaling-law-2026|Shannon Scaling Law]] (Ouyang et al., 2026) reframes LLM pretraining as information transmission over a noisy channel. The loss-function empirical scaling law becomes:

```
C_LLM = a·N^α · log₂(1 + b·D^β / (noise terms))
```

Where:
- **N** (parameters) → channel bandwidth
- **D** (training tokens) → signal power
- **Noise** has three components: data-induced, model-interaction, and irreducible

This predicts **U-shaped degradation** when SNR collapses — explaining catastrophic overtraining and quantization-induced degradation that monotonic power laws cannot. The LLM has a **finite Shannon capacity**: beyond a critical data-parameter combination, scaling without maintaining SNR amplifies noise.

### Connection to Path Entropy (MOP)

The [[concepts/maximum-occupancy-principle|Maximum Occupancy Principle (MOP)]] replaces reward maximization with path-entropy maximization as the behavioral objective. Path entropy is an information-theoretic quantity — the entropy of the trajectory distribution through state space. Under the Shannon perspective, MOP agents maximize the mutual information between action trajectories and environmental states, which is structurally dual to the channel-capacity maximization view.

This connection is deep: MOP's layer 0 in the [[entities/projects/efhf|EFHF architecture]] explicitly operationalizes path-entropy exploration. The Shannon Scaling Law tells us how much information a particular LLM *can* carry — MOP tells us how to shape the encoding toward *useful* exploration.

### Rate-Distortion and Compression

Rate-distortion theory (Shannon's lossy compression framework) provides the lower bound: to achieve distortion D, you need R(D) bits of information. This directly governs:
- **Model compression**: quantization (4-bit, 3-bit) is a rate-distortion tradeoff — how many bits per parameter before Shannon capacity collapses? The Shannon Scaling Law makes this precise.
- **KV-cache compression**: the information-theoretic view tells us which attention heads carry the most information, guiding selective compression.
- **Continual learning**: the plasticity-stability tradeoff is fundamentally rate-distortion — how much of the past must be remembered (rate) to maintain performance on new tasks (distortion)?

See [[compression]] for the specific implementation techniques.

## Connections

- [[sources/papers/shannon-scaling-law-2026]] (0.9) — Shannon-Hartley theorem applied to LLM capacity; the direct source anchor for the noisy-channel view
- [[concepts/maximum-occupancy-principle]] (0.01) — path-entropy maximization; information-theoretic dual of reward maximization
- [[entities/projects/efhf]] (0.005) — five-layer architecture where MOP connects to verifier graphs via information flow
- [[compression]] — rate-distortion tradeoffs in model compression and quantization
- [[scaling-laws]] — empirical scaling laws that the Shannon model generalizes
- [[evidence-lower-bound-elbo]] — KL divergence as training objective
- [[variational-autoencoder]] — information bottleneck principle

## See Also

- [[signal-processing]] — related math but narrower in scope
- [[communication-theory]] — broader field that includes information theory

## Open Questions

- [ ] Can the Shannon Scaling Law's SNR threshold be used as a training-stopping criterion (halt before U-shaped degradation)?
- [ ] Does the MOP path-entropy objective have a natural interpretation as maximizing the conditional mutual information I(trajectory; world-model)?
- [ ] What is the information-theoretic limit of model merging? If each checkpoint is a noisy channel, merging should be bounded by the sum of their capacities minus their mutual information.
- [ ] Can rate-distortion inspired training objectives replace empirical loss functions for long-context models, where the decoder must selectively forget?
