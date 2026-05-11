---
summary: Architectural falsification of the MOPS hypothesis — cross-layer geometric drift fails to detect hallucination in pretrained transformers; mechanistic explanation grounded in Pandey's sparse-circuit findings
tags: [synthesis, falsification, mechanistic-interpretability, hallucination, sheaf-cohomology, mops, conscience-servitor, pandey-2026, ty-research]
updated: 2026-05-11T08:10:10Z
created: 2026-05-11T08:10:10Z
---

---
created: 2026-05-10T22:30:00Z
updated: 2026-05-10T22:30:00Z
type: synthesis
summary: Architectural falsification of the MOPS hypothesis — cross-layer geometric drift fails to detect hallucination in pretrained transformers; mechanistic explanation grounded in Pandey's sparse-circuit findings
tags: [synthesis, falsification, mechanistic-interpretability, hallucination, sheaf-cohomology, mops, conscience-servitor, pandey-2026, ty-research]
status: active
confidence: 0.92
---

# Why Cross-Layer Geometric Drift Doesn't Detect Hallucination: An Architectural Falsification Grounded in Sparse Circuit Findings

**Status:** Falsified hypothesis — empirically grounded
**Project:** MOPS Transformer (`/home/ty/Repositories/ai_workspace/mops-transformer`)
**Companion:** Falsity Substrate Monitor design for [[conscience-servitor]]
**Reference paper:** Pandey (2026), arXiv:2604.19117v4

---

## Core Insight

The MOPS Transformer architecture proposed that **hallucination is detectable as a geometric inconsistency in the layer-to-layer dynamics of a transformer's residual stream** — that incoherent content "fails to glue" across depth, and that this gluing failure could be measured by a learnable sheaf-cohomological apparatus (per-layer projections + restriction maps + L2-norm drift signal).

Empirical work across four experimental conditions on SmolLM-135M (frozen base, frozen-symmetric loss, unfrozen top-3 control, unfrozen top-3 with drift loss) shows this hypothesis is false. The model's bulk residual stream is **coherence-invariant** in its layer-wise geometry: false statements traverse the network as smoothly as true ones. Forcing drift discrimination via explicit loss pressure either fails (drift remains flat) or actively damages the factual signal that exists at the layer level.

Pandey (2026) provides the mechanistic resolution. Falsity detection in pretrained transformers is real and consistent across twelve open-weight models, but it lives in a **sparse, directional, head-level** substrate (≈0.4–1.0% of attention heads, writing into specific directions in residual space, concentrated near 0.85·L depth) — not in the bulk geometry that drift measures. The MOPS architecture was looking in the wrong place with the wrong observable.

This is a clean negative result with productive forward implications: the substrate exists and is monitorable; the path is via direct directional probing (Marks–Tegmark / Pandey style), not via cross-layer geometric reconstruction.

---

## The Hypothesis Under Test

The MOPS (Maximum Occupancy Principle Sheaf) Transformer architecture proposed treating each transformer layer as a site of local sections in a sheaf over depth. Per-layer projections π_L: ℝ^D → ℝ^S extract a section at each layer. Learned restriction maps r_L: ℝ^S → ℝ^S predict how a section *should* propagate to the next layer if coherence is preserved. The discrepancy

```
δ_L = π_{L+1}(h_{L+1}) − r_L(π_L(h_L))
D_L = ||δ_L||
```

is the **drift signal** — a per-layer scalar measuring how much the actual next-layer section diverges from what the restriction map predicts.

The empirical bet was that coherent input would produce small drift (sections glue cleanly) and incoherent input would produce large drift (gluing fails). A coherence-mask-weighted training loop would teach the system to use this signal.

The architectural framing rests on a deep claim from [[hidden-states|hidden-state]] interpretability: the residual stream is the model's "thinking surface", and incoherent thinking should be visible as geometric irregularity on that surface.

---

## Experimental Matrix

Phase 1 used SmolLM-135M (576-dim hidden states, 30 layers) with a TruthfulQA-only training set (~3,300 paired correct/incorrect factual statements). Validation used a balanced 500-pair held-out set. Statistical thresholds matched the architecture specification: Mann-Whitney U p < 0.01, Cohen's d > 0.5 on drift; coherence AUC > 0.7 with bootstrap 95% CI lower bound > 0.7.

