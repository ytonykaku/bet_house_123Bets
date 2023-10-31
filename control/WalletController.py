from models.Wallet import Wallet

from persistence.Persistence import Persistence


class WalletController(object):

    def __init__(self, persistence: Persistence):
        self.persistence = persistence
