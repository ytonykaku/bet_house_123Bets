from persistence.Persistence import Persistence

from models.Fight import Fight
from models.Fighter import Fighter


class FightController(object):

    def __init__(self, persistence: Persistence):
        self.persistence = persistence

    def create_fight(self, f: Fight):
        self.persistence.fight.create_fight(f)

    def fetch_fights(self):
        return self.persistence.fight.fetch_fights()

    def declare_winner(self, fight: Fight, fighter: Fighter):
        self.persistence.fight.declare_winner(fight, fighter)

    def delete(self, fight: Fight):
        self.persistence.fight.delete(fight)
