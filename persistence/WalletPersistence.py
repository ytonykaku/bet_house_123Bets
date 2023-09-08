import sqlite3 as sql3

from models.Wallet import Wallet


class WalletPersistence:

    def __init__(self, cursor: sql3.Cursor):
        self.db_cursor = cursor
        self.queries = dict()

        with open("sql/operations/wallet/insert.sql") as f:
            self.queries["insert"] = f.read()

        with open("sql/operations/wallet/deposit.sql") as f:
            self.queries["deposit"] = f.read()

        with open("sql/operations/wallet/withdraw.sql") as f:
            self.queries["withdraw"] = f.read()

    def insert(self, w: Wallet):
        self.db_cursor.execute(self.queries["insert"], (w.id,))

    def deposit(self, w: Wallet, value: float):
        self.db_cursor.execute(self.queries["deposit"], (value, w.id))

    def withdraw(self, w: Wallet, value: float):
        self.db_cursor.execute(self.queries["withdraw"], (value, w.id))

