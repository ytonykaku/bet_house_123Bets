from models.User import User
from models.Admin import Admin

from persistence.UserPersistence import UserPersistence
from persistence.AdminPersistence import AdminPersistence
from persistence.WalletPersistence import WalletPersistence


class AdminController(object):

    def __init__(self,
                 admin_persistence: AdminPersistence,
                 user_persistence: UserPersistence,
                 wallet_persistence: WalletPersistence):
        self.admin_persistence = admin_persistence
        self.user_persistence = user_persistence
        self.wallet_persistence = wallet_persistence

    def get_from_user(self, user: User) -> Admin:
        return Admin(name=user.name,
                     cpf=user.cpf,
                     email=user.email,
                     login=user.login,
                     uid=user.id)

    def elevate_by_cpf(self, cpf: str) -> None:
        self.user_persistence.elevate_by_cpf(cpf=cpf)

    def depress_by_cpf(self, cpf: str) -> None:
        self.user_persistence.depress_by_cpf(cpf=cpf)

    def fetch_users(self) -> list[User]:
        return self.user_persistence.fetch_users()

    def fetch_user_by_cpf(self, cpf: str) -> User:
        return self.user_persistence.fetch_user_by_cpf(cpf)

    def delete_user(self, u: User):
        self.user_persistence.delete_by_id(id=u.id)

    def has_money_or_bets(self, u: User):
        return self.wallet_persistence.get_by_id(id=u.id).value_available != 0.0


