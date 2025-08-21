from flask import Flask, redirect, url_for, request, render_template
from requests import get

app =  Flask(__name__)

@app.route('/')
def paginaInicial():
    return render_template('inicio.html') #pegar a pagina da pasta templates dentro do projeto

@app.route('/entrar')
def fazerLogin():
    return render_template('login.html')

@app.route('/pagina403')
def pagina403():
    return render_template('pagina403.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/documentacao')
def documentacao():
    return render_template('documentacao.html')

@app.route('/validador', methods=['POST', 'GET']) #validar login e senha, metho recebe 
def validador():
    acesso_u = 'joao'
    acesso_s = '123'
    if request.method == 'POST': #valida se e post
        usuario = request.form['c_usuario'] #receber a informação que recebi de usuario no site olhar na pagina login que vc ira usar
        senha = request.form['c_senha'] #receber a informação que recebi de senha no site olhar na pagina login que vc ira usar
        if usuario == acesso_u and senha == acesso_s:
            return redirect(url_for('welcome')) # redireciona o endereço para welcome se tiver permissão
        else:
            return redirect(url_for('pagina403')) # se não passar o login manda para 
    else:
        usuario = request.args.get('c_usuario') #receber a informação que recebi de senha no site olhar na pagina login que vc ira usar get
        senha = request.args.get('c_senha') #receber a informação que recebi de senha no site olhar na pagina login que vc ira usar get
        if usuario == acesso_u and senha == acesso_s:
            return redirect(url_for('welcome'))
        else:
            return redirect(url_for('pagina403'))
        
if __name__ == '__main__':
    app.run(debug=True)