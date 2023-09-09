import sqlite3 as sql3

from persistence import utils
from models.Punter import Punter


class PunterPersistence:

    def __init__(self, cursor: sql3.Cursor):
        self.db_cursor = cursor

        self.queries = utils.create_operations_dict(
            operations=[ "insert" ],
            SQL_BASE_PATH="sql/punter/"
        )

    def insert(self, p: Punter):
        self.db_cursor.execute(
            self.queries["insert"],
            (p.id,)
        )

        p.wallet.id = self.db_cursor.lastrowid

