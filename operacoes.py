def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError('Não e possivel dividir por 0') #levanta o erro, e inseri um valor no erro
    else:
        return a / b
