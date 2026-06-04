#!/usr/bin/env python3
"""
kanban_upsert.py — push the 2026-06-04 ingest open items to Hermes kanban.

Per the kanban-review skill template. ingest is a workspace-writer agent,
so tasks are created with status='ready' (dispatcher picks up, auto-completes
via detect_crashed_workers in kanban_db.py).
"""
import sqlite3, hashlib, uuid, time, os

DB_PATH = os.path.expanduser("~/.hermes/kanban.db")
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# Check existing non-done tasks (treat blocked/ready/running as live)
cur.execute("SELECT id, title, status FROM tasks WHERE status != 'done' AND status != 'archived'")
existing = {str(row[1]).strip(): row[0] for row in cur.fetchall()}


def upsert(agent, title, body, priority=1):
    key = f"{agent}: {title}".strip()
    if key in existing:
        print(f"  [skip] exists: {key}  (id={existing[key]})")
        return existing[key], "skipped"
    ik = hashlib.sha256(key.encode()).hexdigest()[:16]
    tid = f"t_{uuid.uuid4().hex[:16]}"
    # ingest-agent is a workspace-writer → status='ready' (dispatcher picks up)
    status = "ready"
    cur.execute(
        """
        INSERT INTO tasks
          (id, title, body, assignee, status, priority, created_by, idempotency_key, created_at)
        VALUES (?, ?, ?, ?, ?, ?, 'cron:ingest-2026-06-04', ?, ?)
        """,
        (tid, key, body, agent, status, priority, ik, int(time.time())),
    )
    conn.commit()
    print(f"  [create] {key}  (id={tid})")
    return tid, "created"


# ---- Task 1: orphan concept/entity stubs from today's ingest ----
# The two new source summaries (synapse-wiki-scaling-walkthrough,
# hermes-agent-self-evolution, acdc-llm-task-capability-coevolution-sakana)
# reference 8 concept pages and 1 entity page that do not yet exist.
# librarian work.

orphan_titles = [
    "Create stub concept pages for orphan concepts referenced by 2026-06-04 source summaries",
]
orphan_body = """\
Librarian task — orphan stub creation sweep from 2026-06-04 ingest.

The following concept pages are referenced in newly-created source summaries but do not exist in the wiki (verified via `wiki_search`):

From [[wiki/sources/articles/synapse-wiki-scaling-walkthrough]]:
- `concepts/context-budget` — the `response_budget.py` pattern is a concrete instance of context budgeting
- `duckdb` — the embedded OLAP DB backing the page index

From [[wiki/sources/repositories/hermes-agent-self-evolution]]:
- `dspy` — Stanford declarative LM program framework
- `gepa` — Genetic-Pareto Prompt Evolution (ICLR 2026 Oral)
- `entities/projects/darwinian-evolver` — code-evolution engine used in Phase 4
- `concepts/prompt-evolution` — the underlying technique
- `concepts/agent-self-improvement` — broader category

From [[wiki/sources/papers/acdc-llm-task-capability-coevolution-sakana]]:
- `concepts/quality-diversity` — the QD selection family (DNS, MAP-Elites)
- `concepts/evolutionary-model-merging` — EvoMerge / CQD lineage
- `concepts/coevolution` — the minimal-criteria open-ended variant
- `concepts/coverage-metric` — the central evaluation
- `concepts/synthetic-task-generation` — scientist-LLM pattern
- `concepts/skill-vectors` — behavioral signatures without predefined niches
- `entities/projects/sakana-ai` — the lab behind the paper
- `concepts/model-merging` — broader category
- `concepts/open-endedness` — the OE framework AC/DC instantiates

Plus 1 entity page:
- entity for `hermes-agent-self-evolution` (the Nous Research repo) — `entities/projects/hermes-agent-self-evolution`

Suggested approach:
1. Create each as a stub with frontmatter + a 1-paragraph summary + Connections list linking back to the source page
2. For concept pages that already have a related synthesis page (e.g., `concepts/coevolution` ↔ `wiki/synthesis/insights/oee-knowledge-cluster-insight.md`), add a wikilink to the synthesis page
3. For pages with extensive existing material (e.g., DSPy is in the BES paper's connections, GEPA is referenced in arxiv-2026-05-28 report), pull a few sentences of substance rather than leaving pure stubs

Priority: low (orphan stubs do not block any active pipeline)
""".strip()

print("=== Task: orphan stubs ===")
for t in orphan_titles:
    upsert("librarian", t, orphan_body, priority=1)


print("\nDone.")
conn.close()
