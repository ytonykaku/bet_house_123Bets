from persistence.Persistence import Persistence

from models.Transaction import Transaction
from models.Wallet import Wallet

class TransactionController(object):

    def __init__(self, persistence: Persistence):
        self.persistence = persistence

    def create(self, wallet: Wallet, transaction: Transaction):
        self.persistence.transaction.insert(wallet, transaction)
        wallet.value_available += transaction.value if transaction.ttype == Transaction.DEPOSIT else -transaction.value
