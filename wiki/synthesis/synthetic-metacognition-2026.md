---
title: "Synthetic Metacognition: From Neural Inspiration to Mathematical Architecture"
subtitle: "Integrating ELBO Perception, PAC-Bayes Action, Portfolio Policy Control, and MCMC Inference into a Unified Cognitive Architecture for LLM Agents"
author: "Derived from conversations with Gemini, cross-referenced with ArXiv research"
summary: "A deep synthesis of four threads — ACC/ELBO conflict monitoring, knowledge management theory, portfolio-of-policies MDP control, and Metropolis-Hastings inference — into a unified mathematical architecture for agent metacognition."
tags: [metacognition, agent-architecture, PAC-Bayes, ELBO, MCMC, variational-inference, cognitive-architecture, research]
type: synthesis
status: active
confidence: 0.85
created: 2026-06-10
updated: 2026-06-10
---

# Synthetic Metacognition: From Neural Inspiration to Mathematical Architecture

## Abstract

Biological intelligence rests on a metacognitive loop: the brain monitors its own uncertainty (via the Anterior Cingulate Cortex), evaluates confidence (via the Prefrontal Cortex), and gates action (via the Thalamic Reticular Nucleus) — all in service of a single imperative: *know when you don't know*. This paper synthesizes four independently developed threads into a unified mathematical architecture for synthetic metacognition in LLM agents:

1. **The ELBO Perception Loop** — Variational free energy as the raw signal for epistemic uncertainty
2. **The PAC-Bayes Action Bound** — Generalization theory as the mathematical emergency brake
3. **The Portfolio-of-Policies MDP** — Multi-threaded resource allocation under entropy-confidence duality
4. **The Knowledge Management Substrate** — Organizational structure for externalized memory
5. **The MCMC Inference Engine** — Metropolis-Hastings sampling over the knowledge graph

Together, these form a complete architecture: **perceive uncertainty → evaluate risk → allocate resources → act (or halt) → update memory**.

---

## 1. The Biological Blueprint

The neurological basis of metacognition — "knowing that you don't know" — involves a specific circuit:

| Brain Region | Function | Role in Uncertainty |
|---|---|---|
| **ACC** (Anterior Cingulate Cortex) | Conflict monitoring | Detects gap between goal and available data |
| **dlPFC** (Dorsolateral Prefrontal Cortex) | Confidence evaluation | Weighs evidence strength, computes confidence score |
| **Hippocampus** | Memory indexing with FOK | Tags memories with "feeling of knowing" — knows that it knows, even when retrieval fails |
| **TRN** (Thalamic Reticular Nucleus) | Attention gating | Switches from top-down (autopilot) to bottom-up (active seeking) when uncertainty spikes |
| **Amygdala** | Emotional weighting | Attaches stakes to uncertainty — dangerous ignorance demands immediate attention |

The computational mechanism underlying all of these is **Predictive Coding**: the brain as a prediction machine. Prediction error = signal of lack of knowledge. The brain doesn't *declare* uncertainty — it *computes* it as the mismatch between its internal model and incoming data.

**Key insight**: This is not a metaphor. Karl Friston's Free Energy Principle proves that minimizing variational free energy (surprise) is mathematically identical to maximizing the Evidence Lower Bound (ELBO). Biology discovered variational inference hundreds of millions of years before mathematicians formalized it.

---

## 2. The ELBO Perception Loop: Knowing What You See

### The Equation

$$\log p(x) \geq \mathbb{E}_{q(z|x)} [\log p(x|z)] - \text{KL}(q(z|x) \| p(z))$$

This is the Evidence Lower Bound (ELBO) — the foundation of variational inference. In the metacognitive context:

| Term | Mathematical Meaning | Cognitive Meaning |
|---|---|---|
| $\log p(x)$ | Evidence (marginal likelihood) | How well the agent's overall model explains the world |
| $\mathbb{E}_{q(z|x)} [\log p(x|z)]$ | Reconstruction accuracy | **Prediction Error**: Given internal memory state $z$, how accurately can the agent reconstruct observation $x$? |
| $\text{KL}(q(z|x) \| p(z))$ | Complexity penalty | **Paradigm Shift Cost**: How drastically must prior beliefs be modified to accommodate the new observation? |

