---
summary: Energy-based models — unnormalized density p(x) ∝ exp(-E(x)); train via score matching or contrastive divergence to avoid the partition function.
tags: [generative-models, energy-based, ebm, score-fields]
updated: 2026-06-01T20:41:34Z
created: 2026-06-01T20:41:34Z
---

---
created: 2026-06-01T14:33:00Z
updated: 2026-06-01T14:33:00Z
type: concept
summary: Energy-based models — generative models defined by an unnormalized density p(x) ∝ exp(-E(x)) and trained via score matching or contrastive divergence
tags: [generative-models, energy-based, ebm, score-fields]
status: stub
confidence: 0.65
---

# Energy-Based Models (EBMs)

An EBM defines an unnormalized probability density over data:

```
p_θ(x) = exp(-E_θ(x)) / Z(θ)
```

where `E_θ(x)` is a learned scalar **energy function** (low energy = high probability) and `Z(θ)` is the intractable partition function.

**Sampling:** Langevin dynamics on the energy gradient (the negative score):
```
x_{t+1} = x_t − ε · ∇_x E_θ(x_t) + √(2ε) · z_t
```

**Training (avoiding Z):**
- **Contrastive divergence** — push down energy on data, push up on samples from a short MCMC chain.
- **Score matching** — match `∇_x E_θ(x)` to the data score; partition function cancels.
- **Noise contrastive estimation** — distinguish data from noise.

**Connection to score-based models:** The energy gradient is the negative score: `−∇_x E(x) = ∇_x log p(x)`. The [[little-book-generative-ai-foundations]] primer makes this explicit in Ch. 8, showing EBMs and score-based models as two views of the same object.

## Connections
- [[score-based-models]]
- [[generative-adversarial-networks]]
- [[generative-ai]]
- [[little-book-generative-ai-foundations]]
