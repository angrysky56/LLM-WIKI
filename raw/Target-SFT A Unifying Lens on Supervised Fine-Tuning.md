---
title: "Target-SFT: A Unifying Lens on Supervised Fine-Tuning"
source: "https://txie1.github.io/Target-SFT/"
author:
published:
created: 2026-06-12
description:
tags:
  - "clippings"
---
## A Unifying Lens on SFT Through Target Distribution Design

Overview

SFT is usually studied through its loss function, but each loss implicitly defines a **target distribution** the model is pushed toward. We make this view explicit with the **Q-target framework**, which unifies existing SFT variants under two key design choices, and propose **Target-SFT** to adaptively shape both choices.

- 1 **Framework.** We view the SFT target as a mixture $Q_t = \gamma_t \delta_{y_t} + (1-\gamma_t)\tilde\pi_t$, which relaxes imitation and allows alternatives when the label is uncertain.
- 2 **Unify.** Many existing SFT variants represent implicit choices of $\gamma_t$ and $\tilde\pi_t$.
- 3 **Target-SFT.** We design both branches explicitly: $\gamma_t$ via model probability, and $\tilde\pi_t$ via a teacher-guided distribution. It outperforms across all 10 SFT settings evaluated.

Motivation

## Loss is a surrogate. What target does it lead to?

Invert the cross-entropy gradient to find out: $Q_k = p_k - g_k$.