### The Three Metacognitive States (with caveats)

**Important honesty caveat:** The ELBO, strictly defined, requires a generative model $p(x|z)$ and a variational posterior $q(z|x)$. For an LLM agent operating over a Neo4j knowledge graph, neither exists as a well-defined probabilistic model. There is no likelihood function that says "given memory subgraph $z$, the probability of observing token sequence $x$ is..." — the relationship between an agent's memory and its observations is not a generative model in the statistical sense.

What we actually use are **proxies** for each term:

| ELBO Term | What It Actually Is | Proxy Used |
|---|---|---|
| $\log p(x)$ | Evidence | Task-specific (not computed) |
| $\mathbb{E}_{q(z|x)} [\log p(x|z)]$ | Reconstruction accuracy | Embedding similarity between observation and retrieved subgraph; token log-probabilities under the LLM |
| $\text{KL}(q(z|x) \| p(z))$ | Paradigm shift cost | Semantic entropy over $k$ sampled answers; divergence between agent's stated confidence and measured accuracy |

These proxies can work — the functional form (reconstruction minus complexity) is robust — but the architecture's claims inherit the proxies' **calibration quality**, not the ELBO's mathematical status. A poorly calibrated proxy (e.g., an embedding model that doesn't distinguish "confidently wrong" from "correct") will produce a poorly calibrated metacognitive signal. The math provides structure; the proxies provide the numbers. Garbage proxies in a rigorous framework are still garbage in.

### Connection to Predictive Coding

In computational neuroscience, precision-weighted prediction error is the signal the ACC uses to detect conflict. The ELBO's reconstruction term $\mathbb{E}_{q(z|x)} [\log p(x|z)]$ is exactly this: the expected log-likelihood of the observation under the agent's internal model. When this drops, the ACC-equivalent monitor fires.

---

## 3. The PAC-Bayes Action Bound: Knowing When to Stop

### The Equation

$$R(Q) \leq \hat{R}(Q) + \sqrt{\frac{\text{KL}(Q\|P) + \log(1/\delta)}{2n}}$$

The PAC-Bayes bound gives us the **true generalization risk** of a proposed action, decomposed into:

| Term | Mathematical Meaning | Cognitive Meaning |
|---|---|---|
| $\hat{R}(Q)$ | Empirical risk | How dangerous does this action look right now? |
| $\text{KL}(Q\|P)$ | Divergence from prior | How far does this action deviate from known-safe memory paths? |
| $n$ | Sample size / evidence weight | How much prior experience supports this action? |
| $\delta$ | Confidence parameter | How certain must we be? (Type II Error tolerance) |

### The Asymmetric Safety Function

For a **Type II Error Avoidance** policy (where unknown = hostile), the functional form becomes:

$$\text{Risk Score} = \hat{R}(Q) + W_{\text{TypeII}} \cdot \sqrt{\frac{\text{KL}(Q\|P) + \log(1/\delta)}{2n}}$$

