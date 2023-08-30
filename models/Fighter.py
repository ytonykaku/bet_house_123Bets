class Fighter(object):
    def __init__(self,
                 name: str,
                 category: str,
                 height: float,
                 nacionality: str,
                 n_wins: int,
                 n_loss: int):
        self.name = name
        self.category = category
        self.height = height
        self.nacionality = nacionality
        self.n_wins = n_wins
        self.n_loss = n_loss

    def win(self):
        self.n_wins += 1

    def lose(self):
        self.n_loss += 1

    def __str__(self) -> str:
        return '{' \
               f' "name": "{self.name}", '\
               f' "category": "{self.category}", '\
               f' "height": {self.height}, '\
               f' "nacionality": "{self.nacionality}", '\
               f' "n_wins": {self.n_wins}, '\
               f' "n_loss": {self.n_loss} '\
               '}'

    def __repr__(self) -> str:
        return self.name

