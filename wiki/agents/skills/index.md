# Agents & Skills Master Catalog

> **Sources:** Skill files at `~/.hermes/skills/agent-sheets/` and `~/.hermes/skills/autonomous-ai-agents/`  
> **Wiki root:** `/home/ty/Documents/LLM-WIKI`  
> **Last updated:** 2026-06-09

This catalog covers the full agent fleet: 7 scheduled (cron) agents and 2 manual-only agents.

---

## Scheduled Agents

All scheduled agents run as Hermes cron jobs with `enabled_toolsets`:

```
terminal, file, read_file, web, search, skills, search_files, session_search, patch, write_file
```

> ⚠️ **Critical:** `patch` must be in `enabled_toolsets` — without it, `patch` calls silently fail and the job shows `last_status: ok` while work was skipped. See `references/cron-toolsets.md`.

| Cron ID | Name | Schedule | Skills | Toolset | Key Paths |
|---------|------|----------|--------|---------|-----------|
| `8ea33cfa560a` | Wiki Researcher | daily | researcher-agent | MCP + toolsets | `wiki/scratchpad/agent-sheets/researcher.md` |
| `72599f850df2` | arxiv-top3-weekly | weekly | arxiv-agent | MCP + toolsets | `wiki/scratchpad/agent-sheets/arxiv.md` |
| `eaaa6bdc8503` | world-news-daily | daily | news-agent | MCP + toolsets | `wiki/scratchpad/agent-sheets/news.md` |
| `c838e81a1496` | llm-wiki-raw-ingest | daily | ingest-agent | MCP + toolsets | `wiki/scratchpad/agent-sheets/ingest.md` |
| `48a3a009a820` | Wiki Librarian | daily | librarian-agent | MCP + toolsets | `wiki/scratchpad/agent-sheets/librarian.md` |
| `385aa0819a57` | Wiki Librarians-Assistant | daily (~08:50 AM, after librarian) | librarians-assistant | MCP + toolsets | `wiki/scratchpad/agent-sheets/librarians-assistant.md` |
| `723e76246970` | Wiki Insights Generator | daily (06:00 AM) | insights-agent | MCP + toolsets | `wiki/scratchpad/agent-sheets/insights.md` |

### Detail

#### Wiki Researcher (`researcher-agent`)
- **Cron ID:** `8ea33cfa560a`
- **Schedule:** daily
- **Trigger:** `/researcher-agent`
- **Skills:** `query_knowledge`, `explore_connections`, `generate_insights`, `wiki_search`, `wiki_write_page`, `wiki_fetch_url`
- **Toolsets:** `terminal`, `file`, `web`, `search`, `skills`, `search_files`, `session_search`, `patch`, `write_file`
- **Model:** `minimax/MiniMax-M2.7` (required — scheduler rejects `model=null`)
- **Reports to:** `#research` Discord channel (`1505826045511602176`)
- **Key paths:**
  - Agent sheet: `wiki/scratchpad/agent-sheets/researcher.md`
  - Carryover: `wiki/scratchpad/jobs/reports/researcher/carryover.md`
  - Reports: `wiki/scratchpad/jobs/reports/researcher/`
  - Concepts: `wiki/concepts/`
  - Gap patterns: `~/.hermes/skills/agent-sheets/researcher-agent/references/gap-discovery-patterns.md`
- **Notes:** Stub-first discovery; carryover-driven gap prioritization; MCP graph tools unavailable → fallback to `terminal` + `wiki_search`

#### arxiv-top3-weekly (`arxiv-agent`)
- **Cron ID:** `72599f850df2`
- **Schedule:** weekly
- **Trigger:** `/arxiv-agent`
- **Skills:** `mcp_arxiv_mcp_server_search_papers`, `wiki_write_page`, `wiki_fetch_url`
- **Toolsets:** `terminal`, `file`, `web`, `search`, `skills`, `search_files`, `session_search`, `patch`, `write_file`
- **Reports to:** `#research` Discord channel (`1505826045511602176`)
- **Key paths:**
  - Agent sheet: `wiki/scratchpad/agent-sheets/arxiv.md`
  - Paper storage: `/home/ty/Documents/paper-research/`
  - Source pages: `wiki/sources/papers/`
  - Carryover: `wiki/scratchpad/jobs/reports/arxiv/carryover.md`
