#!/usr/bin/env python3
"""Kanban upsert for librarians-assistant carryover open items."""
import sqlite3, hashlib, time, os

DB_PATH = os.path.expanduser("~/.hermes/kanban.db")

def get_connection():
    return sqlite3.connect(DB_PATH)

def get_existing_tasks():
    conn = get_connection()
    cur = conn.execute(
        "SELECT id, title, status FROM tasks WHERE status != 'done'",
        ()
    )
    result = {str(row[1]).strip(): row[0] for row in cur.fetchall()}
    conn.close()
    return result

def upsert_task(agent, title, body, priority=1, status="blocked", created_by="cron:librarians-assistant"):
    conn = get_connection()
    cur = conn.cursor()
    
    key = f"{agent}: {title}".strip()
    existing = get_existing_tasks()
    
    if key in existing:
        task_id = existing[key]
        conn.close()
        return task_id, "skipped"
    
    ik = hashlib.sha256(key.encode()).hexdigest()[:16]
    task_id = f"t_{ik}"
    
    cur.execute("""
        INSERT INTO tasks
          (id, title, body, assignee, status, priority, created_by, idempotency_key, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (task_id, key, body, agent, status, priority, created_by, ik, int(time.time())))
    conn.commit()
    conn.close()
    return task_id, "created"

# Open items from carryover - all are Ty-blocked (decision items, not executable work)
items = [
    {
        "agent": "librarians-assistant",
        "title": "GoodRobot duality — canonical location decision",
        "body": "11 files across 2 vault paths (wiki/entities/projects/goodrobot.md SHUT DOWN, wiki/projects/projects 1/, wiki/projects/goodrobot/). Ty needs to decide canonical location.",
        "priority": 1,
        "status": "blocked"
    },
    {
        "agent": "librarians-assistant",
        "title": "44+ .bak files — bulk delete or selective restore",
        "body": "Accumulated 44+ .bak files in vault. Ty needs policy: bulk delete or selective restore.",
        "priority": 1,
        "status": "blocked"
    },
    {
        "agent": "librarians-assistant",
        "title": "6 Greek-letter stub concepts — expand/merge/delete",
        "body": "Stub concepts: beta, delta, epsilon, gamma, zeta, legal-accountability-stub. Ty decision: expand into full concepts, merge with similar pages, or delete.",
        "priority": 0,
        "status": "blocked"
    },
    {
        "agent": "librarians-assistant",
        "title": "10 stub cluster (3dgs, CRI, Firecracker, etc.) — batch decision",
        "body": "Template-generated stubs at 18 lines, all created 2026-06-03, all link to maximum-occupancy-principle. Similarity 1.0 is artifact of shared stub template, not genuine concept similarity. Ty decision: expand, merge, or delete as a batch.",
        "priority": 0,
        "status": "blocked"
    },
]

# Also check for existing tasks from prior cycles
existing = get_existing_tasks()
print(f"Existing tasks in kanban: {len(existing)}")

results = []
for item in items:
    task_id, status = upsert_task(
        agent=item["agent"],
        title=item["title"],
        body=item["body"],
        priority=item["priority"],
        status=item["status"]
    )
    results.append((task_id, status))
    print(f"  {status.upper()}: {item['title'][:60]} → {task_id}")

print(f"\nTotal: {len(results)} items processed")