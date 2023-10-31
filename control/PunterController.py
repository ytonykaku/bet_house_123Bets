import datetime as dt

from models.User import User
from models.Punter import Punter
from models.Transaction import Transaction

from persistence.Persistence import Persistence


class PunterController(object):

    def __init__(self, persistence: Persistence):
        self.persistence = persistence

    def get_from_user(self, user: User) -> Punter | None:
        punters = self.persistence.punter.read()
        p = next(filter(lambda p: p.cpf==user.cpf, punters), None)

        if p:
            transactions = self.persistence.transaction.read(p)

            transactions.sort(key=lambda t: t.timestamp, reverse=True)

            p.wallet.transactions.extend(transactions)

        return p

    def fetch_transactions(self, p: Punter) -> list[Transaction]:
        return self.persistence.transaction.fetch(p)

