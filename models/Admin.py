from models import User

class Admin(User):

    def __init__(self,
                 name: str, cpf: str,
                 login: str, password: str):
        super().__init__(name, cpf, login, password, 1)

