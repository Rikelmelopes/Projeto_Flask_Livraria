from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'Percy Jackson - O Ladrão de Raios',
        'autor': 'Rick Riordan'
    },
    {
        'id': 2,
        'título': 'Percy Jackson - O Mar de Monstros',
        'autor': 'Rick Riordan'
    },
    {
        'id': 3,
        'título': 'Percy Jackson - A Maldição do Titã',
        'autor': 'Rick Riordan'
    },
       {
        'id': 4,
        'título': 'Percy Jackson - A Batalha do Labirinto',
        'autor': 'Rick Riordan'
    },
    {
        'id': 5,
        'título': 'Percy Jackson - O Último Olimpiano',
        'autor': 'Rick Riordan'
    },
]

# ---------------Consultar(todos)---------------- Usando metodo GET
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)


# ------------------Consultar(id)--------------- Usando metodo GET
@app.route('/livros/<int:id>',methods=['GET'])
def consultar_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
        
        
# -----------------Editar------------------- Usando metodo PUT
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
        
        
# -----------------Criar-------------------- Usando metodo POST
@app.route('/livros',methods=['POST'])
def criar_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    
    return jsonify(livros)


# ----------------Excluir---------------------- Usando metodo DELETE
@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)

app.run(port=5000,host='localhost',debug=True)