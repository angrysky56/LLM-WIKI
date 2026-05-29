---
created: 2026-05-25 00:34:24+00:00
updated: 2026-05-25 00:34:24+00:00
summary: Warm-start calibration procedure for oMCD parameters β and γ
tags: [meta-cognition, implementation, cognitive-architecture, omcd]
---


---
summary: "Warm-start calibration procedure for β and γ parameters in the oMCD metacognitive control framework, including variance estimation, test suite design, and architectural separation"
tags: [meta-cognition, implementation, cognitive-architecture, oMCD]
---

# oMCD Warm-Start Calibration Protocol

## Overview

The oMCD (online Metacognitive Control of Decisions) model depends on two effort-efficacy parameters — **β** (Type #1) and **γ** (Type #2) — that must be calibrated before production use. Unlike parameters that can be set from first principles, β and γ require an empirical warm-start period of 50–100 decisions per decision domain. This document specifies the calibration procedure.

## Parameter Roles

| Parameter | Formula | Role |
|-----------|---------|------|
| β | `1/σ_i(z) = 1/σ_i⁰ + β·z` | Controls how fast precision improves with resource investment |
| γ | `δ_i ~ N(0, γ·z)` | Controls how much value modes are perturbed by deliberation |

Both parameters govern the rate of change in internal representations as cognitive resources are allocated. If β is too high, the system becomes overconfident too quickly. If γ is too high, deliberation destabilizes value representations. If both are too low, the system under-invests in difficult decisions.

## Warm-Start Procedure

### Phase 1: Initial Seeding (Decisions 1–20)

Use conservative starting values:

```
β₀ = 0.01   (slow precision accumulation)
γ₀ = 0.005  (minimal perturbation)
```

Observe behavior but do not update parameters. Record:
- `z` allocated per decision
- `P_c(z)` estimated confidence
- Net benefit `B(z) - C(z)` for each decision
- Decision outcome (correct/incorrect if ground truth available)

### Phase 2: Adaptive Estimation (Decisions 21–75)

After Phase 1, estimate initial slopes from the observed `(z, P_c)` curve.

**For β**: Fit a linear regression to `1/σ_i(z)` vs `z` across the 20 warm-start decisions. Use ordinary least squares:

```
σ_i(z) ≈ 1 / (1/σ_i⁰ + β·z)
```

Track the residual between predicted and observed `P_c(z)`. Increase β if residuals are negative and systematic (model under-predicts confidence growth). Decrease β if residuals are positive and systematic.

**For γ**: Estimate from the empirical variance of value mode perturbations. Compute the sample variance of decision-to-decision changes in `Δμ` after controlling for resource investment:

```
γ_est = Var(δ_i) / z̄
```

where `z̄` is mean resources invested during Phase 1.

### Phase 3: Validation (Decisions 76–100)

Freeze β and γ estimates from Phase 2. Run the system with frozen parameters. Compare:

- **Calibration curve**: binned P_c(z) vs empirical accuracy. Well-calibrated β should produce accuracy ≈ P_c(z) across all confidence bins.
- **Stopping behavior**: mean `z` should be close to the predicted `ẑ = argmax_z E[B(z) - C(z)]`.
- **Oscillation check**: no systematic oscillation in `z` allocation across consecutive decisions.

### Phase 4: Production Deployment

After 100 decisions with acceptable calibration metrics:

```
|accuracy - P_c(z)| < 0.1 per bin  (calibration error)
Var(z) / mean(z) < 0.5              (stable allocation)
```

Record the validated (β, γ) pair as domain-specific hyperparameter defaults.

## Variance Estimation for V[|Δμ(z)|]

The expected confidence formula requires second-moment estimation:

```
P_c(z) = s(λ · E[|Δμ(z)|] / √(1 + (1/2) · (λ² · V[|Δμ(z)|])))
```

### Online O(1) Update Rule

Maintain running estimates of first and second moments of `|Δμ(z)|`:

```
n ← n + 1
δ ← |Δμ(z)| - m₁         (instantaneous deviation)
m₁ ← m₁ + δ/n             (updated first moment)
m₂ ← m₂ + δ²              (updated second moment)
V[|Δμ(z)|] ← m₂ / n       (second moment)
```

This is a naive but numerically stable online estimator for small `n`. For large `n` (production use), switch to Welford's algorithm for numerical stability:

```
n ← n + 1
δ ← |Δμ(z)| - m₁
m₁ ← m₁ + δ/n
M₂ ← M₂ + δ · (|Δμ(z)| - m₁)
V[|Δμ(z)|] ← M₂ / (n - 1)   (for n ≥ 2)
```

### Gaussian Approximation

For real-time tractability, treat `|Δμ(z)|` as approximately Gamma-distributed (right-skewed positive support). The ratio `E[|Δμ|] / √V[|Δμ|]` then has a known approximation. This avoids explicit distribution tracking while preserving the signal-to-noise interpretation.

## Minimal Test Suite

### Test 1: Precision Update Linearity

**Purpose**: Verify `1/σ_i(z) = 1/σ_i⁰ + β·z` holds empirically.

Synthetic scenario: generate 200 decisions with known ground-truth `σ_i(z)` curves. Fit β from the data. Assert:

```
|β_fitted - β_true| / β_true < 0.2
```

### Test 2: Perturbation Magnitude

**Purpose**: Verify `δ_i ~ N(0, γ·z)` scaling with z.

Synthetic scenario: generate decisions with varying `z ∈ [1, 10]`. For each `z`, collect 50 perturbations `δ_i`. Assert:

```
E[δ_i²] ≈ γ·z   (within 2 standard errors)
|skewness(δ_i)| < 0.3   (normality check)
```

### Test 3: Confidence Calibration

**Purpose**: Verify estimated `P_c(z)` tracks empirical accuracy.

Synthetic scenario: 500 decisions with known ground truth. Bin by `P_c(z)` in 5 bins (0.0–0.2, 0.2–0.4, …, 0.8–1.0). For each bin, compute empirical accuracy. Assert:

```
mean(|empirical_accuracy - bin_center|) < 0.1
```

### Test 4: Optimal Stopping Convergence

**Purpose**: Verify the system converges to `ẑ = argmax_z E[B(z) - C(z)]`.

Synthetic scenario: known reward landscape `B(z) = R·P_c(z)` with known `P_c(z)`. Compute the theoretical `ẑ`. Run 100 independent decision episodes. Assert:

```
mean(|z_achieved - ẑ|) / ẑ < 0.15
```

## Architectural Separation: Value Representation vs. Deliberation

### The Perturbation Problem

The formula `μ_i(z) = μ_i⁰ + δ_i` where `δ_i ~ N(0, γ·z)` creates an architectural hazard: **deliberation itself modifies the internal state it reads**. This is problematic for interpretability and testing — the deliberation process cannot be replayed against the same initial state.

### Recommended Pattern: Explicit Layer Separation

```python
class ValueRepresentationLayer:
    """Immutable-ish value state — perturbations are recorded, not hidden."""
    def __init__(self, μ_i⁰: np.ndarray, σ_i⁰: float):
        self._μ = μ_i⁰.copy()
        self._σ = σ_i⁰
        self.perturbation_log: list[tuple[float, np.ndarray]] = []

    def get_state(self) -> tuple[np.ndarray, float]:
        return self._μ.copy(), self._σ

    def apply_perturbation(self, δ: np.ndarray, z: float) -> None:
        self._μ = self._μ + δ
        self.perturbation_log.append((z, δ.copy()))

    def precision_update(self, β: float, z: float) -> None:
        self._σ = 1.0 / (1.0 / self._σ + β * z)


class DeliberationLayer:
    """Reads value representation but does not mutate it directly."""
    def __init__(self, vrep: ValueRepresentationLayer):
        self._vrep = vrep

    def compute_confidence(self, z: float) -> float:
        μ, σ = self._vrep.get_state()
        # P_c(z) computation uses current state
        return self._sigmoid(self._compute_signal_noise_ratio(μ, σ, z))

    def select_action(self, z: float, ω: float) -> int:
        Q = self._compute_Q(z)
        return 0 if Q >= ω else 1
```

**Key invariant**: The `ValueRepresentationLayer` records all perturbations in `perturbation_log` for auditability. The `DeliberationLayer` reads through `get_state()` and never writes. The perturbation `δ_i` is generated by a separate stochastic process (not by the deliberation layer itself).

## Calibration Validation Checklist

Before deploying β, γ to production:

- [ ] Phase 1 (20 decisions) completed with initial values (β₀, γ₀) = (0.01, 0.005)
- [ ] Phase 2 (55 decisions) produced fitted (β_fit, γ_fit)
- [ ] Phase 3 (25 decisions) validation metrics meet thresholds:
  - Calibration error < 0.1
  - Allocation coefficient of variation < 0.5
- [ ] All 4 synthetic test suite cases pass
- [ ] Perturbation log shows no systematic drift in `μ_i` across warm-start period
- [ ] Variance estimation via Welford's algorithm confirmed numerically stable

## Notes

- β and γ are **per-decision-domain** hyperparameters. A system deployed across multiple domains (e.g., classification + generation) should maintain separate (β, γ) pairs per domain.
- The 50–100 decision warm-start is a practical minimum. For high-stakes domains, extend to 200–500 decisions.
- γ calibration is particularly sensitive to the perturbation distribution assumption. If empirical `δ_i` shows heavy tails (kurtosis > 3), consider switching from Gaussian to Student-t perturbation with estimated degrees of freedom.
- The separation between `ValueRepresentationLayer` and `DeliberationLayer` should be enforced at the type level, not just by convention — use private attributes (`_μ`, `_σ`) with no public setters.

## Related
- [[wiki/index]]
- [[oMCD-calibration-protocol]]

- [[oMCD-calibration-protocol]]

## References

- oMCD model specification: `wiki/concepts/oMCD.md`
- Pathfinder analysis: `wiki/references/portfolio-policies-metacognition.md`
- Agent archetype mappings: `wiki/concepts/agent-taxonomies.md`
