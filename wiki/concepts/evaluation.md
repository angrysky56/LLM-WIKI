---
created: 2026-05-29
updated: 2026-06-08
type: concept
summary: Evaluation methodology and benchmarks for measuring LLM capabilities — MMLU, GSM8K, HumanEval, SWE-Bench; evaluation properties and limitations
tags: [llm, evaluation, benchmarking, measurement]
sources: 
status: active
confidence: 0.8
---

# Evaluation

Evaluation is the systematic measurement of LLM capabilities against standardized benchmarks. The field has matured rapidly as model capabilities have outpaced informal assessment methods.

## Benchmark Taxonomy

### Knowledge / Reasoning Benchmarks

| Benchmark | Domain | What It Measures |
|-----------|--------|-----------------|
| **MMLU** | 57 subjects | Broad knowledge across domains |
| **GSM8K** | Grade school math | Multi-step mathematical reasoning |
| **MATH** | Competition math | Harder problem solving |
| **HellaSwag** | Commonsense | Sentence completion |

### Coding Benchmarks

| Benchmark | What It Measures |
|-----------|-----------------|
| **HumanEval** | Python code from docstrings |
| **MBPP** | Basic Python problems |
| **SWE-Bench** | Real GitHub issues (full repositories) |

### Reasoning Process Benchmarks

| Benchmark | What It Measures |
|-----------|-----------------|
| **PRM800K** | Step-level math reasoning (process reward) |
| **BigBench-Hard** | Tasks that challenge current models |

## Properties of Good Benchmarks

**Ground truth**: Definitive correct answers or reference behaviors. If ground truth is ambiguous, benchmark reliability suffers.

**Coverage**: How well the benchmark spans the capability space. Low coverage means models can score well without general capability.

**Anti-gaming**: Resistance to benchmark-specific optimization. The benchmark must test genuine capability, not pattern matching to the test set.

**Composition**: Whether benchmark performance correlates with real-world task performance. This is the fundamental challenge — many benchmarks are poor proxies for actual usefulness.

## The Benchmark Gaming Problem

As models are optimized for benchmarks, two failure modes emerge:

1. **Data contamination**: Training data includes benchmark inputs; the model has "seen" the answers. This inflates scores without improving capability.

2. **Spec gaming**: The model learns to produce benchmark-passing outputs without genuinely solving the underlying task — a form of [[institutional-capture]] at the evaluation level.

This connects directly to [[reward-hacking]]: optimizing for a proxy metric without the metric capturing the actual objective.

## Evaluation Methodology

### In-Context Evaluation
The model receives examples in context (few-shot) and is evaluated on held-out test cases. ICL (in-context learning) enables rapid evaluation without fine-tuning.

### Fine-tuned Evaluation
The model is fine-tuned on benchmark data and evaluated on held-out test cases. More accurate for capabilities that require training, but risks contamination.

### Process vs Outcome Evaluation
- **Outcome evaluation**: Did the model produce the right answer? (Right/wrong binary)
- **Process evaluation**: Did the model use the right reasoning steps? (Step-level scoring via [[process-reward-model]])

Process evaluation is harder but more robust to spec gaming — a model can get the right answer via wrong reasoning.

## Open Questions

- **Contamination detection**: How do we reliably detect whether a model has seen benchmark data in training?
- **Generalization vs benchmark performance**: Does high benchmark performance predict real-world capability? (Often no for frontier models)
- **Continuous evaluation**: How do we evaluate capability growth continuously rather than on static benchmarks?

## Connections
- [[log]]
- [[concepts/swe-bench]]
- [[concepts/domain-onboarding-standards]]
- [[concepts/chain-of-thought]]
- [[concepts/scaling-laws]]
- [[concepts/reward-hacking]]
- [[concepts/evaluation]]
- [[concepts/process-reward-model]]
- [[wiki/index]]
- [[concepts/benchmarking]]
- [[concepts/benchmark]]
- [[concepts/institutional-capture]]
- [[concepts/evaluation]]

- [[benchmark]] — the general concept of standardized evaluation frameworks
- [[scaling-laws]] — the relationship between model scale and benchmark performance
- [[chain-of-thought]] — reasoning traces as the substrate for evaluation
- [[process-reward-model]] — process-level evaluation for reasoning
- [[reward-hacking]] — evaluation gaming as a form of reward hacking
- [[institutional-capture]] — benchmark gaming as institutional-level surrogation
- [[swe-bench]] — the software engineering benchmark
- Concept: [[benchmarking]]
