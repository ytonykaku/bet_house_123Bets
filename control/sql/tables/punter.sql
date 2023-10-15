CREATE TABLE IF NOT EXISTS Punter (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    login TEXT NOT NULL,
    password TEXT NOT NULL,
    utype INTEGER NOT NULL CHECK(utype in (0, 1)) DEFAULT 0,
    cpf TEXT NOT NULL,
    profit REAL CHECK(profit >= 0.0) DEFAULT 0.0,
    loss REAL CHECK(loss >= 0.0) DEFAULT 0.0
);

