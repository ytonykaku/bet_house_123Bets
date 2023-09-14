CREATE TABLE IF NOT EXISTS Punter (
    uid INTEGER PRIMARY KEY,

    profit REAL DEFAULT 0.0,
    loss REAL DEFAULT 0.0,
    investments TEXT NOT NULL DEFAULT "", -- CSV: Comma Separeted Values,

    FOREIGN KEY(uid) REFERENCES User(id) ON DELETE CASCADE
);

