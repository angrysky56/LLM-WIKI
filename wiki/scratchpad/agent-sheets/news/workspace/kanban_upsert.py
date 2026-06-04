#!/usr/bin/env python3
"""Kanban upsert for news-agent open items surfaced 2026-06-04.
Status='done' (informational cards, dispatcher ignores) per kanban-review skill.
"""
import sqlite3, hashlib, uuid, time, os

DB_PATH = os.path.expanduser("~/.hermes/kanban.db")
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# Check existing non-done tasks to avoid duplicates
cur.execute("SELECT id, title, status FROM tasks WHERE status != 'done'")
existing = {str(row[1]).strip(): row[0] for row in cur.fetchall()}

# Also check all tasks for idempotency on title
cur.execute("SELECT id, title FROM tasks")
all_existing = {str(row[1]).strip(): row[0] for row in cur.fetchall()}

def upsert(agent, title, body, priority=1):
    key = f"{agent}: {title}".strip()
    if key in all_existing:
        return all_existing[key], "skipped"
    ik = hashlib.sha256(key.encode()).hexdigest()[:16]
    tid = f"t_{uuid.uuid4().hex[:16]}"
    cur.execute("""
        INSERT INTO tasks
          (id, title, body, assignee, status, priority, created_by, idempotency_key, created_at)
        VALUES (?, ?, ?, ?, 'done', ?, 'cron:kanban-news', ?, ?)
    """, (tid, key, body, agent, priority, ik, int(time.time())))
    conn.commit()
    return tid, "created"

items = [
    # Story 1 — US House war powers vote
    ("news", "US House 215-208 war powers resolution halt Iran war — follow-up",
     "First successful House check on Trump's war authority since the February Iran war launch. 4 Republicans (Massie, Fitzpatrick, Barrett, Davidson) defected; Democrat Golden (ME) switched to support. Fourth attempt. Concurrent resolution — Senate version advanced in May, full floor vote pending. White House called it unconstitutional. Same day Trump said 'we're close to signing a paper' with Iran — vote may be a face-saving structure for a deal. Open: Senate floor vote timing, Trump response to defections, Iran deal announcement (Trump said 'as soon as this weekend'). See wiki/sources/news/2026/us-house-votes-halt-iran-war-powers-june-4-2026.md",
     1),
    # Story 2 — Israel-Lebanon trilateral
    ("news", "Israel-Lebanon trilateral ceasefire with Hezbollah evacuation clause — follow-up",
     "Fourth round of US-mediated trilateral talks in Washington. Deal requires complete cessation of Hezbollah attacks, evacuation between Israeli border and Litani River (~30km north), new 'pilot security zones' with LAF-only control. No maps. Next talks June 22. Israeli strikes continued same day (9+ killed; strike on ambulance killed 2 paramedics). Far-right ministers Ben-Gvir and Smotrich opposed. Builds on 2026-06-02 'stop all shooting' partial deal. Open: Hezbollah official response, Israeli ground force withdrawal timeline, pilot zone implementation, June 22 agenda. See wiki/sources/news/2026/israel-lebanon-ceasefire-security-zones-june-4-2026.md",
     1),
    # Story 3 — Kim nuclear expansion
    ("news", "Kim Jong Un 'exponential' nuclear arsenal expansion — follow-up",
     "Third disclosed uranium-enrichment site in DPRK. First use of 'exponential' in public. Production capacity 'more than double' 5 years ago. KCNA: 'epochal milestone.' Photos show Kim walking through enrichment centrifuge hall. Analyst read (NK News' O'Carroll): timed to potential Xi visit to Pyongyang, denuclearization being publicly foreclosed on eve of PRC contact. South Korea's JCS confirmed disclosed site is a uranium enrichment facility. Open: Verify site vs previous disclosed sites, Xi visit confirmation, South Korea nuclear-weapon debate acceleration. See wiki/sources/news/2026/kim-jong-un-exponential-nuclear-arsenal-expansion-june-4-2026.md",
     1),
    # Story 4 — Somalia
    ("news", "Somalia Mogadishu capital fighting — president term extension — follow-up",
     "Heavy clashes in Mogadishu Wed-Thu, mortar and anti-tank fire on residential areas including Bakara market. Trigger: President Hassan Sheikh Mohamud's mid-May one-year term extension beyond 2026-05-15 expiry. Opposition includes former president Sharif Sheikh Ahmed and former PM Hassan Ali Khaire. Government reportedly using drones. UN, UK, US condemn. Same resident: 'more intense than [2021] anyone expected.' Strategic opening for al-Shabaab. Wider Horn of Africa instability. Open: death toll, Thursday protest outcomes, AU/ATMIS/UNSOM response, Hassan Sheikh reversal possibility, al-Shabaab response. See wiki/sources/news/2026/somalia-mogadishu-fighting-term-extension-june-4-2026.md",
     1),
    # Story 5 — Ebola
    ("news", "DRC Ebola 'big head start' + US-only Kenya quarantine criticism — follow-up",
     "WHO chief Tedros reframed the timeline: virus 'had a big head start' — actual start could be January 2026 (5+ months undetected). 344+ confirmed DRC cases, 60 deaths; 15 Uganda, 1 death. Open letter to Congress from former top US health officials (31-year CDC veteran Jernigan, IDSA president Nahass) calls the Trump 'American-only' Kenya quarantine facility 'a sharp departure from the standard upheld by every previous administration' — inverts 2014 doctrine. Kenya high court blocked plan but both governments moved forward; first responders at Laikipia airbase May 31. Tedros also named the US travel ban as 'disrupting supply chains.' First major outbreak of the post-USAID-collapse era. Open: contact tracing 45→90% trajectory, IHR EC re-convening, US courts ruling on Kenya facility, South Sudan/Rwanda/Burundi transmission, vaccine pipeline. See wiki/sources/news/2026/ebola-drc-outbreak-began-january-kenya-quarantine-criticized-june-4-2026.md",
     1),
]

results = []
for agent, title, body, prio in items:
    tid, status = upsert(agent, title, body, priority=prio)
    results.append((tid, status, title))

print('=' * 60)
print('NEWS KANBAN UPSERT — 2026-06-04')
print('=' * 60)
for tid, status, title in results:
    print(f'  [{status:8}] {tid}  {title}')

# Print full task list to confirm
cur.execute("SELECT id, title, status, assignee FROM tasks WHERE created_by = 'cron:kanban-news'")
print()
print('All news-created tasks:')
for row in cur.fetchall():
    print(f'  {row[0]}  [{row[2]}]  {row[3]}: {row[1]}')
