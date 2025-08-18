# nome = input("Digite o nome do aluno: ")
# nota_1 = input("Digite a nota do 1 Bimestre: ")
# nota_2 = input("Digite a nota do 2 Bimestre: ")
# nota_3 = input("Digite a nota do 3 Bimestre: ")
# nota_4 = input("Digite a nota do 4 Bimestre: ")

# media = (float(nota_1) + float(nota_2) + float(nota_3) + float(nota_4)) / 4

# print(f'A média final do aluno {nome} é {media}')

nome = input("Digite o nome do aluno: ")
nota_1 = float(input("Digite a nota do 1 Bimestre: "))
nota_2 = float(input("Digite a nota do 2 Bimestre: "))
nota_3 = float(input("Digite a nota do 3 Bimestre: "))
nota_4 = float(input("Digite a nota do 4 Bimestre: "))

media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

print(f'A média final do aluno {nome} é {media}')