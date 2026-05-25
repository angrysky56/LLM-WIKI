# CodeGraph README

**Source:** npm package `@colbymchenry/codegraph` v1.0.0
**Repo:** https://github.com/colbymchenry/codegraph
**License:** MIT

## What It Is

CodeGraph builds a semantic knowledge graph of codebases for faster, smarter code exploration by AI coding agents. It indexes source code via tree-sitter AST parsing, stores symbol relationships in a local SQLite database, and exposes an MCP server for agents to query.

**Core claim:** 35% cheaper · 59% fewer tokens · 49% faster · 70% fewer tool calls vs. non-indexed exploration on VS Code, Excalidraw, Django, Tokio, OkHttp, Gin, Alamofire.

## How It Works

1. **Extraction** — tree-sitter parses source into ASTs. Language-specific queries extract nodes (functions, classes, methods) and edges (calls, imports, extends, implements).
2. **Storage** — local SQLite (`.codegraph/codegraph.db`) with FTS5 full-text search. 100% local, no API keys.
3. **Resolution** — references resolved: calls→definitions, imports→source files, class inheritance, framework patterns.
4. **Auto-Sync** — file watcher uses native OS events (FSEvents/inotify/ReadDirectoryChangesW), debounced 2-second quiet window, incremental sync. Graph stays fresh as you code.

## MCP Tools

| Tool | Purpose |
|------|---------|
| `codegraph_search` | Find symbols by name |
| `codegraph_context` | Build code context for a task |
| `codegraph_callers` | Find what calls a function |
| `codegraph_callees` | Find what a function calls |
| `codegraph_impact` | Analyze affected code radius |
| `codegraph_node` | Get single symbol details |
| `codegraph_files` | Get indexed file structure |
| `codegraph_status` | Check index health and stats |

## CLI Commands

```bash
codegraph init [path]       # Initialize + index
codegraph sync [path]       # Incremental update
codegraph status [path]     # Statistics
codegraph query <search>    # Symbol search
codegraph files [path]      # File structure
codegraph context <task>    # Build AI context
codegraph affected [files]  # Find affected tests
codegraph serve --mcp       # Start MCP server
codegraph install           # Auto-configure agents
```

## Framework-Aware Routes

Recognizes routing in: Django, Flask, FastAPI, Express, NestJS, Laravel, Drupal, Rails, Spring, Gin/chi/gorilla/mux, Axum/actix/Rocket, ASP.NET, Vapor, React Router/SvelteKit.

## Supported Languages

TypeScript, JavaScript, Python, Go, Rust, Java, C#, PHP, Ruby, C, C++, Swift, Kotlin, Scala, Dart, Svelte, Vue, Liquid, Pascal/Delphi, Lua, Luau.

## Benchmark Results (7 repos, Claude Code headless)

| Codebase | Language | Cost | Tokens | Time | Tool calls |
|----------|----------|------|--------|------|------------|
| VS Code | TypeScript | 35% cheaper | 73% fewer | 41% faster | 72% fewer |
| Excalidraw | TypeScript | 47% cheaper | 73% fewer | 60% faster | 86% fewer |
| Django | Python | 34% cheaper | 64% fewer | 59% faster | 81% fewer |
| Tokio | Rust | 52% cheaper | 81% fewer | 63% faster | 89% fewer |
| OkHttp | Java | 17% cheaper | 41% fewer | 36% faster | 64% fewer |
| Gin | Go | 22% cheaper | 23% fewer | 34% faster | 19% fewer |
| Alamofire | Swift | 38% cheaper | 59% fewer | 51% faster | 77% fewer |

## Agent Integration

The README notes: "NEVER call `codegraph_explore` or `codegraph_context` directly in the main session — these return large amounts of source code. Instead, ALWAYS spawn an Explore agent."

For Hermes Agent: `codegraph` is already wired via MCP. The index at `~/Repositories/ai_workspace/.codegraph/` covers 61,909 files, 1,019,424 nodes.

## Key Design Notes

- Zero config — respects `.gitignore` automatically
- Files >1MB skipped (generated bundles, minified JS)
- WAL journal mode for concurrent reads
- Self-contained bundle (Node runtime included) — works without Node.js installed
- Index stored at `.codegraph/codegraph.db` per project
