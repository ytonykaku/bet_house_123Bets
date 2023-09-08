import sqlite3 as sql3

from models.Punter import Punter
from models.Wallet import Wallet


class PunterPersistence:

    def __init__(self, cursor: sql3.Cursor):
        self.db_cursor = cursor
        self.queries = dict()

        with open("sql/operations/punter/insert.sql") as f:
            self.queries["insert"] = f.read()

    def insert(self, p : Punter):
        self.db_cursor.execute(
            self.queries["insert"],
            (p.id,)
        )

        p.wallet.id = self.db_cursor.lastrowid

