from persistence.WalletPersistence import WalletPersistence


class WalletController:

    def __init__(self, persistence: WalletPersistence):
        self.persistence = persistence

