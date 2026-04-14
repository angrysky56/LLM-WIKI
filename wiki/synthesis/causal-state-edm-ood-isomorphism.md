---
summary: Epsilon machine causal states ↔ EDM citation vectors — disruptive papers as OOD state-splitting events; connected to MOP (β = state-splitting appetite) and EFHF (hallucination = lumpability failure)
tags: [computational-mechanics, epsilon-machine, EDM, OOD, citation-networks, disruption, hallucination-detection, synthesis, lumpability, simultaneous-discovery, MOP, EFHF]
updated: 2026-04-14T04:13:57Z
---

# Causal State Isomorphism: Epsilon Machines, EDM, and OOD Detection

**Type:** Synthesis
**Origin:** Ty (original cross-domain insight, 2026-04-10)
**Source paper:** [[edm-framework]] — Kim, Kojaku & Ahn, *Science Advances* 2026
**Confidence:** 0.88 — structural analogy confirmed by paper's formal derivation; LLM application section remains speculative

---

## The Core Claim

EDM's past/future citation vectors are a domain-specific instantiation of epsilon machine causal states. This isomorphism yields a rigorous information-theoretic definition of "disruptive" vs "consolidating" papers, and suggests a novel OOD detection method for LLMs.

---

## Background: Two Frameworks

### Epsilon Machines (Computational Mechanics)
An epsilon machine finds the minimal, optimal predictive model of a stochastic process by grouping all "pasts" that produce the **same conditional probability distribution over futures** into a single **causal state**.

- **Lumpability**: A system is lumpable when its history maps cleanly onto a small set of causal states — the past predicts the future efficiently.
- **State splitting**: When an observation breaks the existing state structure (a past no longer predicts the expected future), the machine must mint a new causal state.

### EDM (Embedding Disruptiveness Measure)
Directional skip-gram trained on citation networks. The disruption score $\Delta_i = 1 - (f_i \cdot p_i)/(|f_i||p_i|)$ formally approximates the **lack of reliance of descendants on antecedents** — how much the citation trajectory has been redirected.

---

## The Isomorphism (Confirmed by Paper's Derivation)

| Epsilon Machine | EDM / Citation Network |
|---|---|
| Causal state | Research trajectory cluster |
| Lumpable history | Consolidating paper — low Δ |
| State-splitting event | Disruptive paper — high Δ |
| Conditional distribution over futures | Future vector $f_i$ |
| OOD observation | Large cosine gap between $p_i$ and $f_i$ |

A consolidating paper is in-distribution with respect to the field's current epsilon machine. A disruptive paper is an OOD event that forces state-splitting.

---

## Three Categories of Discovery

- **Consolidating** (low Δ): fits existing causal state
- **Disruptive** (high Δ): creates new causal state
- **Convergent** (simultaneous discovery): multiple paths to same new causal state — identical future vectors despite different past vectors

---

## Connection to MOP and EFHF

This synthesis is the theoretical bridge connecting three frameworks:

**MOP's β parameter = state-splitting appetite.** When a [[maximum-occupancy-principle]] agent seeks high state entropy (β), it intentionally hunts for state-splitting events — discoveries that force the conceptual epsilon machine to grow. Each genuine high-Δ event increases the statistical complexity (excess entropy) of the world model. MOP selects for *coherent* complexity growth because absorbing states (contradictions) are terminal. See [[mop-edm-cognitive-architecture]] for the full synthesis.

**EFHF's lumpability = controlled disruption.** The [[efhf]] architecture defines hallucination as lumpability failure — the model's macro-level predictions no longer commute with micro-level reality. This is the *same phenomenon* as uncontrolled high-Δ disruption in EDM terms, and as entering absorbing state territory without energy to return in MOP terms. The sheaf-consistency-enforcer detects this via coboundary norms between agents.

**Formally verified (Prover9):** MOP absorbing states → EFHF Kernel 2 transitions → zero future entropy → zero future causal states. The chain is logically proved.

---

## Implication: LLM OOD Detection (Speculative)

Apply past/future vector framework to LLM generation for real-time hallucination detection:
- **Past vector** ≈ context representation
- **Future vector** ≈ generation trajectory representation
- **Disruption signal** = cosine distance per step

Spike without grounded return path = hallucination (uncontrolled disruption). The EFHF L3-L5 stack (mcp-logic → sheaf-enforcer) provides the formal verification to distinguish controlled exploration from hallucinated leaps.

**Simultaneous hallucination fingerprint:** If two different prompts produce the same confabulation with similar future vectors, this identifies systematic confabulation patterns distinct from random noise.

---

## Zettelkasten Curation Signal

Within [[project-synapse]]'s [[zettelkasten-engine]]:
- **Low Δ** → consolidating, potentially redundant → deprioritize
- **High Δ** → disruptive insight, new causal state → flag for attention
- **Convergent future vectors** → simultaneous discovery pattern → merge or link
- **MOP guides which regions to explore next** → prefer high-entropy graph neighborhoods

---

## Open Questions (Updated)

1. ~~Can the disruption score be grounded in computational mechanics?~~ **Partially answered.** Cross-log-probability interpretation confirmed. Full connection to excess entropy remains open.
2. Is cosine distance monotonically related to state-splitting cost? (Requires constructing explicit epsilon machine for a subgraph.)
3. For LLMs: which internal representation serves as past/future vector? KV cache? Hidden state? Attention?
4. Can convergent future vectors identify systematic LLM confabulation patterns?
5. ~~Path entropy ↔ excess entropy?~~ **Partially answered via MOP connection:** β-seeking = state-splitting = complexity growth. See [[mop-edm-cognitive-architecture]].
6. Does independent wiki synthesis page convergence indicate a "ripe" concept worth a dedicated page?

---

## Connections

- [[edm-framework]] — source paper; formal math and empirical results
- [[maximum-occupancy-principle]] — MOP's β = state-splitting appetite; absorbing states = Kernel 2
- [[efhf]] — lumpability framework; hallucination as lumpability failure
- [[mop-edm-cognitive-architecture]] — full synthesis connecting all three frameworks
- [[zettelkasten-engine]] — disruption/convergence as curation heuristics
- [[persistent-knowledge-compilation]] — disruptive papers break pre-compiled knowledge bases
- [[graphrag]] — citation graphs as directly applicable domain
- [[rag]] — consolidating papers are ID w.r.t. RAG index; disruptive ones cause retrieval failure
