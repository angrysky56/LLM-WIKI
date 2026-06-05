---
summary: Normalizing flows — exact-density generative models built from invertible transformations and the change-of-variables formula
tags: [generative-models, normalizing-flows, invertible, exact-density]
updated: 2026-06-05T09:46:28Z
---

---
created: 2026-06-01T14:33:00Z
updated: 2026-06-01T14:33:00Z
type: concept
summary: Normalizing flows — exact-density generative models built from invertible transformations and the change-of-variables formula
tags: [generative-models, normalizing-flows, invertible, exact-density]
status: active
confidence: 0.7
---

# Normalizing Flows

Normalizing flows construct an invertible transformation `f: x ↔ z` between data and a simple base distribution (e.g. `z ~ N(0, I)`). The exact log-density is computable via the change-of-variables formula:

```
log p(x) = log p(z) − log |det(∂f/∂x)|
```

Training maximises the exact log-likelihood — no ELBO, no adversarial loss, no contrastive bound. The constraint is that `f` must be **invertible** with a **tractable Jacobian determinant**.

**Practical constructions:**
- **Coupling layers** (RealNVP, Glow) — split the input, transform one half conditioned on the other. Invertible by construction, with a triangular Jacobian whose determinant is cheap.
- **Autoregressive flows** (MAF, IAF) — stack conditional invertible transformations; equivalent in expressivity to PixelCNN-style density models but with continuous latents.
- **Continuous-time flows** (FFJORD, Neural ODEs) — replace discrete stacks with continuous-depth invertible transformations.

For the derivation, see [[little-book-generative-ai-foundations]] Chapter 7.

## Connections
- [[generative-ai]]
- [[evidence-lower-bound-elbo]] (contrast: flows need no bound)
- [[little-book-generative-ai-foundations]]
