import os
import sqlite3 as sql3

from persistence import utils

from models.Punter import Punter
from models.Transaction import Transaction


class TransactionPersistence(object):

    def __init__(self, cursor: sql3.Cursor):
        self.db_cursor = cursor

        self.queries = utils.create_operations_dict(
            operations=[ "insert",
                        "select-page-order-by-timestamp" ],
            SQL_BASE_PATH=os.path.join("sql", "transaction")
        )

        with open(os.path.join("sql", "transaction", "table.sql")) as f:
            cursor.execute(f.read())

    def insert(self, t: Transaction):
        self.db_cursor.execute(
            self.queries["insert"],
            (t.owner.id, t.ttype, t.value, t.timestamp)
        )

    def select_page_order_by_timestamp(self, p: Punter, page_num: int, num_items: int = 10) -> list[Transaction]:
        transactions: list[tuple[int, int, float, float]] = self.db_cursor.execute(
            self.queries["select-page-order-by-timestamp"],
            { "punter_id": p.id, "page_num": page_num, "num_items": num_items }
        ).fetchall()

        return [
            Transaction(p=p, value=value, ttype=ttype, timestamp=timestamp, id=id)
            for id, ttype, value, timestamp in transactions
        ]

