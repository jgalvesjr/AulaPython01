#biblioteca para calculo
import numpy as np

#criando uma array Numpy (vetor)

arr = np.array([1,2,3,4,5])

print(f'Array Numpy:\n {arr}')

#operacoes matematicas em arrays
print('\n Array multiplicado por 2: ')
print(arr * 2)


print(arr[2] * arr[4])

#operacao entre arrays
arr2 = np.array([10,20,30,40,50]) 
print( arr + arr2 )

#criando uma matriz (2d)
matriz = np.array([[1,2,3],[4,5,6]])
print('\nMatriz de 2X3')
print(matriz)

#soma e media da matriz

print('\nSoma de todos os elementos da matriz')
print(np.sum(matriz))

print('\nMedia de todos os elementos da matriz')
print(np.mean(matriz))

#transposta da matriz
print('\nMatriz Transposta')
print(matriz.T)

#gerando numeros aleatorios usar estaticas, computacao quantica
print('\nNumeros aleatoriosm entre 0 e 1: ')
print(np.random.rand(3,3))


#valar maximo do array
print('\nValor maximo da array')
print(np.max(arr))

#valor minimo do array
print('\nValor minimo da array')
print(np.min(arr))

#Desvio padrao em media por dispersao
print('\nDesvio padrao da array')
print(np.std(arr2))

# indexacao avancada
print('\nElementos maiores que 3')
print(arr[arr > 3 ])

# ordenar os dados
arr3 = np.array([3,50,25,42,7])
print('\n Array ordenada')
print(np.sort(arr3))

# gerando numeros aleatorios entre 1 e 100
print('\nNumeros inteiros entre 1 e 100')
print(np.random.randint(1,100, size=(3,3)))

# reogarnizando dados
print('\nReshape da matriz (2x3) para (3x2)')
print('\nMatriz original')
print(matriz)
print('\nMatriz reshap')
print(matriz.reshape(3,2)) #nao tem np pois a matriz ja herdou