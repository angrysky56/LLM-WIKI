---
created: 2026-05-08T01:12:20Z
updated: 2026-05-08T01:12:20Z
type: project
summary: A framework for self-adaptive agent evolution and structured knowledge bootstrapping, integrated with Hermes.
tags: [agentic-evolution, self-adaptive, hermes, meta-learning, knowledge-synthesis]
status: active
confidence: 0.95
---

# Meta-Harness

Meta-Harness is a high-performance framework designed for **self-adaptive agent evolution** and **structured knowledge bootstrapping**. It focuses on the "picks and shovels" of the AI development cycle: creating verifiable, domain-complete knowledge bases that specialized agents can use to reason accurately.

## Core Objective

The primary goal of Meta-Harness is to solve two fundamental problems in LLM reasoning:
1. **Hallucination under pressure**: By providing domain-complete knowledge instead of shallow training data.
2. **Lack of Provenance**: By maintaining a structured graph with clear citation chains and audit trails.

## Architecture

Meta-Harness employs a multi-tiered architecture for agent improvement:

### 1. The Proposer (Hermes Integration)
The system utilizes the [[hermes-agent|Hermes]] architecture to autonomously propose improvements to agent logic. It resolves local configurations and adapts to specialized domain requirements.

### 2. The Inner Loop (Evaluation & Learning)
- **Prediction**: Agents predict outcomes based on the current state.
- **Verification**: Outputs are verified against ground truth or formal constraints.
- **Learning**: Feedback is ingested to refine agent memory and logic.

### 3. Memory Systems
The framework supports various memory architectures:
- `NoMemory`: Zero-shot baseline.
- `FewShotMemory`: Dynamic context injection based on task similarity.
- `EvolvingMemory`: (Planned) Long-term structural updates via recursive feedback.

## Key Features

- **Standardized Interfaces**: Enforces strict typing and naming conventions (e.g., `predict(text: str)`) to avoid Python built-in shadowing.
- **Domain Onboarding**: Streamlined pipeline for ingesting new specialized domains into the knowledge graph.
- **Verification-First**: Integrated with Prover9/Mace4 (via [[mcp-logic]]) for formal consistency checks when necessary.

## Development Status

The project is currently in the **stabilization phase**. 
- Core infrastructure is hardened.
- Hermes integration is functional and path-robust.
- Unit testing suite is established for all major components.

## Connections
- [[tys-repos]] — Part of Ty's core repository suite.
- [[project-synapse]] — Integrated with Synapse for knowledge synthesis.
- [[hermes-agent]] — Utilizes Hermes for autonomous evolution.
- [[agem]] — Shares concepts with the Agent-Group Evolving Molecular system.
