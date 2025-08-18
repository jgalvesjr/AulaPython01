#aula 01 : Tipos de dados e variaveis

#--- strings (texto) ---------
nome = 'Joao'
curso = 'Python'
mensagem = 'Bem vindo ' + nome + ' ao curso de ' + curso

print(mensagem)

#vamos deixar o usario digitar o nome
nome_usuario = input('Digite o seu nome: ')
curso_usuario = input('Qual é o seu curso? ')

#Usando f-string (forma mais moderna de formatar string)
mensagem2 = f'Olá {nome_usuario}, seja bem vindo ao curso de {curso_usuario}'
print(mensagem2)

#Alguma funcoes uteis
print(nome_usuario.upper()) # Maiusculo
print(nome_usuario.lower()) #minusculo
print(nome_usuario.title()) #primeira letra de cada palavra em maiusculo

#tambem podemos repetir strings com o operador de multitplicação

linha = '-' * 20
print(linha)
print('Exercico concluido com sucesso')
print(linha)