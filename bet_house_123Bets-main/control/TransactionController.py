from persistence.TransactionPersistence import TransactionPersistence


class TransactionController(object):

    def __init__(self, persistence: TransactionPersistence):
        self.persistence = persistence

