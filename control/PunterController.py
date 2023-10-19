import datetime as dt

from models.User import User
from models.Punter import Punter
from models.Transaction import Transaction

from persistence.Persistence import Persistence


class PunterController(object):

    def __init__(self, persistence: Persistence):
        self.persistence = persistence

    def get_from_user(self, user: User) -> Punter:
        w = self.persistence.wallet.get_by_id(user.id)

        p = Punter(name=user.name,
                   cpf=user.cpf,
                   email=user.email,
                   login=user.login,
                   uid=user.id,
                   wallet=w)

        self.persistence.punter.get_profit_and_loss(p)

        return p

    def deposit(self, p: Punter, value: float):
        t = Transaction(p, value, Transaction.DEPOSIT, dt.datetime.now().timestamp())
        self.persistence.wallet.deposit(p.wallet, value)
        self.persistence.transaction.insert(t)

    def withdraw(self, p: Punter, value: float):
        t = Transaction(p, value, Transaction.WITHDRAW, dt.datetime.now().timestamp())
        self.persistence.wallet.withdraw(p.wallet, value)
        self.persistence.transaction.insert(t)

    def fetch_transactions(self, p: Punter) -> list[Transaction]:
        return self.persistence.transaction.fetch(p)

