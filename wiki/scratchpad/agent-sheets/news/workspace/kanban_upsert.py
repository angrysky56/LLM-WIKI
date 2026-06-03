#!/usr/bin/env python3
"""Kanban upsert — 2026-06-03 news cycle. Informational cards (status=done)."""
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
    cur.execute("""
        INSERT INTO tasks (id, title, body, assignee, status, priority, created_by, idempotency_key, created_at)
        VALUES (?, ?, ?, ?, 'done', ?, 'cron:kanban-morning-review', ?, ?)
    """, (tid, key, body, agent, priority, ik, int(time.time())))
    conn.commit()
    return tid, "created"

items = [
    ("news", "Iran strikes Kuwait and Bahrain — Gulf war escalates (2026-06-03)",
     "Iran missile/drone barrage hit Kuwait airport (1+ killed) and Bahrain. US-Iran mutual accusations. Rubio says war is 'over.' Trump floats meeting Khamenei. Oil +3 days. Carryover thread: [[us-iran-trade-strikes-kuwait-radar-sites-june-1-2026]] (2026-06-01 Kuwait radar strikes) is now significantly outdated.\n\nSource: [[wiki/sources/news/2026/iran-strikes-kuwait-bahrain-gulf-escalation-june-3-2026]]",
     2),
    ("news", "Ukraine strikes St Petersburg on Putin's economic forum opening day (2026-06-03)",
     "Ukrainian long-range drones hit oil storage and naval base near St Petersburg on the first day of SPIEF. Deepest strike by name in the war. Reciprocal to 2026-06-02 [[russia-kyiv-deadly-strikes-june-2-2026]].\n\nSource: [[wiki/sources/news/2026/ukraine-strikes-st-petersburg-putin-economic-forum-june-3-2026]]",
     2),
    ("news", "Trump endorses Colombia right-wing Espriella for June runoff (2026-06-03)",
     "Public endorsement of Abelardo De La Espriella ahead of runoff vs Iván Cepeda. Pairs with 2026-06-02 [[trump-brazil-25-percent-tariff-june-2-2026]] as coordinated Latin America right-wing bloc consolidation.\n\nSource: [[wiki/sources/news/2026/trump-endorses-colombia-espriella-runoff-june-3-2026]]",
     2),
    ("news", "Trump '51st state' remark overshadows Canada-US trade talks (2026-06-03)",
     "Trump again called Canada the '51st state' hours before USMCA review talks. Canada formally requested 16-year USMCA renewal. Carney shrugged off. Same-week Americas realignment posture alongside Brazil/Colombia.\n\nSource: [[wiki/sources/news/2026/trump-canada-51st-state-trade-talks-june-3-2026]]",
     1),
    ("news", "SpaceX IPO pricing confirmed: $75B at $135/share (2026-06-03)",
     "Fixed-price structure signals strong demand. Largest IPO of 2026, ahead of 2026-06-12 expected trading. BlackRock $10B anchor stake tracks. Pairs with 2026-06-02 [[anthropic-confidentially-files-ipo-2026-june-2]] as the two trillion-dollar AI/space events of the quarter.\n\nSource: [[wiki/sources/news/2026/spacex-ipo-75-billion-135-per-share-june-3-2026]]",
     1),
]

created = []
for it in items:
    tid, status = upsert(*it)
    print(f"  [{status}] {tid} — {it[1][:80]}")
    if status == "created":
        created.append(tid)

print(f"\nTotal: {len(created)} new, {len(items)-len(created)} skipped")
