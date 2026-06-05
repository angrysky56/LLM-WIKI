---
summary: LMAC uses an LLM as a protocol designer for cooperative multi-agent RL — iteratively refining agent-wise communication schemas via a state-awareness criterion (SAI) that measures per-dimension reconstruction accuracy and inter-agent knowledge imbalance
tags: [paper, arxiv, multi-agent-rl, communication-protocols, llm, cooperative-learning, state-awareness, reflexive-refinement, ctde, sheaf-consistency, efhf-relevance]
sources: https://arxiv.org/abs/2605.18077
confidence: 0.95
---

# LLM-Guided Communication for Cooperative Multi-Agent Reinforcement Learning

## Paper Info
- **Authors:** Sangjun Bae, Yisak Park, Sanghyeon Lee, Seungyul Han (UNIST)
- **arXiv:** 2605.18077v1 [cs.AI] — 2026-05-18
- **Venue:** ICML 2026, Seoul, South Korea
- **Categories:** cs.AI, cs.LG, cs.MA
- **Code:** https://saaangjun.github.io/LMAC/
- **Backbone:** QMIX (value decomposition), with VDN and QPLEX ablations

---

## Executive Summary

LMAC (LLM-driven Multi-Agent Communication) addresses a fundamental problem in cooperative MARL under partial observability: agents receive fragmented observations and must coordinate action without access to the global state. Prior communication methods either broadcast too much redundant information or transmit insufficient state signals. LMAC instead treats communication protocol design as an LLM reasoning task — the LLM receives natural-language descriptions of the task goal, state dimensions, and observation dimensions, then generates and iteratively refines an executable Python protocol that maps local observations to agent-specific messages. Refinement is driven by a two-step criterion: (1) **recovery enhancement** — improve per-dimension state reconstruction accuracy — and (2) **imbalance mitigation** — reduce inter-agent variance in reconstruction quality. The final protocol is integrated into CTDE training via a meta-cognitive encoder-decoder with cycle-consistency regularization. LMAC achieves new state-of-the-art on SMAC-Comm, SMACv2, LBF, and Google Research Football benchmarks.

---

## Technical Approach

### Problem Formalism

Modeled as a **Comm-Dec-POMDP** (Decentralized Partially Observable Markov Decision Process with Communication):
- **G** = ⟨S, A, P, R, O, O, I, n, γ, M⟩
- Agents have local observations `oit = Oi(st)` and action histories `τti`
- Communication messages `mit` are produced per-agent per-timestep and integrated into policies `πi(· | τti, mit)` and utilities `Qi(τti, mit, ait)`
- Training uses CTDE (Centralized Training, Decentralized Execution) — global state available during training, local observations at execution

### LLM-as-Protocol-Designer

The core innovation: instead of learning a communication protocol from scratch via gradient descent, the LLM reasons about what information each agent *needs* to reconstruct the global state.

**Input prompt x = (IT, IP):**
- **IT** (Task Description): natural-language description of the cooperative goal, global state space, and local observation space derived from environment documentation
- **IP** (Protocol Design Instruction): environment-agnostic design principles including uniqueness, sufficiency, compactness, and explicit output format requirements

The LLM outputs executable Python code implementing `communication(o)` — a vectorized function mapping the observation tensor to agent-specific messages. This avoids online LLM interaction at execution time; only the offline protocol design phase uses the LLM.

**Protocol refinement builds on Reflexion (Shinn et al., 2023)** with iteration-specific feedback:

| Step | k | Objective | Feedback content |
|------|---|-----------|-----------------|
| Init | 0 | Generate minimal, task-appropriate protocol | Task prompt only |
| Recovery Enhancement | 1 | Improve per-dimension reconstruction accuracy | SAI per-dimension recovery rates |
| Imbalance Mitigation | 2 | Reduce inter-agent reconstruction variance | SAI inter-agent variance |

### State-Awareness Criterion (SAI)

The quantitative backbone of refinement. An auxiliary decoder Dφ reconstructs global state from agent trajectories with (`l=1`) and without (`l=0`) the message:

```
ŝ^(i,1)_d,t = Dφ(τti, mit, i)_d     [with message]
ŝ^(i,0)_d,t = Dφ(τti, 0, i)_d       [without message]
```

The **State Awareness Indicator** is a per-dimension binary:
```
χ^(i,(k))_l,d,t = I[ |ŝ^(i,l)_d,t − s_d,t| ≤ α ]
```
where α is a reconstruction threshold. Two aggregate criteria are derived:

1. **Recovery success rate** `E_t[h_i χ^(i,(k))_1,d,t]`: fraction of timesteps where the message improves reconstruction — drives Step 1
2. **Knowledge imbalance** `Var_i[h_i χ^(i,(k))_1,d,t]`: inter-agent variance in reconstruction quality — drives Step 2

