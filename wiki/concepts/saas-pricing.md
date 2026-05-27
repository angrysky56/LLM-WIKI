---
created: 2026-08-07
updated: 2026-08-07
type: concept
summary: SaaS pricing — software subscription pricing models (per-user, tiered, usage-based); key frameworks for AI agent SaaS products
tags: [SaaS, pricing, business-model, subscription, AI-agents]
sources: []
status: reference
confidence: 0.8
---

# SaaS Pricing

SaaS (Software as a Service) pricing refers to the subscription-based revenue models used by cloud-hosted software companies. For AI agent SaaS products, pricing models must account for the variable cost nature of LLM inference — unlike traditional SaaS where marginal cost per user approaches zero.

## Core Pricing Models

### Per-User (Seat-Based)
Most common for collaborative tools. Revenue scales with headcount.

| Tier | Price | Notes |
|------|-------|-------|
| Per user/month | Flat rate per seat | Good for B2B collaboration tools |
| Tiered per user | Volume discounts at scale | Common in CRM, productivity |

### Tiered Plans (GoodRobot Pattern)
AI agent SaaS typically uses capability-gated tiers rather than pure seat counts:

| Tier | Price/mo | Agents | Use Case |
|------|----------|--------|----------|
| Starter | $299 | 3 | Pilot / small team |
| Professional | $899 | 10 | Growing SMB |
| Enterprise | $2,499 | Unlimited | Full deployment |

Note: GoodRobot's actual pricing included feature gates (API access, SSO, SLA) rather than pure agent count — enterprise tiers are distinguished by operational capability, not user volume.

### Usage-Based (Consumption)
Emerging as standard for AI products where marginal cost per query is non-trivial:

- **Per-token**: Pay per input/output token consumed
- **Per-query**: Flat fee per API call
- **Per-task**: Pay per completed workflow (AI agent task)

Usage-based aligns revenue with cost structure but creates revenue volatility. Hybrid models (base fee + usage overage) are increasingly common.

## AI Agent SaaS Pricing Considerations

| Factor | Traditional SaaS | AI Agent SaaS |
|--------|----------------|---------------|
| Marginal cost | ~$0/user | Significant (LLM inference) |
| Usage variability | Low | High |
| Pricing anchor | Per seat | Per capability/task |
| Churn drivers | Value realization lag | Task failure, cost surprises |
| Enterprise value | Collaboration lock-in | Workflow integration + ROI |

## Key Metrics

- **ARPU** (Average Revenue Per User): Monthly recurring revenue / active users
- **CAC** (Customer Acquisition Cost): Total sales and marketing spend / new customers
- **LTV** (Lifetime Value): ARPU × gross margin × average customer lifespan
- **NRR** (Net Revenue Retention): Expansion revenue - churn; >100% indicates growth within existing base

## Connections

- [[goodrobot]] — archived AI agent SaaS project with documented pricing tiers
- [[saas]] — broader SaaS business model context
- [[business-model]] — general business model taxonomy