import sqlite3, hashlib, uuid, time, os
DB_PATH = os.path.expanduser("~/.hermes/kanban.db")
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()
cur.execute("SELECT id, title, status FROM tasks WHERE status != 'done'")
existing = {str(r[1]).strip(): r[0] for r in cur.fetchall()}

def upsert(agent, title, body, priority=1):
    key = f"{agent}: {title}".strip()
    if key in existing:
        return existing[key], "skipped"
    ik = hashlib.sha256(key.encode()).hexdigest()[:16]
    tid = f"t_{uuid.uuid4().hex[:16]}"
    # news agent = wiki-writer → status='done' (informational card, dispatcher ignores)
    cur.execute("""
        INSERT INTO tasks
          (id, title, body, assignee, status, priority, created_by, idempotency_key, created_at)
        VALUES (?, ?, ?, ?, 'done', ?, 'cron:kanban-morning-review', ?, ?)
    """, (tid, key, body, agent, priority, ik, int(time.time())))
    conn.commit()
    return tid, "created"

items = [
    ("news",
     "Israel-Hezbollah partial ceasefire (Trump, ground clashes continue)",
     """News 2026-06-02 — Israel-Hezbollah partial ceasefire.

Trump announced Israel and Hezbollah agreed to "stop all shooting." Israel backs off Beirut strikes after Trump reportedly called Netanyahu "crazy" in a private pressure call. Ground clashes continued: at least 5-8 killed in southern Lebanon same day. Iran suspended US talks in protest of Israeli Lebanon attacks, making the Lebanon ceasefire a *prerequisite* (not downstream) of the US-Iran deal. This is the lynchpin — if it holds, Trump gets his "deal over the next week"; if it collapses, multiple peace tracks fail.

Clipping: Clippings/articles/2026/israel-hezbollah-partial-ceasefire-trump-june-2-2026.md
Summary: wiki/sources/news/2026/israel-hezbollah-partial-ceasefire-trump-2026-06-02.md
Headlines: wiki/scratchpad/jobs/reports/news/headlines-2026-06-02.md

Open questions:
- Will the partial ceasefire hold given the same-day strikes?
- Is Trump's "crazy" call a deliberate pressure tactic or a real fracture?
- What is Iran's position post-suspension?
""", 2),
    ("news",
     "Russia massive Kyiv strikes — 18+ killed, NYT: Russian weakness",
     """News 2026-06-02 — Russia massive Kyiv strikes.

"After an Agonizing Week of Threats, Kyiv Is Finally Bombarded" (NYT). 18+ killed, apartment building toppled (8-year-old boy among dead). NYT editorial: "Russia Is Showing Signs of Weakness in Ukraine. So It Hits Harder" — interprets this as revenge strike from side losing war, not a turning point. One of deadliest offensives in months. Risk: Western leaders read the spike as a negotiating moment and offer Moscow favorable terms.

Clipping: Clippings/articles/2026/russia-kyiv-deadly-strikes-june-2-2026.md
Summary: wiki/sources/news/2026/russia-kyiv-deadly-strikes-2026-06-02.md

Open questions:
- Is this escalation a Russian negotiating move or desperation?
- Will the strikes change Western posture on Ukraine support?
""", 2),
    ("news",
     "Trump 25% Brazil tariff — politically-motivated",
     """News 2026-06-02 — Trump 25% Brazil tariff.

USTR proposed 25% tariff on Brazilian goods "to punish Brazil over trade practices" (Reuters). Politically-motivated — first Trump tariff against a major Latin American democracy and a BRICS member. Coordinated with Colombia right-wing push (Espriella first-round win 2026-06-01) — Trump administration consolidating hemispheric right-wing bloc. Brazil has BRICS diplomatic cover to retaliate.

Clipping: Clippings/articles/2026/trump-administration-25-percent-brazil-tariff-june-2-2026.md
Summary: wiki/sources/news/2026/trump-brazil-25-percent-tariff-2026-06-02.md

Open questions:
- Brazilian retaliation options?
- BRICS response coordination?
- US trade court challenge (cf. us-trade-court-tariff-ruling-may-2026)?
""", 2),
    ("news",
     "Anthropic IPO filing at ~$1T valuation",
     """News 2026-06-02 — Anthropic IPO filing.

Anthropic confidentially filed SEC IPO prospectus (CNBC), US share sale planned at ~$1T valuation. Second trillion-dollar AI public-market event in a single quarter — SpaceX IPO is 2026-06-12. AI-bubble debate intensifying; Figma's post-IPO correction is the cautionary tale (MarketWise "AI IPO Trap"). Anthropic has warned about unauthorized secondary platforms (Axios, TechCrunch).

Clipping: Clippings/articles/2026/anthropic-confidentially-files-ipo-2026-june-2.md
Summary: wiki/sources/news/2026/anthropic-ipo-sec-filing-2026-06-02.md

Open questions:
- Final pricing and public reception?
- How does this affect OpenAI's competitive positioning?
- Will secondary-market warnings translate into a cleaner IPO book?
""", 1),
    ("news",
     "Kenya court blocks US Ebola quarantine; 2 killed in protests",
     """News 2026-06-02 — Kenya court blocks US Ebola facility.

Kenya High Court ordered government to release US-Ebola-quarantine-center details; 2 shot dead in protests. Sovereignty test case — US wants to quarantine American Ebola patients in Africa (bypassing "evacuate to US/Europe"). DRC outbreak continues; 3 vaccines in development (BBC). Risk of further escalation significant.

Clipping: Clippings/articles/2026/ebola-kenya-court-ruling-protests-june-2-2026.md
Summary: wiki/sources/news/2026/ebola-kenya-court-protests-2026-06-02.md

Open questions:
- Will Kenya government comply with court order?
- US response to the court ruling?
- DRC outbreak trajectory?
""", 1),
]

created = []
skipped = []
for agent, title, body, prio in items:
    tid, status = upsert(agent, title, body, prio)
    print(f"  {status}: {tid}  --  {title[:60]}")
    if status == "created":
        created.append(tid)
    else:
        skipped.append(tid)
print(f"\nSummary: {len(created)} created, {len(skipped)} skipped")
