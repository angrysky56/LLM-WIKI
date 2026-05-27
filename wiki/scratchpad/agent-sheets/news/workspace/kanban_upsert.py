import sqlite3, hashlib, uuid, time

DB = sqlite3.connect("/home/ty/.hermes/kanban.db")
cur = DB.execute("SELECT id, title, status FROM tasks WHERE status != 'done'", ())
existing = {str(row[1]).strip(): row[0] for row in cur.fetchall()}

def upsert(agent, title, body, priority=1, blocked=False):
    key = f"{agent}: {title}".strip()
    if key in existing:
        return existing[key], "skipped"
    ik = hashlib.sha256(key.encode()).hexdigest()[:16]
    tid = f"t_{uuid.uuid4().hex[:16]}"
    status = "blocked" if blocked else "ready"
    cur.execute("""
        INSERT INTO tasks
          (id, title, body, assignee, status, priority, created_by, idempotency_key, created_at)
        VALUES (?, ?, ?, ?, ?, ?, 'cron:kanban-morning-review', ?, ?)
    """, (tid, key, body, agent, status, priority, ik, int(time.time())))
    DB.commit()
    return tid, "created"

tasks = [
    # Ebola items — web-researcher
    ("web-researcher", "Ebola: Russia Bundibugyo vaccine claim verification",
     "Verify Russia WHO submission, African nation engagement, prior R&D evidence. Source: WION May 27.", 2),
    ("web-researcher", "Ebola: South Sudan border transmission status",
     "Monitor South Sudan spillover risk, WHO border coordination updates.", 2),
    ("web-researcher", "Ebola: official case count update (DRC/Uganda)",
     "Track officialsuspected case count vs IRC Watchlist 'spreading faster than response' assessment.", 1),

    # SpaceX IPO — researcher monitoring
    ("researcher", "SpaceX IPO: BlackRock $10B confirmation tracking",
     "Monitor whether BlackRock confirms $10B stake pre-June 12 listing.", 2),
    ("researcher", "SpaceX IPO: governance disclosure — Musk voting control",
     "Monitor whether SpaceX clarifies Musk voting control pre-IPO quiet period.", 2),

    # Anthropic-Vatican — web-researcher
    ("web-researcher", "Anthropic-Vatican: State Department AI diplomacy guidance",
     "Check if US State Dept issues guidance countering or engaging Vatican AI encyclical position.", 2),
    ("web-researcher", "Anthropic-Vatican: other AI companies respond to encyclical",
     "Monitor whether OpenAI, Google DeepMind, Microsoft respond to Pope Leo 'Magnifica humanitas'.", 2),

    # California AI order — researcher
    ("researcher", "California AI order: state agency implementation actions",
     "Track 60-day review implementation actions from California state agencies.", 1),

    # Tariff/Trade items — researcher
    ("researcher", "EU-US deal: full implementation text, specific tariff rates",
     "Monitor for published implementation text and specific tariff rates post-May 20 ratification.", 1),
]

for agent, title, body, priority in tasks:
    tid, status = upsert(agent, title, body, priority)
    print(f"  [{status}] {agent}: {title} → {tid}")

DB.close()
print("\nDone.")