![Illustration: dataset token → loss gradients → induced target distribution](https://txie1.github.io/Target-SFT/img/figs/target_sft_main.png)

At each prefix $x_t$, the model outputs logits $z$ and a distribution $p = \text{softmax}(z)$. Now suppose there exists some target distribution $Q$ over the vocabulary that we want the model to match. If we train with cross-entropy towards $Q$, then the gradient with respect to a logit $k$ is

$$
\frac{\partial \mathcal{L}_{\text{CE}}}{\partial z_k} = p_k - Q_k
$$

Then given any differentiable loss $\mathcal{L}$ with logit gradient $g_k = \partial \mathcal{L}/\partial z_k$, we can invert this relationship to find the induced target distribution under this update rule:

$$
Q_k := p_k - g_k
$$

This reveals what each loss is actually teaching the model, via the probability updates it defines.

Beyond the choice of loss, SFT is a choice of target distribution.

Loss is the mechanism; the target is what the model actually learns.

Example

## From Loss to Target

Standard SFT learns one-hot target $\delta_{y_t}$; p-loss interpolates from $p$ to $\delta_{y_t}$.

We illustrate this with two losses: standard SFT and p-loss (a token-level variant that scales SFT loss by the model's current probability $p_y$). Applying $Q_k = p_k - g_k$ to each derives the target.

Interactive

This visualizes the comparison. It plots the effects of each loss function, on both the observed token $y_t$ (solid), and a non-observed token $k \ne y_t$ (dashed). Hover on legend to highlight corresponding curves.

Model probability in observed token: $p_y$ = 0.30

Low confidenceMediumHigh confidence

Method SFT p-loss

Token Observed $y_t$ Other tokens $k$

Loss Gradient    $\;\partial\mathcal{L}/\partial z_k$

$1-p_y$

$-p_k$

$p_y(1-p_y)$

$-p_y p_k$

Induced Q-Target

$1$

$2p_y - p_y^2$

$0$

$(1-p_y)\,p_k$

x-axis = current model probability on the token of interest: $p_y$ for the observed token (solid), $p_k$ for other tokens (dashed).

SFT

Constant updates

Gradient pulls toward $y_t$ and suppresses all $k$ with *fixed* strength, no matter how certain the model already is.

Q-target

Always $\delta_{y_t}$ (full probability mass on the observed token)

p-loss

Confidence-scaled updates

Gradient scales with $p_y$: near-zero when uncertain ($p_y \approx 0$), approaches standard SFT strength as $p_y \to 1$.

Q-target

 $p_y \to 0$: $Q \to p$ (no change); $p_y \to 1$: $Q \to \delta_{y_t}$ (SFT)

**Standard SFT's implicit assumption:** every observed token is ideal and uniquely correct, regardless of noise, ambiguity, or alignment with the model's existing knowledge.

Framework

## The Q-Target View

Relax the one-hot target $\delta_{y_t}$ to account for label uncertainty.

But an observed token may be noisy, non-unique, or misaligned with the model. Instead of forcing a rigid one-hot target, we explicitly model for this uncertainty. We replace $\delta_y$ with a mixture distribution $Q_t$ controlled by two design choices:

$$
Q_t = \gamma_t \,\delta_{y_t} + (1 - \gamma_t)\,\tilde{\pi}_t
$$

| Component | Design Question | Effect |
| --- | --- | --- |
| $\gamma_t \in [0,1]$ | How much should we trust the observed token $y_t$? | Controls imitation strength |
| $\tilde{\pi}_t \in \Delta^{\|\mathcal{V}\|}$ | Where should the remaining $(1-\gamma_t)$ mass go? | Shapes alternative supervision |

The training objective under $Q_t$ decomposes cleanly:

$$
\mathcal{L}_Q(\theta) = {\color{#d97706}\gamma_t} \underbrace{\text{CE}(\delta_{y_t},\, \pi_\theta)}_{\text{imitate } y_t} + {\color{#d97706}(1-\gamma_t)} \underbrace{\text{CE}({\color{#2563eb}\tilde\pi_t},\, \pi_\theta)}_{\text{match alternatives}}
$$

This view shows that SFT training balances two forces: imitation of the label and matching of a residual distribution. Standard SFT simply sets $\gamma_t = 1$, collapsing the second term entirely.

Unifying Lens

## SFT variants are implicit Q-target designs

Seemingly different losses vary only in the choice of $\gamma_t$ and $\tilde\pi_t$.

Click any row to see method details ·

<table><thead><tr><th>Method</th><th>Category</th><th><math><semantics><mrow><msub><mi>γ</mi> <mi>t</mi></msub></mrow> <annotation>\gamma_t</annotation></semantics></math></th><th><math><semantics><mrow><msub><mover><mi>π</mi> <mo>~</mo></mover> <mi>t</mi></msub></mrow> <annotation>\tilde\pi_t</annotation></semantics></math></th></tr></thead><tbody><tr><td><strong>Standard SFT</strong></td><td>One-hot</td><td><math><semantics><mrow><mn>1</mn></mrow> <annotation>1</annotation></semantics></math></td><td>—</td></tr><tr><td colspan="4"><p>Objective</p><p><math><semantics><mrow><msubsup><mi>ℓ</mi> <mi>t</mi> <mtext>SFT</mtext></msubsup> <mo>=</mo> <mo>−</mo> <mi>log</mi> <mo>⁡</mo> <msub><mi>p</mi> <mi>t</mi></msub></mrow> <annotation>\ell_t^\text{SFT} = -\log p_t</annotation></semantics></math></p><p>Motivation</p><p>Maximize likelihood of every observed token.</p></td></tr><tr><td><strong>DFT</strong></td><td>Label Trust</td><td><math><semantics><mrow><msub><mi>p</mi> <mi>t</mi></msub></mrow> <annotation>p_t</annotation></semantics></math></td><td><math><semantics><mrow><msub><mi>π</mi> <mi>θ</mi></msub> <mo>(</mo><mo>⋅</mo> <mo>∣</mo> <msub><mi>x</mi> <mi>t</mi></msub><mo>)</mo></mrow> <annotation>\pi_\theta(\cdot\mid x_t)</annotation></semantics></math></td></tr><tr><td colspan="4"><p>Objective</p><p><math><semantics><mrow><msubsup><mi>ℓ</mi> <mi>t</mi> <mtext>DFT</mtext></msubsup> <mo>=</mo> <mo>−</mo> <mtext>sg</mtext> <mo>[</mo><msub><mi>p</mi> <mi>t</mi></msub><mo>]</mo> <mi>log</mi> <mo>⁡</mo> <msub><mi>p</mi> <mi>t</mi></msub></mrow> <annotation>\ell_t^\text{DFT} = -\text{sg}[p_t]\log p_t</annotation></semantics></math></p><p>Motivation</p><p>Use probability weighting to connect SFT with an RL-style objective.<a href="https://arxiv.org/abs/2508.05629">Paper ↗</a></p></td></tr><tr><td><strong>Beyond-log</strong></td><td>Label Trust</td><td><math><semantics><mrow><msubsup><mi>p</mi> <mi>t</mi> <mi>α</mi></msubsup></mrow> <annotation>p_t^\alpha</annotation></semantics></math></td><td><math><semantics><mrow><msub><mi>π</mi> <mi>θ</mi></msub> <mo>(</mo><mo>⋅</mo> <mo>∣</mo> <msub><mi>x</mi> <mi>t</mi></msub><mo>)</mo></mrow> <annotation>\pi_\theta(\cdot\mid x_t)</annotation></semantics></math></td></tr><tr><td colspan="4"><p>Objective</p><p><math><semantics><mrow><msubsup><mi>ℓ</mi> <mi>t</mi> <mi>f</mi></msubsup> <mo>=</mo> <mi>f</mi> <mo>(</mo><msub><mi>p</mi> <mi>t</mi></msub><mo>)</mo><mo>,</mo><msubsup><mi>ℓ</mi> <mi>t</mi> <mi>α</mi></msubsup> <mo>=</mo> <mfrac><mrow><mn>1</mn> <mo>−</mo> <msubsup><mi>p</mi> <mi>t</mi> <mi>α</mi></msubsup></mrow> <mi>α</mi></mfrac></mrow> <annotation>\ell_t^f = f(p_t), \quad \ell_t^\alpha = \frac{1-p_t^\alpha}{\alpha}</annotation></semantics></math></p><p>Motivation</p><p>Use probability-dependent objectives to balance learning across model capacities.<a href="https://arxiv.org/abs/2510.00526">Paper ↗</a></p></td></tr><tr><td><strong>ProFiT</strong></td><td>Label Trust</td><td><math><semantics><mrow><msub><mi>m</mi> <mi>t</mi></msub> <mo>=</mo> <mn>1</mn> <mo>{</mo> <msub><mi>p</mi> <mi>t</mi></msub> <mo>></mo> <mi>τ</mi> <mo>}</mo></mrow> <annotation>m_t = \mathbf{1}\{p_t > \tau\}</annotation></semantics></math></td><td><math><semantics><mrow><msub><mi>π</mi> <mi>θ</mi></msub> <mo>(</mo><mo>⋅</mo> <mo>∣</mo> <msub><mi>x</mi> <mi>t</mi></msub><mo>)</mo></mrow> <annotation>\pi_\theta(\cdot\mid x_t)</annotation></semantics></math></td></tr><tr><td colspan="4"><p>Objective</p><p><math><semantics><mrow><msub><mi>m</mi> <mi>t</mi></msub> <mo>=</mo> <mn>1</mn> <mo>[</mo><mtext>sg</mtext> <mo>(</mo><msub><mi>p</mi> <mi>t</mi></msub><mo>)</mo> <mo>></mo> <mi>τ</mi><mo>]</mo><mo>,</mo><msubsup><mi>ℓ</mi> <mi>t</mi> <mtext>ProFiT</mtext></msubsup> <mo>=</mo> <mo>−</mo> <msub><mi>m</mi> <mi>t</mi></msub> <mi>log</mi> <mo>⁡</mo> <msub><mi>p</mi> <mi>t</mi></msub></mrow> <annotation>m_t = \mathbf{1}[\text{sg}(p_t) > \tau], \quad \ell_t^\text{ProFiT} = -m_t\log p_t</annotation></semantics></math></p><p>Motivation</p><p>Use probability to identify and train on core tokens.<a href="https://arxiv.org/abs/2601.09195">Paper ↗</a></p></td></tr><tr><td><strong>EAFT</strong></td><td>Label Trust</td><td><math><semantics><mrow><msub><mover><mi>H</mi> <mo>~</mo></mover> <mi>t</mi></msub> <mo>=</mo> <mi>H</mi> <mo>(</mo><msubsup><mi>π</mi> <mrow><mi>θ</mi><mo>,</mo><mi>t</mi></mrow> <mrow><mo>(</mo><mi>k</mi><mo>)</mo></mrow></msubsup><mo>)</mo> <mi>/</mi> <mi>log</mi> <mo>⁡</mo> <mi>k</mi></mrow> <annotation>\tilde{H}_t = H(\pi_{\theta,t}^{(k)})/\log k</annotation></semantics></math></td><td><math><semantics><mrow><msub><mi>π</mi> <mi>θ</mi></msub> <mo>(</mo><mo>⋅</mo> <mo>∣</mo> <msub><mi>x</mi> <mi>t</mi></msub><mo>)</mo></mrow> <annotation>\pi_\theta(\cdot\mid x_t)</annotation></semantics></math></td></tr><tr><td colspan="4"><p>Objective</p><p><math><semantics><mrow><msub><mover><mi>H</mi> <mo>~</mo></mover> <mi>t</mi></msub> <mo>=</mo> <mtext>sg</mtext>  ⁣ <mrow><mo>[</mo><mfrac><mrow><mi>H</mi> <mo>(</mo><msubsup><mi>π</mi> <mrow><mi>θ</mi><mo>,</mo><mi>t</mi></mrow> <mrow><mo>(</mo><mi>k</mi><mo>)</mo></mrow></msubsup><mo>)</mo></mrow> <mrow><mi>log</mi> <mo>⁡</mo> <mi>k</mi></mrow></mfrac><mo>]</mo></mrow><mo>,</mo><msubsup><mi>ℓ</mi> <mi>t</mi> <mtext>EAFT</mtext></msubsup> <mo>=</mo> <mo>−</mo> <msub><mover><mi>H</mi> <mo>~</mo></mover> <mi>t</mi></msub> <mi>log</mi> <mo>⁡</mo> <msub><mi>p</mi> <mi>t</mi></msub></mrow> <annotation>\tilde{H}_t = \text{sg}\!\left[\frac{H(\pi_{\theta,t}^{(k)})}{\log k}\right], \quad \ell_t^\text{EAFT} = -\tilde{H}_t\log p_t</annotation></semantics></math></p><p>Motivation</p><p>Use entropy to weight uncertain or knowledge-conflicting tokens.<a href="https://arxiv.org/abs/2601.02151">Paper ↗</a></p></td></tr><tr><td><strong>iw-SFT</strong></td><td>Label Trust</td><td><math><semantics><mrow><mi>w</mi> <mo>(</mo><mi>τ</mi><mo>)</mo> <mo>=</mo> <mi>q</mi> <mo>(</mo><mi>τ</mi><mo>)</mo> <mi>/</mi> <msub><mi>π</mi> <mtext>ref</mtext></msub> <mo>(</mo><mi>τ</mi><mo>)</mo></mrow> <annotation>w(\tau) = q(\tau)/\pi_\text{ref}(\tau)</annotation></semantics></math></td><td><math><semantics><mrow><msub><mi>π</mi> <mi>θ</mi></msub> <mo>(</mo><mo>⋅</mo> <mo>∣</mo> <msub><mi>x</mi> <mi>t</mi></msub><mo>)</mo></mrow> <annotation>\pi_\theta(\cdot\mid x_t)</annotation></semantics></math></td></tr><tr><td colspan="4"><p>Objective</p><p><math><semantics><mrow><mi>w</mi> <mo>(</mo><mi>τ</mi><mo>)</mo> <mo>=</mo> <mfrac><mrow><mi>q</mi> <mo>(</mo><mi>τ</mi><mo>)</mo></mrow> <mrow><msub><mi>π</mi> <mtext>ref</mtext></msub> <mo>(</mo><mi>τ</mi><mo>)</mo></mrow></mfrac>    <mo>(</mo><mi>w</mi> <mtext>trajectory-level</mtext><mo>)</mo><mo>,</mo><msubsup><mi>ℓ</mi> <mi>t</mi> <mtext>iw</mtext></msubsup> <mo>=</mo> <mo>−</mo> <mi>w</mi> <mo>(</mo><mi>τ</mi><mo>)</mo> <mi>log</mi> <mo>⁡</mo> <msub><mi>p</mi> <mi>t</mi></msub></mrow> <annotation>w(\tau) = \frac{q(\tau)}{\pi_\text{ref}(\tau)}\;(w\text{ trajectory-level}), \quad \ell_t^\text{iw} = -w(\tau)\log p_t</annotation></semantics></math></p><p>Motivation</p><p>Use an auxiliary distribution to assign trajectory-level weights.<a href="https://arxiv.org/abs/2507.12856">Paper ↗</a></p></td></tr><tr><td><strong>CFT</strong></td><td>Label Trust</td><td><math><semantics><mrow><msub><mi>c</mi> <mi>t</mi></msub> <mo>=</mo> <mn>1</mn> <mo>{</mo> <msub><mi>y</mi> <mi>t</mi></msub> <mtext>critical</mtext> <mo>}</mo></mrow> <annotation>c_t = \mathbf{1}\{y_t \text{ critical}\}</annotation></semantics></math></td><td><math><semantics><mrow><msub><mi>π</mi> <mi>θ</mi></msub> <mo>(</mo><mo>⋅</mo> <mo>∣</mo> <msub><mi>x</mi> <mi>t</mi></msub><mo>)</mo></mrow> <annotation>\pi_\theta(\cdot\mid x_t)</annotation></semantics></math></td></tr><tr><td colspan="4"><p>Objective</p><p><math><semantics><mrow><msub><mi>c</mi> <mi>t</mi></msub> <mo>=</mo> <mn>1</mn>  ⁣ <mrow><mo>[</mo><mi>∀</mi> <msub><mover><mi>y</mi> <mo>~</mo></mover> <mi>t</mi></msub> <mo>∈</mo> <msub><mi>A</mi> <mi>t</mi></msub><mo>,</mo>   <mtext>Correct</mtext> <mo>(</mo><msub><mi>y</mi> <mrow><mo><</mo> <mi>t</mi></mrow></msub><mo>,</mo><msub><mover><mi>y</mi> <mo>~</mo></mover> <mi>t</mi></msub><mo>,</mo><msub><mi>y</mi> <mrow><mo>></mo> <mi>t</mi></mrow></msub><mo>)</mo> <mo>=</mo> <mn>0</mn><mo>]</mo></mrow></mrow> <annotation>c_t = \mathbf{1}\!\left[\forall\tilde{y}_t \in \mathcal{A}_t,\;\text{Correct}(y_{<t},\tilde{y}_t,y_{>t})=0\right]</annotation></semantics></math> <math><semantics><mrow><msubsup><mi>ℓ</mi> <mi>t</mi> <mtext>CFT</mtext></msubsup> <mo>=</mo> <mo>−</mo> <msub><mi>c</mi> <mi>t</mi></msub> <mi>log</mi> <mo>⁡</mo> <msub><mi>p</mi> <mi>t</mi></msub></mrow> <annotation>\ell_t^\text{CFT} = -c_t\log p_t</annotation></semantics></math></p><p>Motivation</p><p>Update only causally critical / irreplaceable tokens.<a href="https://arxiv.org/abs/2510.10974">Paper ↗</a></p></td></tr><tr><td><strong>Label Smoothing</strong></td><td>Residual Dist.</td><td><math><semantics><mrow><mn>1</mn> <mo>−</mo> <mi>λ</mi></mrow> <annotation>1 - \lambda</annotation></semantics></math></td><td><math><semantics><mrow><mtext>Unif</mtext> <mo>(</mo><mi>V</mi><mo>)</mo></mrow> <annotation>\text{Unif}(\mathcal{V})</annotation></semantics></math></td></tr><tr><td><strong>SFT + KL</strong></td><td>Residual Dist.</td><td><math><semantics><mrow><mfrac><mn>1</mn> <mrow><mn>1</mn> <mo>+</mo> <mi>λ</mi></mrow></mfrac></mrow> <annotation>\frac{1}{1+\lambda}</annotation></semantics></math></td><td><math><semantics><mrow><msub><mi>π</mi> <mtext>ref</mtext></msub> <mo>(</mo><mo>⋅</mo> <mo>∣</mo> <msub><mi>x</mi> <mi>t</mi></msub><mo>)</mo></mrow> <annotation>\pi_\text{ref}(\cdot\mid x_t)</annotation></semantics></math></td></tr><tr><td colspan="4"><p>Objective</p><p><math><semantics><mrow><msubsup><mi>ℓ</mi> <mi>t</mi> <mtext>KL</mtext></msubsup> <mo>=</mo> <mo>−</mo> <mi>log</mi> <mo>⁡</mo> <msub><mi>p</mi> <mi>t</mi></msub> <mo>+</mo> <mi>λ</mi>   <mtext>KL</mtext> <mo>(</mo><msub><mi>π</mi> <mtext>ref</mtext></msub> <mo>(</mo><mo>⋅</mo> <mo>∣</mo> <msub><mi>x</mi> <mi>t</mi></msub><mo>)</mo> <mi>∥</mi> <msub><mi>π</mi> <mi>θ</mi></msub> <mo>(</mo><mo>⋅</mo> <mo>∣</mo> <msub><mi>x</mi> <mi>t</mi></msub><mo>)</mo><mo>)</mo></mrow> <annotation>\ell_t^\text{KL} = -\log p_t + \lambda\,\text{KL}(\pi_\text{ref}(\cdot\mid x_t)\|\pi_\theta(\cdot\mid x_t))</annotation></semantics></math></p><p>Motivation</p><p>Constrain updates with a reference model to limit drift.<a href="https://arxiv.org/abs/2509.04259">Paper ↗</a></p></td></tr><tr><td><strong>ASFT</strong></td><td>Residual Dist.</td><td><math><semantics><mrow><mfrac><msub><mi>p</mi> <mi>t</mi></msub> <mrow><msub><mi>p</mi> <mi>t</mi></msub> <mo>+</mo> <mi>λ</mi></mrow></mfrac></mrow> <annotation>\frac{p_t}{p_t+\lambda}</annotation></semantics></math></td><td><math><semantics><mrow><msub><mi>π</mi> <mtext>base</mtext></msub> <mo>(</mo><mo>⋅</mo> <mo>∣</mo> <msub><mi>x</mi> <mi>t</mi></msub><mo>)</mo></mrow> <annotation>\pi_\text{base}(\cdot\mid x_t)</annotation></semantics></math></td></tr><tr><td colspan="4"><p>Objective</p><p><math><semantics><mrow><msubsup><mi>ℓ</mi> <mi>t</mi> <mtext>ASFT</mtext></msubsup> <mo>=</mo> <msubsup><mi>ℓ</mi> <mi>t</mi> <mtext>DFT</mtext></msubsup> <mo>+</mo> <mi>λ</mi>   <mtext>KL</mtext> <mo>(</mo><msub><mi>π</mi> <mtext>base</mtext></msub> <mo>(</mo><mo>⋅</mo> <mo>∣</mo> <msub><mi>x</mi> <mi>t</mi></msub><mo>)</mo> <mi>∥</mi> <msub><mi>π</mi> <mi>θ</mi></msub> <mo>(</mo><mo>⋅</mo> <mo>∣</mo> <msub><mi>x</mi> <mi>t</mi></msub><mo>)</mo><mo>)</mo></mrow> <annotation>\ell_t^\text{ASFT} = \ell_t^\text{DFT} + \lambda\,\text{KL}(\pi_\text{base}(\cdot\mid x_t)\|\pi_\theta(\cdot\mid x_t))</annotation></semantics></math></p><p>Motivation</p><p>Constrain updates in DFT to prevent distributional drift.<a href="https://arxiv.org/abs/2509.23753">Paper ↗</a></p></td></tr><tr><td><strong>Proximal SFT</strong></td><td>Residual Dist.</td><td>clipping-dependent</td><td><math><semantics><mrow><msub><mi>π</mi> <mtext>old</mtext></msub> <mo>(</mo><mo>⋅</mo> <mo>∣</mo> <msub><mi>x</mi> <mi>t</mi></msub><mo>)</mo></mrow> <annotation>\pi_\text{old}(\cdot\mid x_t)</annotation></semantics></math></td></tr><tr><td colspan="4"><p>Objective</p><p><math><semantics><mrow><msub><mi>r</mi> <mi>t</mi></msub> <mo>=</mo> <mfrac><msub><mi>p</mi> <mi>t</mi></msub> <mrow><msub><mi>π</mi> <mtext>old</mtext></msub> <mo>(</mo><msub><mi>y</mi> <mi>t</mi></msub> <mo>∣</mo> <msub><mi>x</mi> <mi>t</mi></msub><mo>)</mo></mrow></mfrac><mo>,</mo><msubsup><mi>ℓ</mi> <mi>t</mi> <mtext>PSFT</mtext></msubsup> <mo>=</mo> <mo>−</mo> <mi>min</mi> <mo>⁡</mo>  ⁣ <mrow><mo>(</mo><msub><mi>r</mi> <mi>t</mi></msub><mo>,</mo>  <mtext>clip</mtext> <mo>(</mo><msub><mi>r</mi> <mi>t</mi></msub><mo>,</mo><mn>1</mn> <mo>−</mo> <mi>ϵ</mi><mo>,</mo><mn>1</mn> <mo>+</mo> <mi>ϵ</mi><mo>)</mo><mo>)</mo></mrow></mrow> <annotation>r_t = \frac{p_t}{\pi_\text{old}(y_t\mid x_t)}, \quad \ell_t^\text{PSFT} = -\min\!\left(r_t,\,\text{clip}(r_t,1-\epsilon,1+\epsilon)\right)</annotation></semantics></math></p><p>Motivation</p><p>Clip ratio to enforce updates within a trust region.<a href="https://arxiv.org/abs/2508.17784">Paper ↗</a></p></td></tr><tr><td><strong>GEM</strong></td><td>Residual Dist.</td><td><math><semantics><mrow><msubsup><mi>γ</mi> <mi>t</mi> <mi>y</mi></msubsup> <mo>=</mo> <mn>1</mn><mo>,</mo>   <msubsup><mi>γ</mi> <mi>t</mi> <mo>−</mo></msubsup> <mo>=</mo> <mn>1</mn></mrow> <annotation>\gamma_t^y = 1,\;\gamma_t^- = 1</annotation></semantics></math></td><td><math><semantics><mrow><msubsup><mover><mi>π</mi> <mo>~</mo></mover> <mi>t</mi> <mo>+</mo></msubsup> <mo>=</mo> <msub><mi>π</mi> <mi>θ</mi></msub> <mo>(</mo><mo>⋅</mo> <mo>∣</mo> <msub><mi>x</mi> <mi>t</mi></msub><mo>)</mo><mo>,</mo>   <msubsup><mover><mi>π</mi> <mo>~</mo></mover> <mi>t</mi> <mo>−</mo></msubsup> <mo>=</mo> <msubsup><mi>π</mi> <mi>θ</mi> <mrow><mo>(</mo><mi>β</mi><mo>)</mo></mrow></msubsup> <mo>(</mo><mo>⋅</mo> <mo>∣</mo> <msub><mi>x</mi> <mi>t</mi></msub><mo>)</mo></mrow> <annotation>\tilde\pi_t^+ = \pi_\theta(\cdot\mid x_t),\;\tilde\pi_t^- = \pi_\theta^{(\beta)}(\cdot\mid x_t)</annotation></semantics></math></td></tr><tr><td colspan="4"><p>Objective</p><p><math><semantics><mrow><msub><mi>q</mi> <mi>t</mi></msub> <mo>(</mo><mi>v</mi><mo>)</mo> <mo>=</mo> <mfrac><mrow><mtext>sg</mtext> <mo>[</mo><msub><mi>π</mi> <mrow><mi>θ</mi><mo>,</mo><mi>t</mi></mrow></msub> <mo>(</mo><mi>v</mi><mo>)</mo><msup><mo>]</mo> <mrow><mn>1</mn> <mi>/</mi> <mi>β</mi></mrow></msup></mrow> <mrow><munder><mo>∑</mo> <mrow><mi>u</mi> <mo>∈</mo> <mi>V</mi></mrow></munder> <mtext>sg</mtext> <mo>[</mo><msub><mi>π</mi> <mrow><mi>θ</mi><mo>,</mo><mi>t</mi></mrow></msub> <mo>(</mo><mi>u</mi><mo>)</mo><msup><mo>]</mo> <mrow><mn>1</mn> <mi>/</mi> <mi>β</mi></mrow></msup></mrow></mfrac></mrow> <annotation>q_t(v) = \frac{\text{sg}[\pi_{\theta,t}(v)]^{1/\beta}}{\sum_{u\in\mathcal{V}}\text{sg}[\pi_{\theta,t}(u)]^{1/\beta}}</annotation></semantics></math> <math><semantics><mrow><msubsup><mi>ℓ</mi> <mi>t</mi> <mtext>GEM</mtext></msubsup> <mo>=</mo> <mtext>CE</mtext> <mo>(</mo><msub><mi>δ</mi> <msub><mi>y</mi> <mi>t</mi></msub></msub><mo>,</mo><msub><mi>π</mi> <mrow><mi>θ</mi><mo>,</mo><mi>t</mi></mrow></msub><mo>)</mo> <mo>−</mo> <mtext>CE</mtext> <mo>(</mo><msub><mi>q</mi> <mi>t</mi></msub><mo>,</mo><msub><mi>π</mi> <mrow><mi>θ</mi><mo>,</mo><mi>t</mi></mrow></msub><mo>)</mo></mrow> <annotation>\ell_t^\text{GEM} = \text{CE}(\delta_{y_t},\pi_{\theta,t}) - \text{CE}(q_t,\pi_{\theta,t})</annotation></semantics></math></p><p>Motivation</p><p>Control probability transfer from alternatives to the observed token to preserve diversity.<a href="https://arxiv.org/abs/2408.16673">Paper ↗</a></p></td></tr><tr><td><strong>Knowledge Distillation</strong></td><td>Residual Dist.</td><td><math><semantics><mrow><mn>0</mn></mrow> <annotation>0</annotation></semantics></math></td><td><math><semantics><mrow><msub><mi>π</mi> <mi>T</mi></msub> <mo>(</mo><mo>⋅</mo> <mo>∣</mo> <msub><mi>x</mi> <mi>t</mi></msub><mo>)</mo></mrow> <annotation>\pi_T(\cdot\mid x_t)</annotation></semantics></math></td></tr><tr><td colspan="4"><p>Objective</p><p><math><semantics><mrow><msubsup><mi>ℓ</mi> <mi>t</mi> <mtext>KD</mtext></msubsup> <mo>=</mo> <mo>−</mo> <munder><mo>∑</mo> <mrow><mi>v</mi> <mo>∈</mo> <mi>V</mi></mrow></munder> <msub><mi>π</mi> <mi>T</mi></msub> <mo>(</mo><mi>v</mi> <mo>∣</mo> <msub><mi>x</mi> <mi>t</mi></msub><mo>)</mo> <mi>log</mi> <mo>⁡</mo> <msub><mi>π</mi> <mi>S</mi></msub> <mo>(</mo><mi>v</mi> <mo>∣</mo> <msub><mi>x</mi> <mi>t</mi></msub><mo>)</mo></mrow> <annotation>\ell_t^\text{KD} = -\sum_{v\in\mathcal{V}}\pi_T(v\mid x_t)\log\pi_S(v\mid x_t)</annotation></semantics></math></p><p>Motivation</p><p>Use the teacher logit distribution as a soft target.<a href="https://arxiv.org/abs/1503.02531">Paper ↗</a></p></td></tr><tr><td><strong>Distillation (Hybrid)</strong></td><td>Residual Dist.</td><td><math><semantics><mrow><mn>1</mn> <mo>−</mo> <mi>λ</mi></mrow> <annotation>1 - \lambda</annotation></semantics></math></td><td><math><semantics><mrow><msub><mi>π</mi> <mi>T</mi></msub> <mo>(</mo><mo>⋅</mo> <mo>∣</mo> <msub><mi>x</mi> <mi>t</mi></msub><mo>)</mo></mrow> <annotation>\pi_T(\cdot\mid x_t)</annotation></semantics></math></td></tr><tr><td colspan="4"><p>Objective</p><p><math><semantics><mrow><msubsup><mi>ℓ</mi> <mi>t</mi> <mtext>KD-H</mtext></msubsup> <mo>=</mo> <mo>(</mo><mn>1</mn> <mo>−</mo> <mi>λ</mi><mo>)</mo> <mo>[</mo><mo>−</mo> <mi>log</mi> <mo>⁡</mo> <msub><mi>π</mi> <mi>S</mi></msub> <mo>(</mo><msub><mi>y</mi> <mi>t</mi></msub> <mo>∣</mo> <msub><mi>x</mi> <mi>t</mi></msub><mo>)</mo><mo>]</mo> <mo>+</mo> <mi>λ</mi>   <msub><mi>D</mi> <mtext>KL</mtext></msub> <mo>(</mo><msub><mi>π</mi> <mi>T</mi></msub> <mo>(</mo><mo>⋅</mo> <mo>∣</mo> <msub><mi>x</mi> <mi>t</mi></msub><mo>)</mo> <mi>∥</mi> <msub><mi>π</mi> <mi>S</mi></msub> <mo>(</mo><mo>⋅</mo> <mo>∣</mo> <msub><mi>x</mi> <mi>t</mi></msub><mo>)</mo><mo>)</mo></mrow> <annotation>\ell_t^\text{KD-H} = (1-\lambda)[-\log\pi_S(y_t\mid x_t)] + \lambda\,D_\text{KL}(\pi_T(\cdot\mid x_t)\|\pi_S(\cdot\mid x_t))</annotation></semantics></math></p><p>Motivation</p><p>Combine hard-label imitation with teacher logit distribution for enriched soft supervision.<a href="https://arxiv.org/abs/1503.02531">Paper ↗</a></p></td></tr><tr><td><strong>Target-SFT</strong></td><td>Both</td><td><math><semantics><mrow><msub><mi>p</mi> <mi>t</mi></msub></mrow> <annotation>p_t</annotation></semantics></math></td><td><math><semantics><mrow><msubsup><mover><mi>π</mi> <mo>~</mo></mover> <mi>t</mi> <mtext>guided</mtext></msubsup> <mo>∝</mo> <msub><mi>π</mi> <mi>θ</mi></msub> <mo>(</mo><mo>⋅</mo> <mo>∣</mo> <msub><mi>x</mi> <mi>t</mi></msub><msup><mo>)</mo> <mrow><mn>1</mn> <mo>−</mo> <mi>η</mi></mrow></msup>   <msub><mi>π</mi> <mi>T</mi></msub> <mo>(</mo><mo>⋅</mo> <mo>∣</mo> <msub><mi>x</mi> <mi>t</mi></msub><msup><mo>)</mo> <mi>η</mi></msup></mrow> <annotation>\tilde\pi_t^\text{guided} \propto \pi_\theta(\cdot\mid x_t)^{1-\eta}\,\pi_T(\cdot\mid x_t)^\eta</annotation></semantics></math></td></tr><tr><td colspan="4"><p>Objective</p><p><math><semantics><mrow><msubsup><mi>Q</mi> <mi>t</mi> <mtext>TARGET</mtext></msubsup> <mo>=</mo> <msub><mi>p</mi> <mi>t</mi></msub>   <msub><mi>δ</mi> <msub><mi>y</mi> <mi>t</mi></msub></msub> <mo>+</mo> <mo>(</mo><mn>1</mn> <mo>−</mo> <msub><mi>p</mi> <mi>t</mi></msub><mo>)</mo>   <msubsup><mover><mi>π</mi> <mo>~</mo></mover> <mi>t</mi> <mtext>guided</mtext></msubsup></mrow> <annotation>Q_t^\text{TARGET} = p_t\,\delta_{y_t} + (1-p_t)\,\tilde{\pi}_t^\text{guided}</annotation></semantics></math> <math><semantics><mrow><msubsup><mi>ℓ</mi> <mi>t</mi> <mtext>TARGET</mtext></msubsup> <mo>=</mo> <mtext>CE</mtext> <mo>(</mo><msub><mi>π</mi> <mi>θ</mi></msub> <mo>(</mo><mo>⋅</mo> <mo>∣</mo> <msub><mi>x</mi> <mi>t</mi></msub><mo>)</mo><mo>,</mo>  <msubsup><mi>Q</mi> <mi>t</mi> <mtext>TARGET</mtext></msubsup><mo>)</mo></mrow> <annotation>\ell_t^\text{TARGET} = \text{CE}(\pi_\theta(\cdot\mid x_t),\, Q_t^\text{TARGET})</annotation></semantics></math></p><p>Motivation</p><p>Adaptively balance label imitation with teacher-guided fallback. Teacher influence scales with model uncertainty <math><semantics><mrow><mn>1</mn> <mo>−</mo> <msub><mi>p</mi> <mi>t</mi></msub></mrow> <annotation>1-p_t</annotation></semantics></math>.</p></td></tr></tbody></table>

Target-SFT

## Design both branches of Q-target

Define proxy for $\gamma_t$ and adaptively use teacher guidance in alternatives $\tilde\pi_t$.

Model probability $\pi_\theta(y_t \mid x_t)$ naturally encodes the support for $y_t$ among all plausible continuations, based on statistical evidence from pretraining. We use this as proxy for label reliability:

$$
\gamma_t \;=\; \pi_\theta(y_t \mid x_t)=\; p_y \;
$$

To preserve model prior while allowing external supervision, a teacher distribution provides reward-style signals to reshape $\pi_\theta(\cdot\mid x_t)$. This yields a teacher-guided distribution with closed form:

$$
\tilde{\pi}_t^\text{guided}(a) \;\propto\; \pi_\theta(a)^{1-\eta}\,\pi_T(a)^{\eta}
$$

$$
Q_t^\text{TARGET} \;=\; p_y\,\delta_{y_t} \;+\; (1-p_y)\,\tilde{\pi}_t^\text{guided}
$$

Trusted token gets strong supervision, with target approaches standard SFT's one-hot $\delta_{y_t}$; while uncertain token allocates higher weight to teacher-guided alternatives, approaches $\tilde{\pi}_t$. We train with cross-entropy loss to match $Q_t^\text{TARGET}$.

Results

Target-SFT improves reasoning performance across 10 dataset-model settings on math and medical benchmarks. While the baselines fluctuate, Target-SFT consistently achieves the best Average@16 results in every setting.

![Performance summary: Average@16 accuracy across all 10 dataset-model settings](https://txie1.github.io/Target-SFT/img/figs/all_avg.png)

## BibTeX

```
@article{xie2026targetsft,
  title     = {A Unifying Lens on Supervised Fine-Tuning Through Target Distribution Design},
  author    = {Tong Xie, Yuanhao Ban, Yunqi Hong, Sohyun An, Yihang Chen, Cho-Jui Hsieh},
  journal   = {arXiv},
  year      = {2026}
}
```