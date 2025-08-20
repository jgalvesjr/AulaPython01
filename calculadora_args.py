class Calculadora:
    def somar(self, *args):
        return sum(args)
    
    def multiplicar(self, *args):
        resultado = 1
        for num in args:
            resultado *= num
        return resultado 
calc = Calculadora() #dentro do objeto calc vamos chamar a calculadora
print(calc.multiplicar(1,2))
print(calc.multiplicar(1,2,3,4,5))
print('')
print(calc.somar(1,2,3))