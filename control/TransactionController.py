from persistence.Persistence import Persistence


class TransactionController(object):

    def __init__(self, persistence: Persistence):
        self.persistence = persistence

