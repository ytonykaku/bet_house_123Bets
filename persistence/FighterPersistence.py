import os
import sqlite3 as sql3

from models.Fighter import Fighter

from persistence import utils

class FighterPersistence(object):

    def __init__(self, cursor: sql3.Cursor):
        self.db_cursor = cursor

        self.queries = utils.create_operations_dict(
            operations=[ "insert", "fetch-fighters", "fetch-fighter-by-name", "delete-by-name" ],
            SQL_BASE_PATH=os.path.join("sql", "fighter")
        )

        with open(os.path.join("sql", "fighter", "table.sql")) as f:
            cursor.execute(f.read())

    def create_fighter(self, f: Fighter):
        self.db_cursor.execute(self.queries["insert"], (f.name, f.category, f.height, f.nationality))
    
    def fetch_fighters(self):
        q = self.db_cursor.execute(self.queries["fetch-fighters"]).fetchall()

        return [
            Fighter(name, category, float(height), nationality, int(n_wins), int(n_loss))
            for name, category, height, nationality, n_wins, n_loss in q
        ]

    def fetch_fighter_by_name(self, name: str):
        try:
            name, category, height, nationality, n_wins, n_loss = self.db_cursor.execute(self.queries["fetch-fighter-by-name"], (name, )).fetchone()
        except:
            return None

        return Fighter(name, category, float(height), nationality, int(n_wins), int(n_loss))

    def delete_by_name(self, name: str):
        self.db_cursor.execute(self.queries["delete-by-name"], (name, ))

