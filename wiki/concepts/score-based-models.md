---
summary: Score-based generative models — learn ∇_x log p(x) and sample via Langevin dynamics or SDE reverse-time simulation.
tags: [generative-models, score-based, sde, langevin, diffusion]
updated: 2026-06-01T20:41:01Z
created: 2026-06-01T20:41:01Z
---

---
created: 2026-06-01T14:33:00Z
updated: 2026-06-01T14:33:00Z
type: concept
summary: Score-based generative models — learn the score function ∇_x log p(x) and sample via Langevin dynamics or SDE solvers
tags: [generative-models, score-based, sde, langevin, diffusion]
status: stub
confidence: 0.7
---

# Score-Based Generative Models

A score-based model learns the **score function** of the data distribution:

```
s_θ(x) ≈ ∇_x log p(x)
```

Once the score is known, samples are drawn via **Langevin dynamics**:

```
x_{t+1} = x_t + ε · s_θ(x_t) + √(2ε) · z_t,   z_t ~ N(0, I)
```

This pushes samples up the density gradient while injecting noise for exploration.

**Training objectives:**
- **Score matching** (Hyvärinen 2005) — direct regression of the score, but the trace-of-Hessian term is awkward.
- **Denoising score matching** (Vincent 2011) — predict the noise added to a corrupted sample; equivalent in expectation, much more stable. This is the objective used in practice.
- **Fisher divergence** — the natural loss function for learning the score; appears in [[little-book-generative-ai-foundations]] Ch. 6.

**Connection to diffusion:** Score-based models with multi-scale noise (NCSN, Song & Ermon 2019) are mathematically equivalent to DDPM under the right parameterisation. The continuous-time limit is an SDE: forward SDE adds noise, reverse SDE samples by subtracting the score. See [[diffusion-models]] for the discrete-time view.

For the full derivation, see [[little-book-generative-ai-foundations]] Chapter 6.

## Connections
- [[diffusion-models]]
- [[energy-based-models]]
- [[generative-ai]]
- [[little-book-generative-ai-foundations]]
