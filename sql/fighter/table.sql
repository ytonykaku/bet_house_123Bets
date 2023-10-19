CREATE TABLE IF NOT EXISTS Fighter (
    name TEXT PRIMARY KEY,

    category TEXT,
    height REAL,
    nationality TEXT,

    n_wins INTEGER DEFAULT 0,
    n_loss INTEGER DEFAULT 0
);

