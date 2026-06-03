---
created: 2026-06-14
updated: 2026-06-26
type: concept
summary: First-class information-theoretic resource tracking reasoning coherence and energy depletion in agentic AI systems — maps to EFHF Layer 4 coherence monitoring and MOP's energy reservoir
tags: [MOP, EFHF, information-theory, bounded-rationality, coherence, agent-design, epistemic-energy]
sources:
  - "[[maximum-occupancy-principle]]"
  - "[[ramirez-ruiz-mop-2024]]"
status: active
confidence: 0.8
---

# Epistemic Energy

Epistemic energy is the information-theoretic quantity measuring an agent's available reasoning resources at any moment — analogous to metabolic energy in biological systems. It depletes as reasoning progresses, and when it runs out, coherence degrades: the agent enters contradiction (an absorbing state) or produces unreliable output.

## Definition

In the MOP-EDM cognitive architecture, epistemic energy `E` is a scalar resource that:

- **Starts full** when the agent begins a reasoning session
- **Depletes** as the agent generates tokens, maintains context, and processes novel information
- **Accelerates depletion** when encountering high-Δ (high disruption) events — novel territory that requires more inferential work
- **Reaches zero** at the coherence boundary — the point where continuing is worse than stopping

The key analogy from [[agent-native-design]]:

| Physical System | Cognitive System |
|-----------------|------------------|
| Metabolic energy (food) | Epistemic energy (information) |
| Physical exhaustion | Reasoning incoherence |
| Death (absorbing state) | Contradiction (absorbing state) |
| foraging behavior | MOP exploration |

## Why It Matters

Standard LLM systems treat context as a container to be filled and stop when tokens run out. Agent native design says the stopping condition should be epistemic energy depletion — not token budget.

This matters because:
- **Token limits are arbitrary.** An agent can exhaust its useful reasoning before hitting the token limit (coherence degrades mid-context) or have spare capacity after (cheap problem).
- **High-Δ events are warning signals.** When the agent encounters something genuinely novel, it should recognize that continued reasoning is risky — not blindly continue.
- **Absorbing states are terminal.** Contradiction — saying two things that can't both be true — is an absorbing state. No coherent continuation exists. The agent should detect this and stop, not generate more tokens.

## The EDM Connection: Disruption as Depletion Signal

The [[edm-framework]] (Evidence Accumulation with Disruption) provides the measurement mechanism. High Δ (disruption) signals that the current reasoning path is moving into novel territory — territory where the agent's world model has weak coverage. In EDM terms:

- Low Δ = familiar reasoning territory, slow depletion
- High Δ = novel territory, accelerated depletion
- Absorbing Δ = contradiction, instant depletion to zero

This maps to MOP's energy reservoir: food is necessary because exploration burns energy faster than exploitation. Similarly, reasoning about novel concepts burns epistemic energy faster than reasoning within known frames.

## EFHF Layer 4: Coherence Monitoring

In the [[efhf]] five-layer architecture, epistemic energy tracking is Layer 4 (meta-cognitive monitoring):

- **L1 (Hypothesis)**: Generate possible reasoning paths
- **L2 (World model)**: Encode hypotheses in context
- **L3 (Verification)**: Check logical consistency (Prover9 via mcp-logic)
- **L4 (Coherence)**: Track epistemic energy, detect degradation
- **L5 (Persistence)**: Enforce sheaf consistency

L4 is where epistemic energy depletion becomes actionable: if `E < threshold`, the system triggers one of:
- **Conservation**: Switch to shorter, more direct reasoning paths
- **Backup**: Trigger [[working-memory]] rehearsal to consolidate what has been established
- **Abort**: Stop generation if `E` is near zero — no viable continuation exists

## How to Measure It

Open question per [[agent-native-design]]: how do you measure epistemic energy depletion in a live LLM?

Candidate operationalizations:
- **Context utilization**: Fraction of context window that contains novel (unseen) token n-grams
- **Attention entropy**: Entropy of attention weight distribution — higher entropy = more diffuse reasoning = faster depletion
- **Perplexity on known facts**: If the agent is asked to recall facts it should know, degradation in accuracy signals low energy
- **Disruption rate**: Rate of high-Δ events in the EDM sense — novel concept combinations, surprising analogies

None of these are fully validated. This is an active measurement problem.

## Connections
- [[concepts/meta-cognitive-agents]]
- [[concepts/adaptive-computation]]
- [[concepts/agent-native-design]]
- [[scratchpad/jobs/reports/researcher/discovery-2026-06-26]]
- [[concepts/maximum-occupancy-principle]]
- [[concepts/cognitive-world-models-for-llm-agents]]
- [[concepts/edm-framework]]
- [[concepts/latent-reasoning]]
- [[concepts/epistemic-energy]]
- [[concepts/working-memory]]
- [[wiki/index]]
- [[concepts/world-model]]
- [[concepts/bounded-rationality]]
- [[log]]
- [[epistemic-energy]]

- [[agent-native-design]] — the architectural context where epistemic energy is first-class
- [[maximum-occupancy-principle]] — the energy reservoir analogy; MOP agents maximize entropy subject to energy constraints (absorbing states)
- [[working-memory]] — the active maintenance substrate for epistemic energy; attention decay is one depletion mechanism
- [[bounded-rationality]] — epistemic energy is the quantitative form of bounded rationality
- [[efhf]] — Layer 4 (coherence monitoring) implements epistemic energy tracking
- [[mop-edm-cognitive-architecture]] — the synthesis document defining the L4 role
- Concept: [[cognitive-world-models-for-llm-agents]]
- Concept: [[world-model]]


- [[meta-cognitive-agents]]
- [[adaptive-computation]]
- [[latent-reasoning]]
## Open Questions

1. **Measurement**: What is the best operationalization of epistemic energy in a running transformer? Attention entropy? Context utilization? Perplexity on calibration questions?

2. **Refill mechanisms**: How does epistemic energy "refill"? Sleep analogs (idle time)? Memory consolidation ([[working-memory]] rehearsal)? External knowledge retrieval?

3. **Transfer across sessions**: If an agent runs out of epistemic energy mid-task, does the next session start with depleted energy or reset? Markovian carryover partially addresses this but doesn't measure the energy state itself.

4. **Individual differences**: Do different LLMs have different "energy reservoirs"? Does model scale affect capacity, or only efficiency?
