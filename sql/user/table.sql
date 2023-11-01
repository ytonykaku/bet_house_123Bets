CREATE TABLE IF NOT EXISTS User (
    utype INTEGER NOT NULL DEFAULT 0,

    name TEXT NOT NULL,
    cpf TEXT NOT NULL UNIQUE PRIMARY KEY,
    email TEXT NOT NULL UNIQUE,

    login TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);

-- TODO: Check also if the fight has bets.
CREATE TRIGGER IF NOT EXISTS user_protection BEFORE DELETE ON User
FOR EACH ROW
WHEN EXISTS (SELECT 1
             FROM Wallet w
             WHERE w.cpf_owner = OLD.cpf AND (w.available > 0 OR w.applied > 0))
BEGIN
    SELECT RAISE(ABORT, 'Can not delete fighter with fight in progress.');
END;

CREATE TRIGGER IF NOT EXISTS punter_registration AFTER INSERT ON User
WHEN new.utype = 0
BEGIN
    INSERT INTO Punter (    cpf)
                VALUES (new.cpf);
END;

CREATE TRIGGER IF NOT EXISTS admin_registration AFTER INSERT ON User
WHEN new.utype = 1
BEGIN
    INSERT INTO Admin  (    cpf)
                VALUES (new.cpf);
END;

CREATE TRIGGER IF NOT EXISTS depression AFTER UPDATE OF utype ON User
WHEN new.utype = 0
BEGIN
    DELETE FROM Admin WHERE cpf = new.cpf;

    INSERT OR IGNORE INTO Punter (    cpf)
                          VALUES (new.cpf);
END;

CREATE TRIGGER IF NOT EXISTS elevation AFTER UPDATE OF utype ON User
WHEN new.utype = 1
BEGIN
    DELETE FROM Punter WHERE cpf = new.cpf;

    INSERT OR IGNORE INTO Admin  (    cpf)
                          VALUES (new.cpf);
END;

