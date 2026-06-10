#!/usr/bin/env python3
"""Kanban upsert for news-agent informational cards.
Creates status=done cards for open questions so Ty has a unified view.
"""
import sqlite3, hashlib, uuid, time, os

DB_PATH = os.path.expanduser("~/.hermes/kanban.db")
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()
cur.execute("SELECT id, title, status FROM tasks")
existing = {str(r[1]).strip(): r[0] for r in cur.fetchall()}

def upsert(agent, title, body, priority=1):
    key = f"{agent}: {title}".strip()
    if key in existing:
        return existing[key], "skipped"
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
        "title": "Ceasefire durability — Israel Tyre attacks, ceasefire fracturing",
        "body": "Israel attacked Tyre, Lebanon ceasefire fracturing. Track: Hezbollah response, IDF movements, US-Iran diplomatic track. Source: BBC, Al Jazeera, NYT (June 10 RSS)",
    },
    {
        "agent": "news",
        "title": "Iran de-escalation — Trump says peace talks on track",
        "body": "Trump and Iran trade new threats after strikes exchanged. Both sides demand victory. Source: BBC, CBS News, The Guardian (June 10 RSS)",
    },
    {
        "agent": "news",
        "title": "Peru election — runoff still too close to call",
        "body": "Leftist Sanchez takes lead; count could take weeks. Source: NYT, Reuters, Le Monde, Al Jazeera (June 10 RSS)",
    },
    {
        "agent": "news",
        "title": "Ukraine peace conditions — Russia response pending",
        "body": "Zelensky/Europe allies set out 5 conditions. Russia formal rejection/acceptance still pending. Source: BBC, Kyiv Post (June 10 RSS)",
    },
    {
        "agent": "news",
        "title": "Armenia-Russia — sanctions threat materialized",
        "body": "Russia threatens sanctions as Pashinyan pivots from Moscow. Watch for actual sanctions implementation. Source: CNN, The New Voice of Ukraine (June 10 RSS)",
    },
    {
        "agent": "news",
        "title": "World Cup visa disputes — Iran under tight security",
        "body": "Iran team moves under tight security in Mexico after US visa dispute. Somali referee denied entry. Source: Turkiye Today, Gulf News, TRT World (June 10 RSS)",
    },
    {
        "agent": "news",
        "title": "US inflation CPI — 3.4% fastest in 3 years",
        "body": "Fed rate hike bets remain for 2026. Impact on AI IPO pipeline? Source: Bloomberg, Reuters (June 10). Status: NEW source page written.",
    },
    {
        "agent": "news",
        "title": "Belfast anti-immigrant violence",
        "body": "Wave of anti-immigrant violence erupts after stabbing in Belfast. UK leaders call for calm. Source: NYT, Washington Post, BBC (June 10). Status: NEW source page written.",
    },
]

results = []
for item in items:
    tid, action = upsert(item["agent"], item["title"], item["body"])
    results.append(f"{action}: {item['title'][:60]} -> {tid}")
    print(f"{action}: {tid} — {item['title'][:60]}")

conn.close()
print("\nDone. Created/skipped upsert cards.")