from models.User import User
from models.Admin import Admin

from persistence.AdminPersistence import AdminPersistence


class AdminController():

    def __init__(self, persistence: AdminPersistence):
        self.persistence = persistence

    def get_from_user(self, user: User) -> Admin:
        return Admin(name=user.name,
                     cpf=user.cpf,
                     email=user.email,
                     login=user.login,
                     uid=user.id)

