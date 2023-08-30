import datetime as dt

from models import *

adm = Admin(name="Henrique", cpf="12345678910",
            login="hott-henrique", password="password")

p = Punter(name="Henrique", cpf="12345678910",
           login="hott-henrique", password="password",
           profit=0.0, loss=0.0)

w = Wallet(value_available=250.0, value_applied=0.0, owner=p)

p.set_wallet(w)

fA = Fighter(name="Dumb M. F.",
             category="lightweight",
             height=1.50,
             nacionality="USA",
             n_wins=0, n_loss=0)

fB = Fighter(name="Windersson Nunes",
             category="lightweight",
             height=1.78,
             nacionality="BR",
             n_wins=0, n_loss=0)

f = Fight(date=dt.datetime.now().timestamp(),
          fA=fA, oddA=0.0,
          fB=fB, oddB=1.0)

b = Bet(value=100.0, date=dt.datetime.now().timestamp(), wallet=w, winner='B', fight=f)

w.add_investment(b)

f.add_bet(b)

print(f"Punter: {p}")
print(f"Wallet: {w}")
print(f"Bet: {b}")
print(f"Fighter A: {fA}")
print(f"Fighter B: {fB}")
print(f"Fight: {f}")

f.set_winner('A')

print("---------x----------")

print(f"Punter: {p}")
print(f"Wallet: {w}")
print(f"Bet: {b}")
print(f"Fighter A: {fA}")
print(f"Fighter B: {fB}")
print(f"Fight: {f}")

