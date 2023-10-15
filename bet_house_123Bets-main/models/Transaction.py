from models.Punter import Punter


class Transaction:
    DEPOSIT = 1
    WITHDRAW = 0

    def __init__(self, p: Punter, value: float, ttype: int, timestamp: float, id: int = 0):
        self.id = id
        self.owner = p
        self.value = value
        self.ttype = ttype
        self.timestamp = timestamp

    def __str__(self) -> str:
        return '{' \
               f' "id": "{self.id}", ' \
               f' "owner": "{self.owner}", ' \
               f' "value": "{self.value}", ' \
               f' "ttype": "{self.ttype}" ' \
               '}'

