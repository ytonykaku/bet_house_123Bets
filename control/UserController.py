from models.User import User
from persistence.UserPersistence import UserPersistence


class UserController():

    def __init__(self, persistence: UserPersistence):
        self.persistence = persistence

    def authenticate(self, login: str, password: str) -> User | None:
        out = self.persistence.get_auth_info(login=login)

        if out is None:
            return None

        id, truth_password = out

        if password != truth_password:
            return None

        return self.persistence.get_by_id(id=id)


