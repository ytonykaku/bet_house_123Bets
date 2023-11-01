
from models.Fight import Fight
from models.Fighter import Fighter


class Bet(object):

    def __init__(self, fight: Fight, winner: Fighter, value: float):
        self.value = value
        self.winner = winner
        self.fight = fight
