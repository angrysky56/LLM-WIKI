---
summary: Reference catalog of optional skills for Hermes Agent — installable but not active by default
tags: [source, hermes-agent, documentation, skills]
updated: 2026-06-10T16:49:36Z
created: 2026-06-10T16:49:36Z
---

# Optional Skills Catalog — Hermes Agent

**Source:** Official documentation for Hermes Agent's optional skills system. Available at `hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog`.

**Summary:** Hermes Agent ships with a catalog of optional skills under the `optional-skills/` directory. These skills are **not active by default** and must be explicitly installed:

```bash
hermes skills install official/<category>/<skill>
```

Example: `hermes skills install official/blockchain/solana`

## Connections
- [[hermes-agent]] — core agent system
- [[skill-management]] — how skills are installed and managed
