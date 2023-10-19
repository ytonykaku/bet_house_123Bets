from models.Bet import Bet

from persistence.Persistence import Persistence


class BetController(object):

    def __init__(self, persistence: Persistence):
        self.persistence = persistence
