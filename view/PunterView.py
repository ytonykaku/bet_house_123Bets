import typing as t
import datetime as dt
import sqlite3 as sql3

import customtkinter as ctk
import CTkMessagebox

from models.Punter import Punter
from models.Fight import Fight
from models.Fighter import Fighter
from models.Bet import Bet

from models.Transaction import Transaction
from control.Controller import Controller

from view import Frames


class TransactionFormFrame(ctk.CTkFrame):

    def __init__(self, master, confirm_callback, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.label = ctk.CTkLabel(self, text="$")

        self.value = ctk.CTkEntry(self)
        self.confirmation_button = ctk.CTkButton(self, text="Confirm", command=confirm_callback)

    def grid(self, **kwargs):
        super().grid(**kwargs)
        self.label.grid(row=0, column=0, padx=5)
        self.value.grid(row=0, column=1, padx=5)
        self.confirmation_button.grid(row=0, column=2, padx=5)

    def clear(self):
        self.value.delete(0, len(self.value.get()))

class PunterView(ctk.CTkFrame):

    def __init__(self,
                 master,
                 controller: Controller,
                 punter: Punter,
                 post_logout_callback: t.Callable[..., None],
                 **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.controller = controller
        self.punter = punter
        self.post_logout_callback = post_logout_callback

        self.punter_frame = Frames.PunterFrame(self, self.punter)

        self.tabs = ctk.CTkTabview(self, width=500, command=self.on_tab_change)

        self.t1 = self.tabs.add("Deposit")

        self.t1.grid_rowconfigure(0, weight=1)
        self.t1.grid_columnconfigure(0, weight=1)

        self.deposit_tab = TransactionFormFrame(self.t1, self.deposit_value)

        self.t2 = self.tabs.add("Withdraw")

        self.t2.grid_rowconfigure(0, weight=1)
        self.t2.grid_columnconfigure(0, weight=1)

        self.withdraw_tab = TransactionFormFrame(self.t2, self.withdraw_value)

        self.t3 = self.tabs.add("Transactions")

        self.t3.grid_columnconfigure(0, weight=1)

        self.transaction_tab = Frames.SearchFrame(self.t3, keyword="Year", fetch_callback=self.fetch_transactions)

        self.t4 = self.tabs.add("Fights")

        self.t4.grid_columnconfigure(0, weight=1)

        self.fight_tab = Frames.SearchFrame(self.t4, keyword="Name", fetch_callback=self.fetch_fights)

        self.t5 = self.tabs.add("Bets")

        self.t5.grid_columnconfigure(0, weight=1)

        self.bet_tab = Frames.SearchFrame(self.t5, keyword="Name", fetch_callback=self.fetch_bets)

        self.t6 = self.tabs.add("Profile")

        self.t6.grid_columnconfigure(0, weight=1)

        self.profile_tab = Frames.ProfileFrame(self.t6, self.punter, confirm_callback=self.update_profile)

        self.logout_button = ctk.CTkButton(self, text="Logout", fg_color="red", command=self.on_logout_click)

    def grid(self, **kwargs):
        super().grid(**kwargs)
        self.punter_frame.grid()
        self.tabs.grid()
        self.deposit_tab.grid()
        self.withdraw_tab.grid()
        self.transaction_tab.grid()
        self.fight_tab.grid()
        self.bet_tab.grid()
        self.profile_tab.grid()
        self.logout_button.grid(pady=5)

    def on_tab_change(self):
        self.profile_tab.update()

    def update_profile(self):
        bkp_name = str(self.punter.name)
        bkp_email = str(self.punter.email)

        self.punter.name = self.profile_tab.name.get()
        self.punter.email = self.profile_tab.email.get()

        try:
            if not self.punter.name:
                raise Exception("Please, provide a name.")

            if not self.punter.email:
                raise Exception("Please, provide a email.")

            self.controller.user.update(self.punter)
            self.punter_frame.update()
        except sql3.IntegrityError:
            CTkMessagebox.CTkMessagebox(title="ERROR", message="Email already in use.", icon="cancel")
            self.punter.name = bkp_name
            self.punter.email = bkp_email
            return
        except Exception as e:
            CTkMessagebox.CTkMessagebox(title="ERROR", message=str(e), icon="cancel")
            self.punter.name = bkp_name
            self.punter.email = bkp_email
            return

        CTkMessagebox.CTkMessagebox(title="SUCCESS", message="Profile updated.", icon="check")

    def fetch_transactions(self):
        year = self.transaction_tab.get_input()

        self.transaction_tab.clear()

        if year:
            try:
                year = int(year)
            except:
                CTkMessagebox.CTkMessagebox(title="ERROR", message="Please, provide a valid year.", icon="cancel")
                return

        for t in self.punter.wallet.transactions:
            if year and dt.datetime.fromtimestamp(t.timestamp).year != year:
                continue

            master = ctk.CTkFrame(self.transaction_tab.container)

            Frames.TransactionFrame(master=master, transaction=t).grid()

            master.grid()

    def fetch_bets(self):
        fight_name = self.bet_tab.get_input()

        self.bet_tab.clear()

        bets = self.punter.wallet.bets

        if fight_name:
            bets = list(filter(lambda b: b.fight.name == fight_name, bets))

        for bet in bets:
            master = ctk.CTkFrame(self.bet_tab.container)

            Frames.BetFrame(master=master, bet=bet).grid()

            master.grid()

    def fetch_fights(self):
        name = self.fight_tab.get_input()

        self.fight_tab.clear()

        fights = list(filter(lambda f: f.winner == None, self.controller.fight.read()))

        if name:
            fights = list(filter(lambda f: f.name == name, fights))

        for fight in fights:
            master = ctk.CTkFrame(self.fight_tab.container, fg_color="transparent")

            fight_frame = Frames.FightFrame(master=master, fight=fight)

            form = ctk.CTkFrame(master=master, fg_color="transparent")

            value_form = ctk.CTkFrame(master=form, fg_color="transparent")

            entry_value = ctk.CTkEntry(master=value_form, placeholder_text="Value")

            entry_winner = ctk.CTkEntry(master=value_form, placeholder_text="Winner")

            cmd = lambda fight=fight, winner=entry_winner, value=entry_value: \
                         self.bet_on_fight(fight, winner.get(), value.get())

            confirm_bet_button = ctk.CTkButton(form, text="Bet", command=cmd, height=56)

            master.grid()
            fight_frame.grid()
            form.grid()
            value_form.grid(row=0, column=0, pady=5)
            entry_winner.grid(row=0, column=0, padx=5, pady=5)
            entry_value.grid(row=1, column=0, padx=5, pady=5)
            confirm_bet_button.grid(row=0, column=1, pady=5)

    def bet_on_fight(self, fight: Fight, winner: str, value: str):
        try:
            value = float(value)
        except:
            CTkMessagebox.CTkMessagebox(title="ERROR", message="Please, provide a valid value.", icon="cancel")
            return

        winner: Fighter | None = self.controller.fighter.fetch_by_name(winner)

        if not winner or (winner.name not in [ fight.fA.name, fight.fB.name ]):
            CTkMessagebox.CTkMessagebox(title="ERROR", message="Please, provide a valid winner.", icon="cancel")
            return

        try:
            b = Bet(fight, winner, value)

            self.controller.bet.create(self.punter, b)
        except:
            CTkMessagebox.CTkMessagebox(title="ERROR", message=f"Impossible to bet {b.value} bonoros.", icon="cancel")
            return

        CTkMessagebox.CTkMessagebox(title="SUCCESS", message="Bet executed.", icon="check")

        self.punter_frame.update()

    def deposit_value(self):
        try:
            value = float(self.deposit_tab.value.get())

            if value < 0.0:
                CTkMessagebox.CTkMessagebox(title="ERROR", message="Only positive values.", icon="cancel")
                return

            t = Transaction(value, Transaction.DEPOSIT, dt.datetime.now().timestamp())

            self.controller.transaction.create(self.punter.wallet, t)

            self.punter_frame.update()
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

            self.punter_frame.update()
        except:
            CTkMessagebox.CTkMessagebox(title="ERROR", message="Please, provide a valid value.", icon="cancel")

    def on_logout_click(self):
        self.deposit_tab.clear()
        self.withdraw_tab.clear()
        self.transaction_tab.clear()
        self.fight_tab.clear()
        self.bet_tab.clear()
        self.grid_forget()
        self.post_logout_callback()
