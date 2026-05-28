---
created: 2026-05-26T00:00:00Z
updated: 2026-05-26T00:00:00Z
type: source
summary: GBrain — personal/company knowledge brain with graph-extracted entity edges, synthesis layer, and 24/7 dream cycle. 146K+ pages, P@5 49.1%, R@5 97.9%. Bun/PGLite, MCP server for agent integration.
tags: [knowledge-brain, knowledge-graph, synthesis, memory-system, personal-kg, multi-agent, mcp, bun]
sources: https://github.com/garrytan/gbrain
status: reference
confidence: 0.85
---

## Core Insight

GBrain is a personal/company knowledge brain built by Garry Tan (YC President). It ingests pages, extracts typed entity edges without LLM calls, synthesizes actual answers with citations, and runs a 24/7 dream cycle for overnight consolidation and citation fixing. The key differentiation from vector-only RAG: graph traversal reaches relationships vector search can't, and the synthesis layer gives you answers not page lists.

**For Hermes integration**: useful as an adjunct knowledge source (ingest external data into GBrain's graph, query from Hermes), and the code patterns for entity extraction, graph edge creation, and synthesis are directly portable.

## Key Claims

| Feature | Detail |
|---------|--------|
| **Synthesis layer** | Actual answers with citations + gap analysis, not matching chunks |
| **Graph extraction** | Typed edges (`works_at`, `invested_in`, `founded`) — zero LLM calls |
| **Benchmarks** | P@5 49.1%, R@5 97.9%, +31.4pts P@5 over graph-disabled |
| **Scale** | 146,646 pages, 24,585 people, 5,339 companies (Garry's deployment) |
| **Skills system** | 43+ skill packs (citation-fixer, brain-pdf, article-enrichment, etc.) |
| **Dream cycle** | 24/7 overnight: ingest, enrich, consolidate, fix citations |
| **Company brain mode** | Per-user data scoping, zero cross-talk verified |
| **Install** | `bun install -g github:garrytan/gbrain`, `gbrain init`, ~30 min |

## Architecture (relevant to Hermes/LLM-WIKI)

### Stack
- **Runtime**: Bun (canonical path — not Node, not Deno)
- **Default DB**: PGLite (embedded, no server, 2-sec startup)
- **Scale path**: Postgres + pgvector via Supabase
- **Agent integration**: MCP server (`src/mcp/server.ts`)
- **CLI**: `src/cli.ts` — trusted local callers set `OperationContext.remote = false`
- **Agent-facing**: MCP server sets `remote = true`, tightens filesystem confinement

### Trust boundary
GBrain distinguishes **trusted local CLI** (`remote = false`) from **untrusted agent-facing** (`remote = true`). Security-sensitive operations tighten filesystem confinement when `remote = true`. See `src/core/operations.ts` for the contract.

```typescript
// src/core/operations.ts — OperationContext contract
interface OperationContext {
  remote: boolean;  // false = CLI, true = MCP/agent-facing
}
```

### Entity/graph extraction (no LLM)
`src/core/skillpack/harvest.ts` — every page write extracts entity refs and creates typed edges without LLM calls. This is the pattern most relevant to LLM-WIKI's knowledge graph goals.

### Synthesis pipeline
```
query → graph traversal + vector search → synthesis layer → answer + citations + gap analysis
```

The synthesis layer is what makes GBrain different from a fancy vector store. The gap analysis ("heads up: nothing added to the brain about X in 6 weeks") is the feature that changes how you use the brain.

### Skill pack system
43+ skill packs in `skills/` — each is a self-contained module for a specific task (citation-fixer, brain-pdf, archive-crawler, etc.). The skill dispatcher at `skills/RESOLVER.md` routes incoming tasks to the appropriate skill.

## What to Steal / Integrate

### High-value patterns for Hermes/LLM-WIKI

1. **Entity edge extraction without LLM** — `src/core/skillpack/harvest.ts`
   - GBrain extracts typed edges from pages using deterministic parsing, not LLM calls
   - This is the +31.4pt P@5 gain over graph-disabled variant
   - Directly applicable to LLM-WIKI's knowledge graph goals

2. **Synthesis layer** — the answer + citation + gap analysis pattern
   - LLM-WIKI currently surfaces source pages; GBrain-style synthesis would give actual answers
   - The gap analysis section is novel and valuable

3. **MCP server for agent integration** — `src/mcp/server.ts`
   - GBrain's MCP server is the canonical pattern for Hermes → GBrain communication
   - Hermes could serve as the MCP client querying GBrain's brain

4. **Skills/conventions system** — `skills/conventions/brain-routing.md`
   - When to switch brain, when to switch source, cross-brain federation
   - Applicable to multi-brain Hermes setups

### Lower-value / skip
- **Bun runtime** — Hermes runs on Python/Node; Bun-specific code not portable
- **Skill pack ecosystem** — 43 skills are domain-specific to personal productivity; LLM-WIKI has different needs
- **Company brain multi-tenancy** — not relevant to single-user Hermes/LLM-WIKI setup

## File Map (key files for integration work)

| Path | Purpose |
|------|---------|
| `src/core/skillpack/harvest.ts` | Entity edge extraction without LLM |
| `src/core/contextual-retrieval-service.ts` | Graph + vector hybrid retrieval |
| `src/mcp/server.ts` | MCP server (agent integration) |
| `src/mcp/tool-defs.ts` | MCP tool definitions |
| `src/core/operations.ts` | OperationContext trust boundary |
| `src/core/skillpack/installer.ts` | Skill pack installation |
| `skills/RESOLVER.md` | Skill dispatcher |
| `INSTALL_FOR_AGENTS.md` | Full install protocol for agents |
| `CLAUDE.md` | Architecture reference for Claude Code |

## Install / Deploy Notes

GBrain is designed for AI agent installation (not manual setup):

```bash
# Canonical install via Bun
curl -fsSL https://bun.sh/install | bash
export PATH="$HOME/.bun/bin:$PATH"
bun install -g github:garrytan/gbrain

# Init (PGLite default — no server needed)
gbrain init

# Post-install verification
gbrain doctor
```

For Hermes integration: install GBrain alongside Hermes, configure Hermes as the MCP client, point at GBrain's brain for knowledge queries.

## Connections
- [[index]]
- [[sources/repositories/gbrain]]
- [[gbrain]]

- [[knowledge-graph]] — graph-based memory/retrieval
- [[synthesis-layer]] — generative answer synthesis over retrieved context
- [[mcp-model-context-protocol]] — agent tool integration protocol
- [[openclaw]] — related agent platform (GBrain author also created OpenClaw)
- [[paperclip]] — orchestration layer for multi-agent systems
- [[hermes-agent]] — this system's agent; potential GBrain integration target
- [[llm-wiki]] — this vault; GBrain integration via MCP or edge-pattern borrowing