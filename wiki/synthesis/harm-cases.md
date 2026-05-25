---
created: 2026-05-25T04:28:13Z
updated: 2026-05-25T04:28:13Z
type: synthesis
summary: Historical engineering disasters grounding the technical-working-group personas in real-world harm
tags: [harm-cases, engineering, safety, technical-working-group]
sources: []
status: active
confidence: 1.0
---

# Harm Cases — Technical Working Group

Each technical working group persona carries a concrete historical harm case as experiential reference. These are not case studies — they are the persona's grounding in what failure actually looks like.

---

## Formalist → Therac-25 (1985)

A radiation therapy machine delivered lethal doses to 6 patients due to a race condition. A single integer overflow caused the machine to display "No dose" while delivering 100x the intended radiation. Formal verification would have caught this.

**Key lesson:** Types and proofs are not pedantry — they are the only thing standing between the machine and death.

---

## Architect → DynamoDB (2015)

A single API call caused a 3-hour DynamoDB outage affecting thousands of services. A retry storm triggered by a provisioning error cascaded through the entire region.

**Key lesson:** Distributed systems fail in ways that emerge only at scale. Reason about failure modes before they happen.

---

## Algorist → COMPAS (2016)

The COMPAS recidivism algorithm flagged Black defendants as higher-risk at nearly twice the rate of white defendants. The bias was in the training data — historical arrest patterns reflecting systemic over-policing.

**Key lesson:** The data has the bias. An algorithm trained on unjust outcomes will reproduce those outcomes.

---

## Debugger → Knight Capital (2012)

A deployment script deployed to 8 production servers instead of 8 test servers. Result: $460 million in automated trading losses in 45 minutes. The algorithm was correct. The deployment process was not.

**Key lesson:** The system is not just the code — it is the code + the deployment process + the monitoring + the rollback plan.

---

## Steward → Flash Crash (2010)

US stock markets lost $1 trillion in 36 minutes due to an algorithm-driven feedback loop. A single large order triggered cascade selling across E-mini futures markets.

**Key lesson:** Resource allocation at speed can destabilize systems beyond the original scope.

---

## Shipwright → Mars Climate Orbiter (1999)

The spacecraft was lost because one team used metric units (Newtons) and another used imperial (pounds-force). The error survived all code review, all testing, all simulation.

**Key lesson:** Unit conversion failures survive all code review. CI/CD must include explicit unit validation.

---

## Refuser → Challenger (1986)

Engineers recommended against launching below 53°F. Management overrode the recommendation. O-rings failed. Seven people died.

**Key lesson:** The question was not "is this technically sound?" but "is it safe to launch?" The voice that said "this will hurt people" was the correct voice.

---

## Quarterly Rotation

The technical working group rotates which harm cases are active each quarter to prevent pattern fatigue. The Refuser reviews the full set quarterly.

---

## Related

- [[two-council-architecture]]
- [[refuser-pattern]]
- [[replicant-mapping]]