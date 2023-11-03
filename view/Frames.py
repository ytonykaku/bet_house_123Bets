import datetime as dt

from models.User import User
from models.Admin import Admin
from models.Punter import Punter
from models.Fight import Fight
from models.Fighter import Fighter
from models.Wallet import Wallet
from models.Transaction import Transaction
from models.Bet import Bet

import customtkinter as ctk

class SearchFrame(ctk.CTkFrame):

    def __init__(self, master, keyword: str, fetch_callback, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.form = ctk.CTkFrame(self)

        self.input = ctk.CTkEntry(master=self.form, placeholder_text=keyword)

        self.fetch_button = ctk.CTkButton(master=self.form,
                                          text="Fetch",
                                          command=fetch_callback)

        self.container = ctk.CTkScrollableFrame(master=self, width=500)

        self.container.grid_columnconfigure(0, weight=1)

    def get_input(self) -> str:
        return self.input.get()

    def grid(self, **kwargs):
        super().grid(**kwargs)
        self.form.grid()
        self.input.grid(row=0, column=0, padx=5)
        self.fetch_button.grid(row=0, column=1, padx=5)
        self.container.grid()

    def clear(self):
        self.input.delete(0, len(self.input.get()))
        for s in self.container.grid_slaves():
            s.destroy()

class UserFrame(ctk.CTkFrame):

    def __init__(self, master, user: User, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        utype_str = "Admin" if user.utype == 1 else "Punter"

        self.name = ctk.CTkLabel(self, text=f"Name: {user.name}")
        self.cpf = ctk.CTkLabel(self, text=f"CPF: {user.cpf}")
        self.email = ctk.CTkLabel(self, text=f"Email: {user.email}")
        self.type = ctk.CTkLabel(self, text=f"Type: {utype_str}")

    def grid(self, **kwargs):
        self.name.grid()
        self.cpf.grid()
        self.email.grid()
        self.type.grid()
        super().grid(**kwargs)

class AdminFrame(ctk.CTkFrame):

    def __init__(self, master, admin: Admin, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.label = ctk.CTkLabel(self, text=f"Welcome, [ADMIN] {admin.name}!")

    def grid(self, **kwargs):
        super().grid(**kwargs)
        self.label.grid()

class PunterFrame(ctk.CTkFrame):

    def __init__(self, master, punter: Punter, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.punter = punter

        self.name = ctk.CTkLabel(self, text=f"Welcome, {punter.name}!")
        self.bonoros = ctk.CTkLabel(self, text=f"Bonoros: ${punter.wallet.value_available}")
        self.profit = ctk.CTkLabel(self, text=f"Profit: ${punter.profit}")
        self.loss = ctk.CTkLabel(self, text=f"Loss: ${punter.loss}")

    def update(self):
        
        self.bonoros.configure(text=f"Bonoros: ${self.punter.wallet.value_available}")
        self.profit.configure(text=f"Profit: ${self.punter.profit}")
        self.loss.configure(text=f"Loss: ${self.punter.loss}")

    def grid(self, **kwargs):
        super().grid(**kwargs)
        self.name.grid()
        self.bonoros.grid()
        self.profit.grid()
        self.loss.grid()

class FighterFrame(ctk.CTkFrame):

    def __init__(self, master, fighter: Fighter, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.name = ctk.CTkLabel(self, text=f"Name: {fighter.name}", corner_radius=0)
        self.height = ctk.CTkLabel(self, text=f"Height: {fighter.height}", corner_radius=0)
        self.category = ctk.CTkLabel(self, text=f"Category: {fighter.category}", corner_radius=0)
        self.nationality = ctk.CTkLabel(self, text=f"Nationality: {fighter.nationality}", corner_radius=0)
        self.performance = ctk.CTkLabel(self, text=f"W {fighter.n_wins}/{fighter.n_loss} L", corner_radius=0)

    def grid(self, **kwargs):
        super().grid(**kwargs)
        self.name.grid(padx=5)
        self.height.grid(padx=5)
        self.category.grid(padx=5)
        self.nationality.grid(padx=5)
        self.performance.grid(padx=5)

class FightFrame(ctk.CTkFrame):

    def __init__(self, master, fight: Fight, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.name = ctk.CTkLabel(master=self, text=fight.name, corner_radius=0, font=ctk.CTkFont(size=40))

        self.container = ctk.CTkFrame(master=self)

        self.fA = FighterFrame(master=self.container,
                               fighter=fight.fA,
                               corner_radius=0)
        self.mfA = ctk.CTkLabel(master=self.container, text=f"Multiplier: {fight.oddA}", corner_radius=0)

        self.fB = FighterFrame(master=self.container, fighter=fight.fB, corner_radius=0)
        self.mfB = ctk.CTkLabel(master=self.container, text=f"Multiplier: {fight.oddB}", corner_radius=0)

        winner = fight.winner if fight.winner else "Waiting..."
        self.winner = ctk.CTkLabel(self, text=f"Winner: {winner}", corner_radius=0)

    def grid(self, **kwargs):
        super().grid(**kwargs)
        self.name.grid()
        self.container.grid(padx=5, pady=5)
        self.fA.grid(row=0, column=0, padx=5)
        self.mfA.grid(row=1, column=0, padx=5)
        self.fB.grid(row=0, column=1, padx=5)
        self.mfB.grid(row=1, column=1, padx=5)
        self.winner.grid()

class TransactionFrame(ctk.CTkFrame):

    def __init__(self, master, transaction: Transaction, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        ttype_str = 'Deposit' if transaction.ttype == Transaction.DEPOSIT else 'Withdraw'

        self.type = ctk.CTkLabel(self, text=f"Type: {ttype_str}")
        self.value = ctk.CTkLabel(self, text=f"Value: {transaction.value}")
        date_str = dt.datetime.fromtimestamp(transaction.timestamp).strftime("%Y/%m/%d")
        self.date = ctk.CTkLabel(self, text=f"Date: {date_str}")

    def grid(self, **kwargs):
        super().grid(**kwargs)
        self.type.grid(padx=5)
        self.value.grid(padx=5)
        self.date.grid(padx=5)

class BetFrame(ctk.CTkFrame):

    def __init__(self, master, bet: Bet, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        self.fight = FightFrame(self, bet.fight)
        self.description = ctk.CTkLabel(self,
                                        text=f"Investment: {bet.value}$ on {bet.winner.name}",
                                        font=ctk.CTkFont(size=25))

    def grid(self, **kwargs):
        super().grid(**kwargs)
        self.fight.grid(padx=5)
        self.description.grid(padx=5)
