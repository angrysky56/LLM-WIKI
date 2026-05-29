---
created: 2026-05-22
updated: 2026-05-22
type: source
summary: CodeGraph v1.0.0 — AST-based semantic code knowledge graph with MCP server for AI coding agents
tags: [codegraph, mcp, tree-sitter, sqlite, code-indexing, ai-agents]
sources: https://github.com/colbymchenry/codegraph
status: active
confidence: 0.95
---

# CodeGraph README

## Core Concept

CodeGraph builds a semantic knowledge graph of codebases for faster, smarter code exploration by AI coding agents. It indexes source code via tree-sitter AST parsing, stores symbol relationships in a local SQLite database, and exposes an MCP server for agents to query. Zero external dependencies — 100% local, no API keys.

**Core claim**: 35% cheaper · 59% fewer tokens · 49% faster · 70% fewer tool calls vs. non-indexed exploration (benchmarked on VS Code, Excalidraw, Django, Tokio, OkHttp, Gin, Alamofire).

## Key Points

- **Extraction**: tree-sitter parses source into ASTs; language-specific queries extract nodes (functions, classes, methods) and edges (calls, imports, extends, implements)
- **Storage**: local SQLite (`.codegraph/codegraph.db`) with FTS5 full-text search; WAL journal mode for concurrent reads
- **Auto-Sync**: native OS file watchers (FSEvents/inotify/ReadDirectoryChangesW), debounced 2-second quiet window, incremental sync
- **Supported languages**: TypeScript, JavaScript, Python, Go, Rust, Java, C#, PHP, Ruby, C, C++, Swift, Kotlin, Scala, Dart, Svelte, Vue, Svelte, Liquid, Pascal/Delphi, Lua, Luau
- **Framework-aware routing**: Django, Flask, FastAPI, Express, NestJS, Laravel, Drupal, Rails, Spring, Gin/chi/gorilla/mux, Axum/actix/Rocket, ASP.NET, Vapor, React Router/SvelteKit
- **CLI**: `codegraph init`, `sync`, `status`, `query`, `files`, `context`, `affected`, `serve --mcp`
- **MCP tools**: `codegraph_search`, `codegraph_context`, `codegraph_callers`, `codegraph_callees`, `codegraph_impact`, `codegraph_node`, `codegraph_files`, `codegraph_status`
- **Files >1MB skipped** (generated bundles, minified JS); respects `.gitignore` automatically
- **Hermes integration**: index at `~/.codegraph/` covers 61,909 files, 1,019,424 nodes; agents should spawn Explore subagent for large context retrieval

## Connections
- [[sources/documentation/codegraph-readme]]
- [[wiki/index]]
- [[codegraph-readme]]

- [[codegraph-hermes-phase1-implementation]] — Hermes Phase 1 EventBus implementation uses CodeGraph for codebase indexing