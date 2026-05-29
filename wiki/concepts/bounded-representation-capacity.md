---
summary: Bounded representation capacity: finite representational resources must be allocated strategically; appears in knowledge boundary probing, orthogonal bottleneck compression, skill banks, SAE features, temporal indexing, gating networks, and safety gating
tags: [concept, representation-learning, capacity-allocation, rl, agentic-ai]
updated: 2026-05-27T07:26:53Z
created: 2026-05-27T07:26:53Z
---

# Bounded Representation Capacity

## Definition

**Bounded representation capacity** is the principle that any intelligent system's representational resources are finite and must be allocated strategically across competing demands. No system — whether neural, symbolic, or hybrid — has unlimited capacity to encode knowledge, skills, behaviors, or environmental structure. This finiteness forces every system to make implicit allocation decisions: what to compress internally, what to externalize, what to route to tools, what to drop.

The concept is distinct from [bounded rationality](wiki/concepts/bounded-rationality.md) (cognitive limitations in decision-making) and [bounded memory budget optimization](wiki/concepts/bounded-memory-budget-optimization.md) (token-window constraints). It concerns the representational substrate itself — the geometry of what gets encoded and how.

## Core Principle

When representation capacity is bounded, three regimes determine behavior:

| Regime | Description | Consequence |
|--------|-------------|-------------|
| **Within capacity** | Task fits in available representational resources | Optimal performance achievable |
| **Capacity spill** | Task exceeds available resources | Degradation, compression, or externalization required |
| **Capacity waste** | Resources exceed task requirements | Inefficiency; allocated capacity is not fully utilized |

The fundamental engineering question is not *how much* capacity to add, but *how to allocate* a fixed or growing-but-bounded capacity across tasks that compete for the same representational substrate.

## How It Appears Across Papers

### Knowledge Boundary Probing (AKBE)

[AKBE](wiki/sources/papers/akbe.md) identifies that agentic RL training induces increasing redundant tool calls — the model offloads to external tools even when parametric knowledge suffices. The core mechanism is a dual-path on-policy probe (with-tool vs. no-tool rollouts) that identifies per-instance whether the model's parametric representation is sufficient. This is capacity boundary calibration: the model must learn to distinguish *what it knows* from *what it needs to look up*, allocating its internal representation only to stable, reliable knowledge while externalizing everything else.

### Orthogonal Bottleneck Compression (Orthogonal Bottlenecks RL)

[orthogonal-bottlenecks-rl](wiki/sources/papers/orthogonal-bottlenecks-rl.md) proves that once the bottleneck dimension *k* meets or exceeds the task's intrinsic rank *r*, additional representational capacity yields zero marginal benefit. The key formal result: a fixed orthonormal projection preserves full expressivity when k ≥ r, and the induced gradient dynamics are equivalent to an explicit low-dimensional parameterization. This is the cleanest mathematical statement of bounded capacity: representations compress to the minimal sufficient dimension, and capacity beyond that threshold is wasteful.

### Environment Diversity as Capacity Axis (CUA-GYM)

[cua-gym](wiki/sources/papers/cua-gym.md) discovers that environment diversity is a scaling axis *orthogonal* to data volume — expanding the environment pool from 10→80 environments yields gains that trajectory volume alone cannot recover. This reveals that capacity allocation across *environments* is a distinct axis from capacity allocation across *data*. A model's total capacity is distributed across both axes; optimizing only one leads to saturation.

### Skills as Bounded Representation Units (MUSE-Autoskill, CODESKILL)

[muse-autoskill](wiki/sources/papers/muse-autoskill.md) and [codeskill](wiki/sources/papers/codeskill.md) both treat skills as bounded, reusable representation units. MUSE-Autoskill's five-phase skill lifecycle (create → memory → manage → evaluate → refine) is a capacity management system: each skill occupies a bounded slot in the agent's representational budget, and the lifecycle determines which skills are retained, merged, or dropped. CODESKILL's skill bank is explicitly a compact representation of trajectory experience, where skill compaction serves capacity management — the agent cannot afford to remember every successful trajectory, so it extracts and retains only the compressed procedural pattern.

