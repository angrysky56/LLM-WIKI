---
created: 2026-05-25T00:27:19Z
updated: 2026-05-25T00:27:19Z
type: concept
summary: Formal framework for online metacognitive control of decisions with mathematical formulations
tags: [meta-cognition, cognitive-architecture, decision-theory]
sources: []
status: active
confidence: 0.9
---

# oMCD: Online Metacognitive Control of Decisions

**oMCD** (online Metacognitive Control of Decisions) is a formal framework for describing how an autonomous agent modulates its own decision-making processes in real-time. It extends the Metacognitive Control Model (MCM) by specifying precise mathematical formulations for confidence computation, control signal generation, and policy adaptation.

## Core Formalism

### 1. Benefit Function

The **benefit** of maintaining a cognitive option $z$ is:

$$B(z) = R \cdot P_c(z)$$

Where:
- $R$ = reward magnitude (scalar)
- $P_c(z)$ = expected confidence in option $z$, computed by the meta-cognitive self-model

### 2. Cost Function

The **cost** of sustaining option $z$ is:

$$C(z) = \alpha \cdot z^\nu$$

Where:
- $\alpha$ = cost scaling coefficient
- $\nu$ = cost exponent (typically $\nu > 1$ for superlinear cost growth)

### 3. Expected Confidence

The expected confidence $P_c(z)$ is derived from the agent's self-model:

$$P_c(z) = \text{softmax}_z(\mathbf{w} \cdot \mathbf{f}(z))$$

Where $\mathbf{f}(z)$ is the feature vector for option $z$ and $\mathbf{w}$ are learned importance weights.

### 4. Control Signal (Meta-cognitive Action)

The meta-cognitive control signal ż (read "z-hat") is:

$$\dot{z} = \arg\max_z \mathbb{E}[B(z) - C(z)]$$

This selects the option that maximizes expected net benefit — the gap between confidence-projected reward and cognitive cost.

### 5. Precision Update Rule

When the agent detects uncertainty, it recalibrates its precision (inverse variance):

$$\frac{1}{\sigma_i(z)} = \frac{1}{\sigma_i^0} + \beta \cdot z$$

Where:
- $\sigma_i^0$ = baseline variance for dimension $i$
- $\beta$ = learning rate for precision updates

### 6. Value Mode Perturbation

For adaptive exploration, the value estimate is perturbed:

$$\mu_i(z) = \mu_i^0 + \delta_i$$

Where:
- $\mu_i^0$ = baseline value estimate
- $\delta_i$ = perturbation drawn from $\mathcal{N}(0, \tau^2)$

### 7. Optimal Stopping

The **Q-value for stopping** at time $t$ given current accumulated evidence $\Delta\mu(t)$:

$$Q(a(t), \Delta\mu(t)) = \mathbb{E}[R_{\text{stop}} | a(t)] - \lambda \cdot \text{Var}(\Delta\mu(t))$$

Where $\lambda$ is a risk-sensitivity parameter.

### 8. Control Policy

The meta-cognitive control policy $\pi_\omega(t)$ is:

$$\pi_\omega(t) = \softmax\left( \frac{Q(a, \Delta\mu(t))}{\tau} \right)$$

Where $\tau$ is the temperature parameter controlling exploration/exploitation balance.

## The 9-Step oMCD Operational Loop

The complete oMCD cycle executes in this order:

1. **Observe** — Sample current environmental state $s_t$
2. **Generate options** — Enumerate candidate options $Z = \{z_1, z_2, \ldots, z_n\}$
3. **Compute confidence** — For each $z$, calculate $P_c(z)$ via the meta-cognitive self-model
4. **Calculate benefit** — Compute $B(z) = R \cdot P_c(z)$ for each option
5. **Calculate cost** — Compute $C(z) = \alpha \cdot z^\nu$ for each option
6. **Select action** — Set $\dot{z} = \arg\max_z \mathbb{E}[B(z) - C(z)]$
7. **Execute action** — Apply $\dot{z}$ to the cognitive system (adjust attention, memory, reasoning budget)
8. **Receive feedback** — Observe outcome $o_t$ and update confidence estimates
9. **Adapt** — Recalibrate precision $\sigma_i$ and value modes $\mu_i$ based on prediction error

## Relationship to MCM

oMCD is the **online, operationalized extension** of the Metacognitive Control Model (MCM). Where MCM provides the conceptual architecture (knowledge self-model + meta-cognitive self-model + control loop), oMCD provides the specific computational machinery.

See: [[cognitive-architecture]] for the broader MCM context.

## Instantiations by Agent Type

| Agent Type | Primary oMCD Role | Key Parameter |
|------------|-------------------|----------------|
| [[agent-taxonomies#alpha\|Alpha]] | Complexity gating | threshold $\omega(t)$ |
| [[agent-taxonomies#beta\|Beta]] | Optimization target | ż (control signal) |
| [[agent-taxonomies#gamma\|Gamma]] | Learning rate | $\beta$ calibration |
| [[agent-taxonomies#delta\|Delta]] | Parallel rollouts | MDP exploration |
| [[agent-taxonomies#epsilon\|Epsilon]] | Assumption validation | stop criterion |
| [[agent-taxonomies#zeta\|Zeta]] | Entropy regulation | dual to confidence |

## See Also

- [[cognitive-architecture]] — MCM framework overview
- [[agent-taxonomies]] — Agent archetype definitions
- [[hermes-meta-cognition]] — Hermes-specific implementation

## Notes

- oMCD assumes the meta-cognitive self-model is approximately **stationary** over the timescale of a single decision cycle
- The framework is agnostic to the underlying representation substrate (symbolic, neural, hybrid)
- Real-time constraint: the 9-step loop must complete within one environmental timestep