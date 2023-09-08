import sqlite3 as sql3

from models.Punter import Punter
from models.Wallet import Wallet


class PunterPersistence:

    def __init__(self, cursor: sql3.Cursor):
        self.db_cursor = cursor
        self.queries = dict()

        with open("sql/operations/punter/insert.sql") as f:
            self.queries["insert"] = f.read()

        with open("sql/operations/punter/delete-by-id.sql") as f:
            self.queries["delete-by-id"] = f.read()

        with open("sql/operations/punter/select-page.sql") as f:
            self.queries["select-page"] = f.read()

        with open("sql/operations/punter/select-auth-info.sql") as f:
            self.queries["select-auth-info"] = f.read()

        with open("sql/operations/punter/select-by-id.sql") as f:
            self.queries["select-by-id"] = f.read()

    def insert(self, p: Punter):
        self.db_cursor.execute(
            self.queries["insert"],
            (p.name, p.login, p.password, p.cpf, p.wallet.id)
        )

        p.id = self.db_cursor.lastrowid

    def delete(self, p: Punter):
        self.db_cursor.execute(
            self.queries["delete-by-id"],
            (p.id, )
        )

    def get_page(self, page_num: int = 0, n_elements: int = 10) -> list[Punter]:
        users_data: list[tuple[int, str, str, int]] = self.db_cursor.execute(
            self.queries["select-page"],
            (n_elements, (page_num - 1) * n_elements)
        ).fetchall()

        users_objects = list()

        for (id, name, cpf, wallet) in users_data:
            p = Punter(id=id, name=name, cpf=cpf, wallet=Wallet(id=wallet))
            users_objects.append(p)

        return users_objects

    def get_auth_info(self, login: str):
        return self.db_cursor.execute(
            self.queries["select-auth-info"],
            (login, )
        ).fetchone()

    def get_by_id(self, id: int):
        return self.db_cursor.execute(
            self.queries["select-by-id"],
            (id, )
        ).fetchall()

