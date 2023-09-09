import sqlite3 as sql3

from persistence import utils
from models.Wallet import Wallet


class WalletPersistence:

    def __init__(self, cursor: sql3.Cursor):
        self.db_cursor = cursor

        self.queries = utils.create_operations_dict(
            operations=[ "insert",
                         "deposit",
                         "withdraw" ],
            SQL_BASE_PATH="sql/wallet/"
        )

    def insert(self, w: Wallet):
        self.db_cursor.execute(self.queries["insert"], (w.id,))

    def deposit(self, w: Wallet, value: float):
        self.db_cursor.execute(self.queries["deposit"], (value, w.id))

    def withdraw(self, w: Wallet, value: float):
        self.db_cursor.execute(self.queries["withdraw"], (value, w.id))

