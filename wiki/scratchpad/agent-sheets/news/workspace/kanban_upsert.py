#!/usr/bin/env python3
"""
Kanban upsert for news-agent Cycle 19 — informational cards (status=done)
Pattern from news-agent skill: informational cards at status='done' so the
dispatcher ignores them but Ty sees them on the board.
"""
import sqlite3, hashlib, uuid, time, os

DB_PATH = os.path.expanduser("~/.hermes/kanban.db")
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# Gather existing tasks
cur.execute("SELECT id, title, status FROM tasks")
existing = {str(r[1]).strip(): r[0] for r in cur.fetchall()}

def upsert(agent, title, body, priority=1):
    key = f"{agent}: {title}".strip()
    if key in existing:
        tid = existing[key]
        print(f"SKIP {tid} | {key} (already exists)")
        return tid, "skipped"
    ik = hashlib.sha256(key.encode()).hexdigest()[:16]
    tid = f"t_{uuid.uuid4().hex[:16]}"
    now = int(time.time())
    cur.execute(
        "INSERT INTO tasks (id, title, body, assignee, status, priority, created_by, idempotency_key, created_at) VALUES (?, ?, ?, ?, 'done', ?, 'cron:news-cycle19', ?, ?)",
        (tid, key, body, agent, priority, ik, now)
    )
    conn.commit()
    print(f"CREATED {tid} | {key}")
    return tid, "created"

# Open questions from Cycle 19 carryover — surfacing as informational cards
items = [
    ("Iran-Israel escalation: sustained exchange or de-escalate?", 
     "Iran launched missiles at Israel June 8 — first direct exchange since April ceasefire. Watch UN Security Council, Hezbollah second front, Gulf basing, oil spike."),
    ("Peru election runoff: results pending",
     "Votes still being counted in tight Peru presidential runoff. Left-right choice for discontented voters."),
    ("Chornobyl IAEA nuclear safety assessment",
     "Expected any day after Russian drone strike on Chornobyl spent fuel storage (June 7). Still not released."),
    ("Ukraine peace: Russia response to European 5 conditions",
     "European allies set five preconditions for peace talks as US steps back as mediator. Russia's rejection likely."),
    ("AI rally unwind: correction or structural rotation?",
     "Global tech stocks plunged June 8 as AI rally cooled and Middle East crisis drove risk-off. Watch Fed response."),
    ("Philippines earthquake: casualties and tsunami impact",
     "Powerful quake struck Mindanao; tsunami warnings across Indonesia, Japan, Taiwan. Assessments ongoing."),
    ("Xi-Kim North Korea summit outcome",
     "Xi Jinping to meet Kim Jong Un — first since nuclear expansion announcement. Watch for agreements/shifts."),
]

for title, body in items:
    upsert("news", title, body)

conn.close()
print("Done.")