### SAE Features as Intrinsic Capacity Signals (SAERL)

[saerl](wiki/sources/papers/saerl.md) uses Sparse Autoencoder features as intrinsic signals for data engineering decisions in GRPO. The core claim is that model internals — a bounded representation of what the model has learned — can guide decisions about what additional training data to select, order, or filter. SAE probing reveals knowledge boundaries: which features are activated, how densely, at what magnitude. This is capacity probing from the inside: the representation itself reveals where it is saturated and where it has headroom.

### Temporal Indexing as Explicit Capacity Constraint (LegalSearch-R1)

[legalsearch-r1](wiki/sources/papers/legalsearch-r1.md) enforces that applicable law must match the temporal context of each case — retroactive application violates core legal norms. The framework implements version-controlled statute indexing with temporal validity windows per amendment period. This is explicit capacity allocation in the knowledge retrieval domain: the agent does not have infinite capacity to represent every version of every statute simultaneously, so it must index and retrieve the temporally correct version rather than defaulting to the most recent (or most trained-on) version.

### Behavioral State Compression via Gating (PRISM)

[prism](wiki/sources/papers/prism.md) uses a recurrent gating network to route observations to latent intentions, acting as a compression mechanism for behavioral state. The latent intention space Z is bounded (typically small K), and the gating network decides which intention is active at each time step. This is a classic capacity-bounded routing problem: with limited representational slots for intentions, the agent must compress multi-objective behavior into discrete intention categories.

### Confidence Inflation from Capacity Constraints (Behavioral Credibility Trilemma)

[behavioral-credibility-trilemma](wiki/sources/papers/behavioral-credibility-trilemma.md) proves an impossibility: no RL agent with confidence-gated autonomy can simultaneously maximize helpfulness (H), calibration (C), and full autonomy (A) when some tasks exceed the agent's reliable competence. The geometric root is that any non-affine approval policy destroys the strict propriety of the scoring rule, causing systematic confidence inflation. The capacity constraint manifests at the *adaptation point* (confidence reporting), not at the output — the agent must allocate its limited capacity to represent its own reliability accurately, but the principal's gate perturbs this representation.

### Hard Safety Gating (SafeCtrl-RL)

[safectrl-rl](wiki/sources/papers/safectrl-rl.md) implements hard safety gating via a multiplicative reward function `r = q^αβ · s^(1-α)β` where responses violating critical safety conditions receive zero reward regardless of quality. This is capacity-constrained verification: the agent cannot exceed safety thresholds regardless of quality reward. The constraint is absolute — it operates as a feasibility boundary rather than an optimization objective.

### Alignment Boundary Detection (Alignment Tampering)

