---
created: 2026-06-03T00:00:00Z
updated: 2026-06-03T00:00:00Z
type: source
summary: "Faithful Calibration in LRMs (Gani et al., Yale) — first framework to systematically quantify whether large reasoning models *linguistically express* their intrinsic confidence. Three complementary confidence estimators (RCC hidden-state probe, DeepConf log-prob, sampling consistency). LRMs are systematically unfaithful; reasoning training doesn't fix it; prompt interventions from non-reasoning LLMs do not transfer."
tags: [arxiv-2026, calibration, faithfulness, large-reasoning-models, uncertainty-quantification, agent-trust, LRM, paper-2606-03969]
sources: https://arxiv.org/abs/2606.03969
status: active
confidence: 0.92
---

# Quantifying Faithful Confidence Expression in Large Reasoning Models (Gani et al., Yale, 2026)

**arXiv:** 2606.03969
**Authors:** Areeb Gani, Asal Meskin, Gabrielle Kaili-May Liu, Arman Cohan (Yale University)
**Date:** 2026-06-02

## The Problem

Reasoning models (LRMs — DeepSeek-R1, o-series, Qwen3-thinking, etc.) are routinely interpreted by users as showing *deliberation* and *competence* through their long chain-of-thought traces. Users form a confidence impression from the surface of the trace.

**Faithful calibration (FC)** — the alignment between a model's *intrinsic* confidence (what it actually computes) and its *linguistic* confidence (what it says) — is therefore a critical alignment property for LRMs in deployment.

Yet the prevailing paradigm for measuring FC — sampling-consistency on response-level outputs — does not generalise to long CoT traces. Reasoning outputs:
- Lack clear step boundaries
- Exhibit inconsistent step structure across samplings
- Contain steps of unequal semantic importance
- Encode conditional dependencies whose effect on confidence evolves through the trace

## The Framework

### Three Complementary Confidence Estimators (the C side of FC)

The paper introduces a framework that triangulates intrinsic confidence C(sᵢ) at the *step level* via three independent estimators:

| Estimator | Access | What It Captures |
|---|---|---|
| **RCC (Representation-based Confidence)** | White-box hidden states | What the model's hidden states encode about a step's confidence, with a recurrent confidence state carrying history |
| **DeepConf (Token Log-Probability)** | White-box log-probs | Per-token distributional peakedness aggregated over the step span, then clamped to [0,1] |
| **Sampling Consistency (prefix-conditioned)** | Black-box outputs | Fraction of `k=10` prefix-conditioned continuations judged consistent with the original step sᵢ |

The sampling-consistency estimator is *new* — it conditions on the original prompt and prior steps, then samples `k=10` continuations of up to 200 tokens. This is **prefix-conditioned resampling** that controls for conditional dependencies and step-structure variation across traces.

### Linguistic Decisiveness Estimator (the D side of FC)

A judge model (Gemini-2.5-Flash) is prompted with few-shot examples mapping hedging language to numerical scores in [0,1]. The paper validates judge–human agreement (Pearson 0.884, Spearman 0.869 on short-form).

### Faithfulness Metric: cMFG*

```
FC(T) = 1 − (1/|I(T)|) Σ_{i∈I(T)} |D(sᵢ) − C(sᵢ)| ∈ [0, 1]
```

For dataset-level summarisation the paper introduces **cMFG\*** — a width-weighted variant of Yona et al.'s cMFG. Standard cMFG uses fixed equal-width bins; for LRMs trace-level confidence occupies a narrow empirical range, so many bins are empty. **cMFG\*** uses *equal-mass bins* over the model's actual confidence range, with width weighting to preserve averaging over the confidence axis.

## The Empirical Setup

- **7 models** spanning parameter scales and training procedures (DeepSeek-R1-8B, GPT-OSS-20B/120B, Qwen3-8B-thinking, etc.)
- **5 datasets** covering mathematical, scientific, legal, and multi-step soft reasoning: AIME, HLE, SuperGPQA, LegalBench, MuSR
- **Three research questions:**
  - (RQ1) When and to what extent do LRMs faithfully express intrinsic confidence?
  - (RQ2) How do model size, capabilities, and post-training shape FC?
  - (RQ3) Do prompt-based FC methods transfer from non-reasoning to reasoning LLMs?

