from models.User import User
from models.Admin import Admin

from persistence.AdminPersistence import AdminPersistence

from persistence.UserPersistence import UserPersistence

class AdminController(object):

    def __init__(self, admin_persistence: AdminPersistence, user_persistence: UserPersistence):
        self.admin_persistence = admin_persistence
        self.user_persistence = user_persistence

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


