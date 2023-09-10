from persistence.TransactionPersistence import TransactionPersistence


class TransactionController():

    def __init__(self, persistence: TransactionPersistence):
        self.persistence = persistence

