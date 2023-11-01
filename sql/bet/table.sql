CREATE TABLE IF NOT EXISTS Bet (
    owner TEXT NOT NULL,
    fA TEXT NOT NULL,
    fB TEXT NOT NULL,
    winner TEXT NOT NULL,
    value REAL NOT NULL,

    PRIMARY KEY(owner, fA, fB, value),
    FOREIGN KEY(owner) REFERENCES Wallet(cpf_owner),
    FOREIGN KEY(fA, fB) REFERENCES Fight(fA, fB) ON DELETE CASCADE,
    FOREIGN KEY(winner) REFERENCES Fighter(name)
);

CREATE TRIGGER IF NOT EXISTS check_values BEFORE INSERT ON Bet
WHEN EXISTS (SELECT 1
             FROM Wallet w
             WHERE new.owner = w.cpf_owner AND new.value > w.available)
BEGIN
    SELECT RAISE(ABORT, 'Punter has not enough money.');
END;

CREATE TRIGGER IF NOT EXISTS update_values AFTER INSERT ON Bet
BEGIN
    UPDATE Wallet
    SET available = available - new.value,
        applied = applied + new.value
    WHERE
        cpf_owner = new.owner;
END;
