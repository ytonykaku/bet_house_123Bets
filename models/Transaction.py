class Transaction:
    DEPOSIT = 1
    WITHDRAW = 0

    def __init__(self, value: float, ttype: int, timestamp: float):
        self.value = value
        self.ttype = ttype
        self.timestamp = timestamp
