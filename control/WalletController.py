from models.Wallet import Wallet

from persistence.DAO import DAO


class WalletController(object):

    def __init__(self, persistence: DAO):
        self.persistence = persistence
