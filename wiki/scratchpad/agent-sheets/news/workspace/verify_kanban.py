import sqlite3, os
DB_PATH = os.path.expanduser("~/.hermes/kanban.db")
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()
# Show recent tasks from cron:news-agent
cur.execute("SELECT id, title, status, created_at FROM tasks WHERE created_by = 'cron:news-agent' ORDER BY created_at DESC LIMIT 10")
rows = cur.fetchall()
for r in rows:
    print(f"{r[0]} [{r[2]}] {r[1][:80]}")
conn.close()