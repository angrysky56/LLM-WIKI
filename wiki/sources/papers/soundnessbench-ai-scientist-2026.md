---
summary: Benchmark for AI scientist first-gate evaluation; LLMs show pervasive optimism bias on scientific soundness, not reliable as standalone proposal evaluators
tags: [evaluation, benchmark, AI-scientist, soundness, research-triage]
updated: 2026-05-29T14:13:01Z
created: 2026-05-29T14:13:01Z
---

# SoundnessBench: Can Your AI Scientist Really Tell Good Research Ideas from Bad Ones?

## Metadata

| Field | Value |
|-------|-------|
| arXiv ID | 2605.30329 |
| Published | 2026-05-28 |
| Authors | Sy-Tuyen Ho, Minghui Liu, Huy Nghiem, Furong Huang (University of Maryland) |
| Categories | cs.LG |
| PDF | /home/ty/Documents/paper-research/2605.30329v1.pdf |
| Wiki path | wiki/sources/papers/soundnessbench-ai-scientist-2026.md |

## Summary

SoundnessBench evaluates whether LLMs can judge the methodological viability of machine learning research proposals before execution. Using 1,099 reconstructed ICLR submissions labeled with soundness sub-scores, the benchmark tests a critical bottleneck in autonomous research agents: the "first-gate" judgment of whether a proposed experimental design can rigorously test its hypothesis. Across 12 frontier LLMs, results show pervasive optimism bias — models frequently rate low-soundness proposals as sound.

## Key Findings

1. **Pervasive optimism bias**: Under standard prompting, models rate low-soundness proposals as sound; aggressive prompting shifts errors from false positives to false negatives
2. **Not explained by single confounder**: Controls for public-corpus contamination, paper-identifying phrases, surface features, and human audit quality all fail to fully explain the behavior
3. **First benchmark to test pre-execution methodological soundness judgment**: Prior benchmarks (SWE-Bench, MLE-Bench, PaperBench) all evaluate execution outcomes, not upfront proposal viability
4. **Current LLMs are not reliable as standalone first-gate evaluators** for scientific rigor

## Benchmark Design

| Property | Value |
|----------|-------|
| Size | 1,099 ML research proposals |
| Source | ICLR submissions with reviewer soundness sub-scores |
| Ground truth | Expert labels (audited against source papers) |
| Evaluation stage | Pre-execution (proposal-only input) |
| Scope | Proposal-stage methodological integrity in ML research |

## What "Soundness" Means Here

Scoped deliberately to proposal-stage methodological integrity — whether the experimental design can rigorously test the hypothesis — not eventual impact, novelty, or acceptance. The goal is testing whether an agent can identify visible fatal flaws (improper baselines, data leakage, mismatched metrics) *before* execution incurs high costs.

## Why This Matters

Without robust upfront filtering, autonomous research agents risk automating the pursuit of unsound hypotheses — "scaling bad science" by making it easier to generate flawed experiments that appear structurally correct. The soundness gap is a bottleneck for AI acceleration of scientific discovery that existing benchmarks entirely miss.

## Connections

- [[ai-scientist]] — autonomous research agents
- [[research-triage]] — first-gate evaluation of research proposals
- [[evaluating-llms-harness]] — benchmark for LLM evaluation
- [[soundnessbench-ai-scientist-2026]] — self-reference
- [[autosci-memory-centric-research-lifecycle]] — AutoSci's Trust Guard (independent reviewer agent) is a constructive response to SoundnessBench's finding of pervasive optimism bias in LLM self-evaluation; the Trust Guard uses deterministic linting + independent reviewer agent for content validation
