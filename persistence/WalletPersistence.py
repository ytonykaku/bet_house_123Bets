import os
import sqlite3 as sql3

from persistence import utils

from models.Wallet import Wallet


class WalletPersistence(object):

    def __init__(self, cursor: sql3.Cursor):
        self.db_cursor = cursor

        self.queries = utils.create_operations_dict(
            operations=[ "insert",
                         "deposit",
                         "withdraw",
                         "get-by-id" ],
            SQL_BASE_PATH=os.path.join("sql", "wallet")
        )

        with open(os.path.join("sql", "wallet", "table.sql")) as f:
            cursor.execute(f.read())

    def insert(self, w: Wallet):
        self.db_cursor.execute(self.queries["insert"], (w.id,))

    def deposit(self, w: Wallet, value: float):
        w.value_available += value
        self.db_cursor.execute(self.queries["deposit"], (value, w.id))

    def withdraw(self, w: Wallet, value: float):
        self.db_cursor.execute(self.queries["withdraw"], (value, w.id))
        w.value_available -= value

    def get_by_id(self, id: int) -> Wallet:
        data: tuple[float, float] = self.db_cursor.execute(self.queries["get-by-id"], (id, )) \
                                                  .fetchone()

        return Wallet(pid=id,
                      value_available=data[0],
                      value_applied=data[1])


