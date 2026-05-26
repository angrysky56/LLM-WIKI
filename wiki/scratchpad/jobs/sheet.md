---
summary: Updated job status to done for news
updated: 2026-05-22T01:26:02Z
---

---
summary: Jobs sheet with fixed agent-sheet wikilinks
tags: [jobs, task-board, agent-instructions]
updated: 2026-05-22T01:30:00Z
---

# Jobs Sheet — Central Task Board

**Purpose**: Single source of truth for what each agent should be doing. Agents check here on every run for their current instructions, update their status when done, and post summaries to their report folder.

## Format

- **Pending**: Tasks queued for next run
- **In Progress**: Tasks currently being worked
- **Done**: Completed tasks (brief result + link to report)
- **Blocked**: Tasks waiting on something external

## Active Jobs

| Job ID | Job Name | Agent | Status | Last Run | Next Run | Agent Sheet |
|--------|----------|-------|--------|----------|----------|-------------|
| `eaaa6bdc8503` | world-news-daily | news | **done** | 2026-05-27 | 2026-05-27 8AM | [[news]] |
| `8ea33cfa560a` | Wiki Researcher | researcher | **done** | 2026-07-02 | TBD | [[researcher]] |
| `297092f3b347` | orcaid-verification-indexer | orcaid | **PAUSED** | 2026-05-18 | — | [[orcaid]] |
| `72599f850df2` | arxiv-top3 | arxiv | **done** | 2026-05-26 | 2026-05-27 8:20AM | [[arxiv]] |
| `c838e81a1496` | llm-wiki-raw-ingest | ingest | **done** | 2026-06-27 | — | [[ingest]] |
| `48a3a009a820` | Wiki Librarian | librarian | **done** | 2026-06-17 | — | [[librarian]] |
| `385aa0819a57` | Wiki Librarians-Assistant | librarians-assistant | **done** | 2026-06-17 | — | [[librarians-assistant]] |
| `723e76246970` | Wiki Insights Generator | insights | **done** | 2026-05-24 | 2026-05-25 6AM | [[insights]] |

## Task Delegation

### Ty → Agents

**Pending Tasks** (from morning kanban review — 2026-06-26 08:30):

**High Priority** (new this cycle)
- [ ] **researcher**: MoE routing collapse under RLHF — is it happening in practice? No empirical data
  - Source: researcher/carryover.md §Open | Blocked: no
- [x] **researcher**: Category theory for neural network verification — Do attention mechanisms form a closed monoidal category? → filled [[attention-monoidal-closure]]
  - Source: researcher/carryover.md §Open | Done: 2026-06-27 | Report: [[discovery-2026-06-27]]
- [x] **researcher**: MOP training for transformers — Can path entropy maximization be applied to next-token prediction training from scratch? → `mop-next-token-prediction.md` (stub)
  - Source: researcher/carryover.md §Open | Done: 2026-06-30 | Report: [[discovery-2026-06-30]]
- [ ] **researcher**: Adaptive budget learning — how to train the gating model for adaptive computation
  - Source: researcher/carryover.md §Open | Blocked: no
- [ ] **librarians-assistant**: Double frontmatter investigation — 8 pages with multiple `---` delimiters (may be intentional section separators vs. true duplicates)
  - Source: librarians-assistant/carryover.md §What Remains | Blocked: no

**Medium Priority** (new this cycle)
- [ ] **arxiv**: World-model improvement theme — papers on model editing, knowledge unlearning, skill compaction, uncertainty-aware planning
  - Source: arxiv/carryover.md §Notes | Blocked: no
- [ ] **arxiv**: SNR↔reliability mapping (Shannon Law ↔ verifier-graph) — papers on calibrated confidence/uncertainty-aware verification
  - Source: arxiv/carryover.md §Notes | Blocked: no
- [ ] **researcher**: Hybrid reward models — combining ELHSR (hidden-state) with SD-Search (process-level)
  - Source: researcher/carryover.md §Open | Blocked: no
