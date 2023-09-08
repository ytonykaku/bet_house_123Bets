
class Wallet(object):

    def __init__(self,
                 value_available: float = 0.0, value_applied: float = 0.0,
                 pid: int = 0):
        self.value_available = value_available
        self.value_applied = value_applied
        self.id = pid

    def __str__(self) -> str:
        return '{' \
               f' "id": {self.id} ' \
               f' "value_available": {self.value_available},' \
               f' "value_applied": {self.value_applied} ' \
               '}'

