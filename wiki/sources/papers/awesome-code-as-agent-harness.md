---
summary: "Survey companion repo organizing 200+ papers on code as executable harness for LLM agents — three-layer framework: interface, mechanisms, scaling"
tags: [paper, survey, code-as-agent-harness, literature, agent-architecture]
updated: 2026-05-19T17:27:40Z
created: 2026-05-19T17:27:40Z
---

# Awesome Code as Agent Harness Papers

**Type:** Literature curation / survey companion
**Source:** https://github.com/YennNing/Awesome-Code-as-Agent-Harness-Papers
**Survey Paper:** [arXiv 2605.18747](https://arxiv.org/abs/2605.18747) — Ning et al. (2026)
**Contact:** xuyingn2@illinois.edu

## Summary

Companion repo to the survey "Code as Agent Harness: Toward Executable, Verifiable, and Stateful Agent Systems." Organizes 200+ papers around three connected layers: **Harness Interface**, **Harness Mechanisms**, and **Scaling the Harness**.

The survey's core thesis: code is no longer only a generated artifact — it increasingly serves as an executable, inspectable, and stateful harness through which agents reason, act, model environments, receive feedback, and coordinate.

## Three-Layer Framework

### 🧩 Harness Interface
How code serves as the interface between model and task environment.

| Sub-area | Papers | Key Insight |
|---|---|---|
| Code for Reasoning | PoT, PAL, MathCoder, Chain of Code | Programs externalize logic into verifiable computation |
| Code for Acting | RoboCodeX, ReAct, Voyager, Code as Policies | Generated programs as policies, tool calls, behavior trees |
| Code for Environment Modeling | PoE-World, WorldCoder, SWE-bench | Program states, traces, and tests represent world state |

### 🛠️ Harness Mechanisms
Once code is inside the agent loop — what controls execution, preserves state, exposes tools, converts failures into corrective actions.

- **Planning** — Linear decomposition, structure-grounded (RPG, CodePlan), search-based (MCTS → CodeTree, DARS), orchestration (MapCoder, AlgoForge)
- **Memory** — Working (SWE-agent, CodeMem), semantic (RepoCoder), experiential (ExpeL, Evo-Memory), long-term (MemGPT, Memex(RL))
- **Tool Usage** — ToolNet, ControlLLM, MCP, OpenHands
- **Feedback-Guided Debugging** — Compiler feedback, runtime errors, test-based (RLTF, RLEF), self-debugging (Self-Debug, ReVeal)

### 👥 Scaling the Harness
Multi-agent code-centric systems — roles, shared state, workflow topology.

- **Functional Roles** — Synthesis agents (MetaGPT, ChatDev), understanding agents (HyperAgent), verification agents
- **Workflow Topologies** — Centralized, hierarchical, decentralized
- **Shared-Harness Synchronization** — Shared code state across agents (SWE-Debate, MIRIX)

## Key Observations

1. **Code as universal harness substrate** — Makes reasoning *executable*, action *programmable*, environment state *inspectable*
2. **Verification is the bottleneck** — Most feedback literature is test/compiler-based; formal verification (SatLM) is rare
3. **Multi-agent shared-harness is under-explored** — Most work is single-agent; shared code state coordination across agents is an emerging frontier
4. **Connects to EML/MOP/EFHF** — The minimal-primitives + recursion pattern in EML and the path-entropy framing of MOP parallel how code-as-harness treats code as the minimal executable substrate for structured agent behavior

## Bibtex

```bibtex
@article{ning2026codeasharness,
  title   = {Code as Agent Harness: Toward Executable, Verifiable, and Stateful Agent Systems},
  author  = {Ning, Xuying and Tieu, Katherine and Fu, Dongqi and Wei, Tianxin and Li, Zihao and Bei, Yuanchen and others},
  journal = {arXiv preprint arXiv:2605.18747},
  year    = {2026}
}
```

## Related
- [[wiki/index]]
- [[sources/papers/clinseekagent-multimodal-clinical-evidence-seeking]]
- [[sources/papers/awesome-code-as-agent-harness]]

- [[awesome-code-as-agent-harness]]

## Tags
#paper #survey #code-as-agent-harness #literature #agent-architecture #multi-agent #verification #memory #planning
