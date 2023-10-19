from persistence.Persistence import Persistence


class InvestmentController(object):

    def __init__(self, persistence: Persistence):
        self.persistence = persistence

