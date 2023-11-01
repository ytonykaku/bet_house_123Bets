import os
import sqlite3 as sql3

from persistence import utils

from models.Fight import Fight
from models.Fighter import Fighter

class FightPersistence(object):

    def __init__(self, cursor: sql3.Cursor):
        self.db_cursor = cursor

        self.queries = utils.create_operations_dict(
            operations=[ "insert", "fetch", "declare-winner", "delete" ],
            SQL_BASE_PATH=os.path.join("sql", "fight")
        )

        with open(os.path.join("sql", "fight", "table.sql")) as f:
            cursor.executescript(f.read())

    def create(self, f: Fight):
        self.db_cursor.execute(self.queries["insert"], (f.name, f.fA.name, f.oddA, f.fB.name, f.oddB))

    def read(self):
        q = self.db_cursor.execute(self.queries["fetch"]).fetchall()

        return [
            Fight(name,
                  Fighter(fA, categoryA, heightA, nationalityA, n_winsA, n_lossA), oddA,
                  Fighter(fB, categoryB, heightB, nationalityB, n_winsB, n_lossB), oddB,
                  winner)
            for name,
                fA, oddA, categoryA, nationalityA, heightA, n_winsA, n_lossA,
                fB, oddB, categoryB, nationalityB, heightB, n_winsB, n_lossB,
                winner in q
        ]

    def delete(self, fight: Fight):
        self.db_cursor.execute(self.queries["delete"], (fight.name, ))

    def declare_winner(self, fight: Fight, fighter: Fighter):
        self.db_cursor.execute(self.queries["declare-winner"], (fighter.name, fight.name))

