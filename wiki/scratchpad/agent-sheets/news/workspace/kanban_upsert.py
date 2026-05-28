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

# 1. SpaceX IPO BlackRock confirmation — BlackRock still "considering" per multiple sources
results.append(upsert_done(
    "news",
    "SpaceX IPO BlackRock $10B confirmation",
    "SpaceX S-1 filed June 12 target confirmed. BlackRock $10B: still 'considering' per KraneShares, Gotrade, CNBC. No confirmation as of 2026-05-28. Kraken Blog notes 'timeline accelerates' but no BlackRock update. Quiet period approaching."
))

# 2. Anthropic-Vatican State Dept guidance — no public signal detected
results.append(upsert_done(
    "news",
    "Anthropic-Vatican US State Department response",
    "Anthropic was only major AI company at May 27 'Magnifica humanitas' encyclical. Vance called it 'profound' but other officials split. No US State Department guidance detected as of 2026-05-28. Vatican inscribing itself as AI governance actor. Other AI companies (Google, Microsoft, OpenAI) absent."
))

# 3. OpenAI/Erdős proof peer review — months timescale per carryover
results.append(upsert_done(
    "news",
    "OpenAI o1 Erdős proof peer review status",
    "OpenAI o1 formally disproved central Erdős geometry conjecture ~80 years old (May 20). Terence Tao: 'ingenious ideas.' Peer review ongoing — months timescale per mathematical community. Gemini independently solved different 80-year problem 9-to-1 faster. Formal publication status for both unknown as of 2026-05-28."
))

# 4. Russia Bundibugyo vaccine claim verification
results.append(upsert_done(
    "news",
    "Russia Bundibugyo Ebola vaccine claim verification",
    "Russia announced experimental Bundibugyo vaccine (May 27) — no Western pharma has announced Bundibugyo-specific R&D. No WHO submission detected. African nation engagement unknown. Claim is notable geopolitical positioning but unverified as of 2026-05-28."
))

# 5. South Sudan Ebola border detection
results.append(upsert_done(
    "news",
    "South Sudan Ebola border cases detected",
    "South Sudan at breaking point per MSF — violence, hunger as weapon. Violence pushes civilians toward epidemic zones, degrades healthcare. No Ebola cases confirmed at South Sudan border as of 2026-05-28 per carryover. WHO monitoring capacity in conflict zones remains unclear."
))

# 6. California AI 60-day review agency actions
results.append(upsert_done(
    "news",
    "California AI 60-day agency review status",
    "Governor Newsom signed EO May 21. Multiple agencies now implementing. Critics say protections fall short (no mandatory employer obligations, no new funding). 60-day review in progress. Key: whether state agencies meet the review timeline."
))

for tid, status in results:
    print(f"{status}: {tid}")

DB.close()