- **Notes:** PDFs go to `paper-research/` only (NOT wiki/sources/papers/ or Obsidian); HTML list page fallback when API rate-limited; MCP unavailable → `curl` fallback immediately

#### world-news-daily (`news-agent`)
- **Cron ID:** `eaaa6bdc8503`
- **Schedule:** daily
- **Trigger:** `/news-agent`
- **Skills:** RSS discovery via `terminal` + `curl`, `wiki_write_page`, `wiki_lint`
- **Toolsets:** `terminal`, `file`, `web`, `search`, `skills`, `search_files`, `session_search`, `patch`, `write_file`
- **Reports to:** `#news` Discord channel
- **Key paths:**
  - Agent sheet: `wiki/scratchpad/agent-sheets/news.md`
  - Source pages: `wiki/sources/articles/`
  - Carryover: `wiki/scratchpad/jobs/reports/news/carryover.md`
- **Notes:** RSS only (NOT wiki search); 3–5 stories per cycle; MCP tools NOT for discovery — only for post-selection ingestion

#### llm-wiki-raw-ingest (`ingest-agent`)
- **Cron ID:** `c838e81a1496`
- **Schedule:** daily
- **Trigger:** `/ingest-agent`
- **Skills:** `wiki_ingest_raw`, `wiki_write_page`, `wiki_lint`, `wiki_update_index`
- **Toolsets:** `terminal`, `file`, `web`, `search`, `skills`, `search_files`, `session_search`, `patch`, `write_file`
- **Key paths:**
  - Agent sheet: `wiki/scratchpad/agent-sheets/ingest.md`
  - Raw inbox: `/home/ty/Documents/LLM-WIKI/raw/` (at LLM-WIKI root, NOT `wiki/raw/`)
  - Clippings: `/home/ty/Documents/LLM-WIKI/Clippings/`
  - Carryover: `wiki/scratchpad/jobs/reports/ingest/carryover.md`
- **Notes:** `raw/` must be empty after every run; `wiki_ingest_raw` auto-archives to `Clippings/`

#### Wiki Librarian (`librarian-agent`)
- **Cron ID:** `48a3a009a820`
- **Schedule:** daily
- **Trigger:** `/librarian-agent`
- **Skills:** `wiki_lint`, `wiki_cluster_pages`, `wiki_hits_analysis`, `wiki_update_index`, `generate_insights`, `query_knowledge`
- **Toolsets:** `terminal`, `file`, `web`, `search`, `skills`, `search_files`, `session_search`, `patch`, `write_file`
- **MCP Notes:** TWO-STEP availability check required (package import → then actual MCP call); `generate_insights()` times out at 300s — use CLI fallback
- **Key paths:**
  - Agent sheet: `wiki/scratchpad/agent-sheets/librarian.md`
  - Carryover: `wiki/scratchpad/jobs/reports/librarian/carryover.md`
  - Audit fallback: `wiki/scratchpad/full_audit.py`
- **Notes:** 10-task audit checklist → spawns librarians-assistant subagent for Phase 2; broken cron workaround using `delegate_task`

#### Wiki Librarians-Assistant (`librarians-assistant`)
- **Cron ID:** `385aa0819a57`
- **Schedule:** daily (~08:50 AM, after librarian)
- **Trigger:** `/librarians-assistant`
- **Skills:** `wiki_lint`, `wiki_read_page`, `wiki_write_page`, `wiki_search`, `wiki_cluster_pages`
- **Toolsets:** `terminal`, `file`, `web`, `search`, `skills`, `search_files`, `session_search`, `patch`, `write_file`
- **MCP Notes:** Same TWO-STEP availability check as librarian; filesystem fallback when MCP unavailable
- **Key paths:**
  - Agent sheet: `wiki/scratchpad/agent-sheets/librarians-assistant.md`
  - Librarian carryover: `wiki/scratchpad/jobs/reports/librarian/carryover.md`
  - Batch progress: `wiki/scratchpad/jobs/reports/librarian/batch-progress.md`
  - Reference files: `~/.hermes/skills/agent-sheets/librarians-assistant/references/fix-patterns.md`, `~/.hermes/skills/agent-sheets/librarians-assistant/references/stub-fix-log.md`
