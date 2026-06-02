---
created: 2026-07-28
updated: 2026-07-28
type: concept
summary: Diffusion models — generative models that learn to reverse a noise process to generate data
tags: [generative-ai, diffusion, image-generation, generative-models]
sources: []
status: stub
confidence: 0.3
---

# Diffusion Models

Diffusion models are a class of generative models that learn to generate data by reversing a gradual noising process. Starting from pure noise, the model learns to denoise step by step to produce samples matching the training distribution.

## Key Characteristics

- **Denoising diffusion**: Generates samples by iterative denoising
- **Latent diffusion**: Operates in latent space for efficiency (Stable Diffusion architecture)
- **Score-based**: Equivalent to learning the score function of the data distribution
- **Classifier-free guidance**: Uses joint embedding to guide generation without classifier

## Relationship to Other Generative Models

See [[generative-ai]] for comparison with autoregressive transformers, VAEs, and GANs.

For the mathematical foundations (forward/reverse SDE, score matching, ELBO derivations), see the primer [[little-book-generative-ai-foundations]] Chapters 4–6.

See also [[score-based-models]] — score-based models are mathematically equivalent to diffusion under the right parameterisation.

The diffusion ELBO uses the [[evidence-lower-bound-elbo]] as its central training objective.

## See Also
- [[concepts/diffusion-models]]
- [[concepts/generative-ai]]
- [[wiki/index]]
- [[log]]
- [[diffusion-models]]

- [[generative-ai]]: parent concept covering all generative model types