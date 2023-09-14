import typing as t
import datetime as dt

import customtkinter as ctk
import CTkMessagebox

from models.Punter import Punter
from control.PunterController import PunterController
from models.Transaction import Transaction


class PunterView(object):

    def __init__(self, master: ctk.CTk, controller: PunterController):
        self.controller = controller

        self.return_frame: ctk.CTkFrame | None = None

        self.main_frame = ctk.CTkFrame(master, corner_radius=0)
        self.main_frame.grid_columnconfigure(0, weight=1)

        self.main_label = ctk.CTkLabel(self.main_frame,
                                       text="[BUG DETECTED]",
                                       font=ctk.CTkFont(size=20, weight="bold"))
        self.main_label.grid(padx=30, pady=(30, 15))

        self.logout_button = ctk.CTkButton(self.main_frame,
                                           text="Logout",
                                           command=self.on_logout_click,
                                           width=200,
                                           fg_color="red",
                                           hover_color="red")

        self.tabs = ctk.CTkTabview(self.main_frame)

        self.deposit = self.tabs.add("Deposit")
        ctk.CTkLabel(self.deposit, text="$").grid(row=0, column=0)
        self.d_value = ctk.CTkEntry(self.deposit)
        self.d_value.grid(pady=5, padx=5, row=0, column=1)
        self.deposit_btn = ctk.CTkButton(self.deposit,
                                         text="OK",
                                         command=self.deposit_value).grid(row=0, column=2)

        self.withdraw = self.tabs.add("Withdraw")
        ctk.CTkLabel(self.withdraw, text="$").grid(row=0, column=0)
        self.w_value = ctk.CTkEntry(self.withdraw)
        self.w_value.grid(pady=5, padx=5, row=0, column=1)
        self.withdraw_btn = ctk.CTkButton(self.withdraw,
                                          text="OK",
                                          command=self.withdraw_value).grid(row=0, column=2)

        self.transactions = self.tabs.add("Transaction")
        self.fetch_btn = ctk.CTkButton(self.transactions,
                                          text="Fetch",
                                          command=self.fetch_transactions).grid()
        self.transactions_list = ctk.CTkScrollableFrame(master=self.transactions,
                                                 width=300, height=30,
                                                 corner_radius=6)
        self.transactions_list.grid(pady=5)


        self.tabs.grid()

        self.logout_button.grid(padx=30, pady=(15, 15))

    def fetch_transactions(self):
        for s in self.transactions_list.grid_slaves():
            s.destroy()

        transactions = self.controller.fetch_transactions(self.punter)

        for t in transactions:
            master = ctk.CTkFrame(self.transactions_list,
                                  width=300, height=10,
                                  bg_color="white")
            tstr = 'Deposit' if t.ttype == Transaction.DEPOSIT else 'Withdraw'
            ctk.CTkLabel(master,
                         width=300,
                         text=f"Type: {tstr}").grid(padx=5, pady=5)
            ctk.CTkLabel(master,
                         width=300,
                         text=f"Value: {t.value}").grid(padx=5, pady=5)
            ctk.CTkLabel(master,
                         width=300,
                         text=f"Date: {dt.datetime.fromtimestamp(t.timestamp)}").grid(padx=5, pady=5)

            master.grid()


    def deposit_value(self):
        try:
            value = float(self.d_value.get())

            if value < 0.0:
                CTkMessagebox.CTkMessagebox(title="ERROR", message="Only positive values.", icon="cancel")
                return

            self.controller.deposit(self.punter, value)
            self.update_main_label()
        except Exception as _:
            CTkMessagebox.CTkMessagebox(title="ERROR", message="Please, provide a valid value.", icon="cancel")

    def withdraw_value(self):
        try:
            value = float(self.w_value.get())

            if value > self.punter.wallet.value_available:
                raise Exception()

            if value < 0.0:
                CTkMessagebox.CTkMessagebox(title="ERROR", message="Only positive values.", icon="cancel")
                return

            self.controller.withdraw(self.punter, value)
            self.update_main_label()
        except Exception as _:
            CTkMessagebox.CTkMessagebox(title="ERROR", message="Please, provide a valid value.", icon="cancel")

    def activate_view(self, user: Punter, post_logout_callback: t.Callable[..., None]):
        self.punter = user

        self.post_logout_callback = post_logout_callback

        self.update_main_label()

        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=100) # Show main frame

    def update_main_label(self):
        self.main_label.configure(text=f"Welcome, {self.punter.name}!\nYou have: ${self.punter.wallet.value_available} bonoros.")

    def on_logout_click(self):
        self.main_frame.grid_forget()
        self.post_logout_callback()

