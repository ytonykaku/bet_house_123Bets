CREATE TABLE IF NOT EXISTS Fighter (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    height REAL NOT NULL,
    nationality TEXT NOT NULL,
    n_wins INTEGER DEFAULT 0,
    n_loss INTEGER DEFAULT 0


);