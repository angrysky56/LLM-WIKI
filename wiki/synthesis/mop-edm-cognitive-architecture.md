---
summary: Synthesis applying Maximum Occupancy Principle + EDM disruption measurement to AI cognitive architecture — three implementation levels, KL regularization critique, mcp-logic integration, epistemic energy, and coherent complexity growth
tags: [MOP, EDM, cognitive-architecture, entropy, hallucination-detection, epistemic-energy, absorbing-states, RLHF, attention, synthesis, intrinsic-motivation, ethics, KL-divergence, mcp-logic, computational-mechanics]
updated: 2026-04-14T01:03:57Z
---

# MOP-EDM Cognitive Architecture

**Type:** Synthesis — original cross-domain design
**Origin:** Ty (2026-04-13), building on [[maximum-occupancy-principle]], [[edm-framework]], [[causal-state-edm-ood-isomorphism]]
**Confidence:** 0.75 — conceptual framework grounded in formal results; KL insight confirmed by MOP paper's proof; implementation details speculative

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

### MOP Agents Seek Coherent Complexity Growth

When the MOP agent seeks high state entropy (β), it hunts for state-splitting events in the conceptual epsilon machine — discoveries that force the agent's world model to grow by accommodating structures that don't fit existing causal states. The excess entropy (statistical complexity) of the agent's world model increases with each genuine high-Δ event. MOP agents optimize for increasing the complexity of their own understanding. The absorbing state constraint prevents this from degenerating into noise: complexity growth that leads to contradiction is terminal. MOP therefore selects for *coherent* complexity growth — the model seeks to make its world model richer, not just noisier.

---

## The KL Regularization Problem (Key Insight for Training)

The MOP paper proves (Supplemental Sec. F) that **KL-regularization with a uniform default policy is self-defeating for occupancy maximization.** When relative entropy $-D_{KL}(\pi || \pi_0)$ replaces absolute entropy $\mathcal{H}(A|s)$, the immediate intrinsic return becomes $\mathcal{H}(A|s) - \ln|A(s)|$. The negative logarithm *penalizes* states with many available actions — mathematically opposing the goal of exploring diverse action-state paths.

**This directly challenges RLHF's standard structure.** The RLHF objective $\max_\pi \mathbb{E}[R(x)] - \beta_{KL} D_{KL}(\pi || \pi_{ref})$ uses KL divergence from the reference policy as a constraint. MOP proves this *actively suppresses* behavioral diversity — not as an incidental side effect, but as a mathematical consequence of the relative entropy objective. RLHF-trained models collapse toward deterministic responses partly because the KL regularizer penalizes occupying states where many response strategies are available.

An MOP-informed training objective would use absolute entropy as the primary signal and define absorbing states as the constraints, producing models that are *optimally stochastic* — diverse by default, precise when near absorbing boundaries. The absorbing states replace the KL tether to a reference policy: instead of "don't stray too far from a known-good model," the constraint becomes "don't enter states from which no coherent continuation is possible."

---

## Three Implementation Levels

### Level 1: Inference-Time MOP (Most Practical)

**Current state:** Models use greedy decoding (deterministic), temperature sampling (undirected noise), or top-k/top-p (constrained randomness). None have a principled theory of *when* to be variable and *when* to be precise.

**MOP replacement:** Use the optimal policy (Eq. 6) to guide token-level or reasoning-step-level decisions:

$$\pi^*(a|s) \propto \exp\left(\alpha^{-1}\beta \mathcal{H}(S'|s,a) + \alpha^{-1}\gamma V^*(s')\right)$$

Concretely:
- **Epistemic energy tracking:** Monitor context utilization, generation coherence, factual confidence as "energy" metrics. When energy is high, the model explores diverse reasoning paths. When energy is low, the model becomes deterministic and goal-directed — commits to the best-supported conclusion.
- **Absorbing state detection:** Real-time monitoring for repetition loops, self-contradiction, coherence collapse, harmful content trajectories. These are the "walls" of the cognitive environment.
- **EDM disruption monitoring:** Track the past-future vector divergence at each step. Flag when Δ exceeds thresholds without a grounded path back — this is the hallucination signal.

This level requires no retraining — it modifies the inference pipeline only.

### Level 2: Training-Time MOP (Fundamental Change)

**Current paradigm:** Pre-training (next-token prediction) → SFT → RLHF (reward maximization from preferences).

**MOP modification of RLHF:** Replace reward maximization with path entropy maximization using **absolute** entropy, not KL-regularized entropy (see KL problem above).

**Constitutional AI alignment via absorbing states:** Instead of training with explicit preference signals for every scenario, define absorbing states (output types constituting epistemic/ethical dead-ends) and let the model learn to navigate around them while maximizing cognitive diversity. This aligns with deontological constraints: define unconditional prohibitions (absorbing states), let virtue/wisdom (the α/β-balanced policy) emerge from the dynamics.

