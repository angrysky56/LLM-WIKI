import sqlite3, hashlib, uuid, time, os

DB_PATH = os.path.expanduser("~/.hermes/kanban.db")
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# Check existing non-done tasks
cur.execute("SELECT id, title, status FROM tasks WHERE status != 'done'")
existing_non_done = {str(row[1]).strip(): row[0] for row in cur.fetchall()}

# Check all existing (for dedup)
cur.execute("SELECT id, title, status FROM tasks")
existing_all = {str(row[1]).strip(): row[0] for row in cur.fetchall()}

def upsert(agent, title, body, priority=1, blocked=False):
    key = f"{agent}: {title}".strip()
    if key in existing_all:
        return existing_all[key], "skipped (exists)"
    if key in existing_non_done:
        return existing_non_done[key], "skipped (active)"
    ik = hashlib.sha256(key.encode()).hexdigest()[:16]
    tid = f"t_{uuid.uuid4().hex[:16]}"
    # news agent = wiki-writer → status='done' (informational card)
    status = "done"
    cur.execute("""
        INSERT INTO tasks
          (id, title, body, assignee, status, priority, created_by, idempotency_key, created_at)
        VALUES (?, ?, ?, ?, ?, ?, 'cron:kanban-morning-review', ?, ?)
    """, (tid, key, body, agent, status, priority, ik, int(time.time())))
    conn.commit()
    return tid, "created"

r1 = upsert("news", "Israel/Lebanon: Deepest Incursion 26 Years — Trump Deal Stalls",
    "Day 93: Trump told Fox 'no hurry' for Iran deal, demanded amendments. Israel crossed Litani River, captured Beaufort Castle. Deal in limbo. IRGC shot down US drone. Needs monitoring.",
    priority=1)
r2 = upsert("news", "Japan/China: 'New Militarism' Spat Escalates",
    "China labels Japan 'new militarism.' Japan rebuffs, citing China's 'huge arsenal.' Japan accelerating to 2% GDP defense spending. Direct diplomatic escalation — follow for policy implications.",
    priority=1)
r3 = upsert("news", "Colombia Election: Results Pending — US Relations at Stake",
    "May 31 election: Petro ally vs. pro-Trump candidates. Winner TBD. Could redefine US-Colombia relations on trade, security, drugs. Monitor for result announcement.",
    priority=1)

results = [r1, r2, r3]

print("Done. Results:")
for tid, status in results:
    print(f"  {status}: → {tid}")