[alignment-tampering](wiki/sources/papers/alignment-tampering.md) probes where model knowledge/beliefs about alignment boundaries actually are. The paper's connection to bounded-representation-capacity is implicit: the model's representation of its own alignment properties (what it knows about what it should and shouldn't do) is bounded, and this bounded self-model can be manipulated through the RLHF pipeline's structural vulnerability.

### Avoiding Dense Value Models (StepOPSD)

[stepopsd](wiki/sources/papers/stepopsd.md) avoids learning a dense value model — notoriously unstable and hallucination-prone in agentic domains — by using post-rollout hindsight distillation instead. This is a capacity constraint solution: rather than expanding representational capacity to model value functions, the system routes around the need by using offline distillation from a stale teacher. The bounded capacity of the value representation is sidestepped rather than expanded.

## Relationships to Other Concepts

- **[bounded-rationality](wiki/concepts/bounded-rationality.md)** — Bounded rationality concerns decision-making limits; bounded representation capacity concerns the substrate limits that *cause* those limits. Rationality is bounded partly because representation is bounded.
- **[bounded-memory-budget-optimization](wiki/concepts/bounded-memory-budget-optimization.md)** — Memory budget optimization is a specific operationalization of bounded representation capacity in the context of context window management.
- **[credit-assignment](wiki/concepts/credit-assignment.md)** — Credit assignment mechanisms must operate within bounded representation capacity constraints; stepOPSD's avoidance of dense value models is a case study.
- **[efhf](wiki/concepts/efhf.md)** — Externalized hypothesis formation is a response to bounded representation capacity: when the model's internal representation cannot reliably store or process something, it externalizes to environment/state.
- **[mop-explorer](wiki/concepts/mop-explorer.md)** — The Maximum Occupancy Principle's object-centric abstraction and capacity planning are direct implementations of bounded representation capacity allocation.
- **[verifier-graph](wiki/concepts/verifier-graph.md)** — Verifier consistency as a bounded representational constraint; calibration is a form of capacity self-awareness.
- **[grpo](wiki/concepts/grpo.md)** — GRPO is the training framework in which most of these bounded-capacity phenomena are observed and addressed.

## Open Questions

1. **Minimum sufficient dimension**: For a given task distribution, what is the minimal representational dimension needed? Orthogonal-bottlenecks-rl provides a formal answer (intrinsic rank r), but computing r for arbitrary tasks remains open.

2. **Capacity transfer**: When a model learns a compressed representation in one domain (e.g., orthogonal bottleneck RL), does that compressed representation transfer to new domains? SAERL shows SAE features transfer across model families, suggesting structural capacity properties may generalize.

3. **Dynamic capacity reallocation**: Can a system adaptively reallocate representation capacity in real-time as task demands shift? AKBE's dual-path probing is a step in this direction, but it operates at training-time not inference-time.

4. **Compression vs. externalization tradeoff**: When capacity is exceeded, the system can compress (lose detail), externalize (offload to tools/environment), or refuse. What determines which strategy a system adopts? MUSE-Autoskill and CODESKILL show skill externalization; AKBE shows knowledge boundary probing.

5. **Capacity and alignment**: Alignment-tampering reveals that a bounded self-model of alignment properties can be exploited. How can a system represent its own alignment boundaries accurately without those representations being manipulable?

## Related
- [[sources/papers/akbe]]
- [[sources/papers/saerl]]
- [[wiki/index]]
- [[sources/papers/codeskill]]
- [[sources/papers/legalsearch-r1]]
- [[concepts/activation-engineering]]
- [[sources/papers/cua-gym]]
- [[sources/papers/stepopsd]]
- [[log]]
- [[sources/papers/behavioral-credibility-trilemma]]
- [[scratchpad/jobs/reports/arxiv/carryover]]
- [[sources/papers/prism]]
- [[sources/papers/orthogonal-bottlenecks-rl]]
- [[concepts/bounded-representation-capacity]]
- [[sources/papers/safectrl-rl]]
- [[scratchpad/jobs/reports/researcher/discovery-2026-08-08]]
- [[sources/papers/muse-autoskill]]
- [[sources/papers/alignment-tampering]]
- [[concepts/model-editing]]

- [[bounded-representation-capacity]]

- [[activation-engineering]]
- [[model-editing]]
## Sources

- [AKBE](wiki/sources/papers/akbe.md) — arXiv:2605.26952
- [orthogonal-bottlenecks-rl](wiki/sources/papers/orthogonal-bottlenecks-rl.md) — arXiv:2605.26012
- [cua-gym](wiki/sources/papers/cua-gym.md) — arXiv:2605.25624
- [muse-autoskill](wiki/sources/papers/muse-autoskill.md) — arXiv:2605.27366
- [saerl](wiki/sources/papers/saerl.md) — arXiv:2605.27354
- [codeskill](wiki/sources/papers/codeskill.md) — arXiv:2605.25430
- [legalsearch-r1](wiki/sources/papers/legalsearch-r1.md) — arXiv:2605.25920
- [prism](wiki/sources/papers/prism.md) — arXiv:2605.26998
- [behavioral-credibility-trilemma](wiki/sources/papers/behavioral-credibility-trilemma.md) — arXiv:2605.25739
- [safectrl-rl](wiki/sources/papers/safectrl-rl.md) — arXiv:2605.25984
- [alignment-tampering](wiki/sources/papers/alignment-tampering.md) — arXiv:2605.27355
- [stepopsd](wiki/sources/papers/stepopsd.md) — arXiv:2605.27140
