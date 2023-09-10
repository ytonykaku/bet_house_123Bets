import os
import sqlite3 as sql3

from models.User import User
from persistence import utils


class UserPersistence(object):

    def __init__(self, cursor: sql3.Cursor):
        self.db_cursor = cursor

        self.queries = utils.create_operations_dict(
            operations=[ "insert",
                         "delete-by-id",
                         "select-auth-info",
                         "select-page",
                         "update",
                         "elevate-by-cpf",
                         "depress-by-cpf",
                         "select-by-id" ],
            SQL_BASE_PATH=os.path.join("sql", "user")
        )

        with open(os.path.join("sql", "user", "table.sql")) as f:
            cursor.execute(f.read())

    def insert(self, u: User):
        self.db_cursor.execute(
            self.queries["insert"],
            (u.name, u.login, u.password, u.cpf, u.email, u.utype)
        )

        u.id = self.db_cursor.lastrowid


    def get_auth_info(self, login: str) -> tuple[int, str] | None:
        return self.db_cursor.execute(
            self.queries["select-auth-info"],
            (login, )
        ).fetchone()

    def elevate_by_cpf(self, cpf: str):
        self.db_cursor.executescript(
            self.queries["elevate-by-cpf"].format(cpf=cpf),
        )

    def depress_by_cpf(self, cpf: str):
        self.db_cursor.executescript(
            self.queries["depress-by-cpf"].format(cpf=cpf),
        )

    def get_page(self, page_num: int, num_items: int = 10):
        """
        :param page_num: Page to query, starting from one.
        :param num_items: Amount of items to query in a single page.
        """
        user_data: list[tuple[str, str, str, str, int]] = self.db_cursor.execute(
            self.queries["select-page"], { "page_num": page_num, "num_items": num_items }
        ).fetchall()

        return [
            User(name=name, login=login, cpf=cpf, email=email, utype=utype)
            for
            name, login, cpf, email, utype
            in
            user_data
         ]

    def delete_by_id(self, id: int):
        self.db_cursor.execute(
            self.queries["delete-by-id"],
            (id, )
        )

    def get_by_id(self, id: int) -> User:
        user_data: tuple[str, str, str, str, int] = self.db_cursor.execute(
            self.queries["select-by-id"], (id, )
        ).fetchone()

        return User(name=user_data[0],
                    cpf=user_data[1],
                    email=user_data[2],
                    login=user_data[3],
                    utype=user_data[4],
                    id=id)

    def update(self, u: User, new_values: dict):
        """
        :param u: Users that will have values updated. The selection happens by id, so make sure it is valid.
        :param new_values: The value of should be inserted as it was written in the sql script. Example:
        { "name" = '"NEW NAME"'}. Note the double quotes inside the string.
        """
        assignments_as_list = [ f"{k} = {v}" for k, v in new_values.items() ]
        assignments_as_str = ", ".join(assignments_as_list)
        self.db_cursor.execute(self.queries["update"].format(assignments=assignments_as_str), (u.id,))

