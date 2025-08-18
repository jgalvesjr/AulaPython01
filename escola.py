nome_aluno = input("Informe o nome do aluno: ")
tipo_escola = input("Estuda em colécio: \n [1]Publico \n [2]Particular \n")
nota_1 = float(input("Digite a nota do 1 Bimestre: "))
nota_2 = float(input("Digite a nota do 2 Bimestre: "))
nota_3 = float(input("Digite a nota do 3 Bimestre: "))
nota_4 = float(input("Digite a nota do 4 Bimestre: "))
freq_aluno =  int(input("Qual a frequencia do aluno? "))
media_aluno = int((nota_1 + nota_2 + nota_3 + nota_4) / 4)

freq_corte = 70
media_corte = 7

'''
!= diferente
== igual
<= menor igual
>= maior igual
< menor
> maior
'''

if tipo_escola == "2":
    if media_aluno >= media_corte and freq_aluno >= freq_corte:
        resultado = "aprovado"
    else :
        resultado = "reprovado"
        
if tipo_escola == "1":
    if media_aluno >= media_corte or freq_aluno >= freq_corte:
        resultado = "aprovado"
    else :
        resultado = "reprovado"
        
if tipo_escola == "1":
    tipo = "Publica" 
    condicao = "ou"
else:
     tipo = "Particular"
     condicao = "e"
     
print(f"- Tipo: {tipo} \n- Frenquencia de corte: {freq_corte} \n- Condicao: {condicao} \n- Media de corte: {media_corte}")
print(f"Aluno {nome_aluno} com media de {media_aluno} {condicao} frequencia de {freq_aluno} foi {resultado} pela direção")