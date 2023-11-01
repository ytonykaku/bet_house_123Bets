CREATE TABLE IF NOT EXISTS Punter (
    cpf TEXT PRIMARY KEY,

    profit REAL DEFAULT 0.0,
    loss REAL DEFAULT 0.0,

    FOREIGN KEY(cpf) REFERENCES User(cpf) ON DELETE CASCADE
);

CREATE TRIGGER IF NOT EXISTS wallet_creation
AFTER INSERT ON Punter
BEGIN
    INSERT INTO wallet(cpf_owner)
                VALUES(  new.cpf);
END;