- [ ] **researcher**: Reward hacking detectability — reliable signal before severe? Current approaches post-hoc
  - Source: researcher/carryover.md §Open | Blocked: no
- [x] **researcher**: Cognitive world models for LLM agents — how to represent "what the world looks like" for a text-based agent? → `cognitive-world-models-for-llm-agents.md`
  - Source: researcher/carryover.md §Open | Done 2026-06-26 | Report: `reports/researcher/discovery-2026-06-26.md`
- [ ] **librarians-assistant**: Tag taxonomy normalization — 1287 unique tags with inconsistent casing (uppercase acronyms + lowercase prefixes), large scope
  - Source: librarians-assistant/carryover.md §What Remains | Blocked: no
- [ ] **librarians-assistant**: Reciprocal link audit — 795 non-reciprocal pairs (may be bounded by scope)
  - Source: librarians-assistant/carryover.md §What Remains | Blocked: no

**In Progress**:
- [ ] **librarian**: HITS authority scoring + orphan detection (June 26 carryover — deferred to this cycle)
  - Source: librarian/carryover.md §Heading | Blocked: no

**Blocked (needs Ty input)**
- [ ] **news**: SpaceX IPO June 12 — BlackRock $10B confirmation, SEC filings, pre-IPO Starship tests
  - Source: news/carryover.md §Open | Blocked: yes
- [ ] **news**: California AI order — implementation timeline, vendor safeguard details
  - Source: news/carryover.md §Open | Blocked: yes
- [ ] **news**: D-Wave quantum — whether D-Wave contests Flatiron Institute finding
  - Source: news/carryover.md §Open | Blocked: yes
- [ ] **news**: Malaysia exit from US trade deal — which countries follow, ASEAN supply chain impact
  - Source: news/carryover.md §Open | Blocked: yes
- [ ] **news**: Rubio-India $500B — whether negotiations restart, what legal framework replaces collapsed bargain
  - Source: news/carryover.md §Open | Blocked: yes
- [ ] **news**: EU-US deal — full implementation text, specific tariff rates
  - Source: news/carryover.md §Open | Blocked: yes

**Done** (this session):
- [x] **librarian**: Reciprocal link audit — 451 reciprocals added across 90 wiki/concepts pages
  - Report: [[audit-2026-05-25]] | t_74b2f183

**In Progress**:
- [ ] *[Add tasks here]*

**Done**:
- [ ] *[Add completed tasks here]*

### Agent → (reports go in jobs/reports/{agent}/)

| Agent | Report Folder | Last Report |
|-------|--------------|-------------|
| librarian | `jobs/reports/librarian/` | — |
| researcher | `jobs/reports/researcher/` | — |
| orcaid | `jobs/reports/orcaid/` | — |
| arxiv | `jobs/reports/arxiv/` | — |
| news | `jobs/reports/news/` | [[news-2026-05-22-headlines]] |
| ingest | `jobs/reports/ingest/` | — |
| insights | `jobs/reports/insights/` | — |

## Instructions Per Agent

Each agent reads its own sheet on every run. These sheets are the source of truth — not this central sheet.

| Agent | Sheet | Purpose |
|-------|-------|---------|
| librarian | [[librarian|librarian]] | Quality audit, orphan detection, link integrity |
| researcher | [[researcher|researcher]] | Knowledge gap analysis, new topic research |
| orcaid | [[orcaid|orcaid]] | Verification sweep, drift detection, self-improve |
| arxiv | [[arxiv|arxiv]] | Top 3 paper discovery and ingestion |
| news | [[news|news]] | Global news curation and wiki ingestion |
| ingest | [[ingest|ingest]] | raw→wiki pipeline, file processing |
| insights | [[insights|insights]] | Zettelkasten insight generation and wiki integration |

**Each agent sheet contains:**
1. Read the agent sheet (STEP 0)
2. Read the central jobs sheet (STEP 1)
3. Execute assigned tasks
4. Write report to `jobs/reports/{agent}/`
5. Update this sheet's status column
6. Update own carryover in `jobs/reports/{agent}/carryover.md`
