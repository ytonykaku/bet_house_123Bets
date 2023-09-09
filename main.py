import sqlite3 as sql3

from models.Admin import Admin
from models.Punter import Punter
from models.Wallet import Wallet

from persistence.UserPersistence import UserPersistence
from persistence.AdminPersistence import AdminPersistence
from persistence.PunterPersistence import PunterPersistence
from persistence.WalletPersistence import WalletPersistence

"""
# Primeiro Entrega:
- Transaction
    - Insert
    - History
"""

def create_db(db_name: str = "db.sqlite3") -> tuple[sql3.Connection, sql3.Cursor]:
    connection = sql3.connect(db_name)

    connection.execute("PRAGMA foreign_keys = ON;")

    cursor = connection.cursor()

    with open("sql/user/table.sql") as f:
        cursor.execute(f.read())

    with open("sql/admin/table.sql") as f:
        cursor.execute(f.read())

    with open("sql/punter/table.sql") as f:
        cursor.execute(f.read())

    with open("sql/wallet/table.sql") as f:
        cursor.execute(f.read())

    return connection, cursor

conn, cursor = create_db()

user_persistence   = UserPersistence(cursor=cursor)
punter_persistence = PunterPersistence(cursor=cursor)
wallet_persistence = WalletPersistence(cursor=cursor)
admin_persistence  = AdminPersistence(cursor=cursor)

new_users = [
    ("Lucas",   "12345678910", "lucao",   "senha-forte",   "email@example.com" ),
    ("Lucas0",  "12345678911", "lucao0",  "senha-forte0",  "email0@example.com" ),
    ("Lucas1",  "12345678912", "lucao1",  "senha-forte1",  "email1@example.com" ),
    ("Lucas2",  "12345678913", "lucao2",  "senha-forte2",  "email2@example.com" ),
    ("Lucas3",  "12345678914", "lucao3",  "senha-forte3",  "email3@example.com" ),
    ("Lucas4",  "12345678915", "lucao4",  "senha-forte4",  "email4@example.com" ),
    ("Lucas5",  "12345678916", "lucao5",  "senha-forte5",  "email5@example.com" ),
    ("Lucas6",  "12345678917", "lucao6",  "senha-forte6",  "email6@example.com" ),
    ("Lucas7",  "12345678918", "lucao7",  "senha-forte7",  "email7@example.com" ),
    ("Lucas8",  "12345678919", "lucao8",  "senha-forte8",  "email8@example.com" ),
    ("Lucas9",  "12345678920", "lucao9",  "senha-forte9",  "email9@example.com" ),
    ("Lucas10", "12345678921", "lucao10", "senha-forte10", "email10@example.com" ),
    ("Lucas11", "12345678922", "lucao11", "senha-forte11", "email11@example.com" ),
    ("Lucas12", "12345678923", "lucao12", "senha-forte12", "email12@example.com" ),
    ("Lucas13", "12345678924", "lucao13", "senha-forte13", "email13@example.com" ),
    ("Lucas14", "12345678925", "lucao14", "senha-forte14", "email14@example.com" ),
    ("Lucas15", "12345678926", "lucao15", "senha-forte15", "email15@example.com" ),
    ("Lucas16", "12345678927", "lucao16", "senha-forte16", "email16@example.com" ),
    ("Lucas17", "12345678928", "lucao17", "senha-forte17", "email17@example.com" ),
    ("Lucas18", "12345678929", "lucao18", "senha-forte18", "email18@example.com" ),
]

a = Admin(name="Admin", cpf="00000000000", login="admin", password="admin", email="admin@example.com")

user_persistence.insert(a)
admin_persistence.insert(a)

for name, cpf, login, password, email in new_users:
    w = Wallet()

    p = Punter(name=name, cpf=cpf, login=login, password=password, email=email, wallet=w)
    user_persistence.insert(p)

    punter_persistence.insert(p)

    wallet_persistence.insert(w)

    wallet_persistence.deposit(w, 100)

for i in range(5):
    print(*user_persistence.get_page(page_num=i + 1, num_items=5), sep='\n')
    print(('-' * 20) + 'x' + ('-' * 20))

conn.commit()