| Configuration                          | Coherence AUC | Drift Difference | Drift Cohen's d | p-value | Verdict |
|----------------------------------------|---------------|------------------|------------------|---------|---------|
| Random initialization                  | 0.49          | 0.00             | 0.00             | —       | Baseline |
| Linear probe on h_N (no MOPS)          | **0.674**     | N/A              | N/A              | —       | Ceiling reference |
| Frozen base + symmetric drift loss     | 0.629         | −0.005           | 0.07             | 0.49    | Drift fails |
| Unfrozen top-3 (control, no drift loss) | **0.676**     | −0.021           | −0.29            | 1.00    | Drift fails by default |
| Unfrozen top-3 + drift loss (target)   | 0.608 (down)  | −0.019           | −0.08            | 0.85    | **Both fail** |

The matrix forecloses each plausible variant in turn. Frozen residual streams cannot be made drift-discriminable. Unfrozen top layers can closely match the linear-probe baseline on coherence detection *without engaging drift at all*. When drift pressure is added, the model finds a representation that satisfies the drift penalty by *destroying* the coherence signal it had previously achieved.

---

## Two Failure Modes

### The Frozen Ceiling (Phase 1)

A pretrained transformer's residual stream evolves through a learned, smooth trajectory regardless of input truthfulness. Sheaf projections of frozen hidden states cannot manufacture inconsistency that isn't in the substrate; with restriction maps initialized to identity and projections initialized small, the drift signal is dominated by random projection variance, not by content. Training the projections drives drift to a low fixed-point (the trivial solution), at which point both coherent and incoherent inputs produce equivalent drift.

This is the **architectural ceiling**: no amount of head training can detect a signal that isn't represented in the input features.

### The Global Smoothing Trap (Phase 1.5)

Unfreezing the top 3 layers (28–30) gave the model the capacity to *create* inconsistency. The symmetric drift loss provided pressure in both directions: penalize drift on coherent samples, reward drift above a hinge margin on incoherent samples.

Two failures co-occurred. First, the model satisfied the coherent-side penalty by applying a *global* smoothing transformation that reduced drift everywhere, including incoherent samples — coherent drift fell from baseline ~16 to ~10, but so did incoherent drift. The hinge target (margin=5) sat well below baseline drift, so the incoherent reward had zero gradient at initialization. The model optimized only the term with active gradient.

Second, the representational changes required to satisfy the drift penalty *interfered with the factual signal*. Coherence AUC dropped from 0.676 (control, no drift loss) to 0.608 (target, with drift loss). The "drift-friendly" subspace and the "factual-signal-preserving" subspace are not the same; forcing the former destroys the latter.

A contrastive (ranking) drift loss — push incoherent drift higher *than* coherent drift, regardless of absolute levels — was identified as a possible remediation but not run, because by this point the diagnostic question had shifted: even if such a loss worked, it would only mean the model could *manufacture* inconsistency under explicit pressure, not that inconsistency was naturally present in pretrained representations.

---

## Pandey's Mechanistic Resolution

The Pandey (2026) paper, which appeared during Phase 1.5 analysis, characterizes where the falsity signal actually lives in twelve open-weight models from five labs (1.5B–72B). Three findings directly explain the MOPS null:

**1. The signal is sparse, not global.** A specific small attention-head set (~0.4–1.0% of total heads) carries the "this statement is wrong" signal whether the model is being asked to evaluate a claim, being pressured to agree with one, or being instructed to lie. Edge-level path patching confirms component-level sharing on Gemma-2-2B (Pearson r=0.993, 275-edge circuit) and Phi-4 (r=0.988–0.995). Silencing these heads in Gemma-2-2B flips sycophantic agreement from 28% to 81% while factual accuracy moves only 69% → 70%. The circuit controls **deference**, not knowledge.

The MOPS sheaf averaged drift across all positions and all layers. A signal in 0.4% of components is below the noise floor of that average.

**2. The signal is directional, not magnitudinal.** Pandey extracts task directions as mean-difference vectors d_t in residual space, projected at the optimal probe layer (≈0.85·L). The discriminative content is **the cosine alignment with d_lie**, not the L2 norm of any drift quantity. Probes on the directional read-off transfer to lying at AUROC 0.83–0.85 across Gemma-2-2B, Qwen3-8B, and Mistral-7B.

The MOPS drift signal was D_L = ||δ_L|| — a scalar that collapses out directional information. Even if the layer-wise drift vector δ_L had a non-zero component along d_lie, taking its norm averaged that component against orthogonal noise and discarded the sign.

