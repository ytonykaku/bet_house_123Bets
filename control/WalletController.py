from models.Wallet import Wallet

from persistence.Persistence import Persistence


class WalletController(object):

    def __init__(self, persistence: Persistence):
        self.persistence = persistence

    def get_by_id(self, id: int) -> Wallet:
        return self.persistence.wallet.get_by_id(id)

