#flask framework leve trabalhar com web, rotas render template
# usado para mostrar no interpretador (browser) render template, codigo interpretado pelo imterpretador
from flask import Flask, render_template 

#criar o app flask nome manter o padrao app(variavel iria recerber a aplicacao)
app = Flask(__name__)

# rota para a pargina inicial
@app.route('/') #decorator a proxima funcao e o codigo da minha pagina
def inicio():
    return "<h1> Hello world </h1> <br> <h3> Bem vindo a minha pagina inicial <br> <a href='/contato'>Fale Comigo</h3>"

@app.route('/contato')
def contato():
    return '<a href="mailto:jgalvesjr@hotmail.com"> Me mande um e-mail </a> <hr> <a href="/">Voltar</a>' 

#rota com variaveis na url
#Acesse http://127.0.0.1:5000/especial/qqcoisa
@app.route('/especial/<nome>')
def rotaespecial(nome):
    return f'<h1> Seja bem vindo {nome} ao meu sistema! </h1>'


#toda aplicação em flask para rodar tem que ter o codigo abaixo
if __name__ == '__main__': #Verifica se o nome da aplicaçao e verdadeiro
    app.run(debug=True)
