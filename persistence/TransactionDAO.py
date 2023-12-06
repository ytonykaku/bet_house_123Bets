import os
import sqlite3 as sql3

from persistence import utils

from models.Punter import Punter
from models.Wallet import Wallet
from models.Transaction import Transaction


class TransactionDAO(object):

    def __init__(self, cursor: sql3.Cursor):
        self.db_cursor = cursor

        self.queries = utils.create_operations_dict(
            operations=[ "insert",
                         "fetch" ],
            SQL_BASE_PATH=os.path.join("sql", "transaction")
        )

        with open(os.path.join("sql", "transaction", "table.sql")) as f:
            cursor.executescript(f.read())

    def insert(self, w: Wallet, t: Transaction):
        self.db_cursor.execute(
            self.queries["insert"],
            (w.cpf_owner, t.ttype, t.value, t.timestamp)
        )

    def read(self, p: Punter) -> list[Transaction]:
        transactions = self.db_cursor.execute(self.queries["fetch"], (p.cpf, )).fetchall()

        return [
            Transaction(value=value, ttype=ttype, timestamp=timestamp)
            for ttype, value, timestamp in transactions
        ]

