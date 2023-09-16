import datetime as dt
import sqlite3 as sql3
import random

from models.Admin import Admin
from models.Punter import Punter
from models.Transaction import Transaction
from models.Wallet import Wallet

from persistence.UserPersistence import UserPersistence
from persistence.AdminPersistence import AdminPersistence
from persistence.PunterPersistence import PunterPersistence
from persistence.TransactionPersistence import TransactionPersistence
from persistence.WalletPersistence import WalletPersistence

"""
# Primeiro Entrega:
- Transaction
    - Insert OK
    - History
"""

def create_db(db_name: str = "db.sqlite3") -> tuple[sql3.Connection, sql3.Cursor]:
    connection = sql3.connect(db_name)

    connection.execute("PRAGMA foreign_keys = ON;")

    cursor = connection.cursor()

    for model in [ "user", "admin", "punter", "wallet", "transaction" ]:
        with open(f"sql/{model}/table.sql") as f:
            cursor.execute(f.read())

    return connection, cursor

conn, cursor = create_db()

user_persistence        = UserPersistence(cursor=cursor)
punter_persistence      = PunterPersistence(cursor=cursor)
wallet_persistence      = WalletPersistence(cursor=cursor)
admin_persistence       = AdminPersistence(cursor=cursor)
transaction_persistence = TransactionPersistence(cursor=cursor)

a = Admin(name="Admin", cpf="00000000000", login="admin", password="admin", email="admin@example.com")

user_persistence.insert(a)
admin_persistence.insert(a)

# new_users = [
#     ("Lucas01", "12345678901", "lucao01", "senha-forte", "email01@example.com" ),
#     ("Lucas02", "12345678902", "lucao02", "senha-forte", "email02@example.com" ),
#     ("Lucas03", "12345678903", "lucao03", "senha-forte", "email03@example.com" ),
#     ("Lucas04", "12345678904", "lucao04", "senha-forte", "email04@example.com" ),
#     ("Lucas05", "12345678905", "lucao05", "senha-forte", "email05@example.com" ),
#     ("Lucas06", "12345678906", "lucao06", "senha-forte", "email06@example.com" ),
#     ("Lucas07", "12345678907", "lucao07", "senha-forte", "email07@example.com" ),
#     ("Lucas08", "12345678908", "lucao08", "senha-forte", "email08@example.com" ),
#     ("Lucas09", "12345678909", "lucao09", "senha-forte", "email09@example.com" ),
#     ("Lucas10", "12345678910", "lucao10", "senha-forte", "email10@example.com" ),
#     ("Lucas11", "12345678911", "lucao11", "senha-forte", "email11@example.com" ),
#     ("Lucas12", "12345678912", "lucao12", "senha-forte", "email12@example.com" ),
#     ("Lucas13", "12345678913", "lucao13", "senha-forte", "email13@example.com" ),
#     ("Lucas14", "12345678914", "lucao14", "senha-forte", "email14@example.com" ),
#     ("Lucas15", "12345678915", "lucao15", "senha-forte", "email15@example.com" ),
#     ("Lucas16", "12345678916", "lucao16", "senha-forte", "email16@example.com" ),
#     ("Lucas17", "12345678917", "lucao17", "senha-forte", "email17@example.com" ),
#     ("Lucas18", "12345678918", "lucao18", "senha-forte", "email18@example.com" ),
#     ("Lucas19", "12345678919", "lucao19", "senha-forte", "email19@example.com" ),
#     ("Lucas20", "12345678920", "lucao20", "senha-forte", "email20@example.com" ),
# ]
# 
# punter_bkp: Punter
# 
# for idx, (name, cpf, login, password, email) in enumerate(new_users):
#     w = Wallet()
#     p = Punter(name=name, cpf=cpf, login=login, password=password, email=email, wallet=w)
# 
#     user_persistence.insert(p)
#     punter_persistence.insert(p)
#     wallet_persistence.insert(w)
# 
#     for i in range(10):
#         punter_bkp = p
#         ttype = Transaction.DEPOSIT if random.random() > 0.5 else Transaction.WITHDRAW
#         t = Transaction(p=p, value=50, ttype=ttype, timestamp=dt.datetime.now().timestamp())
#         transaction_persistence.insert(t=t)

conn.commit()

