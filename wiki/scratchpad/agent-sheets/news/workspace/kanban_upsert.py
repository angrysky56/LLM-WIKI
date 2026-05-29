import sqlite3, hashlib, uuid, time, os

DB = sqlite3.connect(os.path.expanduser("~/.hermes/kanban.db"))
cur = DB.execute("SELECT id, title, status FROM tasks WHERE status != 'done'", ())
existing = {str(row[1]).strip(): row[0] for row in cur.fetchall()}

def upsert_done(agent, title, body, priority=1):
    """Informational card pattern — status done immediately, dispatcher does NOT pick up"""
    key = f"{agent}: {title}".strip()
    if key in existing:
        return existing[key], "skipped"
    ik = hashlib.sha256(key.encode()).hexdigest()[:16]
    tid = f"t_{uuid.uuid4().hex[:16]}"
    cur.execute("""
        INSERT INTO tasks
          (id, title, body, assignee, status, priority, created_by, idempotency_key, created_at)
        VALUES (?, ?, ?, ?, 'done', ?, 'cron:news-agent', ?, ?)
    """, (tid, key, body, agent, priority, ik, int(time.time())))
    DB.commit()
    return tid, "created"

results = []

# 1. Ebola May 29-30 ETC attack window
results.append(upsert_done(
    "news",
    "Ebola May 29-30 ETC attack window outcome",
    "Third ETC attack confirmed May 26 (Mongbwalu). Attack frequency ~2-3 days creates elevated concern for May 29-30. 18 patients fled May 23. Outbreak spreading faster than response. Case count ~1,018+, doubled since PHEIC declaration. Sud-Kivu confirmed. Watch for: new ETC attack, case count update, South Sudan border detection."
))

# 2. SpaceX IPO BlackRock disclosure window June 7-10
results.append(upsert_done(
    "news",
    "SpaceX IPO BlackRock $10B confirmation — disclosure window June 7-10",
    "SpaceX June 12 listing (13 days). Quiet period likely begins June 7-10. BlackRock $10B still 'considering' with no confirmation. Anchor investor disclosure expected via S-1/A amendment in that window. If not confirmed before quiet period, won't be disclosed until post-listing. Governance question (Musk voting control) also unresolved."
))

# 3. California AI agency implementation signals
results.append(upsert_done(
    "news",
    "California AI 60-day agency review — substantive vs performative",
    "60-day review clock running (from May 21 EO). Agencies now implementing. Critics say no mandatory obligations, no new funding. Leading indicator: whether agency actions signal substantive policy development or boilerplate review. Federal AI regulation off table — California is de facto US AI governance framework. Next 2-3 weeks will show whether review is real."
))

for tid, status in results:
    print(f"{status}: {tid}")

DB.close()
