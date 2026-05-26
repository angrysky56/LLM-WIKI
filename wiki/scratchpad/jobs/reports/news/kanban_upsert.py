import sqlite3, hashlib, time

DB = sqlite3.connect("/home/ty/.hermes/kanban.db")
cur = DB.execute(
    "SELECT id, title, status FROM tasks WHERE status != 'done'",
    ()
)
existing = {str(row[1]).strip(): row[0] for row in cur.fetchall()}

items = [
    ("web-researcher", "Ebola PHEIC: case count update and South Sudan status", "Case count updates (1,200+ suspected — official counts lag reality), South Sudan transmission status, WHO Emergency Committee recommendations, vaccine trial progress. Source: news/carryover.md HIGHEST priority.", 2),
    ("web-researcher", "SpaceX IPO June 12: pre-IPO developments and BlackRock $10B confirmation", "Pre-IPO Starship tests, SEC filings, investor sentiment, BlackRock $10B confirmation before June 12 listing. Source: news/carryover.md.", 2),
    ("web-researcher", "OpenAI o3 math proof: peer review outcome", "Erdős geometry conjecture proof under formal peer review — no verdict yet. Monitor for outcome. Source: news/carryover.md.", 1),
    ("web-researcher", "California AI order: state agency implementation and vendor safeguards", "Implementation actions from the May 21 worker protection order — leading indicator for whether California's AI governance model scales. Source: news/carryover.md.", 1),
    ("web-researcher", "EU-US deal: full implementation text and tariff rates under 2029 window", "Specific tariff rates reduced or merely structured under 2029 expiry window. Source: news/carryover.md.", 1),
    ("web-researcher", "D-Wave quantum: whether D-Wave contests Flatiron Institute finding", "Flatiron Institute tensor network algorithm matched D-Wave's 2019 quantum advantage on classical hardware. Monitor whether D-Wave contests. Source: news/carryover.md.", 1),
    ("web-researcher", "Malaysia exit ripple: which ASEAN countries follow and supply chain impact", "First country to exit US bilateral post-tariff-ruling. Watching for ASEAN nations signaling similar recalibration. Source: news/carryover.md.", 1),
    ("web-researcher", "Rubio-India $500B: whether negotiations restart and legal framework", "Original tariff bargain lost footing after Supreme Court ruling invalidated US tariff authority. Monitor for negotiation restart. Source: news/carryover.md.", 1),
    ("researcher", "EU-US 2029 expiry template: whether other bilateral deals adopt format", "Supreme Court limitations on US unilateral tariff authority make EU-US 2029-expiry format attractive to other countries. Research: which bilateral deals (India, ASEAN) may adopt this template. Source: news/carryover.md.", 1),
]

created = []
for agent, title, body, priority in items:
    key = f"{agent}: {title}".strip()
    if key in existing:
        print(f"SKIP: {key}")
        continue
    ik = hashlib.sha256(key.encode()).hexdigest()[:16]
    tid = f"t_{ik}"
    cur.execute("""
        INSERT INTO tasks
          (id, title, body, assignee, status, priority, created_by, idempotency_key, created_at)
        VALUES (?, ?, ?, ?, ?, ?, 'cron:kanban-morning-review', ?, ?)
    """, (tid, key, body, agent, 'done', priority, ik, int(time.time())))
    created.append((tid, key))

DB.commit()
DB.close()
print(f"Created {len(created)} tasks")
for tid, key in created:
    print(f"  {tid}: {key}")
