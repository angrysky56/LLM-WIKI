import sqlite3, hashlib, uuid, time, os

DB_PATH = os.path.expanduser("~/.hermes/kanban.db")
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# Check all existing (for dedup)
cur.execute("SELECT id, title, status FROM tasks")
existing_all = {str(row[1]).strip(): row[0] for row in cur.fetchall()}

def upsert(agent, title, body, priority=1, blocked=False):
    key = f"{agent}: {title}".strip()
    if key in existing_all:
        return existing_all[key], "skipped (exists)"
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

# News agent informational cards for the 2026-06-01 cycle.
# News writes to wiki, so these go in as status='done' (informational, dispatcher ignores).
items = [
    ("news", "US-Iran Direct Strikes: Kuwait Becomes Theater",
     "Day 94 of Iran war: US bombed Iranian radar sites and air defenses; Iran retaliated by striking US forces in Kuwait with drones and missiles. First time Kuwait is a direct target since 1991 Gulf War. 20 US sites damaged since war start (BBC satellite analysis). Parallel ceasefire talks ongoing (Trump editing draft agreement on enriched uranium + Hormuz).",
     1),
    ("news", "France/UK Seize Russian Tanker 'Tagor' in Atlantic — First-of-Kind",
     "French Navy with UK support intercepted sanctioned Russian shadow-fleet tanker Tagor in the Atlantic; Macron publicly confirmed. First-of-kind NATO European high-seas interdiction of a Russian sanctions-evasion vessel. Direct challenge to G7 $60/bbl price cap architecture.",
     1),
    ("news", "Quantinuum Upsizes IPO to $1.46B at $14.3B Valuation",
     "Honeywell-backed pure-play trapped-ion quantum company targets $1.46B raise at $14.3B valuation. Major public-market validation for quantum hardware. Comes amid Bloomberg-reported AI-bubble debate — quantum positioned as 'next-AI' thesis.",
     1),
    ("news", "Colombia Runoff Set: De la Espriella vs. Cepeda",
     "Right-wing pro-Trump Bukele-inspired De la Espriella leads first round; will face Petro-ally leftist Cepeda in June runoff. Petro's party 'sowing doubt in results' per AP. Colombian peso and assets surged on right-wing lead. Continues Latin America right-wing wave (Argentina/El Salvador/Ecuador pattern).",
     1),
    ("news", "Myanmar Shan State Blast Kills 39+ in Rebel-Held Village",
     "Explosives depot blast flattened rebel-held village in northeast Myanmar (Shan State). Cause under investigation. Civilian impact of post-2021 civil war.",
     2),
]

results = []
for agent, title, body, prio in items:
    results.append(upsert(agent, title, body, priority=prio))

print("Done. Results:")
for tid, status in results:
    print(f"  {status}: → {tid}")
