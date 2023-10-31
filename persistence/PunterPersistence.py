import os
import sqlite3 as sql3

from persistence import utils

from models.Punter import Punter
from models.Wallet import Wallet


class PunterPersistence(object):

    def __init__(self, cursor: sql3.Cursor):
        self.db_cursor = cursor

        self.queries = utils.create_operations_dict(
            operations=[ "insert",
                         "fetch",
                         "select-profit-and-loss" ],
            SQL_BASE_PATH=os.path.join("sql", "punter")
        )

        with open(os.path.join("sql", "punter", "table.sql")) as f:
            cursor.executescript(f.read())

    def insert(self, p: Punter):
        self.db_cursor.execute(
            self.queries["insert"],
            (p.id,)
        )

        p.wallet.id = self.db_cursor.lastrowid

    def read(self):
        punters = self.db_cursor.execute(self.queries["fetch"]).fetchall()

        return [
            Punter(name=name,
                   cpf=cpf,
                   email=email,
                   login=login,
                   password=password,
                   profit=profit,
                   loss=loss,
                   wallet=Wallet(cpf_owner=cpf, value_available=available, value_applied=applied))
            for
            name, login, password, cpf, email, utype, profit, loss, available, applied
            in
            punters
        ]
