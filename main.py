import sqlite3 as sql3

from models.Punter import Punter
from models.Wallet import Wallet

from persistence.WalletPersistence import WalletPersistence
from persistence.PunterPersistence import PunterPersistence

def create_db(db_name: str = "db.sqlite3") -> tuple[sql3.Connection, sql3.Cursor]:
    connection = sql3.connect(db_name)
    connection.execute("PRAGMA foreign_keys = ON;")

    cursor = connection.cursor()


    with open("sql/tables/admin.sql") as f:
        cursor.execute(f.read())

    with open("sql/tables/punter.sql") as f:
        cursor.execute(f.read())

    with open("sql/tables/wallet.sql") as f:
        cursor.execute(f.read())

    return connection, cursor

conn, cursor = create_db()

punter_persistence = PunterPersistence(cursor=cursor)
wallet_persistence = WalletPersistence(cursor=cursor)

new_users = [
    ("Lucas1",  "12345678910", "lucao",   "senha-forte1"),
    ("Lucas2",  "12345678911", "lucao0",  "senha-forte2"),
    ("Lucas3",  "12345678912", "lucao1",  "senha-forte3"),
    ("Lucas4",  "12345678913", "lucao2",  "senha-forte4"),
    ("Lucas5",  "12345678914", "lucao3",  "senha-forte5"),
    ("Lucas6",  "12345678915", "lucao4",  "senha-forte6"),
    ("Lucas7",  "12345678916", "lucao5",  "senha-forte7"),
    ("Lucas8",  "12345678917", "lucao6",  "senha-forte8"),
    ("Lucas9",  "12345678918", "lucao7",  "senha-forte9"),
    ("Lucas10", "12345678919", "lucao8",  "senha-forte10"),
    ("Lucas11", "12345678920", "lucao9",  "senha-forte11"),
    ("Lucas12", "12345678921", "lucao10", "senha-forte12"),
    ("Lucas13", "12345678922", "lucao11", "senha-forte13"),
    ("Lucas14", "12345678923", "lucao12", "senha-forte14"),
    ("Lucas15", "12345678924", "lucao13", "senha-forte15"),
    ("Lucas16", "12345678925", "lucao14", "senha-forte16"),
    ("Lucas17", "12345678926", "lucao15", "senha-forte17"),
    ("Lucas18", "12345678927", "lucao16", "senha-forte18"),
    ("Lucas19", "12345678928", "lucao17", "senha-forte19"),
    ("Lucas20", "12345678929", "lucao18", "senha-forte20"),
]

for name, cpf, login, password in new_users:
    w = Wallet()
    wallet_persistence.insert(w)
    p = Punter(name=name, cpf=cpf, login=login, password=password, wallet=w)
    punter_persistence.insert(p)

id, password = punter_persistence.get_auth_info(login="lucao18")

print(punter_persistence.get_by_id(id=id))

conn.commit()

