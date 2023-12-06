from persistence.DAO import DAO

from models.Fight import Fight
from models.Fighter import Fighter


class FightController(object):

    def __init__(self, persistence: DAO):
        self.persistence = persistence

    def create(self, f: Fight):
        self.persistence.fight.create(f)

    def read(self):
        return self.persistence.fight.read()

    def delete(self, fight: Fight):
        self.persistence.fight.delete(fight)

    def declare_winner(self, fight: Fight, fighter: Fighter):
        self.persistence.fight.declare_winner(fight, fighter)
