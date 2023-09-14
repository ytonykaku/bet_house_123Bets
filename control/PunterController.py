from models.Punter import Punter
from models.User import User

from persistence.PunterPersistence import PunterPersistence
from persistence.TransactionPersistence import TransactionPersistence
from persistence.WalletPersistence import WalletPersistence


class PunterController(object):

    def __init__(self,
                 punter_persistence: PunterPersistence,
                 wallet_persistence: WalletPersistence,
                 transaction_persistence: TransactionPersistence):
        self.punter_persistence = punter_persistence
        self.wallet_persistence = wallet_persistence
        self.transaction_persistence = transaction_persistence

    def get_from_user(self, user: User) -> Punter:
        p = Punter(name=user.name,
                   cpf=user.cpf,
                   email=user.email,
                   login=user.login,
                   uid=user.id,
                   wallet=None)

        self.punter_persistence.get_profit_and_loss(p)

        return p

