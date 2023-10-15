import typing as t
import datetime as dt

import customtkinter as ctk
import CTkMessagebox

from models.Punter import Punter
from control.PunterController import PunterController
from models.Transaction import Transaction

class DepositTab(ctk.CTkFrame):

    def __init__(self, master, deposit_callback, **kwargs):
        super().__init__(master, **kwargs)

        ctk.CTkLabel(self, text="$").grid(row=0, column=0)

        self.value = ctk.CTkEntry(self)
        self.value.grid(pady=5, padx=5, row=0, column=1)

        ctk.CTkButton(self,
                      text="OK",
                      command=deposit_callback).grid(row=0, column=2)

class WithdrawTab(ctk.CTkFrame):

    def __init__(self, master, withdraw_callback, **kwargs):
        super().__init__(master, **kwargs)

        ctk.CTkLabel(self, text="$").grid(row=0, column=0)

        self.value = ctk.CTkEntry(self)
        self.value.grid(pady=5, padx=5, row=0, column=1)

        ctk.CTkButton(self,
                      text="OK",
                      command=withdraw_callback).grid(row=0, column=2)

class TransactionTab(ctk.CTkFrame):

    def __init__(self, master, fetch_callback, **kwargs):
        super().__init__(master, **kwargs)

        self.year = ctk.CTkEntry(master=self, width=300, height=30, placeholder_text="Year")
        self.year.grid(padx=10)

        ctk.CTkButton(master=self,
                      text="Fetch",
                      width=300, height=30,
                      command=fetch_callback,
                      corner_radius=6).grid(pady=5)

        self.transactions = ctk.CTkScrollableFrame(master=self,
                                                   width=300, height=30,
                                                   corner_radius=6)
        self.transactions.grid(pady=5)

    def clear(self):
        for s in self.transactions.grid_slaves():
            s.destroy()

class BetTab(ctk.CTkFrame):

    def __init__(self, master, func_fetch_fights, bet_callback, **kwargs):
        super().__init__(master, **kwargs)

        self.func_fetch_fights = func_fetch_fights
        self.bet_callback = bet_callback

        tab = ctk.CTkTabview(self)

        tab.add("New").grid()
        tab.add("History").grid()
        tab.add("Active").grid()

        tab.grid()

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


        self.tabs = ctk.CTkTabview(self.main_frame)

        self.deposit_tab = DepositTab(self.tabs.add("Deposit"),
                                      self.deposit_value)

        self.deposit_tab.grid()

        self.withdraw_tab = DepositTab(self.tabs.add("Withdraw"),
                                       self.withdraw_value)

        self.withdraw_tab.grid()

        self.transaction_tab = TransactionTab(self.tabs.add("Transaction"),
                                              self.fetch_transactions)

        self.transaction_tab.grid()

        self.bet_tab = BetTab(self.tabs.add("Bet"),
                              lambda : print("Fetch Fights: Not Implemented Yet."),
                              lambda : print("Bet on Fight: Not Implemented Yet."))

        self.bet_tab.grid()

        self.tabs.grid()

        ctk.CTkButton(self.main_frame,
                      text="Logout",
                      command=self.on_logout_click,
                      width=200,
                      fg_color="red",
                      hover_color="red").grid(padx=30, pady=(15, 15))

    def fetch_transactions(self):
        self.transaction_tab.clear()

        transactions = self.controller.fetch_transactions(self.punter)

        year = self.transaction_tab.year.get()

        if year:
            try:
                year = int(year)
            except:
                CTkMessagebox.CTkMessagebox(title="ERROR", message="Please, provide a valid year.", icon="cancel")
                return

        for t in transactions:
            if type(year) == int and dt.datetime.fromtimestamp(t.timestamp).year != year:
                continue

            master = ctk.CTkFrame(self.transaction_tab.transactions,
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
            value = float(self.deposit_tab.value.get())

            if value < 0.0:
                CTkMessagebox.CTkMessagebox(title="ERROR", message="Only positive values.", icon="cancel")
                return

            self.controller.deposit(self.punter, value)
            self.update_main_label()
        except Exception as _:
            CTkMessagebox.CTkMessagebox(title="ERROR", message="Please, provide a valid value.", icon="cancel")

    def withdraw_value(self):
        try:
            value = float(self.withdraw_tab.value.get())

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
        msg = f"Welcome, {self.punter.name}!\nYou have: ${self.punter.wallet.value_available} bonoros."
        self.main_label.configure(text=msg)

    def on_logout_click(self):
        self.main_frame.grid_forget()
        self.post_logout_callback()

