from control.UserController import UserController
from control.AdminController import AdminController
from control.PunterController import PunterController
from control.BetController import BetController
from control.TransactionController import TransactionController
from control.WalletController import WalletController
from control.FighterController import FighterController
from control.FightController import FightController


class Controller(object):

    def __init__(self,
                 user: UserController,
                 admin: AdminController,
                 punter: PunterController,
                 bet: BetController,
                 transaction: TransactionController,
                 wallet: WalletController,
                 fighter: FighterController,
                 fight: FightController):
         self.user = user
         self.admin = admin
         self.punter = punter
         self.bet = bet
         self.transaction = transaction
         self.wallet = wallet
         self.fighter = fighter
         self.fight = fight
