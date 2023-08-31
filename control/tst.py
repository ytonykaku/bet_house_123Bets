import sqlite3 as sql


DATABASE="sqlite3"

conn = sql.connect(database=DATABASE)
cur = conn.cursor()

with open("sql/tables/punter.sql", mode='r') as f:
    cur.execute(f.read())

with open("sql/tables/wallet.sql", mode='r') as f:
    cur.execute(f.read())

with open("sql/tables/admin.sql", mode='r') as f:
    cur.execute(f.read())

insert_query = ""
with open("sql/operations/insert-punter.sql", mode='r') as f:
    insert_query = f.read()

cur.execute(insert_query, ("Henrique", "hott-henrique", "senha", "12345678910"))

conn.commit()

