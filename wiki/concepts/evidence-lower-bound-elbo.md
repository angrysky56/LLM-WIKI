---
summary: The ELBO — Jensen-derived lower bound on log-likelihood that is the central training objective in VAEs, DDPM, and PPCA.
tags: [generative-models, variational-inference, elbo, math]
updated: 2026-06-01T20:40:29Z
created: 2026-06-01T20:40:29Z
---

---
created: 2026-06-01T14:33:00Z
updated: 2026-06-01T14:33:00Z
type: concept
summary: The Evidence Lower Bound — a tractable lower bound on log-likelihood used to train latent-variable generative models
tags: [generative-models, variational-inference, elbo, math]
status: stub
confidence: 0.6
---

# Evidence Lower Bound (ELBO)

The **ELBO** is a lower bound on the log-evidence `log p(x)` for a latent-variable model `p(x) = ∫ p(x|z) p(z) dz`, derived via Jensen's inequality:

```
log p(x) ≥ E_{q(z|x)} [log p(x|z)] − KL(q(z|x) ‖ p(z))
```

Maximising the ELBO is equivalent to (a) making the decoder `p(x|z)` reconstruct the data well, and (b) keeping the approximate posterior `q(z|x)` close to the prior `p(z)`.

The ELBO is the central training objective in:
- [[variational-autoencoder|VAEs]] (amortised inference + decoder likelihood)
- [[diffusion-models|DDPM]] (sum of step-wise KL terms across the noising chain)
- Probabilistic PCA ([[little-book-generative-ai-foundations|source]] Ch. 2)

For the cleanest derivation, see Tianhua Chen's primer [[little-book-generative-ai-foundations]] Chapter 2 (PPCA) and Chapter 3 (VAE).

## Connections
- [[variational-autoencoder]]
- [[diffusion-models]]
- [[generative-ai]]
- [[normalizing-flows]]
- [[little-book-generative-ai-foundations]]
