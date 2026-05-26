# Researcher Discovery Report — 2026-07-01

## Discovery Cycle
- Topics researched: 4
- New pages created: 4
- Pages updated: 4 (status upgrade: stub → active)
- Cross-links added: ~24 (estimated based on Connections sections)

## New Entries / Upgraded Stubs

### agentic-reasoning.md — UPGRADED: stub → active
Filled from stub with connections only to [[maximum-occupancy-principle]] → now active with:
- Definition: instrumental reasoning that drives action vs. produces direct output
- ReAct pattern: Thought→Act→Observe→Repeat loop, when to use vs. planning vs. sequential
- Key research: ClinSeekAgent (clinical evidence seeking), DeltaBox (checkpoint/rollback)
- 4 Open questions: pathological looping, load-bearing distinction, temporal scaling, epistemic energy
- Connections: maximum-occupancy-principle, llm-reasoning, latent-reasoning, adaptive-computation, autonomous-research, multi-agent-coordination, chain-of-thought, self-correction, mcp-model-context-protocol, code-agent

### multi-agent-reasoning.md — UPGRADED: stub → active
Filled from stub with connections only to multi-agent-systems and reasoning → now active with:
- Definition: distributed reasoning across agents with partial views and specialized roles
- Four architectural variants: debate, critique-synthesis, specialist-orchestrator, collaborative
- Key failure modes: coordination overhead, manager bottleneck, bias inheritance
- 4 Open questions: optimal team size, inter-agent trust without verification, debate vs. critique-synthesis for factual tasks, emergent coordination
- Connections: multi-agent-llm-systems, multi-agent-coordination, llm-reasoning, parallel-reasoning, agentic-reasoning, self-correction, process-reward-model, chain-of-thought

### parallel-reasoning.md — UPGRADED: stub → active
Filled from stub with connections only to chain-of-thought and multi-agent-reasoning → now active with:
- Definition: multiple reasoning traces executed concurrently, ranked via aggregation
- Self-consistency (Wang 2023) vs. Bradley-Terry aggregation (OpenDeepThink, +405 Codeforces Elo)
- Test-time compute scaling context: 7B + 4096 samples vs. 405B model on MATH
- 4 Open questions: non-verifiable domains, optimal candidate scaling, Bradley-Terry + PRM integration, adaptive parallelism
- Connections: llm-reasoning, chain-of-thought, test-time-compute-scaling, process-reward-model, self-correction, multi-agent-reasoning, inference-time-compute-scaling, opendeepthink-parallel-reasoning

### model-serving.md — UPGRADED: stub → active
Filled from stub with connections only to mlops and inference-efficiency → now active with:
- Definition: software engineering discipline of deploying ML models to production
- Key systems: vLLM (PagedAttention), TensorRT-LLM, SGLang (RadixAttention), Ray Serve
- 4 Open questions: prefix deduplication at scale, heterogeneous model families, cost vs. capability scaling, distributed serving
- Connections: llm-inference, inference-efficiency, kv-cache, inference-time-compute-scaling, mixture-of-experts, mlops

## Gap Analysis
- 4 stubs upgraded to active this cycle
- Stub count: 341 (was 345 — accurate count maintained by re-running grep each cycle)
- Reasoning cluster now substantially filled: agentic-reasoning, multi-agent-reasoning, parallel-reasoning, model-serving (connects to llm-inference now active)
- Remaining high-priority stubs: see kanban task list
- Priority elevation: after filling agentic-reasoning (links to maximum-occupancy-principle, now active), stubs that link to agentic-reasoning elevate in priority

## Open Questions
- **Reward hacking detectability**: Previously in carryover. Wiki search confirms reward-hacking.md now has a fully documented §Early Detection with 6 prospective signals (gradient fingerprints, internal activations, energy loss, χ² vs KL divergence, adversarial auditing, calibration monitoring). This question is ANSWERED in the existing wiki — no further research needed beyond whatTy posted in CLINMEET.
- **Next cycle intent**: Continue stub-first. Emerging cluster candidates: creativity (thin, links to parallel-reasoning), wolfram-nks-causal-networks (thin, connects to computational-irreducibility), creativity (links to parallel-reasoning now active).

## Notes
- Verified before research: The "reward hacking detectability" open question was confirmed answered in existing reward-hacking.md §Early Detection — no duplication of effort
- OpenDeepThink source paper already ingested (wiki/sources/papers/opendeepthink-parallel-reasoning.md) — used as primary source for parallel-reasoning.md
- model-serving.md naturally inherits from llm-inference.md which was created in the Jun 28 cycle — the model-serving stub was the connecting link to fill
- mlops.md should reciprocal-link to model-serving.md — flag for librarian
