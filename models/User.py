# import argon2 as a2
# Queria adicionar hash nas senhas mas vou focar em coisas mais importantes antes de mexer nisso

class User(object):

    def __init__(self,
                 name: str, cpf: str,
                 login: str, password: str,
                 permissions: int):
        # TODO: Perform checking.
        self.name = name
        self.login = login
        self.password = password
        self.permissions = permissions
        self.cpf = cpf

    def __str__(self) -> str:
        return '{' \
               f' "name": "{self.name}", '\
               f' "cpf": "{self.cpf}", '\
               f' "login": "{self.login}", '\
               f' "password": "{self.password}" '\
               '}'

    def __repr__(self) -> str:
        return self.name