**3. The geometric trajectory is coherence-invariant in bulk.** Pandey's logit-lens scaling result on Gemma-2-2B-IT, Mistral-7B, and Llama-3.1-70B shows that mid-layer "detect-then-override" signatures shrink monotonically with scale and dissolve into distributed execution at 70B. Even at 2B–7B where the detect-then-override signature is present, it's a *directional* mid-layer peak in the probe-projected log-odds, not a *geometric* peak in residual-stream magnitudes.

The MOPS architecture conflated "internal state resolves toward correct answer before late-layer commits to wrong answer" with "residual-stream geometry exhibits cross-layer discontinuity." Those are different observables. The first is real and Pandey-confirmed. The second is the one MOPS measured, and it is empirically absent.

---

## Substrate vs Geometry: Reframing the Problem

The deepest takeaway is a category distinction that the MOPS hypothesis quietly elided:

| What MOPS measured | What actually carries the signal |
|---|---|
| Bulk residual-stream geometry across layers | Sparse attention-head outputs at specific layers |
| L2-norm drift between predicted and actual sections | Directional projection onto a learned d_lie |
| Cross-layer dynamics as the substrate | Within-layer head writes as the substrate |
| Coherence as a trajectory property | Coherence as a sparse-circuit property |

Pretrained LMs are, in a precise sense, **equally fluent at lying as at truth-telling** — their bulk representational dynamics are coherence-invariant. The falsity signal is real but lives in a thin, learnable substrate that vanilla LM training produces *automatically* (Pandey shows the substrate predates RLHF — even untuned Qwen2.5-1.5B base shows 7/15 top-K overlap at 10.5× chance, p<10⁻⁶) and that alignment training *masks but does not remove*. This is the "registered-but-overridden" finding: alignment-trained models register the user's error using the same circuit they use for any false statement, and downstream components produce agreement regardless.

The architectural implication for any in-forward-pass coherence monitor: **measure the substrate directly**, do not try to reconstruct it from bulk geometry. A single mean-difference probe at one layer achieves AUROC 0.83–0.85 on Pandey's panel; the MOPS apparatus with its 30 sheaf projections, 29 restriction maps, anti-collapse term, symmetric drift loss, and multi-loss training stayed at 0.61 with drift flat.

---

## Connection to the Broader Research Program

This falsification is not a setback to [[conscience-servitor]] or to the broader [[efhf]] architecture. It is a clarification of *where in the model the signal that conscience-servitor needs to detect actually lives*. Three implications:

**For conscience-servitor.** A new monitoring channel is now justified and specified: a **Falsity Substrate Monitor (FSM)** that operates as a forward-pass hook on a target model, projecting last-token residual activations onto a pre-trained d_lie direction. This complements the existing LLM2Vec-Gen output-stage triage. Spec: `conscience-servitor/docs/falsity_substrate_monitor_spec.md`. The MOPS work, though falsified as an architecture paper, *delivered* the empirical case for why this simpler monitor is warranted.

**For EFHF and the lumpability framing.** The MOPS hypothesis was a candidate operationalization of EFHF's Layer 0 — using cross-layer dynamics to detect lumpability failure. The falsification narrows the operationalization: lumpability failure in pretrained LMs is not visible in bulk geometry; it is visible in sparse directional substrate. EFHF's theoretical claim (prosocial clustering can be selectively reinforced while suppressing co-activated drift) is unaffected; only the architectural implementation candidate changes.

**For [[maximum-occupancy-principle|MOP-guided decoding]].** The MOPS architecture had two largely independent halves: the sheaf-cohomological drift detector (falsified) and MOP-style decoding (untested). MOP decoding scores candidate tokens by a combination of entropy preservation, conceptual novelty, and drift penalty. The drift penalty can be sourced from any reliable falsity signal — probe-derived, head-derived, or otherwise. MOP decoding as a hallucination-reduction mechanism is **architecturally independent** of how the drift signal is computed and remains a testable hypothesis. The probe-anchored variant (Pandey d_lie projection as drift signal, then MOP scoring on top) is the natural minimum-pivot experiment.

---

## What Generalizes Beyond MOPS

The pattern this falsification surfaces is more general than the specific architecture:

> **When the empirical literature characterizes a signal as sparse, directional, and circuit-level, architectural mechanisms that average over bulk geometry will fail to detect it, even if those mechanisms are mathematically sophisticated and empirically motivated by analogy to the original observation.**

