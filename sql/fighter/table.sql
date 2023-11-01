CREATE TABLE IF NOT EXISTS Fighter (
    name TEXT UNIQUE PRIMARY KEY,

    category TEXT,
    height REAL,
    nationality TEXT,

    n_wins INTEGER DEFAULT 0,
    n_loss INTEGER DEFAULT 0
);

CREATE TRIGGER IF NOT EXISTS prevent_delete_fighter BEFORE DELETE ON Fighter
WHEN EXISTS (SELECT 1
             FROM Fight f
             WHERE f.fA = OLD.name OR f.fB = OLD.name)
BEGIN
    SELECT RAISE(ABORT, 'Can not delete fighter in active fights.');
END;
