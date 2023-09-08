CREATE TABLE IF NOT EXISTS Wallet (
    pid INTEGER PRIMARY KEY,

    value_available REAL NOT NULL CHECK(value_available >= 0.0) DEFAULT 0.0,
    value_applied REAL NOT NULL CHECK(value_applied >= 0.0) DEFAULT 0.0,

    FOREIGN KEY(pid) REFERENCES Punter(uid) ON DELETE CASCADE
);

