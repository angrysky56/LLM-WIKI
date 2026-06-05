---
summary: Power law — mathematical relationship where frequency varies as a power of some quantity
tags: [mathematics, scaling, statistics]
updated: 2026-06-05T09:47:56Z
---

---
created: 2026-05-29
updated: 2026-05-29
type: concept
summary: Power law — mathematical relationship where frequency varies as a power of some quantity
tags: [mathematics, scaling, statistics]
sources:
status: active
confidence: 0.5
---

# Power Law

A power law is a functional relationship where one quantity varies as a power of another:

```
f(x) = a · x^k
```

Power laws appear throughout AI and natural systems:

- **Scaling laws** — model performance vs. compute/data/parameters
- **Zipf's law** — word frequency in natural language
- **Pareto distribution** — wealth distribution, city sizes
- **Neural network loss landscapes** — power-law scaling of generalization

## Connections

- [[power-law-scaling]] — scaling laws in neural networks
- [[scaling-laws]] — relationship between model scale and capability
- [[taylors-law]] — power law in animal behavior ecology
- [[allometric-scaling]] — scaling relationships in biological systems

## Open Questions

- [ ] Is there a principled explanation for why neural network loss scales as a power law with compute? The empirical fit is strong but the theory is still debated.
- [ ] Do power-law scaling trends hold at extreme scales (100T+ parameters), or is there a phase change?
