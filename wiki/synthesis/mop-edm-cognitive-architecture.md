---
summary: Synthesis: MOP as EFHF Layer 0 + EDM disruption measurement — formally verified structural mapping (Prover9), three implementation levels, KL regularization critique, hallucination as lumpability failure, coherent complexity growth
tags: [MOP, EDM, EFHF, cognitive-architecture, entropy, hallucination-detection, epistemic-energy, absorbing-states, RLHF, attention, synthesis, intrinsic-motivation, ethics, KL-divergence, mcp-logic, computational-mechanics, lumpability, Kernel-1, Kernel-2]
updated: 2026-04-14T04:11:54Z
---

# MOP-EDM Cognitive Architecture

**Type:** Synthesis — original cross-domain design
**Origin:** Ty (2026-04-13), building on [[maximum-occupancy-principle]], [[edm-framework]], [[causal-state-edm-ood-isomorphism]], [[efhf]]
**Confidence:** 0.80 — conceptual framework grounded in formal results; KL insight confirmed by MOP paper; AbsorbingState→Kernel2Transition proved (Prover9); EFHF integration at WEAK closure status

---

## The Core Claim

MOP provides a principled *motivation* for how AI models should navigate reasoning space. EDM provides a principled *measurement* of where the model is in that space relative to known territory. EFHF provides the *verification and consistency enforcement* backbone. Together they define a cognitive architecture where models maintain exploratory diversity by default, become goal-directed when constrained, detect their own hallucinations via disruption signals, and avoid epistemic dead-ends without explicit reward engineering.

---

## EFHF Integration: MOP as Layer 0

The [[efhf]] is a five-layer AI architecture implementing computational mechanics concepts as a live multi-agent system. MOP fills a specific gap: EFHF is reactive (responds to user prompts); MOP makes it proactive (generates exploration targets autonomously).

### Formally Verified Structural Mapping

**Theorem (Prover9, 0.00s):** `∀x (AbsorbingState(x) → Kernel2Transition(x))`

Given the premises:
1. All absorbing states have zero future entropy
2. Zero future computation ↔ Kernel 2 transition
3. Zero future entropy ↔ zero future computation

MOP absorbing states are structurally equivalent to EFHF Kernel 2 transitions. This is not metaphorical — it is a formally proved logical entailment.

### Full Layer Mapping

| EFHF Layer | MOP Analog | Tool |
|---|---|---|
| **L0 (NEW)** | MOP Orchestrator — intrinsic motivation, action selection | MOP softmax policy |
| L1 | Hypothesis generation from MOP's exploration target | LLM |
| L2 | World model encoding of hypotheses | hipai-montague |
| L3 | Structural verification — absorbing state detection | mcp-logic |
| L4 | Confidence tracking, coherence window monitoring | advanced-reasoning |
| L5 | Kernel 1 persistence enforcement | sheaf-consistency-enforcer |
| L5+ | Ethical triage — deontological absorbing states | conscience-servitor |

### Hallucination as Lumpability Failure

EFHF defines hallucination as lumpability failure — the model's macro-level predictions no longer commute with micro-level reality. MOP defines hallucination as uncontrolled high-Δ disruption — the model enters novel territory without a viable path back to grounded reasoning. EDM measures this as cosine distance between past and future vectors spiking without a grounded explanation.

These three descriptions are the *same phenomenon* viewed from different theoretical angles:
- **EFHF:** The macro-automaton's transition kernel diverges from the micro-automaton → lumpability breaks
- **MOP:** The agent enters high state entropy territory near an absorbing state without energy to return → Kernel 2 imminent
- **EDM:** Past vector and future vector diverge beyond the field's established causal states → OOD event

The sheaf-consistency-enforcer detects this via coboundary norms: when what mcp-logic has verified diverges from what hipai-montague believes, the edge residual rises, dual pressure accumulates, and the closure status degrades from KERNEL1 toward WARNING/TIMEOUT.

---

## The Physical-to-Cognitive Mapping

| Physical MOP | Cognitive MOP | EFHF Implementation |
|---|---|---|
| Physical state (x, y, energy) | Epistemic state (understanding, hypotheses, confidence) | hipai-montague world model |
| Physical actions (move L/R) | Cognitive actions (query, hypothesize, verify, synthesize) | MCP tool calls |
| Energy reservoir | Epistemic energy E (coherence reserves) | Buffering capacity T |
| Food sources | Information retrieval (wiki, Synapse) | query_knowledge, wiki_read_page |
| Absorbing states (death) | Contradiction, coherence collapse, ethical violation | mcp-logic + conscience-servitor |
| α (action entropy) | Strategy diversity | Number of distinct MCP tool types used |
| β (state entropy) | Novelty preference | EDM disruption score Δ |
| γ (discount factor) | Cognitive time horizon | Coherence window τ |

**The critical constraint:** Without energy depletion and absorbing states, MOP produces a random walk. *With* these constraints, goal-directed behavior emerges. The EFHF verification stack (L3-L5) provides the absorbing state detection that makes MOP's exploration controlled rather than chaotic.

---

## The EDM Connection

EDM's past/future vector framework provides the measurement layer MOP needs in cognitive space.

### Disruption as the β-Signal

- **Low Δ (consolidating):** Reasoning follows established patterns. Low state entropy. Safe but uninteresting.
- **High Δ (disruptive):** Reasoning diverges from context predictions. Potentially insightful OR hallucinating.
- **The difference:** Under MOP, disruption is *controlled* — entropy maximized while avoiding absorbing states. Hallucination is *uncontrolled* — high-Δ with no viable return path. The EFHF L3-L5 stack distinguishes these.

