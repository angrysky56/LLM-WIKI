---
title: "angrysky56/aseke-compass-mcp: Building systemic discernment directly into a population, to recognize how their biological levers are being pulled by external leadership or algorithms—shifts the Cognitive Effort required for an Information System to capture the SEEKING system."
source: "https://github.com/angrysky56/aseke-compass-mcp"
author:
published:
created: 2026-05-01
description: "Building systemic discernment directly into a population, to recognize how their biological levers are being pulled by external leadership or algorithms—shifts the Cognitive Effort required for an Information System to capture the SEEKING system. - angrysky56/aseke-compass-mcp"
tags:
  - "clippings"
---
## ASEKE Compass Engine — MCP Server

Behavioral analysis tools grounded in Panksepp's Affective Neuroscience (1998), Duckitt & Sibley's Dual Process Model (2009), and the ASEKE framework (Hall).

## What This Does

Provides structured analytical patterns for understanding human behavior and intent through the lens of primary emotional systems, Information Structure capture, and transition dynamics.

## Tools

| Tool | Purpose |
| --- | --- |
| `list_all` | Catalog all 7 primary systems and 12 named patterns |
| `get_system_info` | Detailed info on a Panksepp system (neural basis, IS vulnerability, political bridge) |
| `get_pattern_info` | Detailed info on a named pattern (substrate, blind spots, leverage points) |
| `analyze_behavior` | Structured 5-step ASEKE analysis of any behavioral situation |
| `match_patterns` | Signal-based pattern matching against the 12-pattern library |
| `bridge_to_political` | Map system activation to DPM (RWA/SDO)\* with timescale caveats |

\*This tool uses the Dual Process Model (DPM) to map biological emotional systems to political psychology dimensions—specifically Right-Wing Authoritarianism (RWA) and Social Dominance Orientation (SDO).

## Biological Vocabulary: Panksepp's Seven Systems

| System | Role | IS Vulnerability |
| --- | --- | --- |
| **SEEKING** | Curiosity, exploration, goal-pursuit | IS acquisition gateway — hooks curiosity first |
| **RAGE** | Obstacle removal, boundary defense | Requires a target — demagogic IS provides one |
| **FEAR** | Threat detection, escape | Primary authoritarian IS substrate (→ RWA) |
| **PANIC/GRIEF** | Separation distress, bonding need | Desperate belonging-seeking — cults, movements recruit here |
| **CARE** | Nurturing, protection | Circle width determines SDO axis position |
| **PLAY** | Social joy, boundary-testing | Resistant to IS but weaponizable (trolling) |
| **LUST** | Reproductive motivation | LUST+FEAR = purity politics |

## Pattern Library

12 named patterns synthesizing established research: Scapegoat Pivot, Coherence Timeout, Comfort Trap, Burnout Cascade, Algorithmic Escalation, Mirror Conflict, IS Competition, Institutional Mood, Virtue Fortress, Authority Transfer, Narrative Gravity Well, Identity Lock-In.

## Setup

Clone or fork the repository.

```
cd ~/aseke-compass-mcp
npm install
npx tsc
```

### Claude Desktop Config

Add to `~/.config/Claude/claude_desktop_config.json`:

```
{
  "mcpServers": {
    "aseke-compass": {
      "command": "/home/<your_username>/.nvm/versions/node/<your_node_version>/bin/node",
      "args": ["/your/path/to/aseke-compass-mcp/dist/index.js"]
    }
  }
}
```

Restart Claude Desktop after config changes.

## Provenance

**Empirical foundations**: Panksepp (1998), Duckitt & Sibley (2009), Jost & Banaji (1994), Milgram (1963), Kahneman (2011), Sweller (1988), Kahan (2017), Russell (1980), and others.

**Framework contributions**: ASEKE (Hall) — IS capture of primary emotional system output via CE efficiency. [EFHF (Hall)](https://github.com/angrysky56/Emergent-Functional-Hierarchies-Framework) — lumpability, coherence windows. Boundary Conditions (Hall, 2026) — ethical behavior as structurally weaker boundary condition.

The seven primary emotional systems are established cross-species neuroscience. The pattern library synthesizes established findings into original analytical tools. See the companion SKILL.md for full analysis.