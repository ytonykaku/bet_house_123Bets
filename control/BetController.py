from models.Bet import Bet
from models.Punter import Punter

from persistence.Persistence import Persistence


class BetController(object):

    def __init__(self, persistence: Persistence):
        self.persistence = persistence

    def create(self, p: Punter, b: Bet):
        self.persistence.bet.create(p, b)
        p.wallet.value_available -= b.value
        p.wallet.value_applied += b.value
        p.wallet.bets.append(b)

    def fetch_by_punter(self, p: Punter):
        bets = self.persistence.bet.read(p=p)
        return bets