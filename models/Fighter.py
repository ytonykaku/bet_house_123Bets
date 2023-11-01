

class Fighter(object):
    def __init__(self,
                 name: str,
                 category: str,
                 height: float,
                 nationality: str,
                 n_wins: int,
                 n_loss: int):
        self.name = name
        self.category = category
        self.height = height
        self.nationality = nationality
        self.n_wins = n_wins
        self.n_loss = n_loss

    def __eq__(self, other):
        return self.name == other.name

