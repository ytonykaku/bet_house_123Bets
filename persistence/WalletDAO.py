import os
import sqlite3 as sql3

from persistence import utils

from models.Wallet import Wallet


class WalletDAO(object):

    def __init__(self, cursor: sql3.Cursor):
        self.db_cursor = cursor

        self.queries = utils.create_operations_dict(
            operations=[ ],
            SQL_BASE_PATH=os.path.join("sql", "wallet")
        )

        with open(os.path.join("sql", "wallet", "table.sql")) as f:
            cursor.executescript(f.read())