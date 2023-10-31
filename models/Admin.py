from models import User


class Admin(User):

    def __init__(self,
                 name: str,
                 cpf: str,
                 email:str,
                 login: str,
                 password: str):
        super().__init__(name=name,
                         cpf=cpf,
                         email=email,
                         login=login,
                         password=password,
                         utype=1)

