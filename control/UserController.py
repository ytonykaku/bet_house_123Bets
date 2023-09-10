from models.User import User
from persistence.UserPersistence import UserPersistence


class UserController():

    def __init__(self, persistence: UserPersistence):
        self.persistence = persistence

    def authenticate(self, login: str, password: str) -> User | None:
        id, truth_password = self.persistence.get_auth_info(login=login)

        if password == truth_password:
            return User("Test", "0x0", "example@email.com", login=login, id=id)

        return None

