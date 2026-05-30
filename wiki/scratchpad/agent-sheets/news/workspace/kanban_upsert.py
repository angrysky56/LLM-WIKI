import sqlite3, hashlib, uuid, time, os

DB_PATH = os.path.expanduser("~/.hermes/kanban.db")
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# Check existing non-done tasks
cur.execute("SELECT id, title, status FROM tasks WHERE status != 'done'")
existing = {str(row[1]).strip(): row[0] for row in cur.fetchall()}

def upsert(agent, title, body, priority=1, blocked=False):
    key = f"{agent}: {title}".strip()
    if key in existing:
        return existing[key], "skipped"
    ik = hashlib.sha256(key.encode()).hexdigest()[:16]
    tid = f"t_{uuid.uuid4().hex[:16]}"
    # Agent-type determines status:
    # wiki-writers (arxiv/insights/news) → done (informational card)
    # workspace-writers (research/ingest/librarian) → ready or blocked
    wiki_writer_agents = {"arxiv", "insights", "news"}
    if agent in wiki_writer_agents:
        status = "done"   # informational, dispatcher ignores
    else:
        status = "blocked" if blocked else "ready"   # executable, dispatcher picks up
    cur.execute("""
        INSERT INTO tasks
          (id, title, body, assignee, status, priority, created_by, idempotency_key, created_at)
        VALUES (?, ?, ?, ?, ?, ?, 'cron:kanban-morning-review', ?, ?)
    """, (tid, key, body, agent, status, priority, ik, int(time.time())))
    conn.commit()
    return tid, "created"

# New items from news carryover 2026-05-30
items = [
    ("news", "Blue Origin: Launch pad damage scope, months delay confirmation", "May 30 Reuters: New Glenn explosion caused substantial launch pad damage at Cape Canaveral. Months-long delays confirmed. NASA Moon mission timeline directly impacted."),
    ("news", "Ghana anti-LGBT: Presidential signature decision", "Ghana parliament passed anti-LGBT bill May 30. Awaiting presidential signature. Regional human rights tension with Western partners."),
]

for agent, title, body in items:
    tid, result = upsert(agent, title, body, priority=1)
    print(f"{result}: {title[:60]} → {tid}")

print(f"\nTotal non-done tasks after: {len(existing)}")