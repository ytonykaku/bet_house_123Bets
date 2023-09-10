from models.Wallet import Wallet

from persistence.WalletPersistence import WalletPersistence


class WalletController:

    def __init__(self, persistence: WalletPersistence):
        self.persistence = persistence

    def get_wallet_by_id(self, id: int) -> Wallet:
        return self.persistence.get_by_id(id)

