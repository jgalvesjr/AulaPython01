import pandas as pd
import numpy as np

#criando os dados com o  numpy
nomes = ['Anna', 'Pedro', 'Rita', 'Joao', 'Simara', 'Valentina']

idades = np.random.randint(20,50, size=len(nomes))
salarios = np.random.randint(3000,10000, size=len(nomes))

#criar o dataframe com o pandas
df = pd.DataFrame({
    'Nome': nomes,
    'Idade': idades,
    'Salario': salarios
})

print('\n 📈 Dataframe gerado')
print(df)

# adicionar nova coluna de imposto calculado
df['Imposto'] = df['Salario'] * 0.18
print('\n 🦁 Dataframe com coluna imposto calculado')
print(df)

#usando as funcoes no numpy no dataframe
print('\n Idade media do grupo')
print(np.mean(df['Idade']))

# media salarial do grupo
print('\n Media salarial do grupo')
print(np.mean(df['Salario']))

#Filtrar com pandas pessoas com salario acima da media
mediaSalarial = np.mean(df['Salario'])
print('\n Pessoas com salario acima da media')
print(df[df['Salario'] > mediaSalarial])

# estatisticas resumidas
print('\n Resummo estatistico (pandas)')
print(df.describe())