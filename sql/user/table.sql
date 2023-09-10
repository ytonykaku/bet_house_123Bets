CREATE TABLE IF NOT EXISTS User (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL CHECK(length(name) >= 5),
    login TEXT NOT NULL UNIQUE CHECK(length(login) >= 5),
    password TEXT NOT NULL CHECK(length(password) >= 5),
    cpf TEXT NOT NULL UNIQUE CHECK(length(cpf) >= 8),
    email TEXT NOT NULL UNIQUE CHECK(length(email) >= 8),

    utype INTEGER NOT NULL CHECK(utype in (0, 1)) DEFAULT 0
);

