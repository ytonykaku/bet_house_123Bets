import sqlite3 as sql3

from persistence import utils
from models.Admin import Admin


class AdminPersistence:

    def __init__(self, cursor: sql3.Cursor):
        self.db_cursor = cursor

        self.queries = utils.create_operations_dict(
            operations=[ "insert" ],
            SQL_BASE_PATH="sql/punter/"
        )

    def insert(self, a : Admin):
        self.db_cursor.execute(
            self.queries["insert"],
            (a.id,)
        )

