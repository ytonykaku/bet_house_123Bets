import sqlite3 as sql3

import CTkMessagebox
import customtkinter as ctk

from models.User import User
from models.Admin import Admin
from models.Punter import Punter

from view.AdminView import AdminView
from view.PunterView import PunterView

from persistence.UserPersistence import UserPersistence
from persistence.PunterPersistence import PunterPersistence
from persistence.WalletPersistence import WalletPersistence
from persistence.AdminPersistence import AdminPersistence
from persistence.TransactionPersistence import TransactionPersistence

from control.UserController import UserController
from control.PunterController import PunterController
from control.WalletController import WalletController
from control.AdminController import AdminController
from control.TransactionController import TransactionController


def create_db(db_name: str = "db.sqlite3") -> tuple[sql3.Connection, sql3.Cursor]:
    connection = sql3.connect(db_name)

    connection.execute("PRAGMA foreign_keys = ON;")

    cursor = connection.cursor()

    for model in [ "user", "admin", "punter", "wallet", "transaction" ]:
        with open(f"sql/{model}/table.sql") as f:
            cursor.execute(f.read())

    return connection, cursor


class App(ctk.CTk):
    def __init__(self,
                 user_controller: UserController,
                 punter_controller: PunterController,
                 wallet_controller: WalletController,
                 admin_controller: AdminController,
                 transaction_controller: TransactionController):
        super().__init__()
        self.user_controller = user_controller
        self.punter_controller = punter_controller
        self.wallet_controller = wallet_controller
        self.admin_controller = admin_controller
        self.transaction_controller = transaction_controller

        ctk.set_appearance_mode("dark") 
        ctk.set_default_color_theme("green") 

        self.punter_view = PunterView(master=self, controller=self.punter_controller)
        self.admin_view = AdminView(master=self, controller=self.admin_controller)

        self.title("123bets")

        self.login_frame = ctk.CTkFrame(self, corner_radius=0)
        self.login_frame.grid(row=0, column=0, sticky="ns")

        self.login_label = ctk.CTkLabel(self.login_frame, text="Login", font=ctk.CTkFont(size=20, weight="bold"))
        self.login_label.grid(row=0, column=0, padx=30, pady=(150, 15))

        self.username_entry = ctk.CTkEntry(self.login_frame, width=200, placeholder_text="Username")
        self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))

        self.password_entry = ctk.CTkEntry(self.login_frame, width=200, show="*", placeholder_text="Password")
        self.password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))

        self.login_button = ctk.CTkButton(self.login_frame, text="Login", command=self.on_login_click, width=200)
        self.login_button.grid(row=3, column=0, padx=30, pady=(15, 15))

    def on_login_click(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        u: User | None = self.user_controller.authenticate(username, password)

        self.username_entry.delete(0, len(username))
        self.password_entry.delete(0, len(password))

        if u is None:
            CTkMessagebox.CTkMessagebox(title="Error", message="Wrong username or password.", icon="cancel")
            return

        match u.utype:
            case 0:
                p: Punter = self.punter_controller.get_from_user(u)
                p.wallet = self.wallet_controller.get_wallet_by_id(p.id)
                self.punter_view.activate_view(return_frame=self.login_frame, user=p)

            case 1:
                a: Admin = self.admin_controller.get_from_user(u)
                self.admin_view.activate_view(return_frame=self.login_frame, user=a)

def main():
    conn, cursor = create_db()

    user_persistence        = UserPersistence(cursor=cursor)
    punter_persistence      = PunterPersistence(cursor=cursor)
    wallet_persistence      = WalletPersistence(cursor=cursor)
    admin_persistence       = AdminPersistence(cursor=cursor)
    transaction_persistence = TransactionPersistence(cursor=cursor)

    user_controller        = UserController(persistence=user_persistence)
    punter_controller      = PunterController(persistence=punter_persistence)
    wallet_controller      = WalletController(persistence=wallet_persistence)
    admin_controller       = AdminController(persistence=admin_persistence)
    transaction_controller = TransactionController(persistence=transaction_persistence)

    App(user_controller=user_controller,
        punter_controller=punter_controller,
        wallet_controller=wallet_controller,
        admin_controller=admin_controller,
        transaction_controller=transaction_controller).mainloop()

    conn.commit()

if __name__ == "__main__":
    main()

