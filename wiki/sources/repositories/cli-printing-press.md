---
summary: Agent-first CLI generator that reverse-engineers APIs and prints Go CLI + MCP server + Claude Code skill for any API or website. Local SQLite, compound commands, NOI-driven design.
tags: [cli, mcp, agent-native, sqlite, go, api-generation]
updated: 2026-05-10T03:41:50Z
created: 2026-05-10T03:41:50Z
---

# CLI Printing Press

> **Source:** [mvanhorn/cli-printing-press](https://github.com/mvanhorn/cli-printing-press) — archived to [[Clippings/repositories/2026/cli-printing-press]]

## What It Is

An agent-first CLI generator that reads official API docs, studies every competing CLI/MCP server, sniffed undocumented APIs (Google Flights, Dominos, ESPN), and prints a **Go CLI + MCP server + Claude Code skill** for any API or website. No OpenAPI spec required — it reverse-engineers APIs from browser traffic.

Three printed CLIs exist today: ESPN (sniffed, no official API), flight-goat (Kayak + sniffed Google Flights), and linear-pp-cli (50ms queries against local SQLite).

## Core Architecture

- **Dual interface:** Every API gets a Cobra CLI (`<api>-pp-cli`) and MCP server (`<api>-pp-mcp`). Same client, same store, same auth. Shell agents use CLI; IDE agents use MCP.
- **Local-first data layer:** High-gravity resources get domain-specific SQLite tables (not JSON blobs), FTS5 full-text search, cursor-based incremental sync. `sync` → `search` → `sql` all offline.
- **Compound commands:** `stale`, `health`, `bottleneck`, `reconcile` — join across resources and analyze history. Stateless API wrappers cannot do this.
- **Agent-native by default:** Auto-JSON when piped (no `--json`), `--compact` drops to high-gravity fields (60-80% fewer tokens), typed exit codes (0/2/3/4/5/7) for self-correction, `--dry-run` for exploration.

## The Non-Obvious Insight (NOI)

Every API has a secret identity — the data it exposes is useful for something its creators never designed for. The NOI is Phase 0's mandatory creative DNA:

| API | Obvious | Non-obvious |
|-----|---------|-------------|
| Discord | Chat app | Searchable knowledge base |
| Linear | Issue tracker | Team behavior observatory |
| Stripe | Payment processor | Business health monitor |
| GitHub | Code host | Engineering culture fingerprint |

## Pipeline Phases

1. **Phase 0:** Research → write NOI (mandatory, cannot skip)
2. **Phase 1:** Generate spec from research + sniffed traffic
3. **Phase 2:** Verification (scorecard, dogfood, proof-of-behavior, live smoke test)
4. **Phase 3:** Generate Go CLI + MCP server (Codex mode: 60% fewer Opus tokens)
5. **Phase 4:** Polish + publish to [printingpress.dev](https://printingpress.dev)

## Connections

- [[printing-press]] — the project itself
- [[sqlite]] — local-first data layer
- [[fts5]] — full-text search indexing
- [[mcp]] — dual interface generation
- [[cobra]] — Go CLI framework used
- [[agent-native-design]] — design philosophy
- [[compound-commands]] — cross-resource analysis
- [[non-obvious-insight]] — the NOI concept
- [[peter-steinberger]] — discrawl/gogcli inspiration
- [[anthropic]] — Claude Desktop as target agent
