from persistence.Persistence import Persistence

from models.Fighter import Fighter


class FighterController(object):

    def __init__(self, persistence: Persistence):
        self.persistence = persistence

    def create_fighter(self, f: Fighter):
        self.persistence.fighter.create_fighter(f)

    def fetch_fighters(self):
        return self.persistence.fighter.fetch_fighters()

    def fetch_fighter_by_name(self, name: str):
        return self.persistence.fighter.fetch_fighter_by_name(name)

    def delete_fighter_by_name(self, name: str):
        self.persistence.fighter.delete_by_name(name)
