# calcular o quanto o cliente deve receber de troco

valor_compra = float(input('Qual o valor da compra? R$ '))
valor_pago = float(input('Valor pago pelo cliente: R$' ))

troco =  valor_pago - valor_compra

print(f'Troco: R$ {troco:.2f}') #:.2f - duas casas decimais 