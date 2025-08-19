import requests, json # pega os dados

nome = input('Qual o nome que voce deseja buscar? ').strip().lower()
#capturar os dados e jogar em uma caixa - caica = resposta
resposta = requests.get(f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}')

#dados json os dados que vem da url esta em json, tenho que usar a biblioteca para abrir .text vem do request - request objeto
#.text metodo - olhar documentacao do requests
dados = json.loads(resposta.text)

print(resposta)
print(dados[0]['res'][0])

