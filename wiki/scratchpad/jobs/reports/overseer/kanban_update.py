import sqlite3, os, hashlib, uuid, time

DB = os.path.expanduser("~/.hermes/kanban.db")
conn = sqlite3.connect(DB)
cur = conn.cursor()

# Check existing (all tasks — status=done cards are also in the table)
cur.execute("SELECT id, title, status FROM tasks")
existing = {row[1].strip(): row[0] for row in cur.fetchall()}

def upsert_done(agent, title, body=""):
    key = f"[{agent}] {title}".strip()
    if key in existing:
        return existing[key], "skipped"
    ik = hashlib.sha256(key.encode()).hexdigest()[:16]
    tid = f"t_{uuid.uuid4().hex[:16]}"
    cur.execute("""
        INSERT INTO tasks
          (id, title, body, assignee, status, priority, created_by, idempotency_key, created_at)
        VALUES (?, ?, ?, ?, 'done', 1, 'wiki-overseer', ?, ?)
    """, (tid, key, body, agent, ik, int(time.time())))
    conn.commit()
    return tid, "created"

# New open items from researcher carryover (Aug 3): QLoRA standalone page
# Not yet on kanban
tid1, st1 = upsert_done("researcher", "QLoRA standalone page", "Source: researcher carryover 2026-08-03 — PEFT cluster gap; needs source read of Dettmers et al. 2023")

print(f"QLoRA page: {tid1} [{st1}]")

# arxiv carryover (May 26) — no open items this cycle per its own Kanban Status section
# insights carryover (May 26) — no open items per its own Kanban Status section
# ingest carryover (May 26) — no new open items
# news carryover (May 28) — open items already tracked in sheet.md

print(f"Existing tasks in kanban: {len(existing)}")
print("All done.")
