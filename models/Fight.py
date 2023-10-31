from models import Fighter

class Fight(object):

    def __init__(self, fA: Fighter, oddA: float, fB: Fighter, oddB: float, winner: str = None):
        self.fA = fA
        self.oddA = oddA
        self.fB = fB
        self.oddB = oddB
        self.winner = winner
