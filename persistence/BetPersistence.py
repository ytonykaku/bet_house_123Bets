import os
import sqlite3 as sql3

from persistence import utils

from models.Bet import Bet
from models.Fighter import Fighter
from models.Fight import Fight
from models.Punter import Punter


class BetPersistence(object):

    def __init__(self, cursor: sql3.Cursor):
        self.db_cursor = cursor

        self.queries = utils.create_operations_dict(
            operations=[ "insert", "fetch" ],
            SQL_BASE_PATH=os.path.join("sql", "bet")
        )

        with open(os.path.join("sql", "bet", "table.sql")) as f:
            cursor.executescript(f.read())

    def create(self, p: Punter, b: Bet):
        self.db_cursor.execute(self.queries["insert"], (p.cpf, b.fight.name, b.winner.name, b.value))

    def read(self, p: Punter):
        R = self.db_cursor.execute(self.queries["fetch"], (p.cpf, )).fetchall()
# 00000000001|Fight 101|A|5.0|
# Fight 101|A|B|2.0|3.0||
# A|a|1.0|p|0|0|
# B|b|1.0|p|0|0
        return [
            Bet(fight=Fight(nameF,
                            Fighter(nameA, catA, hA, natA, nwA, nlA), oddA,
                            Fighter(nameB, catB, hB, natB, nwB, nlB), oddB),
                winner=Fighter(nameW, catW, hW, natW, nwW, nlW),
                value=value)
            for
            cpf_owner, bet_fight_name, bet_winner, value,
            nameF, fFA, fFB, oddA, oddB, fWinner,
            nameA, catA, hA, natA, nwA, nlA,
            nameB, catB, hB, natB, nwB, nlB,
            nameW, catW, hW, natW, nwW, nlW,
            in R
        ]
