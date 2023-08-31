CREATE TABLE IF NOT EXISTS Wallet (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    value_available REAL NOT NULL CHECK(value_available >= 0.0) DEFAULT 0.0,
    value_applied REAL NOT NULL CHECK(value_applied >= 0.0) DEFAULT 0.0,
    owner INTEGER,
    investments TEXT NOT NULL DEFAULT "", -- CSV: Comma Separeted Values

    FOREIGN KEY(owner) REFERENCES User(id)
);

