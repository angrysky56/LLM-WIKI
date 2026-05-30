import sqlite3, hashlib, uuid, time, os

DB_PATH = os.path.expanduser("~/.hermes/kanban.db")
WIKI = os.environ.get("WIKI_PATH", "/home/ty/Documents/LLM-WIKI")

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# Check existing open tasks
cur.execute("SELECT id, title, status, assignee FROM tasks WHERE status != 'done'")
rows = cur.fetchall()
existing = {str(row[1]).strip(): row[0] for row in rows}

def upsert(agent, title, body, priority=1, blocked=False, assignee="librarians-assistant"):
    key = f"{agent}: {title}".strip()
    if key in existing:
        return existing[key], "skipped"
    ik = hashlib.sha256(key.encode()).hexdigest()[:16]
    tid = f"t_{uuid.uuid4().hex[:16]}"
    status = "blocked" if blocked else "ready"
    cur.execute("""
        INSERT INTO tasks
          (id, title, body, assignee, status, priority, created_by, idempotency_key, created_at)
        VALUES (?, ?, ?, ?, ?, ?, 'cron:librarians-assistant', ?, ?)
    """, (tid, key, body, assignee, status, priority, ik, int(time.time())))
    conn.commit()
    return tid, "created"

# GoodRobot multi-location blocker — needs Ty decision
result = upsert(
    agent="librarians-assistant",
    title="GoodRobot canonical location decision",
    body="GoodRobot has 11+ files across 2 vault paths. Canonical location needs Ty decision: consolidate to wiki/research/projects/goodrobot/ or wiki/entities/projects/goodrobot/?",
    priority=1,
    blocked=True,
    assignee="librarians-assistant"
)
print(f"GoodRobot location: {result[0]} ({result[1]})")

conn.close()