CREATE TABLE IF NOT EXISTS Punter (
    uid INTEGER PRIMARY KEY CHECK(uid != 0),

    profit REAL CHECK(profit >= 0.0) DEFAULT 0.0,
    loss REAL CHECK(loss >= 0.0) DEFAULT 0.0,
    investments TEXT NOT NULL DEFAULT "", -- CSV: Comma Separeted Values,

    FOREIGN KEY(uid) REFERENCES User(id) ON DELETE CASCADE
);

