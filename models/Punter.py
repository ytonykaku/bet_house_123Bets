from models import User, Wallet

class Punter(User):

    def __init__(self,
                 name: str,
                 cpf: str,
                 email: str,
                 login: str = "",
                 password: str = "",
                 wallet: Wallet | None = None,
                 profit: float = 0.0,
                 loss: float = 0.0):
        super().__init__(name=name,
                         cpf=cpf,
                         email=email,
                         login=login,
                         password=password)
        self.wallet = wallet
        self.profit = profit
        self.loss = loss

