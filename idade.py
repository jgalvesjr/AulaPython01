from datetime import datetime
executar = True
dataCorrente = datetime.now()
anoCorrente = dataCorrente.year
while executar:
    try:    
        anoNasc = int(input('Em que ano voce nasceu? '))
        #anoAtual = int(input('Em que ano estamos? '))
        idade =  anoCorrente - anoNasc
        print(f'Voce tem: {idade} anos')
    except ValueError:
        print('Por favor, digite um numero valido para os anos')    
        
    opcao = input('\nDeseja testar novamente? \nSim ou Não? ').strip().lower() #strip tira espaços
    lista = ["não", "n", "nao"]
    if opcao in lista:
        executar = False    
    
    