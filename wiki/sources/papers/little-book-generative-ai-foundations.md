---
summary: Compact (~120pp) mathematical primer on the foundations of the major generative model families (VAE, diffusion/score-based, normalizing flows, GANs, EBMs), derived from first principles. Math-first, no code, foundational rather than frontier.
tags: [generative-models, variational-autoencoders, diffusion-models, score-based-models, normalizing-flows, gans, energy-based-models, mathematical-foundations, textbook, primer]
updated: 2026-06-01T20:39:18Z
created: 2026-06-01T20:39:18Z
---

---
created: 2026-06-01T14:33:00Z
updated: 2026-06-01T14:33:00Z
type: source
summary: A compact mathematical primer covering the foundations of the major generative model families — VAE, diffusion/score-based, normalizing flows, GANs, EBMs — derived step-by-step from first principles.
tags: [generative-models, variational-autoencoders, diffusion-models, score-based-models, normalizing-flows, gans, energy-based-models, mathematical-foundations, textbook, primer]
sources:
  - https://arxiv.org/abs/2605.29713
  - https://arxiv.org/pdf/2605.29713
status: reference
confidence: 0.95
---

# The Little Book of Generative AI Foundations: An Intuitive Mathematical Primer

**Author:** Tianhua Chen (University of Huddersfield, School of Computing and Engineering)
**Preprint:** May 29, 2026
**arXiv:** [2605.29713](https://arxiv.org/abs/2605.29713)
**Genre:** Mathematical textbook / primer (~120 pages, 8 chapters + 2 appendices)
**Stance:** "Foundational rather than frontier-oriented" — math-first, architecture-light, derived step-by-step rather than presented as recipes.

## Core Insight

The major families of generative AI — VAEs, diffusion, score-based, normalizing flows, GANs, EBMs — are not separate architectures but **different answers to one shared question**: how to model a data distribution `p(x)` when direct likelihoods are intractable. The book makes that question explicit and then derives each family from it, showing the shared mathematical scaffolding (latent variables, ELBOs, score fields, change-of-variables, density ratios) underneath what looks like surface-level variety.

If you've been reading papers that gesture at "the ELBO" or "score matching" without showing you the derivation, this is the bridge.

## Scope and Approach

From the preface, the central principles the book organizes around:

> "latent variables, likelihoods, variational bounds, invertible transformations, stochastic noising processes, score fields, adversarial comparison, and energy landscapes."

"Little" refers to **scope, not depth**: the treatment within the chosen scope is intentionally careful. The book builds each idea from prerequisites and does not skip steps. Readers at the research frontier will know most of the material — the value is the careful, step-by-step construction.

## Chapter Map

| # | Chapter | Bridge to |
|---|---------|-----------|
| 1 | Linear Algebra Foundations: From PCA to Autoencoders | Matrices as transformations, eigendecomposition, SVD, reconstruction loss → autoencoders |
| 2 | Probabilistic PCA: A Bridge to Latent-Variable Generative Modelling | Probabilistic framing, EM, Jensen's inequality, ELBO |
| 3 | The Variational Autoencoder: From Probabilistic Latent Variables to Variational Inference | Reparameterisation, amortised inference, the VAE objective |
| 4 | Denoising Diffusion Probabilistic Models (DDPM) | Forward/reverse processes, the diffusion ELBO, simplified step-wise objective |
| 5 | Calculus Foundations for Continuous-Time Generative Modelling | Deterministic and stochastic density evolution → Fokker–Planck |
| 6 | Score-Based Generative Modelling and Continuous-Time Diffusion | Langevin dynamics, score matching, denoising score matching, SDE formulation |
| 7 | Exact Density Models: Normalizing Flows and Autoregressive Factorizations | Invertible transformations, change-of-variables, coupling layers, autoregressive factorization by probability chain rule |
| 8 | Beyond Likelihoods: GANs and Energy-Based Models | Adversarial comparison, Wasserstein distance, EBMs, energy gradients ↔ score fields |

**Appendices:**
- **A** — Gaussian algebra and completing the square (used throughout)
- **B** — Detailed diffusion reverse-posterior derivations (the math many papers skip)

## Key Derivations (what the book actually shows you)

The book earns its keep by being explicit where papers hand-wave. Highlights from the chapter overviews:

**Chapter 2 — PPCA and the ELBO's first appearance.** Shows why PPCA is analytically tractable (the conditional `p(x|z)` and prior `p(z)` are jointly Gaussian, so the marginal is closed-form). Derives the ELBO from Jensen's inequality, then shows EM maximises that bound. This is the only chapter in the standard canon where the ELBO is built up from scratch rather than invoked.

**Chapter 3 — VAE = amortised PPCA + flexible decoder.** The chapter's main move: take the PPCA posterior (which is closed-form because the model is linear-Gaussian) and replace it with a learned `q_φ(z|x)` (an encoder network) when the decoder becomes nonlinear. The reparameterisation trick `z = µ_φ(x) + σ_φ(x) ⊙ ε` with `ε ~ N(0,I)` is derived as a way to push gradients through the sampling step.

**Chapter 4 — DDPM as a sequence of small denoising steps.** The forward process `q(x_t | x_{t-1})` is a fixed Gaussian noising schedule. The reverse process `p_θ(x_{t-1} | x_t)` is learned. The book writes the full ELBO across all timesteps, then shows the step-wise decomposition, then argues that most terms reduce to a noise-prediction loss — the actual DDPM training objective.

**Chapter 5 — Continuous-time bridge.** Discrete-time updates become ODEs in the limit. The Fokker–Planck equation describes how a probability density evolves under a stochastic differential equation. This is the math that lets diffusion be reframed from "many small steps" to "one continuous noising process" — the unification behind score-based continuous-time models.

**Chapter 6 — Score = ∇_x log p(x).** Once you have the score, Langevin dynamics `x_{t+1} = x_t + ε ∇_x log p(x_t) + √(2ε) z_t` samples from `p(x)`. The book shows the Fisher divergence is the natural loss for learning the score, derives denoising score matching (the stable training objective — predict the noise added to a clean sample rather than the raw score), and shows the SDE formulation that unifies DDPM and score-based with NCSN.

**Chapter 7 — Exact density via invertibility.** Normalizing flows use a sequence of invertible transformations `f = f_K ∘ ... ∘ f_1` and the change-of-variables formula to compute `p(x)` exactly. Coupling layers (RealNVP-style) are the practical construction. Autoregressive factorization (`p(x) = ∏_i p(x_i | x_<i)`) is shown as a different exact-density approach — PixelCNN/PixelRNN territory.

**Chapter 8 — When you don't have a likelihood.** GANs replace the likelihood with a learned discriminator; the book derives the minimax objective and walks through the geometric interpretation of Wasserstein distance (WGAN). EBMs model an unnormalized density `p(x) ∝ e^{-E(x)}` and learn the energy; the chapter closes by showing `∇_x log p(x) = -∇_x E(x)`, linking EBMs back to the score-based view from Chapter 6.

## Cross-Chapter Threads

The book is more than a sequence of independent chapters because several threads reappear:

1. **The ELBO.** First appears in Ch. 2 (PPCA, Jensen's inequality), is the central object in Ch. 3 (VAE) and Ch. 4 (DDPM), and disappears in Ch. 7 (exact density → no bound needed) and Ch. 8 (no likelihood at all).
2. **The score `∇_x log p(x)`.** Implicit in Ch. 2 (gradients of log-likelihoods), explicit and central in Ch. 6 (score-based), and reconnected to EBMs in Ch. 8 via the energy gradient.
3. **Latent variables.** PPCA's `z` (Ch. 2) → VAE's `z` (Ch. 3) → diffusion's noisy latent `x_t` (Ch. 4–6) → flow's intermediate `z` (Ch. 7). The "latent" is whatever non-observable quantity the model introduces to make `p(x)` tractable.
4. **Inference vs. learning.** The tension between wanting an exact posterior (PPCA, flows) and accepting an approximate one (VAE, diffusion) is a recurring axis.

## When to Use This Book

**Reach for it when:**
- You've read a paper that says "we use the ELBO" or "score matching" and want to see the derivation.
- You want a single, coherent reference for the math behind the canonical eight generative model families.
- You're teaching a course or building study materials on generative modeling foundations.

**Skip it when:**
- You want architecture details, training tricks, or SOTA benchmarks (explicitly out of scope).
- You want a fast survey rather than a worked-through treatment.
- You need implementations — this is math, not code.

## Related Material in the Wiki

**Concept pages** (created as part of this ingest):
- [[variational-autoencoder]]
- [[score-based-models]]
- [[normalizing-flows]]
- [[energy-based-models]]
- [[generative-adversarial-networks]]
- [[evidence-lower-bound-elbo]]

**Existing related pages** (now linked reciprocally):
- [[generative-ai]]
- [[diffusion-models]]

**Synthesis**:
- [[generative-ai-math-primer-comparison]] — where this primer sits in the canon (Murphy, Prince, Blei, original papers), with a recommended reading order

## Reuse and Origin

The author's preface notes this is a preprint version; the book is positioned as a teaching resource. The math is presented carefully enough to be reused for personal study and citation, though the standard arXiv license terms apply.

## Caveats

- **Preprint, not yet published** — the May 2026 date puts this in the preprint window; structure and notation may still be refined.
- **Foundational, not frontier** — readers looking for transformers-as-generative-models, flow matching beyond score matching basics, or modern video diffusion specifics will need to supplement.
- **No code** — derivations are mathematical, not programmatic. Pair with a code-focused source if you want implementations.

## Confidence

0.95 — the structural overview is from the actual chapter sections of the paper, and the chapter summaries are faithful to the explicit "Overview" sections the author wrote. The cross-chapter threads are my synthesis.
