from random import randint

# Jogo de advinhacao com diversos gatilhos

texto = '''
Difuculdade:
[1] Facil
[2] Intermediario
[3] Dificil
(ou digite facil \ intemediario \ dificil)
'''

#escolha = input('Escolha o nivel de jogo: ')



print('######### Inicio do Jogo #########')
print('--------- Adivinhe o Tesouro------')
print('--------- Feito por: Joao Alves --')
print('')

random = randint(0,100)
chute = 0
chances = 10
menor = 0
maior = 100

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