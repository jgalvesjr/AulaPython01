def minhaFuncao():
    print('Ola pessoal')

minhaFuncao()
minhaFuncao()

cidades = ['Sao Paulo', 'Osasco', 'Cotia', 'Carapicuiba']
cidades2 = ['Suzano', 'Mogi', 'Diadema', 'Maua']
contador = 0

def minhaFuncaoMelhorada(local, giro):
    print(str(giro) + ' - ' + local)
    
for cidade in cidades:
    contador += 1
    minhaFuncaoMelhorada(cidade, contador)

for cidade in cidades2:
    contador += 1
    minhaFuncaoMelhorada(cidade, contador)