import sqlite3 as sql3

import customtkinter as ctk

from models.User import User
from models.Admin import Admin
from models.Punter import Punter
from models.Fighter import Fighter
from models.Fight import Fight
from models.Transaction import Transaction
from models.Bet import Bet

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
from persistence.FightPersistence import FightPersistence
from persistence.FighterPersistence import FighterPersistence

from control.Controller import Controller

from control.UserController import UserController
from control.AdminController import AdminController
from control.PunterController import PunterController
from control.WalletController import WalletController
from control.BetController import BetController
from control.TransactionController import TransactionController
from control.FightController import FightController
from control.FighterController import FighterController


class App(object):

    def __init__(self):
        self.conn, self.cursor = self.create_db()

        persistence = Persistence(user=UserPersistence(cursor=self.cursor),
                                  punter=PunterPersistence(cursor=self.cursor),
                                  wallet=WalletPersistence(cursor=self.cursor),
                                  admin=AdminPersistence(cursor=self.cursor),
                                  transaction=TransactionPersistence(cursor=self.cursor),
                                  fighter=FighterPersistence(cursor=self.cursor),
                                  fight=FightPersistence(cursor=self.cursor),
                                  bet=BetPersistence(cursor=self.cursor))

        self.controller = Controller(punter=PunterController(persistence=persistence),
                                     wallet=WalletController(persistence=persistence),
                                     user=UserController(persistence=persistence),
                                     admin=AdminController(persistence=persistence),
                                     transaction=TransactionController(persistence=persistence),
                                     bet=BetController(persistence=persistence),
                                     fighter=FighterController(persistence=persistence),
                                     fight=FightController(persistence=persistence))

        try:
            a = Admin(name="Admin", cpf="00000000000", login="admin", password="admin", email="admin@example.com")

            persistence.user.insert(a)

            u1 = Punter(name="Henrique", cpf="00000000001", login="hott", password="hott", email="hott@example.com")
            u2 = Punter(name="Daniel", cpf="00000000002", login="dani", password="dani", email="dani@example.com")

            persistence.user.insert(u1)
            persistence.user.insert(u2)

            f1 = Fighter(name="Junior dos Santos", category="MMA", height=1.7, nationality="BR", n_wins=0, n_loss=0)
            f2 = Fighter(name="Marco Ruas", category="MMA", height=1.7, nationality="BR", n_wins=0, n_loss=0)
            f3 = Fighter(name="Charles Oliveira", category="MMA", height=1.7, nationality="BR", n_wins=0, n_loss=0)
            f4 = Fighter(name="Jose Aldo", category="MMA", height=1.7, nationality="BR", n_wins=0, n_loss=0)
            f5 = Fighter(name="Deiveson Figueredo", category="MMA", height=1.7, nationality="BR", n_wins=0, n_loss=0)

            persistence.fighter.create(f1)
            persistence.fighter.create(f2)
            persistence.fighter.create(f3)
            persistence.fighter.create(f4)
            persistence.fighter.create(f5)

            fg1 = Fight("Luta da Boa 001", f1, 2, f5, 3)
            fg2 = Fight("Luta da Boa 002", f4, 4, f3, 6)

            persistence.fight.create(fg1)
            persistence.fight.create(fg2)
        except:
            pass

        self.master = ctk.CTk()
        self.master.title("123bets")
        self.master.geometry("600x500")
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)

        self.user_view = UserView(master=self.master,
                                  controller=self.controller,
                                  post_login_callback=self.post_login,
                                  width=600, height=600)

        self.user_view.grid()

    def post_login(self, u: User):
        match u.utype:
            case 0:
                PunterView(master=self.master,
                           controller=self.controller,
                           punter=self.controller.punter.get_from_user(u),
                           post_logout_callback=self.user_view.grid,
                           width=600, height=600).grid()

            case 1:
                AdminView(master=self.master,
                          admin=self.controller.admin.get_from_user(u),
                          controller=self.controller,
                          post_logout_callback=self.user_view.grid,
                          width=600, height=600).grid()

    def create_db(self, db_name: str = "db.sqlite3") -> tuple[sql3.Connection, sql3.Cursor]:
        connection = sql3.connect(db_name)

        connection.execute("PRAGMA foreign_keys = ON;")

        return connection, connection.cursor()

    def main(self):
        self.master.mainloop()
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

def main():
    App().main()

if __name__ == "__main__":
    main()

