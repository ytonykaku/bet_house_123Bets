CREATE TABLE IF NOT EXISTS PTransaction (
    tid INTEGER PRIMARY KEY AUTOINCREMENT,

    wid INTEGER NOT NULL,

    ttype INTEGER NOT NULL,
    value REAL NOT NULL,
    timestamp REAL NOT NULL,

    FOREIGN KEY(wid) REFERENCES Wallet(wid) ON DELETE CASCADE
);

