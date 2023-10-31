import sqlite3 as sql3

import customtkinter as ctk

from models.User import User
from models.Admin import Admin
from models.Punter import Punter

from view.UserView import UserView
from view.PunterView import PunterView
from view.AdminView import AdminView

from persistence.Persistence import Persistence

from persistence.UserPersistence import UserPersistence
from persistence.AdminPersistence import AdminPersistence
from persistence.PunterPersistence import PunterPersistence
from persistence.WalletPersistence import WalletPersistence
from persistence.TransactionPersistence import TransactionPersistence
from persistence.BetPersistence import BetPersistence
from persistence.InvestmentPersistence import InvestmentPersistence
from persistence.FightPersistence import FightPersistence
from persistence.FighterPersistence import FighterPersistence

from control.Controller import Controller

from control.UserController import UserController
from control.AdminController import AdminController
from control.PunterController import PunterController
from control.WalletController import WalletController
from control.BetController import BetController
from control.TransactionController import TransactionController
from control.InvestmentController import InvestmentController
from control.FightController import FightController
from control.FighterController import FighterController

class App(object):

    def __init__(self):
        self.conn, cursor = self.create_db()


        persistence = Persistence(user=UserPersistence(cursor=cursor),
                                  punter=PunterPersistence(cursor=cursor),
                                  wallet=WalletPersistence(cursor=cursor),
                                  admin=AdminPersistence(cursor=cursor),
                                  transaction=TransactionPersistence(cursor=cursor),
                                  bet=BetPersistence(cursor=cursor),
                                  investment=InvestmentPersistence(cursor=cursor),
                                  fighter=FighterPersistence(cursor=cursor),
                                  fight=FightPersistence(cursor=cursor))

        self.controller = Controller(punter=PunterController(persistence=persistence),
                                     wallet=WalletController(persistence=persistence),
                                     user=UserController(persistence=persistence),
                                     admin=AdminController(persistence=persistence),
                                     transaction=TransactionController(persistence=persistence),
                                     bet=BetController(persistence=persistence),
                                     investment=InvestmentController(persistence=persistence),
                                     fighter=FighterController(persistence=persistence),
                                     fight=FightController(persistence=persistence))

        try:
            a = Admin(name="Admin", cpf="00000000000", login="admin", password="admin", email="admin@example.com")
            persistence.user.insert(a)
            persistence.admin.insert(a)
        except: pass

        self.master = ctk.CTk()
        self.master.title("123bets")

        self.user_view = UserView(master=self.master, controller=self.controller)
        self.punter_view = PunterView(master=self.master, controller=self.controller)
        self.admin_view = AdminView(master=self.master, controller=self.controller)

        self.user_view.activate_view(post_login_callback=self.post_login)

    def post_login(self, u: User):
        match u.utype:
            case 0:
                p: Punter = self.controller.punter.get_from_user(u)
                p.wallet = self.controller.wallet.get_by_id(p.id)
                self.punter_view.activate_view(user=p, post_logout_callback=self.post_logout)

            case 1:
                a: Admin = self.controller.admin.get_from_user(u)
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

