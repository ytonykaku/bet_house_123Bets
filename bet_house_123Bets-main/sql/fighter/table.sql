CREATE TABLE IF NOT EXISTS Fighter (
    fid INTEGER PRIMARY KEY,

    name TEXT,
    category TEXT,
    height REAL,
    nationality TEXT,
    wins INTEGER DEFAULT 0,
    loss INTEGER DEFAULT 0
);

