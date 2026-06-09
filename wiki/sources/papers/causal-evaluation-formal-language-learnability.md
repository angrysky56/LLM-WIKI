---
summary: Causal evaluation framework using formal languages + binning semiring to separate correlation from causation in LM learnability analysis
tags: [arxiv, paper, causal-inference, formal-languages, learnability, language-models, evaluation]
updated: 2026-06-09T08:46:16Z
created: 2026-06-09T08:46:16Z
---

# Causally Evaluating the Learnability of Formal Language Tasks

> **Causally Evaluating the Learnability of Formal Language Tasks** — Snæbjarnarson, Svete, Valvoda, Boumasmoud, DuSell, Cotterell (ETH Zürich / University of Copenhagen), June 2026. arXiv: 2606.09822

## Problem

Language models, as multi-task learners, acquire a wide range of abilities during training. A fundamental question is: **how much task-specific data is needed to learn a given task?** Answering this in natural language is difficult because tasks are hard to delineate and can confound one another. A model that appears to have learned syntax may actually be exploiting correlations with lexical patterns; a model that fails at a task may simply have been exposed to insufficient relevant examples, not because the architecture cannot learn the underlying rule.

Standard evaluation methodology uses **correlational analysis** — measuring task performance as a function of data exposure — but this approach is inherently flawed when tasks share structure. Inter-task confounders mean that an apparent correlation between data frequency and performance may be driven by third factors (similarity to other tasks, shared vocabulary, syntactic overlap).

## Method

The paper introduces a controlled experimental framework using **formal languages induced from probabilistic finite automata (PFAs)** as a testbed:

1. **Binning semiring**: An algebraic object that controls how often a targeted property (a specific state, transition, or symbol pattern) occurs in a sampled corpus. This allows precise intervention on data frequency without changing other properties of the distribution — something impossible in natural language.

2. **Causal graphical model**: The experimental pipeline is formulated as a structural causal model with explicit confounders, enabling proper do-operator-style interventions that distinguish correlation from causation.

3. **Decomposed KL divergence metrics**: Novel evaluation metrics that measure learnability of specific sub-tasks (individual states, transitions, or symbols) rather than aggregate perplexity, enabling fine-grained causal attribution.

The controlled setting uses PFAs where each state, transition, and symbol constitutes a "task" — and these tasks are interrelated through the automaton's structure, reproducing the confounder problem of natural language in a tractable environment.

## Results

- **Correlational analysis leads to incorrect conclusions**: Standard evaluation without causal intervention systematically misattributes learnability — tasks that appear "easy" under correlational metrics turn out to be confounded, and tasks that appear "hard" may be conflated with other factors
- **Causal effect of data frequency**: When properly isolated using the binning semiring, the true causal effect of data frequency on learnability is often weaker than the correlational estimate suggests
- **Confounder structure matters**: The specific structure of inter-task confounders (e.g., shared transitions between automaton states) determines the direction and magnitude of bias in correlational analyses
- **Warning for NLP**: The results serve as a cautionary demonstration about correlational pitfalls in natural-language settings, where confounders are even more numerous and harder to control

## Limitations

- Formal languages are a simplified proxy — findings may not directly transfer to natural language with its amorphous task boundaries
- The binning semiring approach works for PFAs but has no natural analog for natural language corpora
- Only transformer-based language models were evaluated; other architectures (state-space models, RNNs) may behave differently
- The study focuses on token-level learnability; higher-level linguistic phenomena (pragmatics, discourse) are not modeled

## Connections

- Extends the causal evaluation framework from [[causal-inference-in-nlp|Causal Inference in NLP]] (Feder et al., 2022; Valvoda et al., 2022)
- Connects formal language learnability ([[blanks-pfa|Blank's PFA methodology]]) to causal identification — bridging two research communities
- Related to [[task-confounds|task confounds]] literature showing multi-task learning evaluation is unreliable without causal controls
- Complements [[evaluation-cards|Evaluation Cards]] from the same arXiv feed — both address methodological rigor in AI evaluation, from different angles (causal vs. reporting infrastructure)
- The binning semiring is an original algebraic contribution with potential applications in controlled text generation and fairness auditing

## Key Quote

> "Standard correlational methodology can spoil conclusions about formal language learnability. ... Our experiments show that evaluating learnability without causal intervention leads to incorrect conclusions due to confounders in correlational analysis, and serve as a warning about correlational pitfalls in natural-language settings."

## Links

- arXiv: [2606.09822](https://arxiv.org/abs/2606.09822)
- Code: [github.com/vesteinn/causal-eval-formal-languages](https://github.com/vesteinn/causal-eval-formal-languages)
