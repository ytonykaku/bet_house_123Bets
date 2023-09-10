from models.Punter import Punter
from models.User import User
from persistence.PunterPersistence import PunterPersistence


class PunterController():

    def __init__(self, persistence: PunterPersistence):
        self.persistence = persistence

    def get_from_user(self, user: User) -> Punter:
        # TODO: Load fields [profit, loss] from persistence.
        return Punter(name=user.name,
                      cpf=user.cpf,
                      email=user.email,
                      login=user.login,
                      uid=user.id,
                      wallet=None)

