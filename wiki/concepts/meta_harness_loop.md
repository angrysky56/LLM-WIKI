---
created: 2026-05-07T23:21:32Z
updated: 2026-05-29
type: concept
summary: The meta-harness architecture — an agent framework where the harness evaluates and directs specialized sub-agents
sources: []
status: active
confidence: 0.7
tags: [evolution, architecture, meta-harness]
---

# Meta-Harness Evolution Loop

The Evolution Loop is the core mechanism of the Meta-Harness, designed to iteratively improve agent memory systems and domain skills through autonomous experimentation.

/home/ty/Repositories/ai_workspace/meta-harness/README.md

## Architecture

```mermaid
graph TD
    A[Start Iteration] --> B[Generate Candidate]
    B --> C[Validate Code]
    C -- Success --> D[Benchmark Candidate]
    C -- Failure --> B
    D --> E[Record Results]
    E --> F[Select Best Candidate]
    F --> G[Update Frontier]
    G --> H[End Iteration]
```

## Subsystems

### 1. Evolution Engine (`src/meta_harness/engine.py`)

The engine manages the state of the evolution process, including the "frontier" (the best-performing system found so far). It constructs the prompts for the "Proposer" (the LLM responsible for generating new harness code).

### 2. Evaluator (`src/meta_harness/evaluator.py`)

A domain-specific protocol that defines how to run benchmarks and calculate scores. Each new domain (e.g., text classification, legal reasoning) must implement this interface.

### 3. Hermes Wrapper (`src/meta_harness/wrapper.py`)

A bridge to the [[hermes-agent]], allowing the engine to execute autonomous research sessions and capture tool-use traces.

## Onboarding New Domains

To onboard a new domain, follow the Domain Onboarding Standards:

1. Define a `domain_spec.md`.
2. Implement an `Evaluator` for the domain.
3. Provide baseline datasets and helper functions.

## Connections
- [[concepts/meta_harness_loop]]
- [[log]]
- [[wiki/index]]
- [[concepts/hermes_agent]]
- [[synthesis/domain-onboarding-standards]]
- [[concepts/meta_harness_loop]]

- [[hermes-agent]]
- [[agem]]
- [[meta-harness]]
