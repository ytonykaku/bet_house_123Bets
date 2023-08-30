from models import Bet, Punter

class Wallet(object):

    def __init__(self,
                 value_available: float, value_applied: float,
                 owner: Punter, investments: list[Bet] = list()):
        self.value_available = value_available
        self.value_applied = value_applied
        self.owner = owner
        self.investments = investments

    def add_investment(self, bet: Bet) -> None:
        if bet not in self.investments:
            self.investments.append(bet)

    def pay_bet(self, bet: Bet) -> None:
        bet = self.investments.pop(self.investments.index(bet))
        profit = bet.fight.get_winner_odd() * bet.value
        self.value_available += bet.value + profit
        self.owner.add_profit(profit)

    def collect_bet(self, bet: Bet) -> None:
        bet = self.investments.pop(self.investments.index(bet))
        self.value_available -= bet.value
        self.owner.add_loss(bet.value)

    def __str__(self) -> str:
        return '{' \
               f' "owner": "{repr(self.owner)}",' \
               f' "investments": {repr(self.investments)},' \
               f' "value_available": {self.value_available},' \
               f' "value_applied": {self.value_applied} ' \
               '}'

    def __repr__(self) -> str:
        return '{' \
               f' "owner": "{repr(self.owner)}" ' \
               '}'

