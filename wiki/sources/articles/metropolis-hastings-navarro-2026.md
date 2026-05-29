---
summary: Accessible MCMC tutorial on Metropolis-Hastings by Danielle Navarro — proposal distributions, accept-reject step, intuitive grounding.
tags: [MCMC, statistics, sampling, Markov-chain, tutorial]
updated: 2026-05-29T17:11:29Z
created: 2026-05-29T17:11:29Z
---

---
created: 2026-05-29
updated: 2026-05-29
type: source
summary: "Danielle Navarro's accessible introduction to Metropolis-Hastings MCMC: target distributions known up to constant, proposal distributions, accept-reject step, and the intuition behind why it works."
tags: [MCMC, statistics, sampling, Markov-chain, tutorial]
sources: https://blog.djnavarro.net/posts/2023-04-12_metropolis-hastings/
status: active
confidence: 0.95
---

# The Metropolis-Hastings Algorithm

## Metadata

| Field | Value |
|-------|-------|
| Author | Danielle Navarro |
| Source | blog.djnavarro.net |
| Published | 2023-04-12 |
| Type | Tutorial article |
| Wiki path | wiki/sources/articles/metropolis-hastings-navarro-2026.md |

## Summary

Metropolis-Hastings is the most popular Markov chain Monte Carlo (MCMC) method for sampling from arbitrary probability distributions. The core problem it solves: you know the unnormalized form $p(x) \propto g(x)$ but cannot sample directly — you only have access to $g(x)$, not the normalizing constant.

The algorithm works by constructing a Markov chain whose stationary distribution matches the target $p(x)$:

1. **Proposal**: From current state $x_n$, generate a candidate $x^*$ from a proposal distribution $q(x^*|x_n)$ (typically symmetric, e.g., Normal centered on $x_n$)
2. **Accept/Reject**: Compute acceptance probability $A = \min(1, g(x^*)/g(x_n))$ — if the candidate is better (higher $g$), accept it; if not, accept with probability proportional to the ratio
3. **Iterate**: After many iterations, $x_n$ becomes a sample from $p(x)$

## Key Intuitions

- **Target known up to constant**: MCMC exploits the fact that you only need relative probabilities ($g(x^*)/g(x_n)$), not the normalized $p(x)$
- **Proposal flexibility**: The proposal $q$ can be almost anything — symmetric proposals (e.g., Normal) give acceptance ratio that simplifies to $g(x^*)/g(x_n)$
- **Detailed balance**: The accept-reject mechanism ensures the chain satisfies detailed balance, guaranteeing convergence to $p(x)$
- **Burn-in**: Early samples reflect the starting point; discard the burn-in period

## Connections

- [[MCMC]] — Markov chain Monte Carlo methods
- [[entropy-cut-mh-reasoning-2026]] — Entropy-Cut MH builds on this foundation for reasoning traces; that paper uses entropy to find decision points in the proposal distribution
- [[sampling]] — sampling-based reasoning strategies
- [[test-time-scaling]] — test-time compute strategies (related to power distribution sharpening)

## Caveats

This is a beginner-level tutorial — deep mathematical treatment (ergodicity, detailed balance proofs) is omitted. For rigorous coverage, see standard MCMC references.