**α/β/γ as training hyperparameters:**
- α controls reward for trying different reasoning strategies
- β controls reward for reaching surprising conclusions
- γ controls optimization for short-term insight (low γ) vs. long-term understanding (high γ)

### Level 3: Attention-Level MOP (Most Speculative)

**Current attention:** Softmax over dot-product similarities → deterministic mapping from query to attended context, collapsing to dominant patterns.

**MOP attention:** Attention distribution incorporates entropy-maximizing component:
- Allocates attention to novel, underexplored context regions alongside relevant ones
- α controls relevance-novelty balance per attention head
- Internal energy (attention entropy, layer-wise confidence) determines when exploration is safe vs. when precision is needed

**Past/future decomposition of attention:** Causal attention has inherent temporal structure. Hidden states could be decomposed into past-facing (consolidating) and future-facing (generative) components. Monitoring cosine distance between these — attention-level EDM — provides per-layer, per-head disruption signals.

---

## Formal Verification via mcp-logic

The [[mcp-logic]] server provides Prover9 (theorem proving) and Mace4 (model finding) as formal verification tools. In the MOP-EDM architecture, these serve specific roles:

**Absorbing state detection:** Formalize the agent's current beliefs as first-order logic premises. Run `find_model(premises)` — if Mace4 cannot find a satisfying model, the beliefs are inconsistent → contradiction → absorbing state. The current reasoning chain must be terminated or rolled back.

**Hypothesis validation (β-filter):** When the MOP agent proposes a novel connection (high Δ), formalize it as a conclusion and run `find_counterexample(premises, conclusion)`. Counterexample found → reject the connection. No counterexample → tentatively accept. This gates what the exploration drive commits to the knowledge base.

**Abductive insight generation:** When the agent encounters something surprising, `abductive_explain(observation, candidates)` finds the VFE-minimizing explanation — the simplest consistent account. This bridges MOP's "seek high entropy" with formal reasoning: the agent explores freely, but its discoveries are grounded through abductive inference.

**Design-defined absorbing states (answering Open Question 3):** Given the mandate for Type II Error Avoidance, absorbing states must be strictly defined by design within mcp-logic. If the neural component is allowed to "learn" what counts as an epistemic dead-end, it will hallucinate bridges across contradictions to keep exploring — exactly as the MOP paper shows agents fabricate goals to avoid absorbing states.

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
- Never "terminate" — continue exploring until externally stopped

### Zettelkasten Integration

The [[zettelkasten-engine]]'s curation signals map directly:
- **Low Δ insight:** Consolidating — reinforces existing patterns → deprioritize
- **High Δ insight:** Disruptive — new causal state → flag for attention
- **Convergent future vectors:** Simultaneous discovery pattern → merge or link
- **MOP guides which insights to generate next:** Prefer high-entropy regions of the knowledge graph

---

## Open Questions

1. **What internal representations serve as past/future vectors?** KV cache states? Final hidden states? Attention patterns? Key empirical question for Level 2+3.
2. **How to define epistemic energy concretely?** Context utilization percentage? Perplexity over generated tokens? Attention entropy? Some combination?
3. ~~Can absorbing state detection be learned?~~ **Answered:** No — must be designed. Learned absorbing states allow the neural component to hallucinate escape paths. Type II Error Avoidance demands formal, design-time definitions verified via mcp-logic.
4. **Does MOP training actually produce more diverse outputs?** SAC architecture used for continuous MOP suggests yes, but needs empirical validation on language tasks.
5. ~~Is there a connection between MOP's path entropy and computational mechanics' excess entropy?~~ **Partially answered:** Yes. MOP agents seeking high β are hunting for state-splitting events that increase the statistical complexity of their world model. Each genuine high-Δ discovery increases excess entropy. Absorbing states ensure this complexity growth is coherent. Full formal proof connecting path entropy to excess entropy remains open.
6. **Can the α/β ratio be made adaptive?** In physical MOP, α/β is fixed. In cognitive MOP, the optimal ratio might change depending on the task — high β for brainstorming, low β for fact-checking.
7. **Can the KL insight be validated empirically?** Train two models: one with standard RLHF (KL regularization), one with absolute entropy MOP objective + absorbing states. Compare behavioral diversity and output quality.

---

## Connections

- [[maximum-occupancy-principle]] — the foundational theory
- [[ramirez-ruiz-mop-2024]] — source paper with mathematical formalism
- [[edm-framework]] — disruption measurement framework providing the Δ signal
- [[causal-state-edm-ood-isomorphism]] — the epsilon machine bridge; state-splitting as coherent complexity growth
- [[zettelkasten-engine]] — insight generation using MOP-guided exploration
- [[project-synapse]] — MCP infrastructure for epistemic energy replenishment
- [[persistent-knowledge-compilation]] — MOP predicts compiled knowledge bases should maintain stochastic access patterns
- [[prd-ralph-loop-mop-gemini]] — the Gemini conversation that initiated the cognitive MOP framing
