---
summary: Synthesis applying Maximum Occupancy Principle + EDM disruption measurement to AI cognitive architecture — three implementation levels from inference-time guidance to attention-level mechanisms, with epistemic energy, absorbing states, and hallucination detection
tags: [MOP, EDM, cognitive-architecture, entropy, hallucination-detection, epistemic-energy, absorbing-states, RLHF, attention, synthesis, intrinsic-motivation, ethics]
updated: 2026-04-14T00:36:45Z
created: 2026-04-14T00:36:45Z
---

# MOP-EDM Cognitive Architecture

**Type:** Synthesis — original cross-domain design
**Origin:** Ty (2026-04-13), building on [[maximum-occupancy-principle]], [[edm-framework]], [[causal-state-edm-ood-isomorphism]]
**Confidence:** 0.72 — conceptual framework is sound and grounded in formal results; implementation details are speculative; no empirical validation yet

---

## The Core Claim

MOP provides a principled *motivation* for how AI models should navigate reasoning space. EDM provides a principled *measurement* of where the model is in that space relative to known territory. Together they define a cognitive architecture where models maintain exploratory diversity by default, become goal-directed when constrained, detect their own hallucinations via disruption signals, and avoid epistemic dead-ends without explicit reward engineering.

This architecture operates at three levels: inference-time guidance, training-time objectives, and attention-level mechanisms. Each level is progressively more speculative but also more transformative.

---

## The Physical-to-Cognitive Mapping

MOP was developed for embodied agents in physical environments. Applying it to AI cognition requires a precise mapping:

