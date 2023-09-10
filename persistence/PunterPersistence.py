import os
import sqlite3 as sql3

from persistence import utils

from models.Punter import Punter


class PunterPersistence(object):

    def __init__(self, cursor: sql3.Cursor):
        self.db_cursor = cursor

        self.queries = utils.create_operations_dict(
            operations=[ "insert",
                         "select-profit-and-loss" ],
            SQL_BASE_PATH=os.path.join("sql", "punter")
        )

        with open(os.path.join("sql", "punter", "table.sql")) as f:
            cursor.execute(f.read())

    def insert(self, p: Punter):
        self.db_cursor.execute(
            self.queries["insert"],
            (p.id,)
        )

        p.wallet.id = self.db_cursor.lastrowid

    def get_profit_and_loss(self, p: Punter):
        profit, loss =self.db_cursor.execute(
            self.queries["select-profit-and-loss"],
            (p.id,)
        ).fetchone()

        p.profit = profit
        p.loss = loss

