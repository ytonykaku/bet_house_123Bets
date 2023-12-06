import os
import sqlite3 as sql3

from models.User import User
from persistence import utils


class UserDAO(object):

    def __init__(self, cursor: sql3.Cursor):
        self.db_cursor = cursor

        self.queries = utils.create_operations_dict(
            operations=[ "insert",
                         "delete",
                         "fetch",
                         "update-utype",
                         "update" ],
            SQL_BASE_PATH=os.path.join("sql", "user")
        )

        with open(os.path.join("sql", "user", "table.sql")) as f:
            cursor.executescript(f.read())

    def create(self, u: User):
        self.db_cursor.execute(
            self.queries["insert"],
            (u.name, u.login, u.password, u.cpf, u.email, u.utype)
        )

    def read(self):
        user_data = self.db_cursor.execute(self.queries["fetch"]).fetchall()

        return [
            User(name=name, login=login, password=password, cpf=cpf, email=email, utype=utype)
            for
            name, login, password, cpf, email, utype
            in
            user_data
        ]

    def delete(self, user: User):
        self.db_cursor.execute(self.queries["delete"], (user.cpf, ))

    def update(self, user: User):
        self.db_cursor.execute(self.queries["update"], (user.name, user.email, user.cpf))

    def update_utype(self, user: User):
        self.db_cursor.execute(self.queries["update-utype"], (user.utype, user.cpf))
