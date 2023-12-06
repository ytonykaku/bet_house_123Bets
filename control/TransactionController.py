from persistence.DAO import DAO

from models.Transaction import Transaction
from models.Wallet import Wallet

class TransactionController(object):

    def __init__(self, persistence: DAO):
        self.persistence = persistence

    def create(self, wallet: Wallet, transaction: Transaction):
        self.persistence.transaction.create(wallet, transaction)
        wallet.value_available += transaction.value if transaction.ttype == Transaction.DEPOSIT else -transaction.value
        wallet.transactions.insert(0, transaction)
