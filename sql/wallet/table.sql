CREATE TABLE IF NOT EXISTS Wallet (
    pid INTEGER PRIMARY KEY,

    value_available REAL NOT NULL,
    value_applied REAL NOT NULL,

    FOREIGN KEY(pid) REFERENCES Punter(uid) ON DELETE CASCADE
);

