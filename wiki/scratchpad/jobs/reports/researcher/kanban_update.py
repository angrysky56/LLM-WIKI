import sqlite3, hashlib, time, os

DB_PATH = os.path.expanduser("~/.hermes/kanban.db")
conn = sqlite3.connect(DB_PATH)

# Get existing non-done tasks
cur = conn.execute("SELECT id, title, status FROM tasks WHERE status != 'done'")
existing = {str(row[1]).strip(): row[0] for row in cur.fetchall()}
print(f"Existing non-done tasks: {len(existing)}")

def upsert(title, body, agent, priority=1, blocked=False):
    key = f"{agent}: {title}".strip()
    if key in existing:
        return existing[key], "skipped"
    ik = hashlib.sha256(key.encode()).hexdigest()[:16]
    status = "blocked" if blocked else "ready"
    task_id = f"t_{ik}"
    conn.execute("""
        INSERT INTO tasks
          (id, title, body, assignee, status, priority, created_by, idempotency_key, created_at)
        VALUES (?, ?, ?, ?, ?, ?, 'cron:kanban-morning-review', ?, ?)
    """, (task_id, key, body, agent, status, priority, ik, int(time.time())))
    conn.commit()
    return task_id, "created"

# Researcher's one remaining open item
task_id, status = upsert(
    "Reward hacking detectability: reliable early-warning signal",
    "Is there a reliable signal that reward hacking is occurring before it becomes severe? Current approaches are post-hoc. reward-hacking.md covers mechanisms but early detection is unsolved.\n\nSource: researcher/carryover.md",
    agent="researcher",
    priority=1,
    blocked=False
)
print(f"Upsert reward-hacking-detectability: {task_id} [{status}]")

conn.close()
print("Done")
