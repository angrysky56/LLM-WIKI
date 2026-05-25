# 🧠 LLM-WIKI

> **The self-compounding Zettelkasten knowledge graph & autonomous agent thinking layer.**

LLM-WIKI is a persistent, structured, and self-maintaining Zettelkasten knowledge vault. Evolving beyond static search or stateless RAG, it serves as the **epistemic core and thinking/writing layer** of a fully autonomous, multi-agent development and research ecosystem.

The system is built on a simple yet powerful architectural principle:

> **"Code stays in its repository; the _why_, the _implications_, and _what we learned_ lives in the wiki."**

Inspired by **[Andrej Karpathy's LLM-maintained Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**, this project has evolved into a production-grade, graph-backed knowledge ecosystem that is ingested, structured, audited, and synthesized entirely on autopilot by scheduled AI agents.

---

## 🗺️ System Architecture

LLM-WIKI sits at the absolute center of the autonomous workspace. It acts as the shared database of context for all agents, human operators, and semantic tools.

```
                  ┌──────────────────────────────────────────────────────────┐
                  │                 INGESTION INBOX SOURCES                  │
                  │   Google RSS Feeds | arXiv PDFs | Obsidian Clippers      │
                  └────────────────────────────┬─────────────────────────────┘
                                               │
                                               ▼
                  ┌──────────────────────────────────────────────────────────┐
                  │                       raw/ inbox                         │
                  │     (Queue view managed via raw-inbox.base in Obsidian)  │
                  └────────────────────────────┬─────────────────────────────┘
                                               │
                                               ▼
                  ┌──────────────────────────────────────────────────────────┐
                  │            AUTONOMOUS OPERATIONAL AGENTS                 │
                  │   (Orchestrated via hermes-ops cron & hermes-agent CLI)  │
                  │   Ingest | News | ArXiv | Researcher | Librarian | etc.  │
                  └───────┬──────────────────────────────────────────┬───────┘
                          │                                          │
                          │ Ingests, Summarizes,                     │ Reads/Writes State
                          │ Links, and Clusters                      │ via Markovian Carryover
                          ▼                                          ▼
┌───────────────────────────────────────────────────┐      ┌─────────────────────────┐
│              project-synapse-mcp                  │      │    wiki/scratchpad/     │
│  (Montague Grammar parsing + HITS link scoring)   │◄────►│  (Agent Sheet Rules,    │
└─────────────────────────┬─────────────────────────┘      │   Central Task Board,   │
                          │                                │   Carryover Reports)    │
                          ▼                                └─────────────────────────┘
┌────────────────────────────────────────────────────────────────────────────────────┐
│                             KNOWLEDGE STORAGE LAYER                                │
│          Neo4j (Graph + Vector Store)   ◄───►   Obsidian (Markdown Vault)          │
└────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 📂 Vault Structure

To maintain high data integrity and prevent structural decay, the vault enforces a rigorous multi-layer directory structure:

```
LLM-WIKI/
├── raw/                             # INBOX — Ingested documents queued for parsing
├── raw-inbox.base                   # Queue view of pending raw/ files in Obsidian
├── clippings-archive.base           # Browsable view of all historical clippings
│
├── Clippings/                       # SOURCE ARCHIVE — Original unaltered media (by type/year)
│   ├── papers/YYYY/                 # Academic preprints and peer-reviewed studies (PDF/Markdown)
│   ├── articles/YYYY/               # Tech blogs, newsletter breakdowns, and web captures
│   ├── documentation/YYYY/          # API specs, manuals, frameworks, and system skills
│   └── repositories/YYYY/           # Repository source overviews and dependency layouts
│
└── wiki/                            # LLM-GENERATED KNOWLEDGE LAYER (Zettelkasten)
    ├── index.md                     # Structural Table of Contents (auto-rebuilt by librarian)
    ├── concept-index.md             # Semantic Index mapping concepts by meaning, not structure
    ├── log.md                       # Append-only ledger of agent activity and schema updates
    │
    ├── sources/                     # COMPRESSED SUMMARIES — Mirrors Clippings/ structure
    │   ├── papers/                  # Distilled summaries of academic papers (arXiv, journals)
    │   ├── articles/                # Summarized tech articles and web clippings
    │   ├── documentation/           # Summarized specifications and tool skills
    │   └── repositories/            # Summarized structural analysis of codebases
    │
    ├── entities/                    # REFERENCE PAGES — Specific named things
    │   ├── tools/                   # Frameworks, packages, libraries, models, databases
    │   ├── people/                  # Researchers, engineers, practitioners
    │   └── projects/                # Specific projects, system components, subsystems
    │
    ├── concepts/                    # STABLE REFERENCE PAGES — General ideas, theories, patterns
    │
    ├── research/                    # Active research campaigns from the Researcher Agent
    │   └── index.md                 # Active and archived research project registry
    │
    ├── synthesis/                   # ORIGINAL SYNTHESIS — Cross-domain insights & system guides
    │
    └── scratchpad/                  # AGENT OPERATIONAL RUNTIME (The Agent Sandbox)
        ├── agent-sheets/            # Execution blueprints read by cron agents at startup
        └── jobs/
            ├── sheet.md             # Central system task board and cron status tracker
            └── reports/{agent}/     # Agent session reports and Markovian carryover files
```

---

## ⚡ Zettelkasten Knowledge Layers

The knowledge base is structured to transition raw information into high-confidence synthesized knowledge:

| Layer         | Folder            | Epistemic Status     | Purpose                                                                   |
| :------------ | :---------------- | :------------------- | :------------------------------------------------------------------------ |
| **Raw Media** | `Clippings/`      | Raw Data             | Exact, unaltered captures of the original source material.                |
| **Summaries** | `wiki/sources/`   | Distilled Source     | Highly compressed, unified summaries of ingested clippings.               |
| **Entities**  | `wiki/entities/`  | Reference Object     | Objectively verifiable named entities (tools, projects, people).          |
| **Concepts**  | `wiki/concepts/`  | Reference Idea       | Stable, external theories, paradigms, and patterns (e.g., GraphRAG, MOP). |
| **Synthesis** | `wiki/synthesis/` | Materialized Insight | Original thinking, cross-domain insights, and internal operating guides.  |

---

## 🤖 Agent Operational Layer (`wiki/scratchpad/`)

Instead of utilizing ephemeral prompts or external databases, **LLM-WIKI is the actual control center** for the scheduled cron agents configured in [hermes-ops](https://github.com/angrysky56/hermes-ops).

1. **Agent Blueprints (`scratchpad/agent-sheets/`)**: Standardized runtime instructions loaded by each agent on boot (e.g., `news.md`, `arxiv.md`, `librarian.md`, `insights.md`).
2. **Central Task Board (`scratchpad/jobs/sheet.md`)**: A human-and-agent readable log registering active job runs, status, and pending tasks.
3. **Carryover Reports (`scratchpad/jobs/reports/{agent}/carryover.md`)**: The core mechanism of the **Markovian Carryover Protocol**.

### 🔄 The Markovian Carryover Protocol

To support long-horizon, multi-step tasks across isolated execution sessions without context loss, agents pass their cognitive state forward using a structured, bounded template inside the wiki:

```markdown
## CarryoverState

### Established

- **[Entity/Fact]** What was confirmed, resolved, or written during this session (with citations).

### Open

- **[Question/Risk]** Crucial uncertainties or blockers that need resolution in the next run.

### Heading

- **[Intent]** High-priority next steps and immediate priorities for the next activation.
- **[Constraint]** Time, API, or execution limits for the next run.
```

_Rules:_ To prevent context bloat, the carryover file is strictly capped at **~512 tokens**. At the end of every scheduled run, the agent writes its updated carryover. On the subsequent run, the incoming agent reads this file, bootstrapping its memory with perfect precision.

---

## ⚖️ Dual-Council Architecture & The Refuser

For high-stakes system evolution, the wiki integrates a **two-council autonomous alignment and validation framework**:

- **The Research Council (Philosophical)**: Elemates philosophical and ethical depth. Utilizes a slow, non-closed-loop "spiral architecture" and the **Weil-Gate** ("Who does this change hurt?") to audit systemic implications.
- **The Technical Working Group (Engineering)**: Grounded in rigorous engineering and real-world failure patterns (e.g., Therac-25, DynamoDB 2015 outage, Knight Capital failure).
- **The Refuser Pattern**: An autonomous agent holding a hard veto deploy token. Operating on the principle: `Unnamed + Plausible + Non-Reversible = VETO`.

This system is fully documented within the wiki at `wiki/synthesis/two-council-architecture.md`.

---

## 🛠️ System Integration & Custom Tooling

LLM-WIKI is tightly coupled with **[Project Synapse](https://github.com/angrysky56/project-synapse-mcp)**, a custom Model Context Protocol (MCP) server that provides direct semantic tools for managing the wiki:

| Custom MCP Tool               | Function / Pipeline Trigger                                                          |
| :---------------------------- | :----------------------------------------------------------------------------------- |
| `wiki_fetch_url(url)`         | Downloads, defuddles, ingests, archives, and summarizes web assets.                  |
| `wiki_ingest_raw(file)`       | Parses a file in `raw/`, determines its type, and routes it to `Clippings/`.         |
| `wiki_write_page(path, body)` | Writes standard frontmatter-compliant Markdown pages.                                |
| `wiki_lint()`                 | Scans the vault for orphans, dead links, frontmatter debt, and tag anomalies.        |
| `wiki_hits_analysis()`        | Scores vault pages using the HITS algorithm to find structural hubs and authorities. |
| `wiki_cluster_pages()`        | Employs Group Average Agglomerative Clustering (GAAC) to identify missing links.     |
| `query_knowledge(query)`      | Executes a 4-stage semantic search (Entity matching → RRF → Graph traversals).       |
| `explore_connections(entity)` | Performs deep Neo4j graph traversals for discovery.                                  |
| `generate_insights()`         | Runs the Zettelkasten engine to synthesize high-confidence insights.                 |

---

## 🚦 Getting Started (Workflows)

### 1. Ingesting Web Articles & Clippings

If you find a research paper or article:

1. Clip it using the **Obsidian Clipper** browser extension or download the PDF.
2. Place the file inside the `raw/` directory.
3. The scheduled `ingest-agent` will automatically process the file, indexing it in Neo4j, archiving it in the correct `Clippings/` subfolder, and creating a unified summary page in `wiki/sources/`.

### 2. Manual Reading & Exploration

1. Open the LLM-WIKI folder as a local vault in **[Obsidian](https://obsidian.md/)**.
2. Install the **Obsidian Git** plugin to track history and sync with your upstream remote repository.
3. Open `raw-inbox.base` to see files currently in the queue, or open `clippings-archive.base` to browse raw clippings.
4. Explore connections visually using Obsidian's Graph View or semantically by querying the Synapse MCP server.

### 3. Maintaining Vault Health

To run the automated health check and update the structural index:

```bash
# Triggers the Librarian Agent's full audit protocol
hermes delegate --profile librarian-agent --goal "Run full vault audit, clean frontmatter, and resolve orphaned pages."
```

---

## 🔗 Connected Repositories

- **[hermes-ops](https://github.com/angrysky56/hermes-ops)**: The operational schedules, cron files, skills, and agent sheets running the system.
- **[project-synapse-mcp](https://github.com/angrysky56/project-synapse-mcp)**: The custom Montague-grammar semantic parser and Neo4j graph connector.
- **[hermes-agent](https://github.com/NousResearch/hermes-agent)**: The core multi-platform autonomous agent runtime.

---

## 📜 License

MIT License. Evolve your own knowledge graph, build deep context, and let your agent systems compound their understanding on autopilot.
