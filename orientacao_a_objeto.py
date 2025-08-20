class Carro:
    def __init__(self,cor,modelo): #self interagir com o objeto ele memo 
    #def __init__(self,cor,modelo, tipo): Instrutor se a busina muda de carro para carro chamo quando vou chamar o carro se e igual para todos nao
        self.cor = cor
        self.modelo = modelo
        self.velocidade = 0
        self.som = ''
        #self.som = 'Bibibi' # solucao profesor
        #self.som = tipo solucao instrutor
    def acelerar(self, incremento): #self carro, incremente = valor aceleracao
        self.velocidade += incremento
        print(f'O carro {self.modelo} acelerou para {self.velocidade} Km/h')
        
    def parar(self):
        self.velocidade = 0
        print(f'O carro {self.modelo} parou.')
    
    def buzinar(self, estilo):
        self.som = estilo
        print(f'O carro {self.modelo} diz: {self.som}')
    
    #def buzinar1(self): # Instrutor
      #  print(f'O carro {self.modelo} diz {self.som}')
    
    def desacelerar(self, decremento):
        if self.velocidade - decremento <= 0:
            self.velocidade = 0
        else:
            self.velocidade -= decremento
            print(f'O carro {self.modelo} reduziu a velocidade para {self.velocidade} Km/h')


#criando um objeto carro
meu_carro = Carro('Amarelo', 'Fusca')
carro_visita = Carro('Vermelho', 'HRV')
#meu_carro = Carro('Amarelo', 'Fusca', 'BIBIBI') instrutor
meu_carro.acelerar(20)
meu_carro.acelerar(30)
meu_carro.buzinar("Sirene")
meu_carro.desacelerar(10)
meu_carro.parar()

print('')

carro_visita.acelerar(30)
carro_visita.acelerar(30)
carro_visita.buzinar('Bibi')
carro_visita.desacelerar(20)
carro_visita.parar()

carros = [
    Carro('Branco','Fox'),
    Carro('Verde','Corolla'),
    Carro('Preto','Hilux'),
    Carro('Azul','Camaro'),
    Carro('Laranja','Lamborgini' )
    ]

for carro in carros:
    carro.acelerar(50)
    carro.buzinar('Bibi')