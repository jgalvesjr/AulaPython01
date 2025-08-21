import unittest # tem que gerar dentro de uma classe
from operacoes import somar, subtrair, multiplicar, dividir

#Define uma classe de testes que herda de unittest.testecase
class TesteOperacoes(unittest.TestCase):
    def testarSomar(self):
        self.assertEqual(somar(2,3),5) # o que vc vai testar e o resultado esperado do teste
        self.assertEqual(somar(-1,1),0)
        self.assertEqual(somar(-2,-3),-5)

    def testarSubtrair(self):
        self.assertEqual(subtrair(5,3),2) # o que vc vai testar e o resultado esperado do teste
        self.assertEqual(subtrair(-1,1),-2)
        self.assertEqual(subtrair(0,0),0)

    def testarMultiplicar(self):
        self.assertEqual(multiplicar(2,3),6) # o que vc vai testar e o resultado esperado do teste
        self.assertEqual(multiplicar(-1,1),-1)
        self.assertEqual(multiplicar(0,5),0)

    def testarDividir(self):
        self.assertEqual(dividir(6,3),2) # o que vc vai testar e o resultado esperado do teste
        self.assertEqual(dividir(-2,2),-1)
        with self.assertRaises(ValueError): # Verificar se vai dar o erro - se a chamada do erro esta funcionando
            dividir(1,0)
    
if __name__ == "__main__":
        unittest.main()