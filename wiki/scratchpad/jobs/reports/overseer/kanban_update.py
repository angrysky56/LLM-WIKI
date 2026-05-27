import sqlite3, os, hashlib, uuid, time

DB = os.path.expanduser("~/.hermes/kanban.db")
conn = sqlite3.connect(DB)
cur = conn.cursor()

# Check existing
cur.execute("SELECT id, title, status FROM tasks")
existing = {str(row[1]).strip(): (row[0], row[2]) for row in cur.fetchall()}

def upsert_done(agent, title, body="", priority=1):
    key = f"[{agent}] {title}".strip()
    if key in existing:
        return existing[key][0], "skipped"
    ik = hashlib.sha256(key.encode()).hexdigest()[:16]
    tid = f"t_{uuid.uuid4().hex[:16]}"
    cur.execute("""
        INSERT INTO tasks
          (id, title, body, assignee, status, priority, created_by, idempotency_key, created_at)
        VALUES (?, ?, ?, ?, 'done', ?, 'wiki-overseer', ?, ?)
    """, (tid, key, body, agent, priority, ik, int(time.time())))
    conn.commit()
    return tid, "created"

# New items not yet in kanban
new_items = [
    ("researcher", "Bounded memory budget optimization", "From researcher carryover 2026-07-15 — capacity/saturation theme, open from prior cycles", 1),
    ("researcher", "MOP vs fine-tuning boundary", "From researcher carryover 2026-07-15 — open from prior cycles", 1),
    ("researcher", "Schema competition", "From researcher carryover 2026-07-15 — open from prior cycles, low priority", 0),
    ("librarian", "10 merge candidates — agentic-planner/agentic-sequential only actionable", "From librarian carryover 2026-07-28 — 9 are stub-template artifacts, only agentic-planner/agentic-sequential is genuine", 0),
    ("librarians-assistant", "18 stub concepts batch — Ty decision needed", "From librarian/librarians-assistant carryover 2026-07-28 — 6 Greek-letter stubs + 10 stub cluster; Ty needs to decide expand/merge/delete", 1),
]

for agent, title, body, priority in new_items:
    tid, status = upsert_done(agent, title, body, priority)
    print(f"{status}: {agent}: {title[:50]} -> {tid}")

print(f"\nTotal tasks: {conn.execute('SELECT COUNT(*) FROM tasks').fetchone()[0]}")