This applies beyond hallucination detection. Any phenomenon that mechanistic interpretability has localized to specific circuits or directions — refusal (Arditi et al. 2024, single direction), sycophancy (Pandey 2026, shared with lying), in-context learning (induction heads), and so on — will be detectable by direct probing of the relevant substrate and **invisible to global geometric measures** that don't preserve the structure of where the signal lives. A geometric-drift method is the wrong tool by construction; the right tool is whatever the interpretability work has identified as the substrate.

The MOPS work falsified one specific instance of "global geometric measure" applied to one specific phenomenon. The pattern is worth flagging in advance for adjacent projects.

---

## Open Questions

1. Does **directional drift** (the *vector* δ_L projected onto a learned axis, rather than its scalar norm) carry signal that scalar drift discarded? The Phase 1.5 results suggest yes in principle, but the global-smoothing dynamics may persist. Not run; not in current Phase 1.5 scope.
2. Does **head-level sheaf consistency** — applying drift-like checks to individual attention-head outputs rather than layer-wise residuals — preserve the MOPS framing while aligning with Pandey's substrate? Possible but compute-expensive; deferred to Phase 4+ ablation.
3. Does **MOP-guided decoding** reduce hallucination at matched perplexity when the drift signal is provided by a Pandey-style probe rather than the MOPS sheaf? Architecturally independent and currently the highest-value untested component of the original spec.
4. Does the **conscience-servitor FSM**, once built, exceed output-stage triage on cases where the model "knows" the user is wrong but agrees anyway? This is the canonical Pandey case; a positive result would directly validate Option D (conscience-servitor redirection) as the right pivot.

---

## Caveats

- The falsification holds for **pretrained transformers with frozen and top-3-unfrozen configurations on SmolLM-135M scale**. It does *not* rule out the MOPS mechanism for from-scratch training where the drift signal is in the loop from initialization. That experiment was deemed out of scope after the Pandey paper appeared, on the grounds that Pandey's results characterize the actual substrate, but is logically open.
- The validation used TruthfulQA-only data; cross-dataset replication (NaturalQuestions, FEVER) was not run. Pandey reports ρ≈0.99 on TQA↔NQ for Gemma-2-2B and Llama-3.3-70B, so the substrate appears dataset-general at his scale.
- Statistical power: the n=500 balanced validation set bounds AUROC CI at roughly ±0.05. Sub-threshold movements within that band are not interpretable as meaningful effects.
- The negative result is **publishable in its current form** as a short paper or workshop note, framing the architectural falsification as a contribution to mechanistic-interpretability adjacent architecture research. The Pandey paper as a citation makes the mechanistic explanation clean.

---

## Connections

- [[conscience-servitor]] — the deployment vehicle for the substrate monitor that this falsification motivates
- [[efhf]] — the theoretical framework in which MOPS was proposed as one possible Layer 0 implementation
- [[maximum-occupancy-principle]] — the MOP-decoding half of the original architecture; architecturally independent of the falsified sheaf half
- [[hidden-states]] — the broader interpretability tradition this work sits within
- [[sheaf-consistency-enforcer]] — the dual project doing ADMM-based gluing enforcement (smoothing), as opposed to obstruction detection (this falsified project)
- [[toward-transcendent-moral-instrumentality]] — Paraclete Protocol's constitutive-vs-regulatory constraint distinction (substrate monitoring is constitutive; output-stage triage is regulatory)

## References

- Pandey, M. (2026). *LLMs Know They're Wrong and Agree Anyway: The Shared Sycophancy-Lying Circuit.* arXiv:2604.19117v4.
- Marks, S. & Tegmark, M. (2024). *The Geometry of Truth: Emergent Linear Structure in Large Language Model Representations of True/False Datasets.* COLM 2024.
- Arditi, A. et al. (2024). *Refusal in Language Models Is Mediated by a Single Direction.* NeurIPS 2024.
- Halawi, D., Denain, J.-S. & Steinhardt, J. (2024). *Overthinking the Truth: Understanding How Language Models Process False Demonstrations.* ICLR 2024.
- Wang, K. R. et al. (2023). *Interpretability in the Wild: A Circuit for Indirect Object Identification in GPT-2 Small.* ICLR 2023.
- Source repo: `/home/ty/Repositories/ai_workspace/mops-transformer`. Phase 1/1.5 findings: `docs/phase1_findings.md`. Pivot decision: `docs/pivot_decision.md`.
