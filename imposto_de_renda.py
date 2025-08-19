def calculadoraIr(salarioBruto):
    tabelaIr = [
        {'faixa':(0,1903.98),'aliquota':0, 'deducao':0},
        {'faixa':(1903.99,2826.65),'aliquota':7.5, 'deducao':142.80},
        {'faixa':(2826.66,3751.05),'aliquota':15, 'deducao':354.80},
        {'faixa':(3751.06,4664,68),'aliquota':22.5, 'deducao':636.13},
        {'faixa':(4664,69,float('inf')),'aliquota':27.5, 'deducao':869.36} #inf = infinit decimal ao infinito
    ]
    imposto = 0
    
    for faixa in tabelaIr:
        if salarioBruto > faixa['faixa'][0] and salarioBruto <= faixa['faixa'][1]:
            imposto = (salarioBruto * faixa['aliquota']) / 100 - faixa['deducao']
            break
    return imposto

salarioBruto = float(input('informe seu salario bruto: '))
imposto = calculadoraIr(salarioBruto)
salarioLiquido = salarioBruto - imposto
print(f'O imposto de renda devido é de R$ {imposto:.2f}') 
print('')
print(f'O salário liquido a receber é de R$ {salarioLiquido:.2f}')


