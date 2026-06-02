---
summary: Comparative reading guide for mathematical primers on generative AI: Chen (2026, "Little Book"), Murphy (PML 2022-23), Prince (UDL 2023), and the original papers (Blei, Kingma, Goodfellow, Ho, Song) — strengths, weaknesses, recommended order.
tags: [generative-models, mathematical-foundations, primer, reading-list, vae, diffusion-models, gans, normalizing-flows, energy-based-models]
updated: 2026-06-01T21:52:55Z
created: 2026-06-01T21:52:55Z
---

---
created: 2026-06-01T15:30:00Z
updated: 2026-06-01T15:30:00Z
type: synthesis
summary: Comparative guide to mathematical primers on generative AI — Chen (Little Book, 2026), Murphy (PML, 2022–2023), Prince (UDL, 2023), Blei et al. (review articles), with a recommended reading order
tags: [generative-models, mathematical-foundations, primer, reading-list, vae, diffusion-models, gans, normalizing-flows, energy-based-models]
status: reference
confidence: 0.85
---

# Generative AI Mathematics: A Comparison of Four Primers

A working reader's guide to the major math-first treatments of generative modelling, written after working through [Tianhua Chen's *The Little Book of Generative AI Foundations*](https://arxiv.org/abs/2605.29713) (May 2026) and comparing it to the established canon.

## The four primers at a glance

| Primer | Author(s) | Date | Length | Style | Code | Strengths | Weaknesses |
|---|---|---|---|---|---|---|---|
| **The Little Book of Generative AI Foundations** | Tianhua Chen | 2026-05 | ~120 pp, 8 ch | Math-first, derived step-by-step | None — math only | Cleanest ELBO build-up; unifies EBM and score views; doesn't skip | New, no editorial review yet; not SOTA |
| **Probabilistic Machine Learning** (Vol I & II) | Kevin P. Murphy | 2022–2023 | ~2000 pp, 4 books | Encyclopaedic reference | Some Python notebooks | Complete coverage of *all* ML including generative; Pyro/TF code | Too long to read cover-to-cover; heavy notation |
| **Understanding Deep Learning** | Simon Prince | 2023 | ~540 pp | Modern textbook, less formal | Annotated PyTorch notebooks | Excellent figures, modern architectures, practical advice | Less rigorous on derivations; more recipe than derivation |
| **Foundations of ML / review articles** | Blei, Sutskever, Kingma, Rezende, etc. | 2014–2018 | 30–60 pp each | Survey / research-paper style | Math + sometimes code | Authoritative for the *original* presentations; cited by everyone | Out of date; not coherent with each other; assume PhD reader |

There are also important specialised references that are not primers but indispensable when going deep:

- **Goodfellow, Bengio, Courville — *Deep Learning*** (2016) for the canonical GAN derivation and early VAE presentation.
- **Boyd & Vandenberghe — *Introduction to Applied Linear Algebra* / *Convex Optimization*** for the linear-algebra and convex-optimisation background.
- **Wainwright — *High-Dimensional Probability*** for the modern concentration-inequality toolkit behind the EBM and diffusion analyses.

## What each one does best

### Chen (2026) — *The Little Book*

The *tightest* of the four. The first three chapters go PCA → PPCA → VAE in a way that makes the ELBO feel inevitable rather than introduced. Chapters 5–6 are the strongest in the canon: the discrete-to-continuous limit of the diffusion process is written out, the Fokker–Planck equation is derived, and then the score function appears naturally as the gradient of the log-density.

The closing chapters (7–8) are competent but less distinguished: normalizing flows and GANs are covered in 15–20 pages each, which is enough to follow a paper but not enough to *write* one.

**Read it for:** the unification of EBMs and score-based models in Chapter 8, and the only treatment of the diffusion ELBO I've seen that's careful about every term.

### Murphy (PML, 2022–2023)

The standard reference. Volume I covers foundations (probability, linear algebra, gradient methods); Volume II covers deep generative models specifically, with chapters on VAEs, normalizing flows, autoregressive models, energy-based models, GANs, and score-based / diffusion.

Murphy's notation is consistent across the volumes (which is itself a major achievement) and he gives both the math and the practical considerations. The downsides are the size and the fact that it is encyclopaedic rather than pedagogical: you can find any topic, but the path through is yours to construct.

**Read it for:** the definitive notation, exhaustive references, and the only place you'll find careful coverage of *all* of: VAE, NADE, PixelCNN/RNN, MAF, IAF, NICE, RealNVP, Glow, FFJORD, GAN variants, EBMs, NCSN, DDPM, and SDE-based diffusion under one roof.

### Prince (2023) — *Understanding Deep Learning*

The most *modern* of the four. Excellent for getting up to speed on what people actually use in 2023 — diffusion, transformer-based generation, classifier-free guidance, latent diffusion. The figures are the best in the genre; the annotated PyTorch notebooks are a serious asset.

Less rigorous on the derivations. You'll get the *what* and the *how* but not always the *why*.

**Read it for:** figures, modern architectures, and the annotated notebooks. Skip for derivations.

### Blei, Sutskever, Kingma, Rezende — the original papers

- Blei, Kucukelbir, McAuliffe (2017), *Variational Inference: A Review for Statisticians* — the variational-inference foundation.
- Kingma & Welling (2014), *Auto-Encoding Variational Bayes* — the original VAE paper.
- Rezende, Mohamed, Wierstra (2014), *Stochastic Backpropagation and Approximate Inference in Deep Generative Models* — the reparameterisation trick, simultaneously with Kingma.
- Ho, Jain, Abbeel (2020), *Denoising Diffusion Probabilistic Models* — the DDPM paper.
- Song et al. (2021), *Score-Based Generative Modeling through Stochastic Differential Equations* — the continuous-time score-based framework.
- Goodfellow et al. (2014), *Generative Adversarial Networks* — the GAN paper.

These are not primers — they're research papers. But they're short, well-written, and the source of the derivations everyone else paraphrases. The notation is idiosyncratic in each one; the primers exist to give you a unified view.

## Recommended reading order

If you have the time and want to genuinely understand the field:

1. **Chen (2026), chapters 1–3** (~30 pp). The fastest way to get ELBO, VAE, and the variational framework into your head.
2. **Blei et al. (2017), Variational Inference review** (~30 pp). Same ideas, different angle; reinforces the ELBO and shows the broader variational-inference family (mean-field, stochastic VI, etc.).
3. **Chen, chapters 4–6** (~50 pp). The diffusion and score-based content. This is the unique value of Chen's book — I haven't seen it done this cleanly elsewhere.
4. **Ho et al. (2020), DDPM** (~15 pp). Now that you have the ELBO, the original paper is much more readable.
5. **Song et al. (2021), Score-Based via SDEs** (~30 pp). The continuous-time unification. Worth reading now that you have Ch. 5–6 background.
6. **Chen, chapter 7** (~20 pp). Normalizing flows and autoregressive factorization. Read it; it's the only one of the four to handle these correctly together.
7. **Kingma & Welling (2014), original VAE** (~14 pp). Now you can read the original and see the seeds of everything in chapters 1–3.
8. **Goodfellow et al. (2014), GANs** (~10 pp). Short and the historical anchor for everything in the adversarial family.
9. **Chen, chapter 8** (~20 pp). Read last; it ties EBMs and score-based together and gives the Wasserstein-GAN derivation.
10. **Murphy, Vol II, chapters on deep generative models** (~150 pp). Skim; use as reference for the topics that came up short in Chen.
11. **Prince (2023), generative-models chapters** (~80 pp). Read for figures and modern architecture context — classifier-free guidance, latent diffusion, consistency models.

If you have less time:

- **One primer:** Chen. It's the only one that does the math without skipping and is short enough to actually finish.
- **One primer + one paper:** Chen + Kingma & Welling (2014). The VAE is the gateway drug; the original paper is short and becomes a different read after Chen.
- **All four:** Chen first to get the framework, Murphy as reference, Prince for figures and modern context, the original papers to anchor the timeline.

## What this comparison reveals

The four primers differ on one fundamental axis: **how much do they hide under "see the original paper"**?

- Chen hides almost nothing. Every equation in chapters 1–6 is derived from prerequisites. (Chapters 7–8 are denser, but still self-contained.)
- Murphy hides the calculus but cites every result; you can read it linearly but the "aha" moments require following the citations.
- Prince hides the calculus *and* cites lightly; you get the architecture and the figures but not always the math.
- The original papers hide everything; they're written for a community that already has the background.

If you can only read one carefully, Chen is the right answer. If you read it, you'll be equipped to read the rest of the canon and notice which derivations are elided.

## Related pages in the wiki

- [[little-book-generative-ai-foundations]] — the Chen primer
- [[variational-autoencoder]]
- [[score-based-models]]
- [[normalizing-flows]]
- [[energy-based-models]]
- [[generative-adversarial-networks]]
- [[diffusion-models]]
- [[evidence-lower-bound-elbo]]
- [[generative-ai]]

## Caveats

- This comparison is from the perspective of someone who has read Chen cover-to-cover and skimmed the others. The "Murphy" assessment is from having used PML as a reference for years, not from a fresh read.
- I have not read *all* of Murphy Vol II; the chapters on EBMs and diffusion are particularly heavy in places.
- New primers appear regularly. The 2025+ landscape (Yang Song's score-based lecture notes at Stanford, Karras's analysis of diffusion architectures) overlaps with Chen in places and exceeds him in others.
- The field moves. This snapshot is from June 2026; check for newer resources.

## Confidence

0.85 — Chen assessment is from a fresh careful read; Murphy/Prince assessments are from long use rather than fresh cover-to-cover reading. Recommendations are my opinion, not measurement.
