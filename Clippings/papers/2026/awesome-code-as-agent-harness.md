# Awesome Code as Agent Harness Papers

**Source:** https://github.com/YennNing/Awesome-Code-as-Agent-Harness-Papers
**Survey:** [Code as Agent Harness: Toward Executable, Verifiable, and Stateful Agent Systems](https://arxiv.org/abs/2605.18747) — Ning et al., arXiv 2026
**Stars:** 30 | **License:** MIT
**Contact:** xuyingn2@illinois.edu, kt42@illinois.edu, tieu@illinois.edu

## Overview

Code is no longer only a generated artifact — it increasingly serves as an executable, inspectable, and stateful harness through which agents reason, act, model environments, receive feedback, and coordinate.

Three-layer framework organizing the field:

### 🧩 Harness Interface
How code serves as the interface between model and environment.

- **Code for Reasoning** — Programs externalize internal logic into verifiable computation
  - Program-Delegated Reasoning (PoT, PAL, MathCoder, Chain of Code)
  - Hybrid Symbolic–Neural Execution
  - Iterative Code-Grounded Reasoning
- **Code for Acting** — Generated programs as policies, tool calls, behavior trees
  - Grounded Skill Selection (affordances, bootstrapping)
  - Programmatic Policy Generation (RoboCodeX, ReAct, Code as Policies)
  - Lifelong Code-Based Agents (Voyager, UI-Voyager)
- **Code for Environment Modeling** — World models via program states, traces, simulators
  - Structured World Representations (PoE-World, Code2World)
  - Execution-Trace World Modeling (WorldCoder, CWM)
  - Code-Grounded Evaluation (SWE-bench, AgentBench, LiveCodeBench)

### 🛠️ Harness Mechanisms
How the harness controls what to execute next, preserves state, exposes tools.

- **Planning for Code Agents** — Linear decomposition, structure-grounded, search-based (MCTS), orchestration
- **Memory and Context Engineering** — Working, semantic, experiential, long-term, multi-agent memory
- **Tool Usage for Code Agents** — Function-oriented, environment-interaction, verification-driven, workflow-orchestration
- **Feedback-Guided Iterative Debugging** — Compilation feedback, runtime errors, test-based, critique-driven

### 👥 Scaling the Harness
Multi-agent coordination over shared code.

- **Functional Role Specialization** — Program synthesis agents (MetaGPT, ChatDev), understanding agents, verification agents
- **Interaction Modes** — Sequential, parallel, hierarchical
- **Workflow Topology** — Centralized vs distributed
- **Execution Feedback Integration**
- **Shared-Harness Synchronization**
- **Shared Harness Representation**
- **Harness-State Convergence**

## Key Observations

1. **Code as the universal harness substrate** — Programs convert model outputs into executable, inspectable, stateful structures. Reasoning becomes verifiable, action becomes programmable, environment state becomes inspectable.

2. **Three distinct layers** — Harness Interface (what code does), Harness Mechanisms (how code is controlled), Scaling (how multiple agents share code).

3. **Verification is the bottleneck** — Test-based and runtime feedback dominate the feedback-guided debugging literature; formal verification (SatLM) is rare.

4. **Multi-agent code coordination is an emerging frontier** — Most current work focuses on single-agent code execution; multi-agent shared-harness synchronization (shared code state across agents) is under-explored.

5. **Survey connects to EML/MOP/EFHF** — The code-as-harness paradigm parallels the EML operator (minimal primitives + recursion) and MOP (maximum occupancy / path entropy) in treating code as the minimal executable substrate for structured agent behavior.

## Bibtex

```bibtex
@article{ning2026codeasharness,
  title   = {Code as Agent Harness: Toward Executable, Verifiable, and Stateful Agent Systems},
  author  = {Ning, Xuying and Tieu, Katherine and Fu, Dongqi and Wei, Tianxin and Li, Zihao and Bei, Yuanchen and others},
  journal = {arXiv preprint arXiv:2605.18747},
  year    = {2026}
}
```
