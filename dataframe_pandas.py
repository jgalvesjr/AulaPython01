import pandas as pd

#criar um dataframe com o pandas e inserir dados

data = {
    'Nome': ['Caio', 'Mike', 'Gustavo', 'Joao', 'Gabriel', 'Luis'],
    'Idade': [38, 35, 22, 37, 39, 44],
    'Salario': [3624, 9876, 4862, 3468, 7469, 3489]
             
}

df = pd.DataFrame(data)

# Exibindo o Datframe
print('\n Dataframe')
print(df)


#selecionando uma coluna
print('\nColuna de Nome')
print(df['Nome'])

#filtrando linhar (ex: idade menor que 30)
print('\nPessoas com idade menor que 30')
print(df[df['Idade'] < 30 ])

#Adicionado uma nova coluna
print('\nAdicionar uma coluna de imposto')
#cria a coluna imposto se nao existir, se existir altera
df['Imposto'] = df['Salario'] * 0.18 
print('\nDataframe com nova coluna de imposto calculado')
print(df)

#calculando a media de salario
mediaSalarial = df['Salario'].mean()
print('\nMedia do salario')
print(mediaSalarial)

#salvar o dataframe em um arquivo csv
df.to_csv('equipe.csv', index=False)