import os
import sqlite3 as sql3

from persistence import utils

from models.Fight import Fight
from models.Fighter import Fighter

class FightPersistence(object):

    def __init__(self, cursor: sql3.Cursor):
        self.db_cursor = cursor

        self.queries = utils.create_operations_dict(
            operations=[ "insert", "fetch-fights", "declare-winner", "delete" ],
            SQL_BASE_PATH=os.path.join("sql", "fight")
        )

        with open(os.path.join("sql", "fight", "table.sql")) as f:
            cursor.executescript(f.read())

    def create_fight(self, f: Fight):
        self.db_cursor.execute(self.queries["insert"], (f.fA.name, f.oddA, f.fB.name, f.oddB))

    def fetch_fights(self):
        q = self.db_cursor.execute(self.queries["fetch-fights"]).fetchall()

        return [
            Fight(Fighter(fA, categoryA, heightA, nationalityA, n_winsA, n_lossA), oddA,
                  Fighter(fB, categoryB, heightB, nationalityB, n_winsB, n_lossB), oddB,
                          winner)
            for fA, oddA, categoryA, nationalityA, heightA, n_winsA, n_lossA,
                fB, oddB, categoryB, nationalityB, heightB, n_winsB, n_lossB,
                winner in q
        ]

    def declare_winner(self, fight: Fight, fighter: Fighter):
        self.db_cursor.execute(self.queries["declare-winner"], (fighter.name, fight.fA.name, fight.fB.name))

    def delete(self, fight: Fight):
        self.db_cursor.execute(self.queries["delete"], (fight.fA.name, fight.fB.name))
