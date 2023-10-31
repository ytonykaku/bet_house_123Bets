from models.Transaction import Transaction


class Wallet(object):

    def __init__(self,
                 cpf_owner: str,
                 value_available: float,
                 value_applied: float):
        self.cpf_owner = cpf_owner
        self.value_available = value_available
        self.value_applied = value_applied
        self.transactions: list[Transaction] = list()
