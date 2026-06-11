import sqlite3, hashlib, uuid, time, os

DB_PATH = os.path.expanduser("~/.hermes/kanban.db")
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# Get existing tasks for dedup
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

# Open questions from this cycle — informational cards
items = [
    ("news-agent", "Iran-US ceasefire talks: What happens next after Day 2 of strikes?", "US-Iran exchanged strikes for Day 2; Iran closed Hormuz and struck Bahrain/Kuwait/Jordan. Ceasefire talks reportedly intensified alongside military ops. Track: does diplomacy or escalation dominate?"),
    ("news-agent", "Fed pivot: Rate hike probability after ECB action + US PPI spike?", "ECB hiked 25bps (first since 2023) citing Iran energy shock. US PPI fastest in 3+ years. Bond traders now pricing in a Fed 2026 hike. Track: June FOMC meeting outcome."),
    ("news-agent", "SpaceX IPO debut: First-day trading pop after $70B retail orders?", "SpaceX order book closes June 11. $70B+ retail orders, 4x oversubscribed. Retail rotating out of Big Tech to participate. Track: Nasdaq debut valuation, first-day performance."),
    ("news-agent", "UK defense secretary: Who replaces Healey and at what spending level?", "John Healey resigned over military spending. Replacement will signal UK commitment to NATO/Iran/Ukraine commitments. Track: appointment, defense budget trajectory."),
    ("news-agent", "Kenya Ebola crisis: Will US respond to protests with policy change?", "Protester shot dead at anti-US-Ebola-facility protest. NYT calls it a political crisis in Kenya. Track: US response, protests escalation."),
    ("news-agent", "El Niño intensity: Which regions face worst drought/flood/fire impacts?", "NOAA declared El Niño official; potentially strongest in a century. WMO issued global preparedness directive. Track: regional impacts on agriculture, commodities, conflict risk."),
]

results = []
for agent, title, body in items:
    tid, action = upsert(agent, title, body)
    results.append(f"{action}: [{title[:60]}] -> {tid}")
    conn.commit()

conn.close()

for r in results:
    print(r)
print(f"\nTotal: {len(results)} cards processed")