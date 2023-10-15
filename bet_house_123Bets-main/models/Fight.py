from models import Fighter, Bet

class Fight(object):


    def add_bet(self, bet: Bet) -> None:
        self.bets.append(bet)

    def add_bets(self, bets: list[Bet]) -> None:
        self.bets.extend(bets)

    def get_winner_odd(self) -> float:
        if self.winner == "UNKNOWN":
            raise Exception("Figh do not have a winner yet.")

        if self.winner == 'A':
            return self.oddA

        if self.winner == 'B':
            return self.oddB

        raise Exception(f"Unknow winner: {self.winner}")

    def set_winner(self, winner: str) -> None:
        if winner not in [ 'A', 'B' ]:
            raise Exception(f"Unknow fighter: {winner}")

        self.winner = winner

        loser_as_figher, winner_as_figher = (self.fB, self.fA) if self.winner == 'A' else (self.fB, self.fB)

        winner_as_figher.win()
        loser_as_figher.lose()

        for b in self.bets:
            if b.winner == self.winner:
                b.pay()
            else:
                b.collect()

    def __str__(self) -> str:
        return '{' \
               f' "date": {self.date}, '\
               f' "fA": "{repr(self.fA)}", ' \
               f' "oddA": {self.oddA}, '\
               f' "fB": "{repr(self.fB)}", ' \
               f' "oddB": {self.oddB}, '\
               f' "winner": {self.winner}, '\
               f' "bets": {len(self.bets)} '\
               '}'

    def __repr__(self) -> str:
        return f"{repr(self.fA)} x {repr(self.fB)}"

