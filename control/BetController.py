from models.Bet import Bet

from persistence.BetPersistence import BetPersistence


class BetController(object):

    def __init__(self, persistence: BetPersistence):
        self.persistence = persistence