---
summary: GANs — generator vs. discriminator minimax game; Wasserstein variant uses 1-Lipschitz critic for stable training.
tags: [generative-models, gan, adversarial, wasserstein]
updated: 2026-06-01T20:41:53Z
created: 2026-06-01T20:41:53Z
---

---
created: 2026-06-01T14:33:00Z
updated: 2026-06-01T14:33:00Z
type: concept
summary: Generative adversarial networks — generative models trained via a minimax game between a generator and a discriminator; bypass explicit likelihoods
tags: [generative-models, gan, adversarial, wasserstein]
status: stub
confidence: 0.7
---

# Generative Adversarial Networks (GANs)

A GAN trains two networks against each other:
- **Generator** `G_θ(z)` — maps noise `z ~ p(z)` to a synthetic sample.
- **Discriminator** `D_φ(x)` — estimates the probability that `x` is real (training data) vs. fake (from G).

The original Goodfellow et al. (2014) objective is a minimax game:

```
min_G max_D  E_{x ~ p_data}[log D(x)] + E_{z ~ p(z)}[log(1 − D(G(z)))]
```

**Why the adversarial loss works:** It implicitly minimises a divergence between the generator distribution and the data distribution. Different choices of discriminator give different divergences.

**Wasserstein GAN (Arjovsky et al. 2017):** Replace the discriminator (now called a "critic") with a 1-Lipschitz function. The loss is an approximation of the **Wasserstein-1 distance** between distributions, which has better gradients than the Jensen-Shannon divergence the original GAN implicitly minimises — fixes mode collapse and vanishing gradients in many cases.

**Trade-offs vs. likelihood-based models:**
- ✓ Sharp, realistic samples.
- ✗ No explicit density, no likelihood comparison, training is unstable.
- ✗ Mode collapse.

For the derivation, see [[little-book-generative-ai-foundations]] Chapter 8.

## Connections
- [[generative-ai]]
- [[energy-based-models]] (discriminator as learned energy)
- [[little-book-generative-ai-foundations]]
