#!/bin/env python3.11

import sqlite3 as sql3

import customtkinter as ctk

from models.User import User
from models.Admin import Admin
from models.Punter import Punter

from view.UserView import UserView
from view.PunterView import PunterView
from view.AdminView import AdminView

from persistence.UserPersistence import UserPersistence
from persistence.AdminPersistence import AdminPersistence
from persistence.PunterPersistence import PunterPersistence
from persistence.WalletPersistence import WalletPersistence
from persistence.TransactionPersistence import TransactionPersistence

from control.UserController import UserController
from control.AdminController import AdminController
from control.PunterController import PunterController
from control.WalletController import WalletController
from control.TransactionController import TransactionController


class App(object):

    def __init__(self):
        self.conn, cursor = self.create_db()

        user_persistence        = UserPersistence(cursor=cursor)
        punter_persistence      = PunterPersistence(cursor=cursor)
        wallet_persistence      = WalletPersistence(cursor=cursor)
        admin_persistence       = AdminPersistence(cursor=cursor)
        transaction_persistence = TransactionPersistence(cursor=cursor)

        self.punter_controller      = PunterController(punter_persistence=punter_persistence,
                                                       wallet_persistence=wallet_persistence,
                                                       transaction_persistence=transaction_persistence)

        self.wallet_controller      = WalletController(persistence=wallet_persistence)

        self.user_controller        = UserController(user_persistence=user_persistence,
                                                     admin_persistence=admin_persistence,
                                                     punter_persistence=punter_persistence,
                                                     wallet_persistence=wallet_persistence)

        self.admin_controller       = AdminController(admin_persistence=admin_persistence,
                                                      user_persistence=user_persistence)

        self.transaction_controller = TransactionController(persistence=transaction_persistence)

        self.master = ctk.CTk()
        self.master.title("123bets")

        self.user_view = UserView(master=self.master, controller=self.user_controller)
        self.punter_view = PunterView(master=self.master, controller=self.punter_controller)
        self.admin_view = AdminView(master=self.master, controller=self.admin_controller)

        self.user_view.activate_view(post_login_callback=self.post_login)

    def post_login(self, u: User):
        match u.utype:
            case 0:
                p: Punter = self.punter_controller.get_from_user(u)
                p.wallet = self.wallet_controller.get_by_id(p.id)
                self.punter_view.activate_view(user=p, post_logout_callback=self.post_logout)

            case 1:
                a: Admin = self.admin_controller.get_from_user(u)
                self.admin_view.activate_view(user=a, post_logout_callback=self.post_logout)

    def post_logout(self):
        self.user_view.activate_view(post_login_callback=self.post_login)

    def create_db(self, db_name: str = "db.sqlite3") -> tuple[sql3.Connection, sql3.Cursor]:
        connection = sql3.connect(db_name)

        connection.execute("PRAGMA foreign_keys = ON;")

        return connection, connection.cursor()

    def main(self):
        self.master.mainloop()
        self.conn.commit()

def main():
    App().main()

if __name__ == "__main__":
    main()

