---
created: 2026-05-29
updated: 2026-06-08
type: concept
summary: Benchmark — standardized evaluation framework for measuring AI capability; properties, well-known benchmarks (MMLU, GSM8K, HumanEval, SWE-Bench), and key limitations
tags: [evaluation, benchmarking, measurement]
sources: 
status: active
confidence: 0.8
---

# Benchmark

A benchmark is a standardized evaluation framework that allows consistent measurement of AI capabilities across different systems. The core idea: define a fixed test set with known correct answers, evaluate any system against it, and compare results.

## Properties of Good Benchmarks

A benchmark's quality depends on:

| Property | Description | Why It Matters |
|----------|-------------|----------------|
| **Ground truth** | Definitive correct answers or reference behaviors | If ground truth is ambiguous, scores are unreliable |
| **Metric** | Quantitative measure of performance | Must be objective, reproducible |
| **Baseline** | Reference performance to compare against | Without baselines, scores are uninterpretable |
| **Coverage** | How well the benchmark spans the capability space | Low coverage → scores don't predict real capability |
| **Anti-gaming** | Resistance to benchmark-specific optimization | Without this, scores inflate without genuine capability |

## Well-Known AI Benchmarks

### Knowledge and Reasoning

**MMLU** (Massive Multitask Language Understanding): 57 subjects, 15,908 questions. Tests broad knowledge from law to medicine to history. The standard measure of general knowledge.

**GSM8K** (Grade School Math 8K): 8,500 grade school math problems requiring multi-step reasoning. Tests numerical reasoning; scores range from ~20% (small models) to ~95%+ (frontier models).

**MATH**: Competition math problems (AMC, AIME level). Harder than GSM8K; scores typically 30-50% for frontier models.

### Coding

**HumanEval**: 164 Python problems from OpenAI. Each problem provides a function signature + docstring; model writes the implementation. Tests functional correctness.

**SWE-Bench**: Real GitHub issues from popular repositories. Model must produce a patch that resolves the issue and passes the test suite. Much harder than HumanEval — requires navigating complex codebases.

### Emerging Categories

**BIG-Bench Hard**: Tasks where PaLM 2B < human raters. Specifically designed to challenge current models.

**Agent benchmarks**: InterCode, WebArena, GAIA — tests of multi-step task completion requiring tool use, navigation, and planning.

## The Benchmark Gaming Problem

Benchmarks face a fundamental failure mode as they become the target of optimization:

1. **Contamination**: Training data includes benchmark inputs → inflated scores without genuine capability
2. **Spec gaming**: Models learn to produce benchmark-passing outputs without solving the underlying task

This is [[institutional-capture]] at the evaluation level: optimizing for a proxy (benchmark score) without the proxy capturing the actual objective (general capability).

The [[reward-hacking]] connection is direct: the reward function (benchmark score) becomes disconnected from the true objective (useful AI).

## Benchmark Evaluation Methodology

### In-Context (Few-Shot)
Model receives examples in context, then evaluated on held-out test cases. No fine-tuning required; fast evaluation cycle.

### Fine-tuned
Model fine-tuned on benchmark training split, evaluated on held-out test. More accurate for capabilities requiring training, but contamination risk is high.

### Process vs Outcome
- **Outcome evaluation**: Correct/incorrect binary
- **Process evaluation**: Step-level scoring (as in [[process-reward-model]]) — did the model use correct reasoning?

Process evaluation is more robust to spec gaming: wrong reasoning that happens to produce right answers is detectable.

## Connections

- [[evaluation]] — the broader practice of systematic capability measurement
- [[swe-bench]] — software engineering benchmark
- [[chain-of-thought]] — reasoning traces as evaluation substrate
- [[process-reward-model]] — process-level evaluation for reasoning
- [[reward-hacking]] — benchmark gaming as reward hacking
- [[institutional-capture]] — benchmark gaming as institutional surrogation
- [[scaling-laws]] — relationship between model scale and benchmark performance
- Concept: [[code-agent]]
- Concept: [[code-generation]]
