import sqlite3, hashlib, time

DB = sqlite3.connect("/home/ty/.hermes/kanban.db")
cur = DB.execute("SELECT id, title, status FROM tasks WHERE status != 'done'", ())
existing = {str(row[1]).strip(): row[0] for row in cur.fetchall()}

open_items = [
    ("researcher", "Adaptive budget learning: train gating model for adaptive computation", 
     "No clear paper yet. How to train the gating model that decides compute allocation? Needs empirical research.", 
     1, False),
    ("researcher", "Hybrid reward models: combining ELHSR hidden-state with SD-Search process-level signals",
     "Emerging direction — no full treatment. Can ELHSR's lightweight hidden-state scoring be combined with SD-Search's process-level signals for better BoN guidance?",
     1, False),
]

tasks_created = []
for agent, title, body, priority, blocked in open_items:
    key = f"{agent}: {title}".strip()
    if key in existing:
        print(f"SKIP: {key} already exists as {existing[key]}")
        continue
    ik = hashlib.sha256(key.encode()).hexdigest()[:16]
    status = "blocked" if blocked else "ready"
    cur.execute("""
        INSERT INTO tasks
          (id, title, body, assignee, status, priority, created_by, idempotency_key, created_at)
        VALUES (?, ?, ?, ?, ?, ?, 'cron:kanban-morning-review', ?, ?)
    """, (f"t_{ik}", key, body, agent, status, priority, ik, int(time.time())))
    DB.commit()
    print(f"CREATE: {key} -> t_{ik}")
    tasks_created.append(f"t_{ik}")

print(f"\nTotal created: {len(tasks_created)}")
print(f"IDs: {tasks_created}")
DB.close()