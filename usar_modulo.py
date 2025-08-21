import operacoes
import meu_modulo

print(operacoes.somar(2,4))
print(meu_modulo.saudacao('Joao'))

try:
    print(operacoes.dividir(10,0))
except ValueError as e:
    print(f'Erro ao dividir por zero: {e}')