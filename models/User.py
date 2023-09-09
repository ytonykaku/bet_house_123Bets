# import argon2 as a2
# Queria adicionar hash nas senhas mas vou focar em coisas mais importantes antes de mexer nisso

class User(object):

    def __init__(self,
                 name: str, cpf: str, email: str,
                 login: str, password: str = "",
                 permissions: int = 0, id: int = 0):
        self.id = id
        self.name = name
        self.cpf = cpf
        self.email = email
        self.login = login
        self.password = password
        self.permissions = permissions

    def __str__(self) -> str:
        return '{' \
               f' "name": "{self.name}", '\
               f' "cpf": "{self.cpf}", '\
               f' "login": "{self.login}", '\
               f' "email": "{self.email}" '\
               '}'

    def __repr__(self) -> str:
        return self.name
