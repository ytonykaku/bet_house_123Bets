import typing as t
import datetime as dt

import customtkinter as ctk
import CTkMessagebox

from models.Punter import Punter
from models.Fight import Fight
from models.Bet import Bet

from models.Transaction import Transaction
from control.Controller import Controller


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

class FightTab(ctk.CTkFrame):

    def __init__(self, master, fetch_fights_callback, **kwargs):
        super().__init__(master, **kwargs)
        ctk.CTkButton(master=self,
                      text="Fetch",
                      width=300, height=30,
                      command=fetch_fights_callback,
                      corner_radius=6).grid(pady=5)

        self.fights = ctk.CTkScrollableFrame(master=self,
                                             width=300, height=30,
                                             corner_radius=6)

        self.fights.grid()

    def clear(self):
        for s in self.fights.grid_slaves():
            s.destroy()

class BetTab(ctk.CTkFrame):

    def __init__(self, master, fetch_bets_callback, **kwargs):
        super().__init__(master, **kwargs)
        ctk.CTkButton(master=self,
                      text="Fetch",
                      width=300, height=30,
                      command=fetch_bets_callback,
                      corner_radius=6).grid(pady=5)

        self.bets = ctk.CTkScrollableFrame(master=self,
                                             width=300, height=30,
                                             corner_radius=6)

        self.bets.grid()

    def clear(self):
        for s in self.bets.grid_slaves():
            s.destroy()

class PunterView(object):

    def __init__(self, master: ctk.CTk, controller: Controller):
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

        self.withdraw_tab = WithdrawTab(self.tabs.add("Withdraw"),
                                       self.withdraw_value)

        self.withdraw_tab.grid()

        self.transaction_tab = TransactionTab(self.tabs.add("Transaction"),
                                              self.fetch_transactions)

        self.transaction_tab.grid()

        self.fight_tab = FightTab(self.tabs.add("Fights"),
                                  self.fetch_fights)

        self.fight_tab.grid()

        self.bet_tab = BetTab(self.tabs.add("Bets"),
                                  self.fetch_bets)

        self.bet_tab.grid()

        self.tabs.grid()

        ctk.CTkButton(self.main_frame,
                      text="Logout",
                      command=self.on_logout_click,
                      width=200,
                      fg_color="red",
                      hover_color="red").grid(padx=30, pady=(15, 15))

    def fetch_bets(self):
        self.bet_tab.clear()

        bets = self.controller.bet.fetch_by_punter(self.punter)

        for bet in bets:
            master = ctk.CTkFrame(self.bet_tab.bets,
                        width=300, height=10,
                        bg_color="white")
            
            fight = bet.fight

            text = f"Name:{fight.fA.name}\nOdd:{fight.oddA}\nCategory:{fight.fA.category}\nHeight:{fight.fA.height}m" + \
                   f"\nX\n" + \
                   f"Name:{fight.fB.name}\nOdd:{fight.oddB}\nCategory:{fight.fB.category}\nHeight:{fight.fB.height}m\n" + \
                   f"Winner: {bet.winner.name}\n" + \
                   f"Value: {bet.value}"

            ctk.CTkLabel(master,
                         width=300,
                         text=text).grid(padx=5, pady=5)

            master.grid()

    def fetch_fights(self):
        self.fight_tab.clear()

        fights = list(filter(lambda f: f.winner == None, self.controller.fight.read()))

        for fight in fights:
            master = ctk.CTkFrame(self.fight_tab.fights,
                        width=300, height=10,
                        bg_color="white")

            text = f"Name:{fight.fA.name}\nOdd:{fight.oddA}\nCategory:{fight.fA.category}\nHeight:{fight.fA.height}m" + \
                   f"\nX\n" + \
                   f"Name:{fight.fB.name}\nOdd:{fight.oddB}\nCategory:{fight.fB.category}\nHeight:{fight.fB.height}m"

            ctk.CTkLabel(master,
                         width=300,
                         text=text).grid(padx=5, pady=5)

            entry_value = ctk.CTkEntry(master=master, width=300, height=30, placeholder_text="Value")
            entry_value.grid(padx=10)

            entry_winner = ctk.CTkEntry(master=master, width=300, height=30, placeholder_text="Winner")
            entry_winner.grid(padx=10)

            ctk.CTkButton(master,
                          width=300,
                          text="Bet",
                          command=lambda fight=fight: self.bet_on_fight(fight,
                                                                        entry_winner.get(),
                                                                        entry_value.get())).grid(padx=5, pady=5)

            master.grid()

    def bet_on_fight(self, fight: Fight, winner: str, value: float):
        try:
            value = float(value)
        except:
            CTkMessagebox.CTkMessagebox(title="ERROR", message="Please, provide a valid value.", icon="cancel")
            return

        winner = self.controller.fighter.fetch_by_name(winner)

        if not winner:
            CTkMessagebox.CTkMessagebox(title="ERROR", message="Please, provide a valid winner.", icon="cancel")
            return

        try:
            b = Bet(fight, winner, value)

            self.controller.bet.create(self.punter, b)
        except Exception as e:
            print(e)
            CTkMessagebox.CTkMessagebox(title="ERROR", message=f"Impossible to bet {b.value} bonoros.", icon="cancel")
            return

        CTkMessagebox.CTkMessagebox(title="SUCCESS", message="Bet executed.", icon="check")

        self.update_main_label()

    def fetch_transactions(self):
        self.transaction_tab.clear()

        year = self.transaction_tab.year.get()

        if year:
            try:
                year = int(year)
            except:
                CTkMessagebox.CTkMessagebox(title="ERROR", message="Please, provide a valid year.", icon="cancel")
                return

        for t in self.punter.wallet.transactions:
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

            t = Transaction(value, Transaction.DEPOSIT, dt.datetime.now().timestamp())

            self.controller.transaction.create(self.punter.wallet, t)

            self.update_main_label()
        except:
            CTkMessagebox.CTkMessagebox(title="ERROR", message="Please, provide a valid value.", icon="cancel")

    def withdraw_value(self):
        try:
            value = float(self.withdraw_tab.value.get())

            if value > self.punter.wallet.value_available:
                raise Exception()

            if value < 0.0:
                CTkMessagebox.CTkMessagebox(title="ERROR", message="Only positive values.", icon="cancel")
                return

            t = Transaction( value, Transaction.WITHDRAW, dt.datetime.now().timestamp())

            self.controller.transaction.create(self.punter.wallet, t)

            self.update_main_label()
        except:
            CTkMessagebox.CTkMessagebox(title="ERROR", message="Please, provide a valid value.", icon="cancel")

    def activate_view(self, user: Punter, post_logout_callback: t.Callable[..., None]):
        self.punter = user

        self.post_logout_callback = post_logout_callback

        self.update_main_label()

        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=100) # Show main frame

    def update_main_label(self):
        msg = f"Welcome, {self.punter.name}!\n" + \
              f"You have: ${self.punter.wallet.value_available} bonoros.\n" + \
              f"Profit: ${self.punter.profit}\n" + \
              f"Loss: ${self.punter.loss}"

        self.main_label.configure(text=msg)

    def on_logout_click(self):
        self.transaction_tab.clear()
        self.main_frame.grid_forget()
        self.post_logout_callback()
