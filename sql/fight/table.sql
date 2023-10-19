CREATE TABLE IF NOT EXISTS Fight (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    fA TEXT,
    fB TEXT,

    oddA REAL,
    oddB REAL,

    winner INTEGER,

    FOREIGN KEY(fA) REFERENCES Fighter(name),
    FOREIGN KEY(fB) REFERENCES Fighter(name)
);

