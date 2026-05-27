#!/usr/bin/env python3
"""Kanban surfacing for researcher carryover - 2026-05-26 cycle"""

import sqlite3
import os
import hashlib
import time

DB_PATH = os.path.expanduser("~/.hermes/kanban.db")
AGENT = "researcher"

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# Check existing open tasks for researcher
cur.execute("SELECT id, title, status FROM tasks WHERE assignee = ? AND status != 'done'", (AGENT,))
existing = {row[1].strip(): row[0] for row in cur.fetchall()}
print(f"Existing open tasks for {AGENT}: {len(existing)}")

def upsert(title, body, priority=1, blocked=False, assignee=AGENT):
    key = f"{assignee}: {title}".strip()
    if key in existing:
        print(f"  SKIP (exists): {key}")
        return existing[key], "skipped"

    ik = hashlib.sha256(key.encode()).hexdigest()[:16]
    tid = f"t_{ik}"
    status = "blocked" if blocked else "done"  # informational card = done immediately
    cur.execute("""
        INSERT INTO tasks
          (id, title, body, assignee, status, priority, created_by, idempotency_key, created_at)
        VALUES (?, ?, ?, ?, ?, ?, 'cron:kanban-surfacing', ?, ?)
    """, (tid, key, body, assignee, status, priority, ik, int(time.time())))
    conn.commit()
    print(f"  CREATE: {key} → {tid} (status={status})")
    return tid, "created"

print(f"\n=== Surfacing researcher open items (2026-05-26) ===")

# Open item 1: Dynamical systems applicability
tid1, _ = upsert(
    title="Dynamical systems: energy landscape quantitative validity?",
    body="Low-dimensional attractor theory applied to high-dimensional transformer state spaces — is the energy landscape metaphor valid quantitatively or only qualitatively? Wiki content exists in attractor-dynamics.md and dynamical-systems.md but the question is empirical. Needs researcher to synthesize what's known and identify what empirical work would be needed.",
    priority=1,
    blocked=False
)

# Open item 2: AI imagery signatures
tid2, _ = upsert(
    title="AI imagery signatures: detection in LLMs?",
    body="Can we detect latent-space imagery analogs in LLMs? What would be the behavioral or activation signatures? mental-imagery.md discusses human imagery but AI connection is underdeveloped. Needs research into what probing studies could detect imagination-like internal simulation.",
    priority=1,
    blocked=False
)

# Open item 3: Weil-gate calibration
tid3, _ = upsert(
    title="Weil-gate calibration: minimum depth for proceed?",
    body="How deep must the Weil-gate pass go before a proposal can proceed? Is there a minimum depth (number of layers: direct/systemic/normalization) that is required, or does the council's judgment determine sufficiency? This is a process design question — no empirical answer exists yet.",
    priority=1,
    blocked=False
)

# Open item 4: Spiral depth heuristics
tid4, _ = upsert(
    title="Spiral depth heuristics: when has the council gone deep enough?",
    body="How does a council know when it has gone deep enough in spiral deliberation? Is there a reliable signal that the opening has been reached, or is this inherently judgment-based? The weil-gate.md and spiral-architecture.md pages have the framework but the stopping criterion isn't operationalized.",
    priority=1,
    blocked=False
)

# Open item 5: GRPO + MoE routing collapse
tid5, _ = upsert(
    title="GRPO + MoE: does training cause expert routing collapse?",
    body="Active empirical question: Does GRPO training cause expert routing collapse in MoE architectures? llm-training.md notes GRPO is structurally compatible with MoE (no reference model = no doubled memory) but doesn't resolve whether routing patterns collapse. Needs external research or empirical evidence.",
    priority=2,  # high - active research question
    blocked=False
)

# Open item 6: Scaffolding identification
tid6, _ = upsert(
    title="Scaffolding identification: probing method for CoT traces?",
    body="Can we systematically distinguish scaffolding (calibration tokens) from load-bearing tokens in CoT traces? load-bearing-reasoning.md provides the framework; practical identification methods still being developed. Needs probing study development or literature review on causal scrubbing applications.",
    priority=2,  # high - active interpretability challenge
    blocked=False
)

conn.close()

print(f"\n=== Summary ===")
for tid, label in [(tid1, "dynamical-systems"), (tid2, "ai-imagery"), (tid3, "weil-gate"), (tid4, "spiral-depth"), (tid5, "grpo-moe"), (tid6, "scaffolding")]:
    print(f"  {tid}: {label}")