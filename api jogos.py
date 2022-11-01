#API para  consulta, criação, edição e exclusão de jogos

    # - localhost/jogos (GET)
    # - localhost/jogos (POST)
    # - localhost/jogos/id (GET)
    # - localhost/jogos/id (PUT)
    # - localhost/jogos (DELETE)
from flask import Flask, jsonify, request

api = Flask(__name__)

jogos = [
    {
        'id': 1,
        'titulo': 'The Legende of Zelda',
        'empresa': 'Nintendo',
    },
    {
        'id': 2,
        'titulo': 'God of War',
        'empresa': 'Ubisoft',
    },
    {
        'id': 3,
        'titulo': 'Resident Evil',
        'empresa': 'Capcom',
    },
    {
        'id': 4,
        'titulo': 'FIFA',
        'empresa': 'EA',
    },

]

#consultar(All)
@api.route('/jogos',methods=['GET'])
def obter_jogos():
    return jsonify(jogos)

#consultar por id
@api.route('/jogos/<int:id>',methods=['GET'])
def obter_jogos_por_id(id):
    for jogo in jogos:
       if jogo.get('id') == id:
            return jsonify(jogo)

#editar 
@api.route('/jogos/<int:id>',methods=['PUT'])
def editar_jogo_por_id(id):
    jogo_alterado = request.get_json()
    for indice, jogo in enumerate(jogos):
        if jogo.get('id') == id:
            jogos[indice].update(jogo_alterado)
            return jsonify(jogos[indice])

#criar
@api.route('/jogos',methods=['POST'])
def incluir_um_novo_jogo():
    novo_jogo = request.get_json()
    jogos.append(novo_jogo)
    return jsonify(jogos)

#excluir
@api.route('/jogos<int:id>',methods=['DELETE'])
def excluir_jogos(id):
    for indice, id, jogo in enumerate(jogos):
        if jogo.get('id') == id:
            del jogos[indice]
    return jsonify(jogos)

#run
api.run(port=5000, host='localhost', debug = True)