## Headline Findings

### RQ1 — LRMs are systematically unfaithful

- Across all 7 models and all 5 datasets, the **decisiveness–confidence gap is large and systematic**
- Different intrinsic-confidence estimators **disagree substantially on identical traces** — conclusions from any single estimator should be treated with caution
- The decisiveness–confidence gap is *not* the same as factual miscalibration (accuracy vs. confidence); it's a *linguistic* misalignment

### RQ2 — Reasoning training does not improve FC

- **Reasoning training on its own does not improve faithful calibration** relative to non-reasoning counterparts
- **Distillation differentially reshapes FC vs reasoning training** — by modulating internal confidence but not necessarily decisiveness
- Larger models do not necessarily exhibit better FC

### RQ3 — Prompt interventions from non-reasoning LLMs do not transfer

- Prompt-based interventions that *boost* FC in non-reasoning LLMs (perception prompts, metacognitive system prompts like MetSens+Hedge) **largely fail to generalise to LRMs**
- The complexity of reasoning tasks and structured task formats makes prompt intervention insufficient

## Why It Matters

The paper establishes **faithful calibration as a necessary and under-examined alignment problem for LRMs**. The implications:

1. **For users:** "If the model says it is 80% sure" is not a meaningful signal in LRM traces — the model may be 95% sure and express 60% decisiveness, or 30% sure and express 90% decisiveness, in either direction.
2. **For evaluators:** Outcome-only scoring (used by HLL, MATCHA, FinHarness, SoundnessBench in prior cycles) misses the FC gap. The field needs *trace-conditional* scoring on top of outcome scoring.
3. **For alignment research:** Reasoning training and prompt engineering are not enough. FC may require *training-time* intervention on the decisiveness head, or *post-hoc* projection of intrinsic confidence into the language space.
4. **For agent deployment:** An agent that over-asserts its uncertainty is unsafe; an agent that under-asserts is also unsafe (users trust false confident reports). The FC gap is a deployment-readiness barrier for any LRM that has to communicate uncertainty to humans or other agents.

## Methodological Contribution to Wiki Threads

The paper's **prefix-conditioned sampling** for confidence estimation is a method upgrade that should propagate through the evaluation infrastructure thread (MATCHA, FinHarness, SoundnessBench from prior cycles). The three-estimator triangulation pattern is a template for any future "intrinsic-X vs expressed-X" measurement.

The **cMFG\*** metric is the right answer to the fixed-bin-emptiness problem that would otherwise break FC evaluation in low-confidence regimes — a small methodological fix that should become standard.

## Limitations

- Judge model is Gemini-2.5-Flash; switching judges may shift decisiveness scores
- The 3-estimator triangulation is necessary but not sufficient — no ground truth for *correct* decisiveness
- Sampling budget (k=10, 200-token continuations, max 20 steps per trace) is a practical compromise; full coverage would be ideal
- The paper does not propose a *fix* — only a measurement framework

## Connections to Wiki

### Wiki concepts
- [[calibration]] — directly extends with reasoning-trace-aware measurement
- [[faithfulness]] — extends CoT faithfulness to *confidence-expression* faithfulness
- [[uncertainty-quantification]] — adds the *linguistic* dimension to UQ
- [[agent-trust]] — the FC gap is exactly the trust violation that prevents LRMs from being deployed in workflows that depend on self-reported uncertainty
- [[bounded-representation-capacity]] — the FC gap is a *bounded self-model* problem: the model has a limited capacity to *represent its own confidence accurately*, and decisiveness is the misaligned projection
- [[verifier-graphs]] — the prefix-conditioned sampling estimator is a verifier graph realised as a conditional-resampling protocol
- [[meta-cognitive-agents]] — the entire framework is the first systematic measurement of *meta-cognition* in LRMs
- [[parallel-reasoning]] — sampling-consistency for confidence is structurally similar to parallel-decoding for verification
- [[oMCD]] — the multi-estimator triangulation is an oMCD-style disagreement diagnosis

