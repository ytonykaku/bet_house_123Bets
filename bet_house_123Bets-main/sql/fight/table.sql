CREATE TABLE IF NOT EXISTS Fight (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date VALUES ('YYYY-MM-DD'),
    fA INTEGER,
    fB INTEGER,
    betsfA REAL CHECK(betsfA >= 0.0) DEFAULT 0.0,
    betsfB REAL CHECK(betsfB >= 0.0) DEFAULT 0.0,
    winner INTEGER,

    FOREIGN KEY(fA) REFERENCES Fighter(fid)
    FOREIGN KEY(fB) REFERENCES Fighter(fid)
    FOREIGN KEY(winner) REFERENCES Fighter(fid)
);