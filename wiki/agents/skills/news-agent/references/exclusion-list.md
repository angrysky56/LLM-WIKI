# News Agent Exclusion List

Stories and categories to exclude from ingestion unless they explicitly intersect active research threads.

## Routine / Low-Significance News

- **Routine tariff rate tracking** — Bloomberg/Tax Foundation daily tariff updates are operational data, not news
- **General AI regulation news** — unless it represents a significant policy shift, new legislation, or enforcement action
- **SpaceX launches** — routine operational launches; include only if orbital milestone, first-of-kind achievement, or planetary significance
- **Sports scores, standings, transfers** — soft news with no research thread intersection
- **Celebrity/entertainment news** — soft news, exclude unless it intersects active threads
- **Market daily summaries** — routine price/economic reporting without significant policy implication

## Criteria for Inclusion

A story should be ingested if it meets at least one of:
- **Will this matter in 6 months?** —结构性变化, not短期波动
- **Does it connect to existing wiki threads?** — Cross-link potential
- **Is it globally significant, not just local noise?** — Scope matters
- **Does it represent a first-of-kind event?** — Unprecedented actions, technologies, or policies

## Monitor-Only Categories

These are tracked conceptually but not individually ingested:

| Category | Reason for Exclusion |
|----------|----------------------|
| Routine economic indicators (CPI, unemployment) | Already covered by macro monitoring |
| Incremental tech product releases | No structural significance |
| Political polling without election proximity | Noise, not signal |
| Social media trends | Ephemeral unless broader implications |

## Token Budget Protection

Exclusion is enforced to protect the **3-5 stories per cycle / ~15,000 token budget**. When in doubt, exclude and note in the excluded section of the report rather than ingest and over-run budget.