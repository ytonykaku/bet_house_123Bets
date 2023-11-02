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
                     password=user.password)

    def elevate(self, user: User) -> None:
        user.utype = 1
        self.persistence.user.update_utype(user)

    def depress(self, user: User) -> None:
        user.utype = 0
        self.persistence.user.update_utype(user)

    def fetch(self) -> list[User]:
        return self.persistence.user.read()

    def fetch_user_by_cpf(self, cpf: str) -> User:
        users = self.persistence.user.read()
        return next(filter(lambda u: u.cpf == cpf, users))

    def delete(self, u: User):
        self.persistence.user.delete(u)
