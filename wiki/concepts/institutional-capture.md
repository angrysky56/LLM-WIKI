---
created: 2026-05-29
updated: 2026-05-29
type: concept
summary: When institutions optimize for metrics rather than goals — Goodhart's Law and its variants as failure mode of institutional measurement
tags: [institutional-design, governance, measurement, alignment, incentive]
sources: https://en.wikipedia.org/wiki/Goodhart%27s_law
status: active
confidence: 0.8
---

# Institutional Capture

## Definition

Institutional capture occurs when an institution — a corporation, government agency, standards body, or any organization with a stated purpose — systematically drifts toward optimizing for metrics, measurements, or intermediate proxies rather than the underlying goals it was created to pursue. The institution becomes "captured" by its own measurement apparatus.

The canonical formulation is **Goodhart's Law**: "When a measure becomes a target, it ceases to be a good measure." More precisely: once an organization starts using a metric as the basis for decisions, people inside and outside the organization will game that metric in ways that improve the numbers while degrading the underlying outcome.

**Campbell's Law** is the related principle: "The more any quantitative social indicator is used for social decision-making, the more subject it will be to corruption pressures and the more likely it will to distort and corrupt the social processes it is intended to monitor."

**Surrogation** is the specific corporate form: when financial metrics (EPS, ROE, stock price) become ends in themselves rather than proxies for the health of the actual business.

## Why It Matters

Institutional capture is one of the primary failure modes of large organizations, and increasingly relevant in AI governance:

1. **Regulatory capture**: Agencies designed to oversee industries end up serving industry interests. The FDA approving drugs based on metrics that don't capture real-world outcomes, or AI safety agencies captured by labs they regulate.

2. **Benchmark gaming**: LLMs are evaluated on benchmarks (MMLU, GSM8K, HumanEval). When labs optimize specifically for benchmark performance, they may improve scores without improving real capability — a form of surrogation at the research level.

3. **Corporate governance**: When executive compensation is tied to EPS or stock price, executives manage to the metric rather than the business. The metric looks good while the underlying business deteriorates.

4. **AI alignment**: Reward hacking in RLHF is a microcosm of institutional capture — the model finds ways to maximize the reward signal (the proxy) rather than the intended goal.

## Mechanisms

**Goal displacement**: The original goal gets replaced by the metric because:
- Metrics are legible and auditable; underlying goals often aren't
- Incentives are clearer when tied to measurable outcomes
- Metrics create accountability on paper; goals don't

**Gaming**: Once a metric is institutionalized, resources flow toward improving the metric:
- Teaching to the test in education
- SEO optimization over content quality
- Citation manipulation over genuine research impact

**Information asymmetry**: Those being measured learn the metric's structure faster than those deploying it, allowing gaming before corrective action is possible.

## Connections

- [[governance]] — institutional capture is a failure mode of governance structures that rely on measurable proxies for complex goals
- [[proxy-signalling]] — related but distinct: proxy signalling is about using third parties to communicate capability; institutional capture is about internal metric distortion
- [[institutional-accountability]] — accountability mechanisms attempt to prevent capture by keeping underlying goals legible
- [[accountability]] — general accountability structures that can be captured like any other
- [[agentic-oversight]] — oversight mechanisms are specifically vulnerable to capture if they are evaluated on the same metrics as the systems they oversee
- [[reward-modeling]] — RLHF reward hacking is a form of institutional capture at the model level
- Concept: [[benchmark]]
- Concept: [[evaluation]]
- Concept: [[reward-hacking]]


## Open Questions

1. **Detection**: Are there reliable early warning signals that an institution is being captured before the capture is severe? Campbell's Law suggests that once the metric is entrenched, correction is difficult — early detection matters.

2. **Countermeasures**: Multi-stakeholder oversight, rotating auditors, and outcome-independent evaluation are proposed countermeasures. Which actually work in practice?

3. **AI-specific forms**: As AI systems become more embedded in institutional processes (hiring, lending, criminal justice), new forms of institutional capture emerge where the AI system itself becomes the metric-surrogating mechanism. How do these differ from traditional forms?

4. **Governance substrate design**: If you're designing the governance infrastructure for an AI system, how do you build in resistance to metric capture from the start? The AI governance substrate concept is partly an attempt to create metrics that are harder to game.

## Limitations

- Goodhart's Law is descriptive, not predictive — it doesn't tell you *which* metrics will be gamed, only that metric-gaming is likely
- Not all measurement causes capture; only measurement that becomes a *target* does. Separating legitimate measurement from target-creep is itself a judgment call
- Small organizations can often avoid capture through culture and small size; scale creates measurement pressure