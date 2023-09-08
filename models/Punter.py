from models import User, Wallet

class Punter(User):

    def __init__(self,
                 name: str, cpf: str, wallet: Wallet,
                 login: str = "", password: str = "",
                 profit: float = 0.0, loss: float = 0.0,
                 uid: int = 0):
        super().__init__(name, cpf, login, password, uid)
        self.profit = profit
        self.loss = loss
        self.wallet = wallet

    def add_profit(self, value: float) -> None:
        self.profit += value

    def add_loss(self, value: float) -> None:
        self.loss += value

    def __str__(self) -> str:
        return '{' \
               f' "name": "{self.name}", '\
               f' "cpf": "{self.cpf}", '\
               f' "login": "{self.login}", '\
               f' "password": "{self.password}", '\
               f' "profit": {self.profit}, '\
               f' "loss": {self.loss} '\
               '}'

