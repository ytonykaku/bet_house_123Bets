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

    def elevate(self, user: User) -> None:
        user.utype = 1
        self.persistence.user.update_utype(user)

    def depress(self, user: User) -> None:
        user.utype = 0
        self.persistence.user.update_utype(user)

    def fetch(self) -> list[User]:
        return self.persistence.user.read()

    def fetch_by_cpf(self, cpf: str) -> User:
        return filter(lambda user: user.cpf == cpf, self.persistence.user.read())

    def delete(self, u: User):
        self.persistence.user.delete(u)

    def has_money_or_bets(self, u: User):
        return self.persistence.wallet.get_by_id(id=u.id).value_available != 0.0

