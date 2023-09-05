import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Admin (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    login TEXT NOT NULL,
    password TEXT NOT NULL,
    utype INTEGER NOT NULL CHECK(utype in (0, 1)) DEFAULT 1,
    cpf TEXT NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Punter (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    login TEXT NOT NULL,
    password TEXT NOT NULL,
    utype INTEGER NOT NULL CHECK(utype in (0, 1)) DEFAULT 0,
    cpf TEXT NOT NULL,
    profit REAL CHECK(profit >= 0.0) DEFAULT 0.0,
    loss REAL CHECK(loss >= 0.0) DEFAULT 0.0
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Wallet (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    value_available REAL NOT NULL CHECK(value_available >= 0.0) DEFAULT 0.0,
    value_applied REAL NOT NULL CHECK(value_applied >= 0.0) DEFAULT 0.0,
    owner INTEGER,
    investments TEXT NOT NULL DEFAULT "", -- CSV: Comma Separated Values

    FOREIGN KEY(owner) REFERENCES User(id)
);
""")

def add_admin(name, login, password, cpf):
    cursor.execute("""
    INSERT INTO Admin (id, name, login, password, utype, cpf)
    VALUES (id,?,?,?,utype,?)  
    """, (name, login, password, cpf))
    conn.commit()

def add_punter(name, login, password, utype, cpf):
    cursor.execute("""
    INSERT INTO Admin (id , name, login, password, utype, cpf, profit, loss)
    VALUES (id,?,?,?,utype,?,profit,loss)  
    """, (name, login, password, cpf))
    conn.commit()

def add_wallet(investments):
    cursor.execute("""
    INSERT INTO Admin (id, value_available, value_applied, owner, investments)
    VALUES (id,0,0,owner,?)  
    """, (investments))
    conn.commit()

def update_wallet(owner, value, operation):
    if operation == 1:
        for row in cursor.execute("""
                SELECT value_available
                FROM Wallet
                WHERE owner = ?
                """, (owner)):
            currentValue = row[0]
            break
        value += currentValue
        cursor.execute("""
        UPDATE Wallet
        SET value_available = ?
        """, (value))
    else:
        for row in cursor.execute("""
                SELECT value_available
                FROM Wallet
                WHERE owner = ?
                """, (owner)):
            currentValue = row[0]
            break
        value -= currentValue
        cursor.execute("""
        UPDATE Wallet
        SET value_available = ?
        """, (value))

def callLogin(login: str, password: str, usersList):
    for loggins in usersList:
        if login == loggins.login and password == loggins.password:
            print(f'Usuario', login, 'logado com sucesso')
            return True-
        else:
            print('Usuario ou senha incorretos')
            return False