#!/usr/bin/env python3
"""Upsert informational kanban cards for news agent open questions.
   Cards are status='done' so dispatcher ignores them; they exist for
   Ty's unified view via kanban-review."""
import sqlite3, hashlib, uuid, time, os

DB_PATH = os.path.expanduser("~/.hermes/kanban.db")
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

cur.execute("SELECT id, title, status FROM tasks")
existing = {str(r[1]).strip(): r[0] for r in cur.fetchall()}

def upsert(agent, title, body, priority=1):
    key = f"{agent}: {title}".strip()
    if key in existing:
        tid, status = existing[key], "skipped"
        return tid, status
    ik = hashlib.sha256(key.encode()).hexdigest()[:16]
    tid = f"t_{uuid.uuid4().hex[:16]}"
    cur.execute(
        "INSERT INTO tasks (id, title, body, assignee, status, priority, created_by, idempotency_key, created_at) VALUES (?, ?, ?, ?, 'done', ?, 'cron:news-agent', ?, ?)",
        (tid, key, body, agent, priority, ik, int(time.time()))
    )
    conn.commit()
    return tid, "created"

items = [
    {
        "agent": "news",
        "title": "Follow-up: IAEA Chornobyl assessment + London talks",
        "body": "Chornobyl drone strike on spent fuel storage: Monitor IAEA radiation assessment and London talks outcome. Expected within 48h of June 7 strike.",
        "priority": 2
    },
    {
        "agent": "news",
        "title": "Follow-up: Israel-Beirut ceasefire collapse risk",
        "body": "Israel struck Beirut suburb days after US-brokered truce. Watch for Hezbollah official response and any further strikes that would confirm ceasefire collapse.",
        "priority": 2
    },
    {
        "agent": "news",
        "title": "Follow-up: Armenia election preliminary results",
        "body": "Armenia parliamentary election June 7. Pashinyan seeks third term under Russian pressure. Preliminary results will determine Westward pivot trajectory.",
        "priority": 2
    },
    {
        "agent": "news",
        "title": "Follow-up: Peru election runoff results",
        "body": "Peru presidential runoff — left vs right amid violence surge. Results expected within days.",
        "priority": 1
    },
    {
        "agent": "news",
        "title": "Follow-up: OPEC+ quota market reaction",
        "body": "OPEC+ symbolic July quota increase blocked by Persian Gulf blockade. Track crude price movement and actual production changes.",
        "priority": 1
    },
    {
        "agent": "news",
        "title": "Follow-up: USMCA trade tension timeline",
        "body": "US, Mexico, Canada missed July USMCA review deadline. Track next round of trade talks and any tariff developments.",
        "priority": 1
    },
]

results = []
for item in items:
    tid, status = upsert(item["agent"], item["title"], item["body"], item["priority"])
    results.append(f"  [{status}] {item['title']}: {tid}")

print("Kanban informational cards results:")
print("\n".join(results))
conn.close()