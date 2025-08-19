def divisao(a, b):
    try: # tenta efetuar a drivisao
        resultado = a / b
        print(f'Resultado da divisao de {a} por {b} é: {resultado}')
    except ZeroDivisionError:
        # Se houver um erro de divisao por zero o codigo entra dentro do execpe e é executado
        print('Erro: Não é possivel dividor por zero')
    except TypeError:
        # Caso algum valor naos eja um numero, esse except sera executado
        print('Erro: Ambos os valores precisam ser numero.')
    except Exception as e: #e pode ser qq coisa 
        #captura qq outro erro que não tenho sido tratado os anteriores
        print(f'Erro inesperado: {e}')
    else: # se der sucesso no bloco try ele executa o else (sem erros)
        print('Operacao realizado com sucesso!')
    finally: #Sempre sera executado se sucesso ou erro
        print('Processo de divisao finalizado')

# teste 01 - Divisao normal
divisao(10, 2)
# teste 02 - Divisao por zero
divisao(10, 0)
# teste 03 - Divisao por tipos invalidos
divisao(10, 'dois')
# teste 04 - Divisao com erro inesperado
divisao(0, 'dois')