### Meta-Cognitive Representation Learning (Online Training)

The designed protocol `fC` generates messages `mit = fC(τt)` during MARL training. An encoder-decoder pair:
- **Encψ**: `zti = Encψ(τti, mit)` — produces latent representation
- **Decψ**: reconstructs global state `ŝt = Decψ(zti)` and predicts SAI `χ̂id,t`

Three training losses:
1. **Reconstruction loss**: minimizes `||ŝt − st||²` — state fidelity
2. **SAI loss**: predicts χid,t per training batch — distinguishes reliable knowledge from uncertainty
3. **Cycle-consistency loss**: `ẑti = Encc,ψ(Decψ(zti))` trained to reconstruct zti — penalizes redundant content, encourages compact task-relevant representations

The latent `zti` is fed into individual utilities `Qi(τti, zti)` and the joint Qtot via TD learning (QMIX backbone).

---

## Key Results

### Performance Gains
- **SMAC-Comm** (4 scenarios): LMAC converges faster and achieves higher final success rates than all baselines; approaches QMIX+State upper bound
- **SMACv2** (stochastic, randomized unit config): LMAC **surpasses QMIX+State** in all three race matchups (terran, protoss, zerg 5v5), suggesting LLM-designed protocols filter task-relevant features more effectively than raw global state under high stochasticity
- **LBF**: faster convergence, higher final performance
- **Google Research Football**: outperforms all baselines including QMIX+State; compact message representations avoid the dimensionality penalty of raw state provision

### Ablations (SMAC-Comm 1o_10b_vs_1r)
| Component | Win Rate |
|-----------|----------|
| k=0 (initial) | 68.5 ± 3.8 |
| k=1 (after recovery enhancement) | 77.8 ± 2.2 |
| k=2 (after imbalance mitigation, full) | **82.9 ± 1.9** |
| w/o cycle-consistency | 76.6 ± 5.6 |
| w/o SAI signal | 66.5 ± 2.1 |

Step-wise refinement yields ~14% absolute gain. Both cycle-consistency and SAI contribute substantially. All LLM variants (GPT-4.1, GPT-4.1-mini, o1-mini, Claude, Gemini) achieve competitive results; performance is driven by the refinement procedure, not the specific model.

### Trajectory-Level Analysis (1o_10b_vs_1r)
Three refinement stages:
1. **k=0**: Overseer broadcasts Roach relative offset (Δx, Δy) from itself — partial localization only
2. **k=1**: Feedback shows Overseer's own position is hard to infer; protocol adds Overseer relative position + recent history as localization cues
3. **k=2**: Variance-based feedback shows some Banelings can't disambiguate which teammates they observe; protocol adds fixed anchor coordinate centered on Overseer + explicit teammate IDs

Recovery success rate monotonically increases; knowledge imbalance monotonically decreases; win rate follows.

---

## Key Quotes

> *"To address this, we propose LLM-driven Multi-Agent Communication (LMAC), which leverages a large language model's reasoning capability to design a communication protocol that enables all agents to reconstruct the underlying state as accurately and uniformly as possible."*

> *"Efficient state reconstruction requires exchanging only the essential messages needed for recovery, yet identifying them is challenging because it demands understanding the task objective and the relationship between the state and observations."*

> *"Our method substantially reduces LLM usage cost, provides explicit criteria that target improved state recovery, and remains applicable to general multi-agent environments given task instructions."*

> *"We jointly train the encoder-decoder to reconstruct st and predict χid,t, encouraging a meta-cognitive representation that distinguishes reliable knowledge from uncertainty."*

---

## Structural Insights

### Why LLM-as-Designer Works Here

The key insight is that the LLM's world model (from pretraining) can infer *task-critical state dimensions* from natural-language descriptions without environment interaction. This sidesteps the need for online LLM usage at each timestep — the protocol design is done once offline. The LLM's ability to reason about which observation dimensions correlate with which state variables, and which agents have access to which information, enables it to propose minimal sufficient communication schemas that gradient-based methods must discover from scratch.

### The State-Awareness Criterion as Supervisory Signal

The SAI is not just for protocol design — it persists as a training signal. By predicting whether a given state dimension is recoverable, the encoder learns a representation that *separates reliable from unreliable knowledge*. This is analogous to a metacognitive uncertainty estimate: the agent learns not just what is true, but how confident it should be about each dimension of its reconstructed state.

### Compactness via Cycle Consistency

The cycle-consistency constraint (`Encc,ψ(Decψ(zti)) ≈ zti`) forces the latent to be decompressable back through the same encoder — information that cannot survive the encode-decode-encode round trip is discarded. This formalizes the intuition that messages should be *self-contained*: they should contain no more information than can be faithfully represented and transmitted.

