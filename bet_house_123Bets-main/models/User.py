

class User(object):

    def __init__(self,
                 name: str,
                 cpf: str,
                 email: str,
                 login: str,
                 password: str = "",
                 utype: int = 0,
                 id: int = 0):
        self.id = id
        self.name = name
        self.cpf = cpf
        self.email = email
        self.login = login
        self.password = password
        self.utype = utype

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

