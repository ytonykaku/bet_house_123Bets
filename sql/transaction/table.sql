CREATE TABLE IF NOT EXISTS PTransaction (
    wallet TEXT NOT NULL,

    ttype INTEGER NOT NULL,
    value REAL NOT NULL,
    timestamp REAL NOT NULL,

    PRIMARY KEY(wallet, ttype, timestamp)

    FOREIGN KEY(wallet) REFERENCES Wallet(cpf_owner) ON DELETE CASCADE
);

CREATE TRIGGER IF NOT EXISTS wallet_transaction AFTER INSERT ON PTransaction
BEGIN
    UPDATE
        Wallet
    SET
        available = available + new.value
    WHERE
        cpf_owner = new.wallet;
END;
