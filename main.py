import datetime as dt
from models.Operations import addUser
from models.Operations import callMenu
from models.Operations import callLogin
from models.Operations import callUserMenu


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
             nationality="USA",
             n_wins=0, n_loss=0)

fB = Fighter(name="Windersson Nunes",
             category="lightweight",
             height=1.78,
             nationality="BR",
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

# implementando o menu

usersList = []
action = 1
counter = 0
while(1):
    if counter <= 1:
        callMenu()
    action = input()
    counter += 1
    if action == '1':
        print(f'Digite o seu nome')
        name = input()
        print(f'Digite o seu CPF')
        cpf = input()
        print(f'Digite o seu login')
        login = input()
        print(f'Digite a sua senha')
        password = input()
        addUser(name, cpf, login, password, '0', usersList)
    elif action == '2':
        print(f'Digite o seu login')
        login = input()
        print(f'Digite sua senha')
        password = input()
        didLogin = callLogin(login, password, usersList)
        if didLogin == True:
            callUserMenu(usersList, login)