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
    # News agent writes to wiki, not workspace → informational card, dispatcher ignores
    status = "done"
    cur.execute("""
        INSERT INTO tasks
          (id, title, body, assignee, status, priority, created_by, idempotency_key, created_at)
        VALUES (?, ?, ?, ?, ?, ?, 'cron:kanban-morning-review', ?, ?)
    """, (tid, key, body, agent, status, priority, ik, int(time.time())))
    conn.commit()
    return tid, "created"

# Items that genuinely cannot be answered from current wiki/synapse context
items = [
    ("news", "Romania/NATO: Article 4 consultation outcome",
     "First Russian attack on NATO territory (May 29). Romania considering Article 4. Need outcome of NATO consultations and whether posture changes.", 2),
    ("news", "SpaceX IPO: BlackRock $10B confirmation before quiet period",
     "Window closes when quiet period begins (likely within days). S-1 filed June 12 listing. BlackRock still 'considering' per carryover — needs confirmation before quiet period.", 2),
    ("news", "Trump/Iran: Final determination timing and Hormuz condition",
     "Trump deferred decision May 29. Framework agreed with Iran hardliners trying to derail. Key condition: Hormuz Strait reopening. Need outcome.", 2),
    ("news", "Ebola: Case count update, Sud-Kivu trajectory, South Sudan border",
     "1,018+ cases, Sud-Kivu first case May 26, WHO chief in DRC May 29. Need: case count updates, spread trajectory, South Sudan border cases, NV-387 trial status.", 1),
    ("news", "California AI: Agency implementation signals substantive vs performative",
     "60-day review clock running. Need agency-level actions that indicate whether implementation is substantive or performative.", 1),
]

for agent, title, body, priority in items:
    tid, state = upsert(agent, title, body, priority)
    print(f"{state}: {title} → {tid}")

print(f"\nTotal tasks: {len(items)}")
conn.close()