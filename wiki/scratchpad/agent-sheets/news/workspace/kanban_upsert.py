#!/usr/bin/env python3
"""Kanban upsert for news-agent Cycle 20 — informational cards (status=done)."""
import sqlite3, hashlib, uuid, time, os
DB_PATH = os.path.expanduser("~/.hermes/kanban.db")
conn = sqlite3.connect(DB_PATH); cur = conn.cursor()
cur.execute("SELECT id, title, status FROM tasks")
existing = {str(r[1]).strip(): r[0] for r in cur.fetchall()}
def upsert(agent, title, body, priority=1):
    key = f"{agent}: {title}".strip()
    if key in existing: return existing[key], "skipped"
    ik = hashlib.sha256(key.encode()).hexdigest()[:16]
    tid = f"t_{uuid.uuid4().hex[:16]}"
    cur.execute("INSERT INTO tasks (id, title, body, assignee, status, priority, created_by, idempotency_key, created_at) VALUES (?, ?, ?, ?, 'done', ?, 'cron:kanban-morning-review', ?, ?)",
        (tid, key, body, agent, priority, ik, int(time.time())))
    conn.commit(); return tid, "created"

# --- Cycle 20 news topics ---
items = [
    ("news-agent", "Open Q: Israel-Hezbollah ceasefire durability",
     "Will the Trump-mediated ceasefire hold? Watch for Hezbollah official response, IDF verification, border incidents in first 48 hours. Source: wiki/sources/news/2026/israel-hezbollah-ceasefire-trump-june-8-2026.md"),
    ("news-agent", "Open Q: USMCA missed July deadline fallout",
     "US, Mexico, Canada miss July USMCA review date — trade tensions ramp up. Google News exclusive catch. Source: wiki/sources/news/2026/usmca-review-deadline-missed-june-8-2026.md"),
    ("news-agent", "Open Q: Peru presidential runoff dead heat",
     "Too close to call. Weeks of counting expected. Source: BBC, NYT, AJ, Bloomberg"),
    ("news-agent", "Open Q: Chornobyl IAEA — no restart timeline",
     "IAEA Board of Governors statement: no timeline for nuclear waste site restart after Russian strikes. Partially resolved. Source: IAEA/Interfax-Ukraine"),
    ("news-agent", "Open Q: Russia response to European peace conditions",
     "Five conditions outlined by Ukraine, UK, France, Germany. No formal Russian response yet."),
    ("news-agent", "Open Q: Xi-Kim summit — strategic cooperation",
     "Xi in Pyongyang calling for strengthened strategic cooperation. Any concrete agreements? Source: AJ, NYT, Guardian, GN"),
    ("news-agent", "Open Q: AI sell-off — correction or rotation?",
     "Tech tumbling as Fed rate hike odds rise. Iran de-escalation may stabilize markets. Source: Bloomberg, Reuters, Economic Times"),
    ("news-agent", "Written: Israel-Hezbollah ceasefire (Trump-mediated)",
     "Source page written: israel-hezbollah-ceasefire-trump-june-8-2026. Part of 3-page cycle."),
    ("news-agent", "Written: USMCA missed deadline",
     "Source page written: usmca-review-deadline-missed-june-8-2026"),
    ("news-agent", "Written: Ebola 2014 record warning",
     "Source page written: ebola-central-africa-2014-record-warning-june-8-2026. US health officials warn DRC outbreak could match 2014 scale."),
]
for agent, title, body in items:
    tid, action = upsert(agent, title, body)
    print(f"  {action:8s} {tid[:12]} -> {title[:60]}")
conn.close()