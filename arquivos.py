import pandas as pd #biblioteca manupular arquivo - 'as pd' -pd alias para panda

# carregar um arquivo do excel
def carregarArquivoCsv(caminhoArquivo):
    # carrega os dados do arquivo xlsx em  um dateframe
    #dateframe estaço virtual onde os dados estao alocado
    try: 
        df = pd.read_csv(caminhoArquivo)
        print('Arquivo carregado com sucesso!')
        #print(df.head())
        return df
    except Exception as errinho:
        print(f'Erro: {errinho}')
# local onde esta o arquivo a ser carregado

def salvarArquivoCsv(df, caminhoSaida):
    df.to_csv(caminhoSaida, index=False) # caminnoSaida - omne vai sairlva, sem numero coluna
    print(f'Arquivo salvo com sucesso em: {caminhoSaida}')
    
def salvarArquivoXlsx(df, caminhoSaida):
    df.to_excel(caminhoSaida, index=False)
    print(f'Arquivo salvo com sucesso em: {caminhoSaida}')

localarquivo = 'C:/Users/integral/Desktop/python_Joao/base.csv'
df = carregarArquivoCsv(localarquivo)

df['Nova Coluna'] = df['Vendas'] * 2 #vai criar a coluna Nova Coluna em Data frame e colocar vendas * 2
#print(df.head())

#df['Media Vendas'] = (df['Radio'] + df['Jornal'] + df['Vendas']) / 3
df['Media Vendas'] = df[['TV', 'Radio', 'Jornal']].mean(axis=1) # axis quero realziar o calculo no eixo 1 horizonta l
print(df.head())

#salvarArquivoCsv(df, caminhoSaida)

tipo = input('Deseja exportar:\n1 - Excel\n2 - CSV\n')
nome = input("Qual o nome do arquivo? ")
caminhoPrincipal = 'C:/Users/integral/Desktop/python_Joao/'
#caminhoSaidaCsv = 'C:/Users/integral/Desktop/python_Joao/'

if tipo == '1':
    salvarArquivoXlsx(df, f'{caminhoPrincipal}{nome}.xlsx')
elif tipo == '2':
    salvarArquivoCsv(df, f'{caminhoPrincipal}{nome}.csv')
else:
    print('Tipo invalido, digite um tipo XLSX ou CSV')