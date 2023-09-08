import sqlite3 as sql3

from models.Admin import Admin


class AdminPersistence:

    def __init__(self, cursor: sql3.Cursor):
        self.db_cursor = cursor
        self.queries = dict()

        with open("sql/operations/admin/insert.sql") as f:
            self.queries["insert"] = f.read()

    def insert(self, a : Admin):
        self.db_cursor.execute(
            self.queries["insert"],
            (a.id,)
        )

