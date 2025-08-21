import plotly.graph_objects as go

#dados do grafico
valores_x = [1, 2, 3, 4, 5] #dados eixo x
valores_y = [10, 11, 12, 13, 14]

#criar grafico de linhar
#criar o grafico dentro de uma caixa - a variavel fig (nome padrao)
fig = go.Figure(
    data = go.Scatter( x = valores_x,
                       y = valores_y,
                       mode = 'lines+markers',
                       name = 'Linha 1'
                       )
    )

#Adicionando o titulo e o rotulo dos eixos
fig.update_layout(
  title = 'Grafico de linhas interativas', 
  xaxis_title = 'Eixo do X',
  yaxis_title = 'Eixo do y'
  )

#exibir o grafico criado
fig.show()
