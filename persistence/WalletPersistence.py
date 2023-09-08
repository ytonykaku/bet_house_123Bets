import sqlite3 as sql3

from models.Wallet import Wallet


class WalletPersistence:

    def __init__(self, cursor: sql3.Cursor):
        self.db_cursor = cursor
        self.queries = dict()

        with open("sql/operations/wallet/insert.sql") as f:
            self.queries["insert"] = f.read()

        with open("sql/operations/wallet/delete-by-id.sql") as f:
            self.queries["delete-by-id"] = f.read()

    def insert(self, w: Wallet):
        self.db_cursor.execute(self.queries["insert"])
        w.id = self.db_cursor.lastrowid

    def delete(self, w: Wallet):
        self.db_cursor.execute(self.queries["delete-by-id"], (w.id, ))

