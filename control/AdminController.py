from models.User import User
from models.Admin import Admin

from persistence.Persistence import Persistence


class AdminController(object):

    def __init__(self, persistence: Persistence):
        self.persistence = persistence

    def get_from_user(self, user: User) -> Admin:
        return Admin(name=user.name,
                     cpf=user.cpf,
                     email=user.email,
                     login=user.login,
                     uid=user.id)

    def elevate_by_cpf(self, cpf: str) -> None:
        self.persistence.user.elevate_by_cpf(cpf=cpf)

    def depress_by_cpf(self, cpf: str) -> None:
        self.persistence.user.depress_by_cpf(cpf=cpf)

    def fetch_users(self) -> list[User]:
        return self.persistence.user.fetch_users()

    def fetch_user_by_cpf(self, cpf: str) -> User:
        return self.persistence.user.fetch_user_by_cpf(cpf)

    def delete_user(self, u: User):
        self.persistence.user.delete_by_id(id=u.id)

    def has_money_or_bets(self, u: User):
        return self.persistence.wallet.get_by_id(id=u.id).value_available != 0.0

