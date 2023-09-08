CREATE TABLE IF NOT EXISTS Punter (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL,
    login TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    cpf TEXT NOT NULL UNIQUE,

    profit REAL CHECK(profit >= 0.0) DEFAULT 0.0,
    loss REAL CHECK(loss >= 0.0) DEFAULT 0.0,

    investments TEXT NOT NULL DEFAULT "", -- CSV: Comma Separeted Values,

    wallet INTEGER NOT NULL CHECK(wallet != 0),

    utype INTEGER NOT NULL CHECK(utype in (0, 1)) DEFAULT 0,

    FOREIGN KEY(wallet) REFERENCES Wallet(id) ON DELETE CASCADE
);

