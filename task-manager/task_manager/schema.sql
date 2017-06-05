CREATE TABLE IF NOT EXISTS task_man (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        task_text TEXT NOT NULL DEFAULT '',
        start_date TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
        status TEXT NOT NULL DEFAULT 'open',
        end_date TEXT NOT NULL DEFAULT ''
)