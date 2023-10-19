
from persistence.UserPersistence import UserPersistence
from persistence.AdminPersistence import AdminPersistence
from persistence.PunterPersistence import PunterPersistence
from persistence.BetPersistence import BetPersistence
from persistence.TransactionPersistence import TransactionPersistence
from persistence.WalletPersistence import WalletPersistence
from persistence.InvestmentPersistence import InvestmentPersistence
from persistence.FighterPersistence import FighterPersistence
from persistence.FightPersistence import FightPersistence


class Persistence(object):

    def __init__(self,
                 user: UserPersistence,
                 admin: AdminPersistence,
                 punter: PunterPersistence,
                 bet: BetPersistence,
                 transaction: TransactionPersistence,
                 wallet: WalletPersistence,
                 investment: InvestmentPersistence,
                 fighter: FighterPersistence,
                 fight: FightPersistence):
         self.user = user
         self.admin = admin
         self.punter = punter
         self.bet = bet
         self.transaction = transaction
         self.wallet = wallet
         self.investment = investment
         self.fighter = fighter
         self.fight = fight

