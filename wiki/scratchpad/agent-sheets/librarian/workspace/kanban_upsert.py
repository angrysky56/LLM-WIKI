import sqlite3, hashlib, uuid, time, os

DB = sqlite3.connect(os.path.expanduser("~/.hermes/kanban.db"))
cur = DB.execute("SELECT id, title, status FROM tasks WHERE status != 'done'")
existing = {str(row[1]).strip(): row[0] for row in cur.fetchall()}

def upsert(agent, title, body, priority=1, blocked=False):
    key = f"{agent}: {title}".strip()
    if key in existing:
        return existing[key], "skipped"
    ik = hashlib.sha256(key.encode()).hexdigest()[:16]
    tid = f"t_{uuid.uuid4().hex[:16]}"
    status = "blocked" if blocked else "ready"
    cur.execute("""
        INSERT INTO tasks
          (id, title, body, assignee, status, priority, created_by, idempotency_key, created_at)
        VALUES (?, ?, ?, ?, ?, ?, 'cron:librarian-audit', ?, ?)
    """, (tid, key, body, agent, status, priority, ik, int(time.time())))
    DB.commit()
    return tid, "created"

tasks = [
    ("librarians-assistant", "276 orphans — batch identify non-operational",
     "276 orphan pages detected by wiki_lint. ~200+ are operational (carryovers, SKILL files, reports). Batch-identify the non-operational content orphans and relink to appropriate hub pages.",
     1, False),
    ("librarians-assistant", "74 missing frontmatter — batch fix operational files",
     "74 pages without frontmatter. Mostly operational: agent carryovers, templates, workflow docs. Batch add minimal frontmatter (created, updated, type, status) to non-operational files.",
     1, False),
    ("librarians-assistant", "594 non-reciprocal links — batch close gaps",
     "594 A→B wikilinks where B doesn't link back. Notable: [[autonomous-agents]] → [[mcp]], [[agentic-oversight]], [[bounded-structured-memory]], [[markovian-carryover]], [[llm-agents]], [[reinforcement-learning]], [[agentic-planner]] all missing returns. Batch close highest-value gaps.",
     2, False),
    ("librarian", "test-time-compute-scaling broken wikilink fix",
     "wiki/concepts/test-time-compute-scaling.md links to [[parallel-reasoning]] but should be [[inference-time-compute-scaling]]. Quick wikilink fix.",
     1, False),
    ("librarians-assistant", "Merge candidate: agentic-planner ↔ agentic-reflection ↔ agentic-sequential",
     "GAAC clustering: similarity 1.0 between these three pages. Review content overlap; decide to merge or keep separate.",
     2, False),
]

for agent, title, body, priority, blocked in tasks:
    tid, status = upsert(agent, title, body, priority, blocked)
    print(f"{status.upper()}: {agent}: {title[:50]} -> {tid}")

DB.close()