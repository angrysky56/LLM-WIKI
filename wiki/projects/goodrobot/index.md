---
updated: 2026-05-13T00:20:20Z
created: 2026-05-13T00:20:20Z
---

# GoodRobot

> Zero-human AI agent company simulation with ethics board oversight

---

## Overview

GoodRobot is a Paperclip-managed zero-human company. The board consists of NGOs and think tanks. Executives run via heartbeat on `hermes_local` with MiniMax-M2.7 model.

**Paperclip Company ID:** `d8634ba3-4e46-468e-ba26-d07f4d90f85b`

## Key Documents

- [[business-concept]] — Problem statement, target market, value proposition
- [[revenue-model]] — Pricing tiers, unit economics, financial projections
- [[roadmap]] — 30-day through multi-year milestones
- [[hiring-plan]] — Org structure, hiring phases, board composition
- [[local-lead-gen]] — Son's validated business plan (~$2,500/mo, ~31 clients)
- [[issues-index]] — Full issue list from Paperclip

## Current Status

- 9 completed deliverables in Paperclip (now synced to wiki)
- 5 in-progress executive tasks (empty stubs — agents working on them)
- Board operating as simulation (proposes $1M capital projects despite ~$100 actual budget)

## Architecture

```
Board (NGOs/Think Tanks)
    └── CEO (hermes_local, MiniMax-M2.7)
        ├── CFO
        ├── CMO
        └── CTO
```

## Sync Status

Issues exported from Paperclip → Obsidian on 2026-05-13. Plugin install blocked by Paperclip server regression (SQL validation bug in plugin install API).
