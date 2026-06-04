---
created: 2026-07-01
updated: 2026-07-01
type: concept
summary: Reasoning in agentic contexts — iterative tool use, ReAct pattern, multi-step planning under uncertainty, and the distinction between reactive and proactive reasoning
tags: [reasoning, agentic, react, tool-use, planning, llm-agents]
sources: https://arxiv.org/abs/2505.19913, https://arxiv.org/abs/2504.09559
status: active
confidence: 0.85
---

# Agentic Reasoning

## Definition

Agentic reasoning is the capability pattern that emerges when an LLM reasons not to produce a direct response but to select and execute actions in service of a goal, typically involving tool calls, environment interactions, and multi-step plans with uncertain paths. The defining feature is that **reasoning is instrumental — it drives action rather than output.**

This contrasts with non-agentic reasoning (e.g., CoT for math problems) where the reasoning trace is part of the output itself. In agentic reasoning, intermediate reasoning steps may be executed as internal monologues that trigger external actions — not exposed to the end user in the same way.

## Why It Matters

Agentic reasoning is the backbone of deployed LLM agents. A model that can only reason about fixed inputs cannot adapt to real-world tasks where conditions change, external data is required, or the solution path is not known in advance. The gap between a reasoning model (o1/o3) and an agentic model is the gap between *generating* reasoning traces and *using* them to drive behavior.

ClinSeekAgent (2025) exemplifies agentic clinical reasoning: the model must iteratively seek evidence from multimodal sources (PubMed, medical databases), evaluate retrieved context, and revise its evidence request — not just output a conclusion. The reasoning is inseparable from the action.

## The ReAct Pattern

**ReAct** (Reasoning + Acting) is the dominant agentic reasoning architecture. The agent iteratively:

1. **Reason** — generates an internal thought about what to do next
2. **Act** — executes a tool call or state-changing action
3. **Observe** — processes the result back into the reasoning context
4. **Repeat** — until a stopping condition is reached

```
Thought: I need to search for relevant clinical trials...
Action: search(query="COVID-19 vaccine efficacy immunocompromised")
Observation: 847 results returned, 12 relevant after filtering...
Thought: Let me dig deeper into trial NCT04702...
Action: fetch(url="https://clinicaltrials.gov/...")
...
```

ReAct is the right pattern when the solution path is **unknown and must emerge** from iterative interaction with the environment.

### ReAct vs. Pure Planning

| Property | ReAct | Planning |
|----------|-------|----------|
| Path to goal | Unknown — discovers through action | Known upfront — plan before acting |
| Thinking | Interleaved with action | Upfront before any action |
| Failure mode | Excessive looping | Plan fails when reality diverges |
| Best for | Open-ended exploration, tool-heavy tasks | Well-scoped tasks with known constraints |

### ReAct vs. Sequential Workflow

Sequential workflows (DAG-based) assume all steps are known upfront. ReAct is used when a step's input depends on a prior step's output that isn't knowable until execution. Hierarchical task decomposition (PlanAge, HuggingNLP) can bridge this by decomposing first, then switching to ReAct for uncertain sub-tasks.

## Key Research

**ClinSeekAgent** (arXiv:2505.19913) — Multimodal clinical evidence seeking agent demonstrating that agentic reasoning in medicine requires iterative evidence retrieval rather than static retrieval. The key finding: evidence is assumed in most systems, not retrieved on demand. Shows that medical reasoning requires a feedback loop between question decomposition, evidence retrieval, and answer synthesis.

**DeltaBox** (arXiv:2504.09559) — Stateful agent checkpoint/rollback mechanism. Introduces explicit checkpoint-rollback for agentic workflows where partial progress can be recovered. Shows that +5.9pp pass rate improvement over linear ReAct on Claude Sonnet 4.6. Demonstrates that state management is a core part of agentic reasoning architecture, not an afterthought.

**Agentic Research Pipeline limitations** — CUSP (2026) found that AI agents can generate plausible research directions but fail at temporal forecasting and feasibility prediction. The synthesis and evaluation stages of agentic pipelines have fundamental limitations — "scientific taste" is partly a temporal reasoning failure.

## Connections
- [[sources/papers/clinseekagent-multimodal-clinical-evidence-seeking]]
- [[concepts/maximum-occupancy-principle]]
- [[concepts/multi-agent-reasoning]]
- [[log]]
- [[wiki/index]]
- [[concepts/agentic-reasoning]]
- [[concepts/hybrid-agents]]
- [[concepts/agentic-reasoning]]

- [[concepts/maximum-occupancy-principle]] — Layer 0 intrinsic motivation framework that drives goal formation and exploration bias in agentic reasoning; MOP Layer 0 generates objectives before reasoning begins
- [[llm-reasoning]] — The foundational reasoning substrate; agentic reasoning layers ReAct on top of base reasoning capabilities
- [[latent-reasoning]] — Internal reasoning that may not be expressed in the output; relevant when the agent's internal monologue differs from its expressed reasoning
- [[adaptive-computation]] — Adaptive computation depth matters when the agent needs to decide how long to think before acting; early exit vs. extended reasoning
- [[autonomous-research]] — Six-stage agentic research pipeline where agentic reasoning is the execution engine
- [[multi-agent-coordination]] — When multiple agentic reasoning agents interact, coordination mechanisms become necessary (shared state, message passing, market-based)
- [[chain-of-thought]] — Non-agentic reasoning pattern; CoT is output, ReAct is action
- [[self-correction]] — ReAct loops benefit from self-correction capability; models that can identify and revise their own reasoning mid-loop perform better
- [[mcp-model-context-protocol]] — The tool ecosystem for agentic reasoning; MCP is what makes action execution tractable
- [[code-agent]] — Code agents are the canonical agentic reasoning application; they execute code as the primary action

- [[multi-agent-reasoning]]
- [[hybrid-agents]]
## Open Questions

1. **When does ReAct loop become pathological?** Excessive ReAct looping (infinite tool calls) is a known failure mode. What are the principled stopping signals — and can they be detected before the loop becomes costly?

2. **Agentic reasoning vs. load-bearing reasoning**: Is agentic reasoning a distinct cognitive mode or just "reasoning + tools"? The distinction matters for capability evaluation and for designing benchmarks that test reasoning under action constraints.

3. **Temporal scaling of agentic reasoning**: OpenDeepThink showed that parallel reasoning at test-time improves outputs. Can parallel execution be integrated with the ReAct loop — spawning multiple action branches and ranking them mid-execution rather than purely sequential?

4. **Epistemic energy in agentic loops**: The MOP/EFHF framework treats reasoning as energy-depleting. In agentic reasoning, how does tool execution cost vs. reasoning cost trade off? Is there an "epistemic budget" per action step?

## Limitations

- **ReAct is slow**: Each iteration incurs latency from model inference + tool execution. Real-time applications (voice, interactive) challenge the viability of deep ReAct chains.
- **Tool reliability propagates**: The agent's capability is capped by tool quality. A powerful reasoning model with unreliable tools becomes an unreliable agent.
- **Benchmark mismatch**: Most LLM reasoning benchmarks (MMLU, GSM8K) test non-agentic reasoning. Agentic benchmarks (FEATS, ClinSeekAgent) are emerging but sparse.
- **Planning-ReAct tradeoff is task-dependent**: No single pattern dominates. The wrong choice wastes compute. The cost of getting it wrong grows with task complexity.
