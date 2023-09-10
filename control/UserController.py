from models.User import User
from models.Admin import Admin
from models.Punter import Punter
from models.Wallet import Wallet

from persistence.UserPersistence import UserPersistence
from persistence.AdminPersistence import AdminPersistence
from persistence.PunterPersistence import PunterPersistence
from persistence.WalletPersistence import WalletPersistence


class UserController(object):

    def __init__(self,
                 user_persistence: UserPersistence,
                 punter_persistence: PunterPersistence,
                 wallet_persistence: WalletPersistence,
                 admin_persistence: AdminPersistence):
        self.user_persistence = user_persistence
        self.admin_persistence = admin_persistence
        self.punter_persistence = punter_persistence
        self.wallet_persistence = wallet_persistence

    def authenticate(self, login: str, password: str) -> User | None:
        out = self.user_persistence.get_auth_info(login=login)

        if out is None:
            return None

        id, truth_password = out

        if password != truth_password:
            return None

        return self.user_persistence.get_by_id(id=id)

    def register(self, u: User):
        self.user_persistence.insert(u)

        match u.utype:
            case 0:
                w = Wallet()
                p = Punter(name=u.name, cpf=u.cpf, login=u.login, password=u.password, email=u.email, wallet=w, uid=u.id)

                self.punter_persistence.insert(p)
                self.wallet_persistence.insert(w)
            case 1:
                a = Admin(name=u.name, cpf=u.cpf, login=u.login, password=u.password, email=u.email, uid=u.id)
                self.admin_persistence.insert(a)

