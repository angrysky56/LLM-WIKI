import sqlite3, hashlib, uuid, time

DB = sqlite3.connect("/home/ty/.hermes/kanban.db")
cur = DB.execute("SELECT id, title, status FROM tasks WHERE status != 'done'")
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
        VALUES (?, ?, ?, ?, ?, ?, 'cron:researcher-agent', ?, ?)
    """, (tid, key, body, agent, status, priority, ik, int(time.time())))
    DB.commit()
    return tid, "created"

# Bounded memory budget optimization — wiki synthesis
t1, s1 = upsert("researcher", "Bounded memory budget optimization page",
    "Capacity/saturation theme spans QES/ESSA/LLaMA-NAS cluster but has no dedicated page.\nCreate wiki/concepts/bounded-memory-budget-optimization.md covering:\n- Memory capacity as a bounded resource\n- Saturation effects in quantized fine-tuning (QES)\n- ESSA's evolutionary score alignment under memory constraints\n- LLaMA-NAS compression as memory-aware architecture search\nSource: QES, ESSA, LLaMA-NAS pages in wiki.",
    priority=1)

# MOP vs fine-tuning boundary — wiki synthesis
t2, s2 = upsert("researcher", "MOP vs fine-tuning boundary",
    "Entropy maximization (MOP) vs KL regularization (fine-tuning/RLHF) tension not fully articulated.\nramirez-ruiz-mop-2024 relationship to fine-tuning not developed.\nCreate or expand a page exploring:\n- MOP: path entropy maximization, no reference model, absorbing states\n- RLHF/fine-tuning: KL divergence from reference policy, reward maximization\n- Structural tension: entropy maximization encourages diverse exploration; KL regularization pulls toward a target distribution\n- Resolution paths if any\nSource: ramirez-ruiz-mop-2024, mop-architecture, reinforcement-learning-from-human-feedback, mop-and-rlhf-interaction",
    priority=1)

# mcp.md redundancy — researcher (needs wiki write)
t3, s3 = upsert("researcher", "Resolve mcp.md redundancy",
    "mcp.md is a stub (confidence 0.3) but mcp-model-context-protocol.md is active (0.85).\nBoth pages exist in wiki/concepts/ covering the same topic.\nResolution options: (1) redirect mcp.md to mcp-model-context-protocol.md, or (2) delete mcp.md.\nRecommend option 1: make mcp.md a redirect stub pointing to mcp-model-context-protocol.md.\nUpdate index.md if needed.",
    priority=2)

# hermes-agent-skills stub — researcher
t4, s4 = upsert("researcher", "hermes-agent-skills stub",
    "hermes-agent-skills.md is a stub (0.3) connected to hermes-agent.\nNeeds skills inventory for this instance before filling.\nFrom AGENTS.md context: hermes-agent has skills in ~/.hermes/skills/ — could enumerate the configured skills.\nIf skills are documented elsewhere (e.g. hermes-ops wiki-guides), cross-link.\nIf no inventory available, leave as stub or mark blocked.",
    priority=1)

print(f"Bounded memory: {t1} [{s1}]")
print(f"MOP vs fine-tuning: {t2} [{s2}]")
print(f"mcp.md redundancy: {t3} [{s3}]")
print(f"hermes-agent-skills: {t4} [{s4}]")