| Physical MOP | Cognitive MOP |
|---|---|
| Physical state (x, y, energy) | Epistemic state (current understanding, hypotheses held, confidence levels) |
| Physical actions (move L/R/U/D) | Cognitive actions (query source, hypothesize, connect concepts, verify, revise belief, synthesize) |
| State transitions p(s'|s,a) | How a cognitive action changes understanding — determined by model architecture + environment |
| Energy reservoir | **Epistemic energy** — context window budget, token limits, coherence reserves, factual confidence |
| Food sources | Information sources (wiki queries, database lookups, paper retrieval) — replenish epistemic energy |
| Absorbing states (death) | Epistemic dead-ends: contradiction, circular reasoning, context exhaustion, harmful content generation, coherence collapse |
| α (action entropy) | Diversity of cognitive strategies — try different reasoning approaches |
| β (state entropy) | Preference for novel/surprising conceptual outcomes — seek disruption |
| γ (discount factor) | Cognitive time horizon — greedy insight-grabbing vs. building toward deep understanding |

**The critical constraint:** Without epistemic energy depletion and absorbing states, MOP just produces a random walk through concept space. *With* these constraints, genuinely goal-directed behavior emerges — the model naturally seeks information sources when its epistemic energy is low, just as the MOP mouse seeks food when hungry. The constraint is what creates the intelligence.

---

## The EDM Connection

EDM's past/future vector framework provides the measurement layer MOP needs in cognitive space.

### Past/Future Vectors for Model Representations

At each reasoning step, the model's internal state can be decomposed into:
- **Past vector** ($p_i$): representation of what the context/prompt/prior reasoning says — "where the model came from"
- **Future vector** ($f_i$): representation of where generation is heading — "where the model is going"

The disruption score $\Delta = 1 - \cos(f_i, p_i)$ measures how much the model's trajectory diverges from what its context predicts. This is directly analogous to EDM's measurement of scientific disruption.

### Disruption as the β-Signal

MOP's β parameter controls preference for state entropy — novel outcomes. EDM's Δ measures exactly this: how *novel* the current reasoning trajectory is relative to established patterns.

- **Low Δ (consolidating):** The model's reasoning follows patterns predicted by its context. Low state entropy. Safe but potentially uninteresting.
- **High Δ (disruptive):** The model's reasoning diverges from context predictions. High state entropy. Potentially insightful OR potentially hallucinating.
- **The difference between insight and hallucination:** Under MOP's optimal policy, disruption is *controlled* — the agent maximizes entropy while avoiding absorbing states (contradictions, factual errors). Hallucination is *uncontrolled* disruption — the model enters high-Δ territory without a viable path back to grounded reasoning.

### Simultaneous Discovery Detection

EDM found that simultaneous discovery papers have nearly identical future vectors despite different past vectors. The cognitive analog: if two different prompts/contexts lead the model to the same conceptual territory (similar future vectors), this indicates a **convergent insight** — something structurally robust in the model's knowledge. If they converge on the same *wrong* answer, this fingerprints a **systematic confabulation pattern** distinguishable from random noise.

---

## Three Implementation Levels

### Level 1: Inference-Time MOP (Most Practical)

**Current state:** Models use greedy decoding (deterministic), temperature sampling (undirected noise), or top-k/top-p (constrained randomness). None of these have a principled theory of *when* to be variable and *when* to be precise.

**MOP replacement:** Use the optimal policy (Eq. 6) to guide token-level or reasoning-step-level decisions:

$$\pi^*(a|s) \propto \exp\left(\alpha^{-1}\beta \mathcal{H}(S'|s,a) + \alpha^{-1}\gamma V^*(s')\right)$$

Concretely:
- **Epistemic energy tracking:** Monitor context utilization, generation coherence, factual confidence as "energy" metrics. When energy is high, the model explores diverse reasoning paths. When energy is low, the model becomes deterministic and goal-directed — commits to the best-supported conclusion.
- **Absorbing state detection:** Real-time monitoring for repetition loops, self-contradiction, coherence collapse, harmful content trajectories. These are the "walls" of the cognitive environment.
- **EDM disruption monitoring:** Track the past-future vector divergence at each step. Flag when Δ exceeds thresholds without a grounded path back — this is the hallucination signal.

This level requires no retraining — it modifies the inference pipeline only.

### Level 2: Training-Time MOP (Fundamental Change)

**Current paradigm:** Pre-training (next-token prediction) → SFT → RLHF (reward maximization from preferences).

**MOP modification of RLHF:** Replace reward maximization with path entropy maximization.

The standard RLHF objective:
$$\max_\pi \mathbb{E}[R(s,a)] + \lambda \mathcal{H}(\pi)$$
uses entropy as a *regularizer* — a secondary term that helps exploration during training but is ultimately dominated by the reward signal. The trained model converges toward deterministic behavior.

The MOP training objective:
$$\max_\pi \mathbb{E}\left[\sum_t \gamma^t \left(\alpha \mathcal{H}(A|s_t) + \beta \mathcal{H}(S'|s_t, a_t)\right)\right]$$
uses entropy as the *primary objective*. The trained model converges toward stochastic behavior that is variable by default and deterministic only near absorbing states.

**Constitutional AI alignment via absorbing states:** Instead of training the model with explicit preference signals for every possible scenario, define the absorbing states (types of outputs that constitute epistemic/ethical dead-ends) and let the model learn to navigate around them while maximizing cognitive diversity. This aligns with a deontological constraint structure: define the unconditional prohibitions (absorbing states), and let virtue/wisdom (the α/β-balanced exploration policy) emerge from the dynamics.

**α/β/γ as training hyperparameters:**
- α controls how much the model is rewarded for trying different reasoning strategies
- β controls how much the model is rewarded for reaching surprising conclusions
- γ controls whether the model optimizes for short-term insight (low γ) or long-term understanding (high γ)

### Level 3: Attention-Level MOP (Most Speculative)

**Current attention:** Softmax over dot-product similarities produces a deterministic mapping from query to attended context. The model attends to whatever is most "relevant" — collapsing to dominant patterns.

**MOP attention:** The attention distribution incorporates an entropy-maximizing component:
- The model doesn't just attend to the most relevant tokens
- It also allocates attention to *novel, underexplored* regions of the context
- α controls the relevance-novelty balance per attention head
- Internal energy (attention entropy, layer-wise confidence) determines when exploration is safe vs. when precision is needed

**Past/future decomposition of attention:** Causal attention already has a temporal structure — earlier positions inform later ones. The hidden state at each position could be decomposed into past-facing (consolidating prior context) and future-facing (setting up future generation) components. Monitoring the cosine distance between these — an attention-level EDM — would provide per-layer, per-head disruption signals.

This level would require novel architectural modifications and is a research direction, not an implementation plan. However, it has connections to existing work on attention entropy regularization, attention diversity, and multi-head attention redundancy reduction.

---

## Connection to the Ethical Framework

MOP's structure maps cleanly onto the deontological → virtue → utilitarian hierarchy:

| Ethical Layer | MOP Analog | Mechanism |
|---|---|---|
| **Deontology** (harm = harm, unconditional) | Absorbing states | Defined categorically; avoided regardless of context; no cost-benefit analysis |
| **Virtue** (wisdom, integrity, empathy, fairness) | The α/β-balanced optimal policy | Wisdom = appropriate balance of exploration and precision; integrity = consistent policy; fairness = maximizing *shared* state entropy (the altruism result) |
| **Utilitarianism as servant** | MOP's core principle | Rewards/utility are *means* to continued exploration, never the goal; utility serves path entropy, not the reverse |

This is not a metaphor. MOP formally proves that when you make utility (reward) the servant of entropy (possibility), you get agents that survive, explore, cooperate, and adapt. When you make utility the master (reward maximization), you get agents that park at food sources, exploit single strategies, and lose behavioral diversity.

---

## Integration with Existing System

### Ralph Loop + MOP

A standard Ralph Loop is a reward maximizer: complete PRD tasks, check boxes, terminate. An MOP-driven Ralph Loop would:
- Use MOP's value function to choose which conceptual region to explore next
- Maintain epistemic energy tracking (context window utilization)
- Seek information sources (wiki queries via [[project-synapse]], paper retrieval) when energy is low
- Use [[mcp-logic]] for absorbing state detection (contradiction, logical inconsistency)
- Use EDM-style disruption signals to distinguish genuine insights from hallucinated connections
- Never "terminate" — continue exploring until externally stopped, just as a MOP agent continues moving

### Zettelkasten Integration

The [[zettelkasten-engine]]'s curation signals map directly:
- **Low Δ insight:** Consolidating — reinforces existing patterns → deprioritize
- **High Δ insight:** Disruptive — new causal state → flag for attention
- **Convergent future vectors:** Simultaneous discovery pattern → merge or link as "same concept reached by different paths"
- **MOP guides which insights to generate next:** Prefer high-entropy regions of the knowledge graph — concepts with many unresolved connections, underexplored neighborhoods, or high-confidence gaps

---

## Open Questions

1. **What internal representations serve as past/future vectors?** KV cache states? Final hidden states? Attention patterns? This is the key empirical question for Level 2+3.
2. **How to define epistemic energy concretely?** Context utilization percentage? Perplexity over generated tokens? Attention entropy? Some combination?
3. **Can absorbing state detection be learned?** Or must absorbing states be defined by design (as MOP requires in the physical case)?
4. **Does MOP training actually produce more diverse outputs?** The SAC architecture used for continuous MOP suggests yes, but this needs empirical validation on language tasks.
5. **Is there a connection between MOP's path entropy and computational mechanics' excess entropy?** If so, disruptive reasoning (high Δ) corresponds to high statistical complexity cost — the model is "paying" to create new causal states in its reasoning chain.
6. **Can the α/β ratio be made adaptive?** In physical MOP, α/β is fixed. In cognitive MOP, the optimal ratio might change depending on the task — high β for brainstorming, low β for fact-checking.

---

## Connections

- [[maximum-occupancy-principle]] — the foundational theory
- [[ramirez-ruiz-mop-2024]] — source paper with mathematical formalism
- [[edm-framework]] — disruption measurement framework providing the Δ signal
- [[causal-state-edm-ood-isomorphism]] — the epsilon machine bridge connecting EDM to causal information theory
- [[zettelkasten-engine]] — the insight generation system that would use MOP-guided exploration
- [[project-synapse]] — the MCP infrastructure providing knowledge graph access for epistemic energy replenishment
- [[persistent-knowledge-compilation]] — MOP predicts that compiled knowledge bases should maintain stochastic access patterns rather than deterministic retrieval hierarchies
