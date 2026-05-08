---
summary: Designing a hierarchical multi-agent system on Discord using Hermes harness — 3-tier architecture with mention-based routing, validated by Anthropic's Multiagent Sessions
tags: [multi-agent, discord, hermes-agent, orchestration, architecture, mcp]
updated: 2026-05-08T01:28:37Z
created: 2026-05-08T01:28:37Z
---

# Hermes Agents Running in Discord — Multi-Agent Architecture

**Source:** [Gemini conversation](https://gemini.google.com/app/4d241e0651a9bd1f) (2026-05-07)
**Type:** Design exploration — multi-agent system on Discord

## Core Idea

Using Discord as a visual UI for a hierarchical Multi-Agent System (MAS) built on Hermes Agent harness instances, each with distinct tools and personas. The architecture maps Discord's native structure (channels + threads) onto a DAG of agent interactions.

## Architecture: 3-Tier Hierarchy

### Tier 1: Main Orchestrator (Root)
- Lives in the main Discord channel
- Routes user requests to appropriate Agency Orchestrators
- Only displays high-level requests and final outputs — keeps channel clean

### Tier 2: Agency Orchestrators (Managers)
- Lives in dedicated Discord threads (`#research-agency`, `#logic-agency`, `#graph-agency`)
- Breaks macro-tasks into micro-tasks
- Coordinates sub-agents, synthesizes results, reports back to Main Orchestrator

### Tier 3: Tool-Centric Sub-Agents (Specialists)
- Each bound to a specific MCP server or capability
- Examples: Logic agent (mcp-logic), Graph agent (Neo4j/Cypher), Research agent, Forecasting agent (TimesFM)
- Designed around their tools — stripped-down prompts, single-purpose

## Key Technical Considerations

- **Mention-based routing**: Bots only respond when `@mentioned`, preventing runaway loops
- **Bot-ignore override**: Discord bots default to ignoring other bots; needs `allowBots: "mentions"` config
- **Rate limits**: Essential to prevent token-burning infinite loops
- **Hermes harness advantages**: Persistent memory, automated skill creation, native MCP integration

## Industry Validation

- **Anthropic Multiagent Sessions** (released May 7, 2026 — same day as this conversation): Claude API now supports Coordinator → Sub-agent fanout with isolated session threads. Same architectural pattern.
- **GitHub issue #50806**: Developer running 7 Hermes instances with mention-based Discord routing. Real friction: bot-ignore config.

## Relevance to LLM-WIKI

This architecture is the execution layer for domain knowledge workflows. The Synapse/Neo4j pipeline provides the knowledge substrate; the Discord agent swarm provides the execution and interaction surface. Together they form a complete agentic knowledge-work platform.