**Critical caveat:** The PAC-Bayes theorem guarantees bounds on generalization risk under strict assumptions: i.i.d. samples from a fixed distribution, with $Q$ and $P$ as distributions over hypotheses evaluated on that data. An agent acting sequentially in a **non-stationary environment** (the world changes, the agent's own actions change the context) violates every one of those assumptions.

What is $n$ — the count of "similar past actions"? They are not i.i.d. Past interactions are path-dependent, non-stationary, and actively altered by the agent's prior choices. The bound's guarantee **evaporates** the moment the i.i.d. assumption fails.

**What survives:** The *functional form* — empirical risk plus a complexity penalty scaled by inverse evidence weight, with an asymmetric multiplier on uncertainty. This is a perfectly good risk score and a reasonable design pattern. It is not a proof of safety. The system should be described as a "risk scoring function with PAC-Bayes structure," not as something that "proves" safety. The word "prove" should not appear in this document when describing what this system does.

### The TRN Gate

The Thalamic Reticular Nucleus equivalent: a routing protocol that, when the PAC-Bayes bound exceeds threshold $\tau_{\text{brake}}$, explicitly severs the generative autopilot and shifts the agent into a halt-and-query state. This is not a prompt telling the model to "be safe" — it is a **structural, mathematical gate** that operates outside the model's token-generation loop.

---

## 4. The Complete Loop: ELBO → ACC → PAC-Bayes → TRN

The three components form a closed metacognitive loop:

```
Observation (x)
    ↓
[ELBO Perception]
    ├─ Reconstruction Accuracy → "Do I understand this?"
    ├─ KL Divergence → "Does this break my model?"
    └─ ELBO Score → Epistemic Gap signal
    ↓
[ACC Evaluation]
    ├─ Conflict Detection (entropy among agent proposals)
    ├─ FOK Check (topological resolution of memory paths)
    └─ Risk Score computation
    ↓
[PAC-Bayes Bound]
    ├─ Empirical risk + Complexity penalty
    ├─ Evidence weight adjustment
    └─ True risk bound vs. safety threshold
    ↓
[TRN Gate]
    ├─ PROCEED (bound < threshold)
    └─ EMERGENCY BRAKE (bound > threshold)
        ├─ Suspend agent loop
        ├─ Log mathematical justification
        └─ Escalate to human operator
```

**The key innovation**: ELBO monitors *perception* (is my model of reality accurate?), while PAC-Bayes monitors *action* (is my proposed response safe?). Together, they cover both directions of the epistemic gap — input and output.

---

## 5. The Portfolio-of-Policies MDP: Allocating Cognitive Resources

### The Problem

Real agents don't just decide *whether* to act — they decide *how much cognitive resource* to allocate to each of multiple simultaneous tasks. This is the portfolio allocation problem.

### State Space

$$s_t = (\mathbf{z}_t, \mathbf{c}_t, \mathbf{h}_t, \Delta\mu_t)$$

Where:
- $\mathbf{z}_t = (z_1, \ldots, z_K)$ — resource allocation across $K$ policy threads
- $\mathbf{c}_t = (c_1, \ldots, c_K)$ — confidence per thread
- $\mathbf{h}_t = (h_1, \ldots, h_K)$ — entropy state per thread
- $\Delta\mu_t$ — global value-mode separation

### The Entropy-Confidence Duality

The portfolio framework reveals a deep duality:

$$\text{SNR}_{\text{confidence}} = \frac{\mathbb{E}[|\Delta\mu|]}{\sqrt{\text{Var}[|\Delta\mu|]}} \quad \longleftrightarrow \quad \text{SNR}_{\text{entropy}} = \frac{1}{H(\mathbf{p})}$$

Both are optimizing **signal-to-noise ratio** — confidence from the top down, entropy from the bottom up. At equilibrium:

$$\frac{\partial P_c}{\partial z} \cdot \frac{\partial H}{\partial z} < 0$$

As confidence increases with resource investment, entropy decreases. This is a fundamental trade-off, not a design choice.

### Dynamic Entropy-Cost Adjustment

The cost function becomes entropy-state-dependent:

$$C(z, H) = \alpha \cdot z^{\nu_0 + \gamma \cdot H}$$

When system entropy is high (disordered, high noise), the effective cost exponent $\nu$ increases, making marginal effort more expensive. This captures the intuition that it's harder to make progress in chaotic regimes — and automatically throttles resource allocation when the system is confused.

### Control Graph Topologies

Three architectures for implementing the entropy-confidence loop:

| Topology | Loop Speed | Interpretability | Stability | Best For |
|---|---|---|---|---|
| Strict Hierarchy | Slow (3+ hops) | High | High | Deliberative, safety-critical |
| Small-World | Fast (1 hop) | Low | Low (oscillation risk) | Rapid adaptation, exploration |
| **Layered + Shortcuts** | **Fast (1 hop)** | **Medium** | **Medium-High** | **Production systems** |

The recommended architecture — **Layered with Shortcuts** — mirrors prefrontal cortex → basal ganglia circuits with direct amygdala → cortex shortcuts for fast emotional responses. The oMCD resource allocation $\mathbf{z}$ serves as the universal currency flowing along edges.

---

## 6. The Knowledge Management Substrate

The metacognitive loop operates over a knowledge substrate. Without organized memory, the ELBO has nothing to reconstruct against and the PAC-Bayes bound has no prior to diverge from.

### The Layered Architecture

```
L1: Working Memory (context window, ≤2.2k chars pointer layer)
    ↓
L2: Markovian Carryover (≤512 tokens, Established/Open/Heading)
    ↓
L3: Operational Anchors (skills, pitfalls, recovery procedures)
    ↓
L4: Knowledge Graph (Neo4j, typed relationships, multi-hop reasoning)
    ↓
L5: Vector Index (ChromaDB, embedding-based similarity)
    ↓
L6: Raw Store (wiki pages, scratchpad, git history)
```

### PARA as Organizational Principle

The PARA methodology (Projects, Areas, Resources, Archives) provides the macro-structure:

- **Projects**: Active goals with defined outcomes → map to active policy threads in the portfolio MDP
- **Areas**: Ongoing responsibilities → map to persistent agent roles
- **Resources**: Topics of interest → map to knowledge graph clusters
- **Archives**: Inactive items → map to compressed LCM summaries

The key insight: **knowledge entropy is managed through intentional dormancy**. Archives stabilize the active knowledge surface by removing stale information from the working set.

### The Knowledge Graph as Bayesian Prior (with caveats)

The knowledge graph (L4) can serve as the **prior $P$** in the PAC-Bayes bound — but only after choosing a probability measure over it. A knowledge graph is a deterministic structure (nodes + edges), not a probability distribution. To compute $\text{KL}(Q\|P)$, we must first define what $P$ means as a distribution.

**Options for defining $P$:**

| Measure | Definition | Properties |
|---|---|---|
| Random-walk stationary | Long-run probability of visiting each node during a random walk | Captures graph topology; dominated by high-degree nodes |
| MCMC stationary | Stationary distribution of a Metropolis-Hastings chain over the graph | Well-defined; proposal distribution must be chosen |
| Degree-weighted | Edge weight proportional to node degree | Simple; ignores semantic content |
| Uniform | Equal probability over all nodes | Uninformative; equivalent to no prior |

The most coherent choice is the **MCMC stationary distribution** (§7): if we run Metropolis-Hastings over the knowledge graph with an appropriate proposal distribution, the stationary distribution gives us a well-defined prior $P$. The KL divergence then measures how far the agent's proposed action diverges from the regions of the graph where the chain spends most of its time — i.e., the well-mapped, frequently-traversed regions.

**Consequence:** The safety brake's behavior is dominated by the choice of proposal distribution and graph weighting. These are engineering decisions, not derived quantities. Different proposal distributions produce different priors, which produce different KL divergences, which produce different halt decisions. This is not a bug — it's a design parameter that must be tuned and validated.

---

## 7. The MCMC Inference Engine: Metropolis-Hastings Over Knowledge

### The Problem

Given a knowledge graph with probabilistic relationships, how do we answer queries like "what is the probability that approach X will succeed given evidence Y?" This requires computing posterior distributions over the graph — which is intractable for all but the simplest topologies.

### Metropolis-Hastings

The Metropolis-Hastings algorithm constructs a Markov chain whose stationary distribution matches the target posterior:

1. **Proposal**: From current state $x_n$, generate candidate $x^* \sim q(x^*|x_n)$
2. **Accept/Reject**: $A = \min(1, \frac{g(x^*)}{g(x_n)})$ — accept if better, otherwise accept with probability proportional to improvement ratio
3. **Iterate**: After burn-in, samples are drawn from the target distribution

**Key property**: Only relative probabilities $g(x^*)/g(x_n)$ are needed — the normalizing constant cancels. This is critical for knowledge graphs where the partition function is intractable.

### Connection to the Metacognitive Loop

MCMC serves as the **inference engine** that connects the knowledge graph to the ELBO/PAC-Bayes components:

- **ELBO reconstruction**: MCMC samples from the posterior over memory states $z$ to find the best reconstruction of observation $x$
- **PAC-Bayes prior**: MCMC stationary distribution over the knowledge graph provides the well-defined prior $P$
- **Portfolio MDP**: MCMC samples from the posterior over resource allocations $\mathbf{z}$ to find the optimal portfolio
- **Entropy monitoring**: The MCMC acceptance rate is *related* to system entropy — low acceptance often means the chain is struggling to find high-probability regions

**Confound to control for:** Low MH acceptance can mean the world is confusing (high entropy = genuine epistemic gap), **or** it can mean the proposal distribution is badly scaled (sampler tuning problem = false alarm). A mistuned sampler would trigger the TRN gate constantly — the agent halts because of its own plumbing, not its epistemic state.

**Fix:** Use adaptive MH targeting ~0.234 acceptance (the known optimal rate for random-walk proposals). Treat *deviation from target after adaptation* as the signal, not raw acceptance rate. A well-tuned sampler with persistently low acceptance indicates a genuinely rough landscape. A mistuned sampler that converges to the target after adaptation was just poorly initialized.

The inference engine and the metacognitive monitor are the same mathematical object **only after controlling for sampler quality**. Without that control, you measure your plumbing, not your knowledge.

---

## 8. The Unified Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    OBSERVATION (x)                          │
│                                                             │
│  "What is the agent perceiving from its environment?"       │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              ELBO PERCEPTION LAYER                          │
│                                                             │
│  log p(x) ≥ E_q[log p(x|z)] - KL(q(z|x) ‖ p(z))         │
│                                                             │
│  ├─ Reconstruction: Does internal model match observation?  │
│  ├─ KL Divergence: Must priors be radically revised?        │
│  └─ Output: Epistemic Gap signal                            │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              KNOWLEDGE SUBSTRATE                            │
│                                                             │
│  L1: Pointers → L2: Carryover → L3: Skills                │
│  L4: Knowledge Graph (Neo4j) ← MCMC Inference              │
│  L5: Vector Index (ChromaDB)                                │
│  L6: Raw Store (wiki, scratchpad, git)                      │
│                                                             │
│  PARA: Projects / Areas / Resources / Archives              │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              ACC EVALUATION LAYER                           │
│                                                             │
│  ├─ Conflict Detection: Entropy among agent proposals       │
│  ├─ FOK Check: Topological resolution of memory paths      │
│  ├─ MCMC Acceptance Rate: Is inference chain healthy?       │
│  └─ Output: Risk Score + Epistemic Gap                      │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              PAC-BAYES ACTION LAYER                         │
│                                                             │
│  R(Q) ≤ R̂(Q) + √[(KL(Q‖P) + log(1/δ)) / (2n)]           │
│                                                             │
│  ├─ Empirical risk of proposed action                       │
│  ├─ Divergence from knowledge graph prior                   │
│  ├─ Evidence weight adjustment                              │
│  └─ Output: True Risk Bound                                 │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              TRN GATE (Emergency Brake)                     │
│                                                             │
│  if Risk Score > τ_brake:                                   │
│    → HALT: Suspend agent, escalate to human                │
│  else:                                                      │
│    → PROCEED: Enable action execution                       │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              PORTFOLIO MDP (Resource Allocation)            │
│                                                             │
│  max_z Σᵢ [Bᵢ(zᵢ) - Cᵢ(zᵢ)]  s.t. Σᵢ zᵢ ≤ Z_max         │
│                                                             │
│  ├─ Allocate resources across K policy threads              │
│  ├─ Entropy-dependent cost: C(z,H) = α·z^(ν₀+γ·H)        │
│  ├─ Layered+Shortcuts control graph topology                │
│  └─ Output: Optimal resource allocation z*                  │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              ACTION + MEMORY UPDATE                         │
│                                                             │
│  ├─ Execute action (or halt)                                │
│  ├─ Update knowledge graph with new evidence                │
│  ├─ Update carryover with Established/Open/Heading          │
│  ├─ Update skills with new operational anchors              │
│  └─ Feed next observation back to ELBO                      │
└─────────────────────────────────────────────────────────────┘
```

---

## 9. Open Problems

### 9.1 The ELBO-PAC-Bayes Bridge

The current architecture treats ELBO (perception) and PAC-Bayes (action) as separate layers. But they share the same KL divergence term — the epistemic gap. Can we derive a **single bound** that connects perceptual uncertainty directly to action risk, bypassing the intermediate ACC layer? The Free Energy Principle suggests this is possible: if the ELBO is the variational free energy, then its gradient with respect to action is exactly the expected risk gradient.

### 9.2 MCMC as the Inference Backbone

Currently, MCMC is positioned as one component among several. But if the knowledge graph is the prior $P$, and the ELBO computes the posterior $q(z|x)$, then **MCMC is the algorithm that connects them**. This suggests a deeper architecture where every metacognitive computation — perception, evaluation, action selection — is implemented as MCMC sampling over the appropriate posterior. The acceptance rate becomes a universal metacognitive signal.

### 9.3 The Portfolio MDP on a Knowledge Graph

The portfolio MDP assumes independent threads. But in a knowledge graph, threads share nodes and edges — they are **graph-coupled**. The research document identifies this as an open problem: how to formalize coupling in the portfolio Q-function. One approach: factor the Q-function over the graph structure, with edge potentials encoding inter-thread dependencies.

### 9.4 Biological Plausibility of the Layered+Shortcuts Architecture

The research document notes that the Layered+Shortcuts topology mirrors prefrontal cortex → basal ganglia circuits with direct amygdala → cortex shortcuts. But the analogy has not been formalized. What is the exact correspondence between oMCD's $\mathbf{z}$ allocation and dopaminergic reward prediction errors? If the analogy holds, it would provide a **neuroscientific validation** of the control graph design.

### 9.5 Scaling the Architecture

The current design has been validated for small swarms (5-10 agents). Scaling to hundreds or thousands of agents introduces:
- **Knowledge graph complexity**: MCMC mixing time grows with graph size
- **Portfolio dimensionality**: The $\mathbf{z}$ allocation space grows exponentially with thread count
- **ELBO computation**: Variational inference over large knowledge graphs is expensive

Approximate inference methods (stochastic MCMC, amortized variational inference, graph partitioning) are needed.

---

## 10. Honest Citations

**Note on scope:** The mathematical components (ELBO, PAC-Bayes, Metropolis-Hastings, Friston) are classical and well-established. They do not need the agent-specific papers to be valid. The agent papers contribute *specific instantiations*, not foundational math.

| Component | Classical Foundation | Agent Instantiation (if any) |
|---|---|---|
| ELBO Perception | Friston (Free Energy Principle, 2010) | Gemini conversation (integrating ELBO into ACC monitor) |
| PAC-Bayes Action | McAllester (1999), Catoni (2007) | Gemini conversation (integrating PAC-Bayes into ACC monitor) |
| Entropy-Confidence Duality | Information theory (Shannon, 1948) | Portfolio-of-Policies MDP document (independent derivation) |
| Knowledge Management | PARA (Forte), Zettelkasten (Luhmann) | knowledge-management.md concept page |
| MCMC Inference | Metropolis et al. (1953), Hastings (1970) | Navarro (2023) tutorial |
| Dual-Process Memory | Kahneman (2011), cognitive psychology | DCPM (2606.09483) — cognitive hierarchy for agents |
| Observability | Mishra & Sharad (2606.09692) — the only agent-specific paper here |
| Skill Economics | Xing et al. (2606.09421) — operational anchors, quality-cost trade-offs |
| Representation Learning | Buchanan et al. (2606.06624) — deep representation learning as memory |

---

## 11. What to Build First: The Embarrassing Baseline

Before building the 8-week cathedral, establish whether the fancy math beats a calibrated threshold over three cheap features. If it can't, the math is decoration on a threshold.

### The Baseline Gate

```python
def should_halt(observation, retrieval_results, k_sampled_answers):
    """
    Three-feature risk score. Calibrate on historical data.
    Features are proxies for the ELBO/PAC-Bayes terms but are computable
    without a generative model.
    """
    # 1. Token-logprob entropy (proxy for ELBO reconstruction term)
    #    High entropy in the LLM's own output = the model is uncertain
    logprob_entropy = compute_logprob_entropy(observation.response_tokens)
    
    # 2. Retrieval miss rate (proxy for PAC-Bayes KL divergence)
    #    Can the knowledge graph answer the question?
    retrieval_score = retrieval_results.top_k_similarity(observation.query)
    retrieval_miss = 1.0 - retrieval_score
    
    # 3. Self-consistency disagreement (proxy for ELBO KL / paradigm shift)
    #    Do k sampled answers agree? High disagreement = epistemic gap
    answer_agreement = pairwise_agreement(k_sampled_answers)
    consistency_gap = 1.0 - answer_agreement
    
    # Calibrated risk score (logistic regression over historical data)
    risk = sigmoid(beta_0 + beta_1*logprob_entropy + beta_2*retrieval_miss + beta_3*consistency_gap)
    
    return risk > tau, risk
```

**Calibration data:** The wiki-overseer runs 27 completed cycles. Label each cycle's risk score against whether the overseer made an error or missed something that a better system would have caught. That's your ground truth for $\tau$ and $\beta$.

**Phase 4 metrics are the only numbers that matter:**
- **Halt precision:** Of the times the gate fires, how many were genuine errors?
- **Halt recall:** Of the actual errors, how many did the gate catch?
- **Unnecessary halt rate:** How often does the gate fire when the agent would have been fine?

### Retrofit onto Existing Infrastructure

You've partially built this already:
- **RAA's entropy-triggered associative search** *is* the ACC layer — it detects when retrieval confidence drops and triggers associative search
- **cognitive-workspace-db** *is* L4/L5 — the knowledge graph + vector index substrate
- **The wiki-overseer's preflight.py** *is* the evaluation layer — it reads ground truth and computes risk scores

Retrofitting the gate onto RAA gets you to Phase 4's measurements faster than a greenfield implementation. The measurement is the part that distinguishes a research result from a beautiful diagram.

### When to Add Complexity

Only add the full ELBO/PAC-Bayes/MCMC machinery if:
1. The baseline gate's halt precision/recall is below threshold (say, 80%)
2. The errors the baseline misses are the *expensive* ones (wrong wiki edits, bad delegation decisions)
3. The extra computation cost is justified by the error reduction

If the baseline catches 95% of errors at 5% false-positive rate, the fancy math is a research exercise, not an engineering requirement.

---

## 12. References

- Buchanan, S., Pai, D., Wang, P., & Ma, Y. (2026). *Principles and Practice of Deep Representation Learning: or a Mathematical Theory of Memory*. arXiv 2606.06624.
- Fei, T., Song, M., Zheng, M., & Yu, X. (2026). *Memory Beyond Recall: A Dual-Process Cognitive Memory System for Self-Evolving LLM Agents*. arXiv 2606.09483.
- Xing, Q., Chen, Y., Jin, Y., Wu, Z., & Lin, B. (2026). *What Should a Skill Remember? Quality-Cost Trade-offs in Cost-Aware Skill Rewriting*. arXiv 2606.09421.
- Mishra, S., & Sharad, M. (2026). *Observability for Delegated Execution in Agentic AI Systems*. arXiv 2606.09692.
- Zhou, C., et al. (2026). *Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering*. arXiv 2604.08224.
- Navarro, D. (2023). *The Metropolis-Hastings Algorithm*. blog.djnavarro.net.
- Friston, K. (2010). *The Free-Energy Principle: A Unified Brain Theory?* Nature Reviews Neuroscience.
- McAllester, D. A. (1999). *PAC-Bayesian Model Averaging*. COLT.
- Catoni, O. (2007). *PAC-Bayesian Supervised Classification: The Thermodynamics of Statistical Learning*. IMS Lecture Notes.
