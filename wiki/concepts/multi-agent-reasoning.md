---
created: 2026-07-01
updated: 2026-07-01
type: concept
summary: Reasoning architectures that span multiple LLM agents — collaborative problem-solving, debate, arbitration, and the failure modes of multi-agent reasoning systems
tags: [reasoning, multi-agent, collaboration, debate, llm-agents]
sources: https://arxiv.org/abs/2505.10905, https://arxiv.org/abs/2505.19913
status: active
confidence: 0.85
---

# Multi-Agent Reasoning

## Definition

Multi-agent reasoning is reasoning that is distributed across multiple LLM agents, where different agents contribute distinct reasoning components — drafts, critiques, evaluations, or synthesis — that are then aggregated into a unified result. The key distinction from single-agent reasoning is that each agent has a partial view, a specialized role, and the output emerges from their interaction rather than from any single agent.

Common architectural variants:

- **Collaborative**: Agents work toward a shared answer with shared context (shared-state or message-passing)
- **Debate**: Agents argue competing positions; an adjudicator or self-consistency vote resolves
- **Critique-synthesis**: One agent generates, another critiques, a third synthesizes
- **Specialist-orchestrator**: A manager decomposes the problem and assigns sub-tasks to specialist agents

## Why It Matters

Many reasoning tasks exceed what a single agent can reliably handle alone — either because the knowledge domain is too broad, the task requires independent validation, or the reasoning trace太长 (long) and error-prone without checkpointing. Multi-agent reasoning addresses these by distributing the cognitive load.

The critical insight from recent research (2025–2026): **multi-agent reasoning systems are only as good as their coordination mechanism**. Simply spawning multiple agents doesn't improve reasoning — the interaction protocol matters far more than the individual model quality.

## Key Architectures

### Debate Architecture

In LLM debate, agents take opposing positions on a question and argue for their side. The key assumption: the weaker argument will fail more comprehensively when both sides have equal capability. Typically combined with a judge LLM that scores the debate.

**Limitation**: Both agents are reasoning about the same evidence. If the evidence itself is incomplete or misleading, debate amplifies the noise rather than correcting it. Debate works best for questions where the truth is discoverable through competitive scrutiny of a shared argument, not for questions requiring novel evidence retrieval.

### Critique-Synthesis Pipeline

1. **Generator agent**: Produces a candidate answer
2. **Critic agent**: Evaluates the generator's answer, identifies specific flaws
3. **Synthesizer agent**: Integrates the critique into a revised answer

This is structurally similar to the RefineNet/self-correction pattern, but distributed across agents with distinct system prompts and context windows. ClinSeekAgent's evidence-seeking pipeline is effectively a critique-synthesis pattern: the agent generates queries, retrieves evidence, critiques the retrieved evidence quality, and synthesizes into a clinical answer.

### Specialist-Orchestrator

A manager agent decomposes a complex goal into sub-goals, assigns each to a specialist agent (potentially using different system prompts, tools, or specialties), collects results, and synthesizes. This is the most common production architecture for multi-agent systems.

**Key failure mode**: The manager becomes the bottleneck and single point of failure. If the manager lacks the domain knowledge to decompose correctly, the specialists are solving the wrong problems.

## Connections
- [[wiki/index]]
- [[concepts/reasoning]]
- [[concepts/multi-agent-reasoning]]
- [[log]]
- [[concepts/parallel-reasoning]]
- [[concepts/multi-agent-reasoning]]

- [[multi-agent-llm-systems]] — Structural taxonomy of multi-agent architectures; multi-agent reasoning is one application of multi-agent systems
- [[multi-agent-coordination]] — The coordination mechanisms (shared state, message passing, market-based, swarm) that enable multi-agent reasoning
- [[llm-reasoning]] — Base reasoning capability; multi-agent reasoning layers coordination on top of individual reasoning
- [[parallel-reasoning]] — Shares the insight that running multiple reasoning processes in parallel improves output quality; OpenDeepThink's Bradley-Terry aggregation is a ranking mechanism without explicit agents
- [[agentic-reasoning]] — ReAct is the foundational single-agent pattern; multi-agent reasoning extends this to coordinated multi-agent ReAct
- [[self-correction]] — Single-agent critique-synthesis as a form of self-correction; multi-agent reasoning distributes this across agents
- [[process-reward-model]] — PRM as step-level judge could serve as adjudicator in multi-agent debate, scoring each reasoning step rather than just the final answer
- [[chain-of-thought]] — CoT is single-agent sequential reasoning; multi-agent reasoning can be seen as parallel CoT with interaction

- [[reasoning]]
## Open Questions

1. **Optimal team size**: At what number of agents does added diversity hit diminishing returns vs. coordination overhead? Current systems range from 2–10. Does the optimal team size scale with task complexity or domain breadth?

2. **Inter-agent trust without verification**: When Specialist A accepts Specialist B's output, what checks prevent cascading errors? If each agent independently verifies all claims, coordination overhead becomes prohibitive. What's the minimal trust model that permits efficient multi-agent reasoning?

3. **Debate vs. critique-synthesis for factual tasks**: For tasks requiring factual retrieval (clinical evidence, legal research), debate may amplify misinformation if both agents start from the same incomplete evidence set. Critique-synthesis seems better suited — but does it generalize?

4. **Emergent coordination without explicit protocols**: Recent work on implicit multi-agent coordination suggests agents can coordinate through shared context without explicit message-passing protocols. Does this scale to complex reasoning tasks or only to simple collaborative tasks?

## Limitations

- **Coordination overhead**: Every inter-agent handoff adds latency and a potential failure point. Multi-agent reasoning is slower than single-agent by design.
- **Inheritance of biases**: If all agents share the same base model, they inherit the same systemic biases. Diversity across agents (model families, fine-tunes, system prompts) is required for genuine error correction.
- **Evaluation difficulty**: Multi-agent reasoning outputs are hard to attribute. Was the answer correct because of good synthesis or despite bad individual components? This makes systematic improvement difficult.
- **Credit assignment**: When a multi-agent system fails, it's hard to determine which agent was responsible. This impedes debugging and improvement.