- **Notes:** Receives audit results from librarian; 50+ fixes per session or hard blocker; MCP-unavailable fallback uses `full_audit.py`

#### Wiki Insights Generator (`insights-agent`)
- **Cron ID:** `723e76246970`
- **Schedule:** daily (06:00 AM)
- **Trigger:** `/insights-agent`
- **Skills:** `debug_test`, `wiki_update_index` (cron context: deferred), `synapse_remember` (cron context: deferred)
- **Toolsets:** `terminal`, `file`, `web`, `search`, `skills`, `search_files`, `session_search`, `patch`, `write_file`
- **Key paths:**
  - Agent sheet: `wiki/scratchpad/agent-sheets/insights.md`
  - Insight output: `/home/ty/Repositories/ai_workspace/project-synapse-mcp/data/insights/latest.md`
  - JSON data: `/home/ty/Repositories/ai_workspace/project-synapse-mcp/data/insights/latest.json`
  - Insight pages: `/home/ty/Documents/LLM-WIKI/wiki/synthesis/insights/`
  - Carryover: `wiki/scratchpad/jobs/reports/insights/carryover.md`
- **Notes:** CLI wrapper (NOT MCP tool — MCP times out at 300s); confidence ≥ 0.7 threshold for page creation; MCP tools deferred to active session

---

## Manual-Only Agents

These agents are triggered on-demand and have cron jobs that are **paused** or **not configured**.

### OrCAID (`orcaid`)
- **Location:** `/home/ty/Repositories/ai_workspace/OrCAID/`
- **Skill:** `~/.hermes/skills/autonomous-ai-agents/orcaid/SKILL.md`
- **Trigger phrases:** `run OrCAID`, `commit0`, `self_improve`, `paperbench`, `add OrCAID task`
- **Triggers:** manual only (cron `297092f3b347` is PAUSED)
- **Entry:** `cd /home/ty/Repositories/ai_workspace/OrCAID && uv run python -m orcaid.cli [flags...]`
- **Three task types:**
  - `commit0` — implement stubs, run pytest (primary)
  - `self_improve` — OrCAID self-improvement (ast.parse syntax check)
  - `paperbench` — reproduce ML papers (LLM judge evaluated)
- **Pipeline:** arXiv cron → papers to `paper-research/` → Paper2Code-Enhanced generates repo → OrCAID commit0 validates + fixes
- **Key paths:**
  - Skill: `~/.hermes/skills/autonomous-ai-agents/orcaid/SKILL.md`
  - Bridge storage: `~/.hermes/orcaid-bridge/`
  - Orchestrator memory: `~/.hermes/orchestrator-memory/`
- **Model:** `minimax/MiniMax-M2.7` via OpenAI compat endpoint
- **Required env:** `LLM_BASE_URL=https://api.minimax.io/v1` (NOT `/anthropic/v1/messages`)

### Paper2Code-Enhanced (`paper2code-enhanced`)
- **Location:** `/home/ty/Repositories/ai_workspace/Paper2Code-Enhanced/`
- **Skill:** `~/.hermes/skills/autonomous-ai-agents/paper2code-enhanced/SKILL.md`
- **Trigger phrases:** `paper to code`, `generate from paper`, `reproduce paper`, `paper2code`, `TreeOfThoughts`, `Yao et al`
- **Triggers:** manual only (not on cron)
- **Entry:** Python API via `codes/pipeline.py` (CLI is broken; use Python API)
- **Three stages:** planning (`1_planning.py`) → analyzing (`2_analyzing.py`) → coding (`3_coding.py`)
- **Output:** `<PaperName>_repo/` with `config.yaml`, `main.py`, `utils.py`, etc.
- **Pipeline:** Paper2Code generates repo → OrCAID commit0 validates and fixes
- **Cost:** ~$0.50–0.70 per run (~1 hour)
- **Key paths:**
  - Repo: `/home/ty/Repositories/ai_workspace/Paper2Code-Enhanced/`
  - Pipeline: `codes/pipeline.py`
  - Evaluation: `codes/eval.py`
  - Output: `outputs/<PaperName>_repo/`
