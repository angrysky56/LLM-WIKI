#!/usr/bin/env python3
import sqlite3, os, hashlib, uuid

DB = os.path.expanduser("~/.hermes/kanban.db")
conn = sqlite3.connect(DB)
cur = conn.cursor()

# Check existing
cur.execute("SELECT id, title, status FROM tasks")
existing = {row[1].strip(): row[0] for row in cur.fetchall()}
print(f"Existing kanban tasks (non-done): {len(existing)}")

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
    """, (tid, key, body, agent, ik, __import__('time').time()))
    conn.commit()
    return tid, "created"

items = [
    # researcher open items
    ("researcher", "llama-nas — fill stub (needs source read from ml-evolution)", "Open from carryover 2026-07-15. Source: ml-evolution-benchmarking-protocol"),
    ("researcher", "qora/QLoRA — create standalone concept page", "Open from carryover 2026-07-15. Separate from LoRA variant mention"),
    ("researcher", "bounded memory budget optimization", "Open from prior carryover cycles"),
    ("researcher", "MOP vs fine-tuning boundary", "Open from prior carryover cycles"),
    ("researcher", "schema competition", "Open from prior carryover cycles"),
    # arxiv open items (bounded representation theme next steps)
    ("arxiv", "world-model improvement papers — next theme search", "Next cycle: model editing, knowledge unlearning, skill compaction, uncertainty-aware planning"),
    ("arxiv", "SNR ↔ reliability mapping — calibrated confidence/uncertainty verification papers", "Shannon Law SNR maps to verifier-graph reliability ratio"),
    ("arxiv", "capacity-aware skill construction papers", "SkillOpt bounded edits + SkillLens meta-skill → capacity budgets for skill docs"),
    # news open items
    ("news", "Ebola case count updates — South Sudan transmission, thermostable vaccine, May 29/30 attack window", "Open from carryover 2026-05-28. WHO EC recommendations active"),
    ("news", "SpaceX IPO June 12 — BlackRock $10B confirmation, Musk voting control clarification", "Open from carryover 2026-05-28. 16 days to listing"),
    ("news", "OpenAI math proof peer review outcome", "Open from carryover 2026-05-28. o3 solved Erdős geometry conjecture"),
    ("news", "California AI order — state agency implementation actions", "Open from carryover 2026-05-28. 60-day review ongoing"),
    ("news", "EU-US 2029 expiry mechanism — template for India/ASEAN bilateral deals", "Open from carryover 2026-05-28. Supreme Court limits US tariff authority"),
    # librarian open items (non-blocked, actionable)
    ("librarian", "105 broken links — update t_8d4282a9420e6d6e with new list", "Partial: 23 knowledge layer issues, 71 operational/non-actionable"),
    # insights open items
    ("insights", "Index 4 new insight pages + record episodic memory", "t_ef13d830fc611d11. Titans-memory-architecture, para-system-cluster, oee-knowledge-cluster, francesca-albanese-sanctions"),
]

created = []
skipped = []
for agent, title, body in items:
    tid, status = upsert_done(agent, title, body)
    if status == "created":
        created.append((agent, title, tid))
    else:
        skipped.append((agent, title))

print(f"\nCreated: {len(created)}")
for a, t, tid in created:
    print(f"  {a}: {t} → {tid}")
print(f"\nSkipped (already exists): {len(skipped)}")
for a, t in skipped:
    print(f"  {a}: {t}")

conn.close()