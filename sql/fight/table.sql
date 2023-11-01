CREATE TABLE IF NOT EXISTS Fight (
    name TEXT PRIMARY KEY,
    fA TEXT,
    fB TEXT,

    oddA REAL,
    oddB REAL,

    winner TEXT NULL,

    FOREIGN KEY(fA) REFERENCES Fighter(name) ON DELETE CASCADE,
    FOREIGN KEY(fB) REFERENCES Fighter(name) ON DELETE CASCADE,
    FOREIGN KEY(winner) REFERENCES Fighter(name)
);

CREATE TRIGGER IF NOT EXISTS winner_declaration_A
AFTER UPDATE OF winner ON Fight
FOR EACH ROW
WHEN new.winner = old.fA
BEGIN
    UPDATE Fighter SET n_wins = n_wins + 1 WHERE name = old.fA;
    UPDATE Fighter SET n_loss = n_loss + 1 WHERE name = old.fB;

    UPDATE Wallet
    SET available = available + bets.value * old.oddA,
        applied = applied - bets.value
    FROM (SELECT *
          FROM Bet b
          WHERE b.fight_name = old.name) AS bets
    WHERE bets.owner = cpf_owner AND bets.winner = old.fA;

    UPDATE Punter
    SET profit = profit + bets.value * old.oddA - bets.value
    FROM (SELECT *
          FROM Bet b
          WHERE b.fight_name = old.name) AS bets
    WHERE bets.owner = cpf AND bets.winner = old.fA;

    UPDATE Punter
    SET loss = loss + bets.value
    FROM (SELECT *
          FROM Bet b
          WHERE b.fight_name = old.name) AS bets
    WHERE bets.owner = cpf AND bets.winner = old.fB;
END;

CREATE TRIGGER IF NOT EXISTS winner_declaration_B
AFTER UPDATE OF winner ON Fight
FOR EACH ROW
WHEN new.winner = old.fB
BEGIN
    UPDATE Fighter SET n_wins = n_wins + 1 WHERE name = old.fB;
    UPDATE Fighter SET n_loss = n_loss + 1 WHERE name = old.fA;

    UPDATE Wallet
    SET available = available + bets.value * old.oddB,
        applied = applied - bets.value
    FROM (SELECT *
          FROM Bet b
          WHERE b.fight_name = old.name) AS bets
    WHERE bets.owner = cpf_owner AND bets.winner = old.fB;

    UPDATE Punter
    SET profit = profit + bets.value * old.oddB - bets.value
    FROM (SELECT *
          FROM Bet b
          WHERE b.fight_name = old.name) AS bets
    WHERE bets.owner = cpf AND bets.winner = old.fB;

    UPDATE Punter
    SET loss = loss + bets.value
    FROM (SELECT *
          FROM Bet b
          WHERE b.fight_name = old.name) AS bets
    WHERE bets.owner = cpf AND bets.winner = old.fA;
END;
