palavra = "tangamandapio"
contator = 0

for letra in palavra:
    print(str(contator) + " - " + letra)
    contator += 1
 
cidades = ['Sao Paulo', 'Osasco', 'Cotia', 'Carapicuiba']

for cidade in cidades:
    print(cidade)
    
print("")
print(cidades[0])


print("----- While -------")
botao_executar = True #boleano ligado ou desligado true/false
contador = 0

while botao_executar:
   print(contador)
   contador += 1 
   if contador >= 10:
       botao_executar = False
print("Fim do looping")

