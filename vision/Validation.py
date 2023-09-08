def validarCpf(cpf):
    if not cpf:
        raise ValueError("CPF não pode estar vazio")

    cpf = cpf.replace(".", "").replace("-", "")

    if not cpf.isdigit():
        raise ValueError("CPF deve conter apenas dígitos")

    if len(cpf) != 11:
        raise ValueError("CPF deve conter 11 dígitos")

    return cpf

def validarValor(valor):
    if not valor:
        raise ValueError("O valor não pode estar vazio")

    valor = valor.strip()

    if not all(char.isdigit() or char in ('.', ',') for char in valor):
        raise ValueError("O valor deve conter apenas dígitos, ponto decimal ou vírgula")

    valor = valor.replace(",", ".")

    try:
        valor_decimal = float(valor)
    except ValueError:
        raise ValueError("O valor não é um número decimal válido")

    return valor_decimal

def validarVazio(entrada):
    if not entrada:
        raise ValueError("não pode estar vazio")

    return entrada