CREATE TABLE IF NOT EXISTS Bet (
    bid INTEGER PRIMARY KEY AUTOINCREMENT,
    wallet INTEGER,
    value REAL NOT NULL CHECK(value >= 0.0),
    date VALUES ('YYYY-MM-DD'),
    winner INTEGER NOT NULL DEFAULT "",
    fight INTEGER,
    owner INTEGER

    FOREIGN KEY(owner) REFERENCES User(id)
    FOREIGN KEY(wallet) REFERENCES Wallet(id)
    FOREIGN KEY(fight) REFERENCES Fight(id)
);

/* Acho que não precisamos do atributo wallet porque tem o owner que referencia o mesmo lugar */
