from models.Wallet import Wallet
from models.Fight import Fight


class Bet(object):
    id_counter = 0

    def __init__(self, value: float, date: float, wallet: Wallet, winner: str, fight: Fight, id: int = 0):
        self.wallet = wallet
        self.value = value
        self.date = date
        self.winner = winner
        self.fight = fight
        self.odd = None

        if id:
            self.id = id
        else:
            Bet.id_counter = Bet.id_counter + 1
            self.id = Bet.id_counter

    def __eq__(self, other) -> bool:
        return self.id == other.id

    def __str__(self) -> str:
        return '{' \
               f' "wallet": {repr(self.wallet)}, ' \
               f' "value": {self.value}, '\
               f' "date": {self.date}, '\
               f' "winner": "{self.winner}", '\
               f' "fight": "{repr(self.fight)}" '\
               '}'

    def __repr__(self) -> str:
        return '{' \
               f' "value": {self.value}, '\
               f' "fight": "{repr(self.fight)}" '\
               '}'