### Related papers (wiki)
- [[finharness-2026]] — FinHarness evaluated outcome; this paper extends the score to FC. Together they form a two-axis evaluation: outcome × faithfulness
- [[matcha-2026]] — MATCHA's process-validated scoring is *adjacent* to FC. Where MATCHA asks "is the action sequence right?", this paper asks "is the expressed confidence faithful?"
- [[soundnessbench-ai-scientist-2026]] — SoundnessBench's process validation gains a calibration dimension here
- [[hll-humanitys-last-line-verification-2026]] — HLL's trace-conditioned validation is a *case* of the broader FC problem: did the agent *actually* arrive at the answer through a valid trace, or just write down the right number? This paper generalises the question to *confidence*
- [[autosci-memory-centric-research-lifecycle-2026]] — AutoSci's lifecycle is about *what* the agent records; FC is about *how confidently* it reports what it records
- [[stateful-monitoring-distributed-agent-attacks-2026]] — monitoring needs the agent's self-reported confidence to be reliable; FC is a prerequisite for trustworthy self-monitoring
- [[monitoring-agentic-systems-reliability-2026]] — same direction: monitoring agents requires faithful self-reports
- [[boiling-frog-agentic-safety-2026]] — boiling-the-frog attacks exploit the decisiveness-confidence gap; a model that confidently reports its low confidence is *more* exploitable
- [[skillopt-self-evolving-2026]] — SkillOpt optimises skill content; FC says the model's *expression of what it learned* may not reflect what it learned. Skills evolved via self-evaluation inherit this gap

### Thread Cross-Cuts
This is a direct contribution to the **deployment-readiness thread** (capability-vs-deployment gap, from 2026-06-02 cycle): LRMs are *capable* of correct answers but *unfaithful* in expressing their confidence. Both gaps share the same root: **bounded self-model**. The model cannot accurately represent its own knowledge state, and that limit manifests as either outcome failure (capability) or expression failure (faithfulness).

## Key Quote

> "Despite the importance of FC and wide usage of LRMs, the extent to which LRMs can faithfully express their confidence remains poorly understood. ... Results demonstrate that current LRMs systematically struggle to faithfully express their intrinsic uncertainty in words, and that reasoning training on its own does not improve this alignment relative to non-reasoning counterparts. Prompt-level interventions that boost faithful calibration of LLMs largely fail to generalize to LRMs."

## What To Watch
## What To Watch
- **Faithful-calibration as a training objective** — adding a "decisiveness-alignment" loss term during reasoning training is the natural next step
- **Confidence-decisiveness projection layers** — explicit architectural components that project internal confidence to surface decisiveness
- **FC for agents that communicate with other agents** — multi-agent LRM systems will be especially vulnerable to FC gaps, since one agent's unfaithful confidence becomes another agent's input
- **Calibration-vs-faithfulness disambiguation** — future work should clearly separate "the model's *expected* confidence matches its *empirical* accuracy" (classical calibration) from "the model's *expressed* confidence matches its *intrinsic* confidence" (faithfulness). This paper is squarely in the second camp.

### Cross-cycle (2026-06-04 batch)
- **FC ↔ [[arxiv-2605-30335-locally-coherent-globally-incoherent]]:** This paper's "what the model says vs what the model knows" gap is the *intra-model* version of Kotawala's "what component A says vs what the system jointly knows" gap. FC is a single-model faithfulness failure; Kotawala's ε★ is a multi-model compositional failure. Same root cause (bounded self-model), different scope.
- **FC ↔ [[arxiv-2605-30348-llmsurgeon-data-mixture-surgery]]:** FC's prefix-conditioned-sampling estimator and LLMSurgeon's calibrated-confusion-matrix inverse problem are both *post-hoc* recoveries of latent properties from observable behaviour. FC recovers the model's intrinsic confidence; LLMSurgeon recovers the pretraining data mixture. Both turn "the model can't introspect this" into a solvable inference problem.
- **FC ↔ [[arxiv-2605-30343-reasoning-in-memory-rim]]:** RiM is a method that *uses* the residual stream for computation rather than communicating it externally. FC shows the *expressed* confidence is unfaithful. Combining the two: a latent-reasoning model that uses RiM-style memory blocks *cannot* express faithful per-step confidence, because the intermediate steps are invisible. The FC problem is *worse* for latent-reasoning systems.
