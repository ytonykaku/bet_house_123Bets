from models.Punter import Punter
from models.User import User

from persistence.PunterPersistence import PunterPersistence


class PunterController(object):

    def __init__(self, persistence: PunterPersistence):
        self.persistence = persistence

    def get_from_user(self, user: User) -> Punter:
        p = Punter(name=user.name,
                   cpf=user.cpf,
                   email=user.email,
                   login=user.login,
                   uid=user.id,
                   wallet=None)

        self.persistence.get_profit_and_loss(p)

        return p

