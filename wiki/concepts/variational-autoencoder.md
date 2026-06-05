---
summary: Variational autoencoder — generative model that combines an encoder network (amortised posterior) with a decoder and is trained by maximising the ELBO
tags: [generative-models, vae, variational-inference, elbo]
updated: 2026-06-05T09:47:05Z
---

---
created: 2026-06-01T14:33:00Z
updated: 2026-06-01T14:33:00Z
type: concept
summary: Variational autoencoder — generative model that combines an encoder network (amortised posterior) with a decoder and is trained by maximising the ELBO
tags: [generative-models, vae, variational-inference, elbo]
status: active
confidence: 0.7
---

# Variational Autoencoder (VAE)

A VAE is a latent-variable generative model trained by maximising the [[evidence-lower-bound-elbo|ELBO]]:

```
L = E_{q_φ(z|x)} [log p_θ(x|z)] − KL(q_φ(z|x) ‖ p(z))
```

- **Encoder** `q_φ(z|x)` — a neural network that outputs the parameters of an approximate posterior (typically diagonal Gaussian: mean `µ_φ(x)` and variance `σ_φ(x)²`).
- **Decoder** `p_θ(x|z)` — a neural network that reconstructs `x` from a latent sample.
- **Reparameterisation trick** — sample `z = µ_φ(x) + σ_φ(x) ⊙ ε` with `ε ~ N(0,I)` so gradients flow through the sampling step.
- **Amortised inference** — the encoder is shared across all data points, so inference cost is one forward pass per example.

The VAE is the amortised, nonlinear generalisation of Probabilistic PCA. For the derivation from first principles, see [[little-book-generative-ai-foundations]] Chapter 3.

## Connections
- [[evidence-lower-bound-elbo]]
- [[generative-ai]]
- [[little-book-generative-ai-foundations]]
