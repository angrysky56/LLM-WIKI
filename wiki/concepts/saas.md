---
summary: SaaS — cloud-hosted subscription software delivery model
tags: [SaaS, software, subscription, cloud, business-model]
updated: 2026-05-27T14:28:15Z
created: 2026-05-27T14:28:15Z
---

---
created: 2026-08-09
updated: 2026-08-09
type: concept
summary: SaaS (Software as a Service) — cloud-hosted subscription software model; alternative term to SaaS pricing for business model concept
tags: [SaaS, software, subscription, cloud, business-model]
sources: []
status: reference
confidence: 0.8
---

# SaaS

**SaaS** (Software as a Service) is a software delivery model where applications are hosted in the cloud by a provider and made available to customers via subscription, typically over the internet. Unlike traditional on-premises software, SaaS requires no local installation and is accessed through a web browser or thin client.

## Key Characteristics

| Characteristic | Description |
|---------------|-------------|
| **Cloud hosting** | Provider maintains servers, databases, and application |
| **Subscription pricing** | Monthly/annual recurring revenue (ARR) |
| **Automatic updates** | Provider pushes updates; no customer installation |
| **Multi-tenant architecture** | Single instance serves multiple customers |
| **API-first design** | Typically exposes APIs for integrations |
| **Usage-based options** | Per-user, per-seat, per-query, or tiered pricing |

## SaaS vs Traditional Software

| Dimension | On-Premises | SaaS |
|-----------|------------|------|
| Upfront cost | High (license + infrastructure) | Low (subscription only) |
| Marginal cost | High (per server deployment) | Low (~zero for additional users) |
| Scalability | Manual provisioning | Automatic (elastic scaling) |
| Maintenance | In-house IT team | Provider handles |
| Cash flow | Large capital expenditure | Operating expense |

## AI Agent SaaS Considerations

For AI agent products, SaaS pricing must account for the variable cost of LLM inference — unlike traditional SaaS where marginal cost per user approaches zero:

- **Per-token pricing**: Pay per input/output token consumed
- **Per-task pricing**: Pay per completed agent workflow
- **Hybrid models**: Base fee + usage overage

See [[saas-pricing]] for the detailed pricing model breakdown.

## Connections

- [[saas-pricing]] — detailed AI agent SaaS pricing models and frameworks
- [[business-model]] — broader business model taxonomy
- [[goodrobot]] — archived AI agent SaaS project with documented pricing tiers
