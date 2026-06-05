import sqlite3, hashlib, uuid, time, os

DB_PATH = os.path.expanduser("~/.hermes/kanban.db")
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# Check existing tasks — avoid duplicates
cur.execute("SELECT id, title, status FROM tasks")
existing = {str(r[1]).strip(): r[0] for r in cur.fetchall()}

def upsert(agent, title, body, priority=1):
    key = f"{agent}: {title}".strip()
    if key in existing:
        return existing[key], "skipped"
    ik = hashlib.sha256(key.encode()).hexdigest()[:16]
    tid = f"t_{uuid.uuid4().hex[:16]}"
    cur.execute(
        "INSERT INTO tasks (id, title, body, assignee, status, priority, created_by, idempotency_key, created_at) VALUES (?, ?, ?, ?, 'done', ?, 'cron:kanban-morning-review', ?, ?)",
        (tid, key, body, agent, priority, ik, int(time.time()))
    )
    conn.commit()
    return tid, "created"

# === ITEMS FOR THIS CYCLE (2026-06-05) ===
items = [
    {
        "agent": "news",
        "title": "Xi Jinping visits North Korea for Kim Jong Un summit",
        "body": "Xi to meet Kim weeks after meeting Trump and Putin, one day after Kim's exponential nuclear arsenal announcement. Xi attempts to reassert Chinese influence as Russia reduces DPRK's China dependence.",
        "priority": 2,
    },
    {
        "agent": "news",
        "title": "Hezbollah rejects Lebanon-Israel ceasefire deal",
        "body": "Hezbollah explicitly rejected the US-brokered June 4 trilateral deal. Deal required Hezbollah to stop firing first — group was not at the table. Fighting continues; June 22 talks uncertain.",
        "priority": 2,
    },
    {
        "agent": "news",
        "title": "Ukraine drone blast at Romanian NATO port + Zelensky peace offer",
        "body": "Malfunctioning Ukrainian naval drone exploded at Romanian Black Sea port. EC: 'direct consequence' of war. Zelensky published open letter proposing face-to-face talks with Putin.",
        "priority": 1,
    },
    {
        "agent": "news",
        "title": "US jobs data forces full Fed rate-hike pricing",
        "body": "May employment topped expectations. $31T Treasury market fully prices in Fed rate hike this year. S&P record streak in danger as AI selloff continues. First rate-hike pricing since Fed's pause.",
        "priority": 1,
    },
    {
        "agent": "news",
        "title": "Trump proposes forced-labor tariffs on 60 economies",
        "body": "10%+ surcharge proposed on 59 countries + EU for forced labor practices. Broadest trade action in modern US history. Covers China, EU, Mexico, India, most trading partners.",
        "priority": 1,
    },
]

for item in items:
    tid, action = upsert(item["agent"], item["title"], item["body"], item["priority"])
    print(f"[{action}] {item['agent']}: {item['title']} → {tid}")

conn.close()
print(f"\nDone. {len(items)} items processed.")