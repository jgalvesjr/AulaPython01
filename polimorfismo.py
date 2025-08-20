#classe base (superclass) que repesenta o animal
class Animal:
    def fazerSom(self):
        # metodo generico que sera sobrecrito pelas subclasses
        # o uso do pass indica que nao a implementacao aqui
        pass 
    
# classe que herda de animal e representa o cachorro
class Cachorro(Animal): #classe cachorro chamando animal
    def fazerSom(self):
        #implementacao especifica para cachorro
        return 'Au Au'
    
class Gato(Animal): #Clase
    def fazerSom(self): #funcao dentro classe torna-se um metodo
        return 'Miau'

class Passarinho(Animal): #Clase
    def fazerSom(self): #funcao dentro classe torna-se um metodo
        return 'Pia'

#funcao que recebe quaçquer objeto do tipo animal (ou subclasse)
# e chama o metodo fazerSom() - uso efetivo do polimorfismo
def fazerAnimalFalar(animal: Animal): #minusculo variavale - maisculo classe animal mesmo que Animal - apelido
    print(animal.fazerSom())
    
#criando objetos
cachorro = Cachorro()
gato = Gato()
passarinho = Passarinho()
#chama o metodo de cada animal de forma polimorfica
fazerAnimalFalar(cachorro)
fazerAnimalFalar(gato)
fazerAnimalFalar(passarinho)

# ideia o que eu desejo fazer quando eu uso o animal e a super classe sem nada dentro dela
#pass - criar classe sem nada dentro, sem definir nada la

# usando lista de animais (laco + polimofismo)
# animais = [
#     cachorro, gato, passarinho
# ]

fazenda = [
    Cachorro(),
    Gato(),
    Passarinho()
]

print('')
for animal in fazenda:
    fazerAnimalFalar(animal)