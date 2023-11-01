CREATE TABLE IF NOT EXISTS Fight (
    fA TEXT,
    fB TEXT,

    oddA REAL,
    oddB REAL,

    winner TEXT NULL,

    PRIMARY KEY (fA, fB),

    FOREIGN KEY(fA) REFERENCES Fighter(name) ON DELETE CASCADE,
    FOREIGN KEY(fB) REFERENCES Fighter(name) ON DELETE CASCADE,
    FOREIGN KEY(winner) REFERENCES Fighter(name)
);

CREATE TRIGGER IF NOT EXISTS winner_declaration AFTER UPDATE OF winner ON Fight
WHEN old.winner IS NULL
BEGIN
    UPDATE Fighter SET n_wins = n_wins + 1 WHERE name = new.winner;
    UPDATE Fighter SET n_loss = n_loss + 1 WHERE name != new.winner and (name = new.fA or name = new.fB);
    -- TODO: Pay all bets.
    DELETE FROM Fight WHERE fA = old.fA and fb = old.fB;
END;

