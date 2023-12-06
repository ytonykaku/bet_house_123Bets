from persistence.DAO import DAO

from models.Fighter import Fighter


class FighterController(object):

    def __init__(self, persistence: DAO):
        self.persistence = persistence

    def create(self, f: Fighter):
        self.persistence.fighter.create(f)

    def fetch(self):
        return self.persistence.fighter.read()

    def fetch_by_name(self, name: str):
        fighters = self.persistence.fighter.read()
        return next(filter(lambda f: f.name == name, fighters), None)

    def delete(self, name: str):
        self.persistence.fighter.delete(name)
