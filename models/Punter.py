from models import User, Wallet

class Punter(User):

    def __init__(self,
                 name: str, cpf: str, email: str,
                 wallet: Wallet | None = None,
                 login: str = "",
                 password: str = "",
                 profit: float = 0.0,
                 loss: float = 0.0,
                 uid: int = 0):
        super().__init__(name=name, cpf=cpf, email=email,
                         login=login, password=password,
                         id=uid)
        self.profit = profit
        self.loss = loss
        self.wallet = wallet

    def __str__(self) -> str:
        return self.name