---

## Relevance to EFHF / AGEM / MOP

### Connection to EFHF Architecture

| LMAC Component | EFHF Layer | Structural Analogy |
|----------------|-----------|-------------------|
| LLM protocol design (offline) | Layer 1 (LLM hypothesis generation) | LLM provides structural scaffold — both use world knowledge to propose a structure before gradient-based refinement |
| State-Awareness Criterion (SAI) | Layer 4 (meta-cognitive monitoring) | Both distinguish reliable from unreliable knowledge; both use a criterion signal to gate or weight downstream processing |
| Meta-cognitive encoder-decoder | Layer 2 (Montague world model) | Both reconstruct a distribution-independent world state; both use encoding/decoding to ensure representations are self-consistent |
| Cycle-consistency loss | Layer 5 (sheaf consistency enforcement) | Both enforce that information remains invariant through a round-trip transformation — sheaf consistency is the more general version |
| Protocol refinement (iterative feedback) | conscience-servitor (Layer 5+) | Both use multi-step reflective feedback to improve output quality; both are pre-response refinement stages |

### The State-Awareness / Sheaf Consistency Connection

The most structurally important connection: **LMAC's state-awareness criterion is a discrete, per-dimension version of sheaf consistency enforcement**.

In sheaf consistency, local assignments (observations, beliefs) must be *compatible* across overlapping regions — no local constraint should imply a contradiction when combined. LMAC's SAI tracks exactly this: when agent i can reconstruct state dimension d but agent j cannot, there is a *local inconsistency* in their knowledge states. The imbalance mitigation step (k=2) is the protocol-level analog of enforcing a sheaf condition: when a cover's sections disagree, the protocol adds bridging information to restore consistency.

Formally:
- **Sheaf consistency**: local-to-global constraint satisfaction across a cover
- **LMAC state-awareness**: inter-agent agreement constraint across observation-message pairs
- **LMAC imbalance**: the sheaf "patching" operation — adding missing sections to resolve inconsistency

### Connection to MOP

LMAC's communication protocol refinement is orthogonal to MOP but complementary for multi-agent settings:

- **MOP** (Layer 0): defines *which* state-space regions to explore — maximizes path entropy, avoids absorbing states
- **LMAC**: defines *how* agents communicate to recover shared state — minimizes state reconstruction error, maximizes coordination

In a combined EFHF+MOP+LMAC stack, MOP would generate exploration targets, EFHF would verify structural consistency (Layer 3-5), and LMAC would manage inter-agent state agreement during cooperative tasks. The SAI could serve as an additional intrinsic reward signal for MOP: agents with low reconstruction confidence (χ ≈ 0) are in "unknown state territory" — high MOP β/entropy value.

### Connection to AGEM

AGEM (Agent Group Evolving Molecular System) presumably manages multi-agent group dynamics. LMAC provides a protocol-level mechanism for AGEM: when AGEM agents need to coordinate, LMAC's protocol design ensures their communication is both *sufficient* (all critical state dimensions recoverable) and *non-redundant* (compact messages, no duplication). The SAI could inform AGEM's group coherence metrics.

---

## Limitations and Future Directions

1. **Offline LLM overhead**: Protocol refinement requires auxiliary decoder training + offline LLM calls; modest in practice but not negligible
2. **LLM capability dependence**: Protocol quality varies with LLM reasoning ability; ablations show robustness across models but GPT-4.1 leads
3. **Structured descriptions required**: Designed for environments with semantic state/observation descriptions; extension to visual inputs requires object-centric representation learning first
4. **Refinement saturation**: Performance saturates at k=2; two refinement steps appear sufficient for most tasks

---

## Connections
- [[sources/papers/bae-lmac-2026]]
- [[wiki/index]]
- [[bae-lmac-2026]]

- [[entities/projects/efhf]] — five-layer cognitive architecture; LMAC's metacognitive encoder maps to EFHF L2, SAI maps to L4, cycle-consistency maps to L5 sheaf enforcement
- [[concepts/maximum-occupancy-principle]] — complementary: MOP selects exploration targets, LMAC manages inter-agent state agreement
- [[sheaf-consistency-enforcer]] — the general case of LMAC's state-awareness criterion; SAI imbalance = discrete sheaf patching
- [[mcp-logic]] — structural verification layer could verify LMAC protocol properties formally
- [[project-synapse]] — knowledge graph could store and retrieve LMAC protocol variants per task type
- [[edm-framework]] — high disruption (state entropy) regions in EDM space may correlate with low SAI scores (agents cannot reconstruct novel states)
- [[ramirez-ruiz-mop-2024]] — source paper for MOP Layer 0 integration
