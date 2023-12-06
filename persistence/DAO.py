
from persistence.UserDAO import UserDAO
from persistence.AdminDAO import AdminDAO
from persistence.PunterDAO import PunterDAO
from persistence.BetDAO import BetDAO
from persistence.TransactionDAO import TransactionDAO
from persistence.WalletDAO import WalletDAO
from persistence.FighterDAO import FighterDAO
from persistence.FightDAO import FightDAO


class DAO(object):

    def __init__(self,
                 user: UserDAO,
                 admin: AdminDAO,
                 punter: PunterDAO,
                 bet: BetDAO,
                 transaction: TransactionDAO,
                 wallet: WalletDAO,
                 fighter: FighterDAO,
                 fight: FightDAO):
         self.user = user
         self.admin = admin
         self.punter = punter
         self.bet = bet
         self.transaction = transaction
         self.wallet = wallet
         self.fighter = fighter
         self.fight = fight

