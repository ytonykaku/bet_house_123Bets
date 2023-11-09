from models.User import User
from persistence.Persistence import Persistence


class UserController(object):

    def __init__(self, persistence: Persistence):
        self.persistence = persistence

    def authenticate(self, login: str, password: str) -> User | None:
        users = self.persistence.user.read()
        return next(filter(lambda u: u.login == login and u.password == password, users), None)

    def register(self, u: User):
        self.persistence.user.insert(u)

    def update(self, u: User):
        self.persistence.user.update(u)
