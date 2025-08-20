#usar bibliotec sql para conectar em bancos como oracle
import sqlite3

# connectar ao banco de dados ou criar um novo se não existir

def conenctarBanco():
    conexao = sqlite3.connect('bancodedados.db') 
    return conexao

#Criar uma tabela
def criarTabela():
    conexao = conenctarBanco() # abrea a conexao
    cursor = conexao.cursor() #cria um cursor para executar os comandos sql
     #cria a tabela se ela não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            idade INTEGER
        )
    ''')
    conexao.commit()
    conexao.close()

def inserirUsuario(nome, idade):
    conexao = conenctarBanco()
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO usuarios (nome, idade)
        VALUES(?, ?)             
                   ''', (nome, idade)) #nome, idade caira no nome idade tabela que ira cair em ? ?
    conexao.commit()
    conexao.close()
    
def listarUsuarios():
    conexao = conenctarBanco()
    cursor = conexao.cursor()
    cursor.execute ('''
        SELECT * FROM usuarios
    ''')
    usuarios = cursor.fetchall() #separar os elementos, se nao fizer mostra em uma linha só
    for usuario in usuarios:
        print(usuario)
    conexao.close()
    
def atualizarUsuario(id, novoNome, novaIdade):
    conexao = conenctarBanco()
    cursor = conexao.cursor()
    cursor.execute('''
        UPDATE usuarios
        SET nome = ?, idade = ?
        WHERE id = ?
    ''',(novoNome, novaIdade, id))
    conexao.commit()
    conexao.close()
    
def excluirUsuario(id):
    conexao = conenctarBanco()
    cursor = conexao.cursor()
    cursor.execute('''
        DELETE FROM usuarios
        WHERE id = ?            
    ''',(id,)) #quando e valor unico tem que colocar a virgula
    conexao.commit()
    conexao.close()
    
#exemplo de uso da funcoes crud

#criar a tabela
listaUsuarios = [('Rita', 50), ('Anna', 60), ('Pedro', 70), ('Joao', 80), ('Silmara', 30), ('Bia', 55)]
criarTabela()
# inserirUsuario('Rita', 44)
# inserirUsuario('Anna', 17)
# inserirUsuario('Pedro', 13)
# inserirUsuario('Joao', 48)
for usuario in listaUsuarios:
    inserirUsuario(usuario[0], usuario[1])
    
# listar todos os usuario cadastrador no banco
print('Usuarios antes de atualizar')
listarUsuarios()
print('-----------------------------------------')

#atualiar a idade e nome de usuario
atualizarUsuario(1, 'Rita', 20)
atualizarUsuario(2, 'Anna', 60)

excluirUsuario(7)
print('Usuarios depois da atualizacao')
listarUsuarios()
print('------------------------------')

