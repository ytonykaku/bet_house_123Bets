from models import User, Wallet, Punter, Admin


def callMenu():
    print('--- Bem vindo a Bet House APS ---')
    print(f'Lembre-se: apostas são apenas para entretenimento, seja consciente!')
    print(f'-------------------------------------------------')
    print(f'1 - Cadastrar usuario')
    print(f'2 - Realizar Login')
    print(f'3 - Visualizar apostas em andamento')
    print(f'4 - Visualizar apostas encerradas')
    print(f'0 - Sair')
#inserir lista de usuarios na funcao callUserMenu    
def callUserMenu(usersList: list, login):
    print('--- Bem vindo ao menu de usuários ---')
    print(f'Lembre-se: apostas são apenas para entretenimento, seja consciente!')
    for user in usersList:
        if user.login == login:
            name = user.name
            balance = user.wallet.value_available
    print(f'Nome: ', name, 'Saldo: ', balance)
    print(f'1 - Visualizar Apostas')
    print(f'2 - Depositar dinhheiro')
    print(f'3 - Sacar dinheiro')
    print(f'4 - ')
    print(f'0 - Sair')

def callLogin(login: str, password: str, usersList):
    for loggins in usersList:
        if login == loggins.login and password == loggins.password:
            print(f'Usuario', login, 'logado com sucesso')
            return True
        else:
            print('Usuario ou senha incorretos')
            return False

def addUser(name: str, cpf: str,
                 login: str, password: str,
                 permissions: int, punterList: list):
    for user in usersList:
        if user.cpf == cpf:
            print('Usuario ja cadastrado')
            return None
    else: 
        usersList.append(User(name, cpf, login, password, permissions))
        print('Usuario adicionado')
        return None

def addFighter(name: str,
                 category: str,
                 height: float,
                 nationality: str,
                 n_wins: int,
                 n_loss: int,
                 fighterList: list): 
    if name and category in fighterList:
        print('Lutador ja cadastrado')
        return None
    else: 
        fighterList.append(Fighter(name, category, nationa))
        print('Lutador adicionado')
        return None


def add_punter(self, wallet: Wallet) -> None:
    self.wallet = wallet