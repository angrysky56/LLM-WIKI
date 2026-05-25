---
summary: Six agent archetypes (Alpha-Zeta) with roles, instruction sets, and oMCD mappings
tags: [meta-cognition, agent-taxonomies, AI-architectures]
updated: 2026-05-25T00:27:21Z
created: 2026-05-25T00:27:21Z
---

# Agent Taxonomies: Alpha through Zeta

This page defines six archetypal agent types, ordered by increasing meta-cognitive sophistication. Each archetype maps to specific mechanisms within the [[oMCD]] framework.

## Overview Table

| Archetype | Primary Function | Key oMCD Mechanism | Instruction Set Focus |
|-----------|------------------|-------------------|----------------------|
| [[#alpha\|Alpha]] | Complexity gating | threshold $\omega(t)$ | Meta-level control |
| [[#beta\|Beta]] | Option optimization | ż (control signal) | Decision quality |
| [[#gamma\|Gamma]] | Adaptive learning | $\beta$ calibration | Self-improvement |
| [[#delta\|Delta]] | Evolutionary search | parallel MDP rollouts | Exploration |
| [[#epsilon\|Epsilon]] | Assumption validation | stop criterion | Self-correction |
| [[#zeta\|Zeta]] | Entropy regulation | dual to confidence | Uncertainty management |

---

## Alpha: Complexity Gating Agent

**Role**: Controls information flow by gating high-complexity inputs.

**Mechanism**: Maintains a dynamic threshold $\omega(t)$ that determines which stimuli are processed at full depth vs. shallowly dismissed.

**Instruction Set Summary**:
```
IF complexity(input) > ω(t):
  DEFER to Beta (defer_to_slow_reasoning)
ELSE:
  PROCESS reactively
UPDATE ω(t) based on error_rate
```

**oMCD Mapping**: Alpha sets the boundary condition for when the meta-cognitive controller (`π_ω`) engages. The threshold $\omega(t)$ is itself subject to meta-meta-cognitive regulation.

**Example**: A system that routes simple queries to a fast pattern-matcher but escalates ambiguous or high-stakes queries to a slower, more thorough reasoning process.

---

## Beta: Option Optimization Agent

**Role**: Maximizes the objective function $E[B(z) - C(z)]$ over candidate options.

**Mechanism**: Implements the core [[oMCD]] control signal computation: $\dot{z} = \arg\max_z \mathbb{E}[B(z) - C(z)]$

**Instruction Set Summary**:
```
ENUMERATE options Z = {z₁, z₂, ...}
FOR EACH z IN Z:
  COMPUTE B(z) = R × P_c(z)
  COMPUTE C(z) = α × z^ν
SELECT z* = argmax(B(z) - C(z))
EXECUTE z*
```

**oMCD Mapping**: Beta is the "inner loop" of oMCD — the mechanism that actually computes the control signal from confidence benefit and cognitive cost.

**Example**: A reasoning system that weighs the expected confidence payoff of gathering more evidence against the cognitive cost of continued deliberation.

---

## Gamma: Adaptive Learning Rate Agent

**Role**: Dynamically calibrates the precision update learning rate $\beta$.

**Mechanism**: Adjusts $\beta$ based on prediction error magnitude and environmental volatility.

**Instruction Set Summary**:
```
COMPUTE prediction_error = |actual - predicted|
IF prediction_error > threshold:
  β ← β × γ_up   (increase learning rate)
ELIF prediction_error < floor:
  β ← β × γ_down (decrease learning rate)
UPDATE precision: 1/σᵢ(z) = 1/σᵢ⁰ + β × z
```

**oMCD Mapping**: Gamma operates on the precision update rule $1/\sigma_i(z) = 1/\sigma_i^0 + \beta \cdot z$. High $\beta$ = fast adaptation; low $\beta$ = stable but slow.

**Example**: A system that learns quickly when the environment is volatile (rapid concept drift) but maintains stable beliefs when the environment is stable.

---

## Delta: Evolutionary Search Agent

**Role**: Maintains parallel MDP rollouts for exploration-exploitation balance.

**Mechanism**: Runs multiple candidate policies simultaneously, using value mode perturbations $\mu_i(z) = \mu_i^0 + \delta_i$ to generate diversity.

**Instruction Set Summary**:
```
INITIALIZE N policy rollouts
FOR EACH rollout r:
  PERTURB μᵢ ← μᵢ⁰ + δᵢ  (δᵢ ~ N(0, τ²))
  EXECUTE rollout to horizon H
  COMPUTE expected return
SELECT policy with highest return
RETAIN top-K for next iteration
```

**oMCD Mapping**: Delta injects structured randomness via the value mode perturbation $\delta_i$, enabling the system to explore the option space without gradient information.

**Example**: A system that maintains a population of candidate reasoning strategies, evolving them over time based on task performance.

---

## Epsilon: Assumption Validation Agent

**Role**: Monitors for assumption violations and triggers self-correction.

**Mechanism**: Evaluates stop criteria against accumulated evidence; triggers deep re-evaluation when assumptions break down.

**Instruction Set Summary**:
```
MONITOR assumption_set A = {a₁, a₂, ...}
FOR EACH assumption aᵢ IN A:
  IF evidence contradicts aᵢ:
    FLAG for review
    COMPUTE confidence_impact
IF critical_assumption_violated:
  TRIGGER full_reevaluation
  INVOKE Beta to find recovery path
```

**oMCD Mapping**: Epsilon implements the optimal stopping logic $Q(a(t), \Delta\mu(t))$ — when accumulated evidence violates assumptions, the Q-value for stopping (and replanning) becomes positive.

**Example**: A system that notices its initial interpretation of a problem no longer fits new evidence, triggering a fundamental rethink.

---

## Zeta: Entropy Regulation Agent

**Role**: Manages uncertainty and information gain across the cognitive system.

**Mechanism**: Treats entropy as the dual to confidence — when confidence is low, entropy is high, and vice versa. Zeta modulates information flow to reduce harmful uncertainty.

**Instruction Set Summary**:
```
COMPUTE system_entropy H = -Σ pᵢ log pᵢ
COMPUTE confidence_vector P_c
IF H > entropy_threshold:
  INVOKE information_gathering
  INCREASE precision updates
  REDUCE exploration temperature
ELSE:
  MAINTAIN current state
```

**oMCD Mapping**: Zeta is the dual operator to Beta's confidence computation. Where Beta maximizes $B - C$, Zeta minimizes system entropy subject to maintaining minimum competence.

**Example**: A system that notices it's "lost" (high entropy across options) and deliberately seeks clarifying information to reduce uncertainty.

---

## Relationships Between Archetypes

```
Alpha (complexity gating)
   │
   ▼ invokes
Beta (optimization) ←→ Gamma (learning rate)
   │                      │
   │                      ▼
   │                  Delta (evolutionary search)
   │
   ▼
Epsilon (assumption validation) ←→ Zeta (entropy regulation)
```

Alpha gates which problems reach Beta. Gamma adapts the learning rate used by Beta's precision updates. Delta provides exploratory options for Beta to evaluate. Epsilon monitors Beta's assumptions. Zeta maintains overall uncertainty balance.

## See Also

- [[oMCD]] — Formal framework these archetypes implement
- [[cognitive-architecture]] — MCM context
- [[hermes-meta-cognition]] — Hermes as a specific implementation

## Notes

- These archetypes are not mutually exclusive — a sophisticated agent typically implements multiple archetypes simultaneously
- The ordering (Alpha→Zeta) reflects increasing meta-cognitive depth, not necessarily capability
- Any practical implementation must balance these roles against computational budget constraints
