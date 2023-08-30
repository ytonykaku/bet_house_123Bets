from models import User, Wallet

class Punter(User):

    def __init__(self,
                 name: str, cpf: int,
                 login: str, password: str,
                 profit: float, loss: float):
        super().__init__(name, cpf, login, password, 0)
        self.profit = profit
        self.loss = loss
        self.wallet = None

    def add_profit(self, value: float) -> None:
        self.profit += value

    def add_loss(self, value: float) -> None:
        self.loss += value

    def set_wallet(self, wallet: Wallet) -> None:
        self.wallet = wallet

    def __str__(self) -> str:
        return '{' \
               f' "name": "{self.name}", '\
               f' "cpf": "{self.cpf}", '\
               f' "login": "{self.login}", '\
               f' "password": "{self.password}", '\
               f' "profit": {self.profit}, '\
               f' "loss": {self.loss} '\
               '}'

