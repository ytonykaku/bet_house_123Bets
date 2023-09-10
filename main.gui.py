import sqlite3 as sql3
from typing import Any, Tuple, Union, Optional, Union

import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

from vision.Fontes import Fonts

from models.User import User

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

        self.title('Login')

        self.login_frame = ctk.CTkFrame(self, corner_radius=0)
        self.login_frame.grid(row=0, column=0, sticky="ns")

        self.login_label = ctk.CTkLabel(self.login_frame, text="Login Page", font=ctk.CTkFont(size=20, weight="bold"))
        self.login_label.grid(row=0, column=0, padx=30, pady=(150, 15))

        self.username_entry = ctk.CTkEntry(self.login_frame, width=200, placeholder_text="username")
        self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.password_entry = ctk.CTkEntry(self.login_frame, width=200, show="*", placeholder_text="password")
        self.password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))

        self.login_button = ctk.CTkButton(self.login_frame, text="Login", command=self.login_event, width=200)
        self.login_button.grid(row=3, column=0, padx=30, pady=(15, 15))

    def login_event(self):
        u: User | None = self.user_controller.authenticate(self.username_entry.get(), self.password_entry.get())
        print(u)
        # TODO: Check type and and instantiate the correct class.

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

