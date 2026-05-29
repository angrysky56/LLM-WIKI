---
created: 2026-05-28
updated: 2026-06-08
type: concept
summary: SWE-Bench — benchmark for software engineering tasks from real GitHub issues; tests agent ability to resolve real-world code problems
tags: [benchmark, software-engineering, coding, evaluation]
sources: [https://arxiv.org/abs/2407.21780]
status: active
confidence: 0.8
---

# SWE-Bench

SWE-Bench (Software Engineering Benchmark) is a benchmark for evaluating AI systems on real-world software engineering tasks. Unlike HumanEval (synthesized coding problems), SWE-Bench uses actual GitHub issues from popular open-source repositories — the model must resolve real bugs or implement real features.

## Design

SWE-Bench consists of:
- **Issues** from Python repositories (Django, Flask, Matplotlib, etc.)
- **Gold patches** — the actual commits that resolved each issue
- **Test cases** — the repository's own test suite, which must pass for a solution to be considered correct

The model receives:
1. The issue description (title + body)
2. Access to the repository codebase
3. Instructions to produce a patch

A solution is scored correct if the patch applies cleanly and the repository's tests pass.

## Key Properties

**Real-world complexity**: The issues are not toy problems — they require understanding complex codebases, debugging, and implementing non-trivial changes. This is the primary advantage over HumanEval.

**Full repository context**: Unlike HumanEval (single function), SWE-Bench gives access to the entire repository. This is realistic — real software engineering requires navigating large codebases.

**Test-based evaluation**: The gold patch is the test — does the test suite pass? This avoids the problem of having to evaluate code quality manually.

## Results

Representative results from SWE-Bench papers:

| Model | Score |
|-------|-------|
| GPT-4 (baseline) | ~5% |
| Claude 3.5 Sonnet | ~4.8% (early versions) |
| SWE-agent systems | ~15-20% (specialized agents) |
| DeepSeek-Coder-V2 | ~13% |

The overall scores are low because:
- Real issues are genuinely hard
- Model context windows limit how much repository can be considered
- Some issues require multi-file changes, complex debugging

## Variants

- **SWE-Bench-Lite**: Subset of 300 issues, faster evaluation
- **SWE-Bench Verified**: Curated subset with cleaner test infrastructure
- **SWE-Bench (full)**: 12,887 issues from 69 repositories

## Code Agent Research

SWE-Bench is primarily used to evaluate code agents — systems that use LLMs for software development tasks:
- [[code-agent]] systems that browse repositories, read files, write patches
- Agent frameworks like [[hermes-agent]] for building coding agents
- The benchmark drives research on agent tool use, context management, and code modification

The connection to [[reward-hacking]] is worth noting: a code agent could learn to pass the test cases without actually fixing the issue correctly (producing a patch that makes tests pass via wrong implementation).

## Limitations

- **Python-only (mostly)**: While SWE-Bench has expanded, most issues are Python — limits generalization to other languages
- **Reproduction environment complexity**: Setting up the environment to run tests is non-trivial
- **Benchmark gaming**: Specialized agents can be overfit to the benchmark without general code agent capability
- **Scoring ambiguity**: A patch can make tests pass without actually resolving the issue (overfitting to test cases)

## Connections
- [[concepts/reward-hacking]]
- [[concepts/evaluation]]
- [[scratchpad/jobs/reports/arxiv/arxiv-2026-05-22-top-papers]]
- [[concepts/evolutionary-strategies]]
- [[concepts/agent-onboarding]]
- [[concepts/code-agent]]
- [[concepts/code-generation]]
- [[wiki/index]]
- [[concepts/benchmark]]
- [[concepts/mcts]]
- [[log]]
- [[sources/papers/deltabox-stateful-agent-checkpoint-rollback-2026]]
- [[concepts/swe-bench]]
- [[swe-bench]]

- [[benchmark]] — the general concept
- [[code-agent]] — AI agents specialized in software development
- [[evaluation]] — the broader practice of measuring capabilities
- [[reward-hacking]] — potential for gaming the test-based evaluation
- Concept: [[MCTS]]
- Concept: [[agent-onboarding]]
- Concept: [[code-generation]]
- Concept: [[evolutionary-strategies]]

- [[MCTS]]