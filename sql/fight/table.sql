CREATE TABLE IF NOT EXISTS Fight (
    fA TEXT,
    fB TEXT,

    oddA REAL,
    oddB REAL,

    winner TEXT NULL,

    PRIMARY KEY (fA, fB),

    FOREIGN KEY(fA) REFERENCES Fighter(name),
    FOREIGN KEY(fB) REFERENCES Fighter(name),
    FOREIGN KEY(winner) REFERENCES Fighter(name)
);

CREATE TRIGGER IF NOT EXISTS winner_declaration AFTER UPDATE OF winner ON Fight
WHEN old.winner != ""
BEGIN
    UPDATE Fighter SET n_wins = n_wins + 1 WHERE name = new.winner;
    UPDATE Fighter SET n_loss = n_loss + 1 WHERE name != new.winner and (name = new.fA or name = new.fB);
END;

