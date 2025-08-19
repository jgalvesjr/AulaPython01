from random import randint
# Jogo de advinhacao com diversos gatilhos

escolhas = '''
Difuculdade:
[1] Facil
[2] Intermediario
[3] Dificil
[4] Sair
(ou digite facil \ intemediario \ dificil \ sair)
'''

print('######### Inicio do Jogo #########')
print('--------- Adivinhe o Tesouro------')
print('--------- Feito por: Joao Alves --')
print('')

dificuldade = input('Escolha o seu nivel de diculdade (facil/medio/dificil)').strip().lower()

if dificuldade == 'facil':
    mmenor = 0
    maior = 100
    chances = 10
elif dificuldade == 'medio':
    menor = 0
    maior = 200
    chances = 15
else:
    menor = 0
    maior = 1000
    chances = 20

random = randint(menor,maior)
chute = 0


print(f'Que os jogos comecem!!!\nVoce tem {chances} chances para acertar\nPense com cuidado!!!')
#while chute != random:
while chances >= 0:
    chute = input(f'Digite um numero entre {menor} e {maior}: ')
    if chute.isnumeric():
        chute =int(chute)
        chances -= 1
        if chute == random:
            print('')
            #print(f'Parabens voce venceu, o numero era {random} e voce ainda tinha {chances}')
            print('Parabens voce venceu, o numero era {} e voce ainda tinha {} tentativas'.format(random, chances))
            print('')
            break
        else: #poderia colcoar um if abaixo fora do else, porém irei testar de novo
            if chute > random:
                print(f'O numero é menor que {chute}. ')
            else:
                print(f'O numero é maior que {chute}.')
                
            print(f'Voce possui mais {chances} tentativas!!!')
            print('')
        if chances == 0:
            print('')
            print('Suas chances acabaram, voce perdeu')
            print(f'O valor esperado era {random}')
            print('')
            break

print('######### Fim de Jogo #############')
print('######### Obriado por jogar  ######')