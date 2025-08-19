executar = True
def decisao():
    global executar #alterar globalmente não somente dentro da funcao
    repetir = input('Deseja realizar outra conta? ').strip().lower()
    if repetir == '1' or repetir == 'nao':
        executar = False
        
while executar:
    escolhas = '''
    [1] ou [+] para Somar
    [2] ou [-] para Subtrair
    [3] ou [/] para Dividir
    [4] ou [*] para Multiplicar
    [5] para Sair
    (ou digite sua opção somar / subtrair / multiplicar / dividir / sair)
    '''
    
    print(escolhas)
    operador = input('Qual sua opção?: ').strip().lower()
    if operador == '5' or operador == 'sair':
        print('Saindo da calculadora. Orbigado por utilizar!')
        print('----------------- Fim do sistema -----------------------')
        break
    
    valor01 = int(input('Escolha seu primeiro valor: '))
    valor02 = int(input('Escolha seu segundo valor: '))
    
    textinho = '''
    [1] Não, desejo sair! 
    [2] Sim, desejo realizar outro calculo
    (ou digite sim / não)
    '''
    
    # ----------- opercao de soma --------------
    if operador == '1' or operador == '+' or operador == 'somar':
        resultado = valor01 + valor02
        print(f'Resultado é: {resultado}' )
        print(textinho) 
        decisao()
        
    # ----------- opercao de subtracao --------------
    if operador == '2' or operador == '-' or operador == 'subtrair':
        resultado = valor01 - valor02
        print(f'Resultado é: {resultado}' )
        print(textinho) 
        decisao()
        
    # ----------- opercao de dividir --------------
    if operador == '3' or operador == '/' or operador == 'dividir':
        if valor02 == 0:
            print('Divisao por 0 nao e permitida')
        else:
            resultado = valor01 / valor02
            print(f'Resultado é: {resultado}' )
        print(textinho) 
        decisao()
    
    # ----------- opercao de multiplicar --------------
    if operador == '4' or operador == '*' or operador == 'multiplicar':
        resultado = valor01 * valor02
        print(f'Resultado é: {resultado}' )
        print(textinho) 
        decisao()    
    
        #se repete em todas as tarefas criar funcao
        # repetir = input('Deseja realizar outra conta? ')c
        # if repetir == '1' or repetir == 'nao':
        #     executar = False