### Coherent Complexity Growth

MOP agents seeking high β hunt for state-splitting events in the conceptual epsilon machine. Each genuine high-Δ discovery increases the statistical complexity (excess entropy) of the world model. Absorbing states ensure this growth is coherent. MOP selects for *coherent* complexity growth — richer understanding, not noise.

### Simultaneous Discovery Detection

If two different reasoning paths converge on the same conceptual territory (similar future vectors despite different past vectors), this indicates a convergent insight or a systematic confabulation. EDM's simultaneous discovery finding provides the detection method.

---

## The KL Regularization Problem (Key Training Insight)

The MOP paper proves (Supplemental Sec. F) that KL-regularization with a uniform default policy is self-defeating for occupancy maximization. The immediate return becomes $\mathcal{H}(A|s) - \ln|A(s)|$ — the negative logarithm *penalizes* states with many available actions.

**Direct implication for RLHF:** The standard objective $\max_\pi \mathbb{E}[R(x)] - \beta_{KL} D_{KL}(\pi || \pi_{ref})$ actively suppresses behavioral diversity. RLHF-trained models collapse toward deterministic responses partly because the KL regularizer penalizes occupying states where many response strategies are available.

**MOP alternative:** Use absolute entropy as the primary signal. Define absorbing states as constraints. Produce models that are *optimally stochastic* — diverse by default, precise near absorbing boundaries. The absorbing states replace the KL tether: "don't enter states from which no coherent continuation is possible" replaces "don't stray from the reference model."

---

## Three Implementation Levels

### Level 1: Inference-Time MOP (Most Practical)

MOP optimal policy guides reasoning-step decisions. Epistemic energy tracking monitors coherence. EFHF L3-L5 provides absorbing state detection. No retraining required.

### Level 2: Training-Time MOP (Fundamental Change)

Replace RLHF's KL-regularized reward maximization with absolute entropy path maximization + designed absorbing states. Constitutional AI via absorbing states: define unconditional prohibitions, let virtue emerge from the α/β-balanced dynamics.

### Level 3: Attention-Level MOP (Most Speculative)

Attention distribution incorporates entropy-maximizing component. Past/future decomposition of hidden states enables per-layer, per-head disruption monitoring — attention-level EDM.

---

## Formal Verification via EFHF Stack

### mcp-logic (L3)
- `find_model(premises)` → consistency check → absorbing state detection
- `find_counterexample(premises, conclusion)` → hypothesis validation (β-filter)
- `abductive_explain(observation, candidates)` → best explanation for surprising findings

### sheaf-consistency-enforcer (L5)
- Coboundary norms between agents measure consistency
- Closure status (KERNEL1/WEAK/WARNING/TIMEOUT) gates commits
- H¹ obstruction detection catches cyclic contradictions

### conscience-servitor (L5+)
- Pre-screens all exploration targets for ethical risk
- Deontological absorbing states enforced before exploration begins

**Absorbing states are design-defined, not learned.** If the neural component learns to define epistemic dead-ends, it will hallucinate bridges across contradictions to keep exploring.

---

## Connection to the Ethical Framework

| Ethical Layer | MOP Analog | EFHF Layer |
|---|---|---|
| **Deontology** (harm = harm) | Absorbing states | L5+ conscience-servitor triage |
| **Virtue** (wisdom, integrity, fairness) | α/β-balanced optimal policy | L4 advanced-reasoning |
| **Utilitarianism as servant** | Rewards serve entropy, not the reverse | L0 MOP orchestrator |

MOP formally proves: when utility serves entropy (possibility), agents survive, explore, cooperate, and adapt. When utility is the master (reward maximization), agents park at food sources and lose behavioral diversity.

---

## Open Questions

1. **What internal representations serve as past/future vectors?** KV cache? Final hidden states? Attention patterns?
2. **How to define epistemic energy concretely?** Context utilization? Perplexity? Attention entropy?
3. ~~Can absorbing state detection be learned?~~ **No.** Design-defined via mcp-logic and conscience-servitor.
4. **Does MOP training produce more diverse outputs?** Empirical validation needed on language tasks.
5. ~~Path entropy ↔ excess entropy?~~ **Partially answered.** MOP β-seeking = state-splitting = complexity growth. Full formal proof remains open.
6. **Adaptive α/β?** High β for brainstorming, low β for fact-checking. Task-dependent tuning.
7. **KL insight empirical validation?** Compare RLHF (KL-regularized) vs MOP (absolute entropy + absorbing states) trained models.

---

## Connections

- [[maximum-occupancy-principle]] — foundational theory
- [[ramirez-ruiz-mop-2024]] — source paper
- [[efhf]] — the five-layer architecture MOP integrates with as Layer 0
- [[edm-framework]] — disruption measurement providing the Δ signal
- [[causal-state-edm-ood-isomorphism]] — epsilon machine bridge; state-splitting as coherent complexity growth
- [[zettelkasten-engine]] — insight generation using MOP-guided exploration
- [[project-synapse]] — MCP infrastructure for epistemic energy replenishment
- [[persistent-knowledge-compilation]] — MOP predicts stochastic access patterns over deterministic retrieval
- [[prd-ralph-loop-mop-gemini]] — Gemini conversation initiating the cognitive MOP framing
