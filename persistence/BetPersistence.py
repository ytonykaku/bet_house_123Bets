import os
import sqlite3 as sql3

from persistence import utils

from models.Bet import Bet

class BetPersistence(object):

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

    def insert(self, b: Bet):
        self.db_cursor.execute(self.queries["insert"], (b.id,))

    def update(self, b: Bet):
        self.db_cursor.execute(self.queries["insert"], (b.id,))