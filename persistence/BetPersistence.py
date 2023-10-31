import os
import sqlite3 as sql3

from persistence import utils

from models.Bet import Bet

class BetPersistence(object):

    def __init__(self, cursor: sql3.Cursor):
        self.db_cursor = cursor

        self.queries = utils.create_operations_dict(
            operations=[ ],
            SQL_BASE_PATH=os.path.join("sql", "bet")
        )

        with open(os.path.join("sql", "bet", "table.sql")) as f:
            cursor.execute(f.read())
