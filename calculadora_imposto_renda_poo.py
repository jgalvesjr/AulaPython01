# classe que repesenta a tabela de imposto de renda (IR)
# se tivesse outra tabela criaria outra classe ou como self (mais elegante ) como tabela IRBr e Tabela IRUS
class TabelaIr:
    def __init__(self):
        # lista de dicionarios com as faixas salariais e valores
        self.tabela = [
            {'faixa':(0,1903.98),'aliquota':0, 'deducao':0},
            {'faixa':(1903.99,2826.65),'aliquota':7.5, 'deducao':142.80},
            {'faixa':(2826.66,3751.05),'aliquota':15, 'deducao':354.80},
            {'faixa':(3751.06,4664,68),'aliquota':22.5, 'deducao':636.13},
            {'faixa':(4664,69,float('inf')),'aliquota':27.5, 'deducao':869.36} #inf = infinit decimal ao infinito
        ]

## classe responsavel por calcular o imposto com base na tabela

class CalculadoraIr: # capturamos as informações
    def __init__(self, salarioBruto, tabelaIr):
        self.salarioBruto = salarioBruto
        self.tabelaIr =  tabelaIr
    
    def calcular(self):
        imposto = 0 # iniciando o imposto com 0
        #percore cada faixa da tabela
        for faixa in self.tabelaIr.tabela:
            if self.salarioBruto > faixa['faixa'][0] and self.salarioBruto <= faixa['faixa'][1]:
                imposto = (self.salarioBruto * faixa['aliquota']) / 100 - faixa['deducao']
                break
        return imposto

# criar uma instancia da tabela ir
tabelaIr = TabelaIr()
# pede o salario bruto do usuario
salarioBruto = float(input('Informe o salario bruto:\n(Apenas numero)'))
# cria a calculadora de IR com o salario da tabela
calculadora = CalculadoraIr(salarioBruto,tabelaIr)
#calcula o imposto devido
imposto = calculadora.calcular()

print(f'O imposto de renda devido é de R$ {imposto:.2f}')