- **Model:** `minimax/MiniMax-M2.7` (recommended for thinking/reasoning blocks)
- **Required env:** `LLM_BASE_URL=https://api.minimax.io/v1`

---

## Key Paths Quick Reference

| Agent | Wiki Root | Agent Sheet | Carryover | Reports |
|-------|-----------|-------------|-----------|---------|
| researcher-agent | `/home/ty/Documents/LLM-WIKI` | `wiki/scratchpad/agent-sheets/researcher.md` | `wiki/scratchpad/jobs/reports/researcher/carryover.md` | `wiki/scratchpad/jobs/reports/researcher/` |
| arxiv-agent | `/home/ty/Documents/LLM-WIKI` | `wiki/scratchpad/agent-sheets/arxiv.md` | `wiki/scratchpad/jobs/reports/arxiv/carryover.md` | `wiki/scratchpad/jobs/reports/arxiv/` |
| news-agent | `/home/ty/Documents/LLM-WIKI` | `wiki/scratchpad/agent-sheets/news.md` | `wiki/scratchpad/jobs/reports/news/carryover.md` | `wiki/scratchpad/jobs/reports/news/` |
| ingest-agent | `/home/ty/Documents/LLM-WIKI` | `wiki/scratchpad/agent-sheets/ingest.md` | `wiki/scratchpad/jobs/reports/ingest/carryover.md` | `wiki/scratchpad/jobs/reports/ingest/` |
| librarian-agent | `/home/ty/Documents/LLM-WIKI` | `wiki/scratchpad/agent-sheets/librarian.md` | `wiki/scratchpad/jobs/reports/librarian/carryover.md` | `wiki/scratchpad/jobs/reports/librarian/` |
| librarians-assistant | `/home/ty/Documents/LLM-WIKI` | `wiki/scratchpad/agent-sheets/librarians-assistant.md` | `wiki/scratchpad/jobs/reports/librarians-assistant/carryover.md` | `wiki/scratchpad/jobs/reports/librarians-assistant/` |
| insights-agent | `/home/ty/Documents/LLM-WIKI` | `wiki/scratchpad/agent-sheets/insights.md` | `wiki/scratchpad/jobs/reports/insights/carryover.md` | `wiki/scratchpad/jobs/reports/insights/` |
| orcaid | `/home/ty/Repositories/ai_workspace/OrCAID/` | `~/.hermes/skills/autonomous-ai-agents/orcaid/SKILL.md` | — | `~/.hermes/orcaid-bridge/` |
| paper2code-enhanced | `/home/ty/Repositories/ai_workspace/Paper2Code-Enhanced/` | `~/.hermes/skills/autonomous-ai-agents/paper2code-enhanced/SKILL.md` | — | `outputs/<PaperName>_repo/` |

| Resource | Path |
|----------|------|
| Wiki root | `/home/ty/Documents/LLM-WIKI/` |
| Paper storage | `/home/ty/Documents/paper-research/` |
| Raw inbox | `/home/ty/Documents/LLM-WIKI/raw/` |
| Clippings archive | `/home/ty/Documents/LLM-WIKI/Clippings/` |
| Synapse MCP | `/home/ty/Repositories/ai_workspace/project-synapse-mcp` |
| Orchestrator memory | `~/.hermes/orchestrator-memory/` |
| OrCAID bridge | `~/.hermes/orcaid-bridge/` |
| Cron toolsets ref | `~/.hermes/skills/agent-sheets/librarians-assistant/references/cron-toolsets.md` |
