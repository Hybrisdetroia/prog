from config import app, bd, jsonify, request
from models import Computador, Usuario, LanHouse


@app.route('/', methods=['GET'])
def index():
  return '''<h1>Página inicial</h1>
            <br />
            <a href="/listar_computadores">
                Clique para listar os computadores cadastrados
            </a>'''


@app.route('/listar_computadores', methods=['GET'])
def listar_computadores():
    computadores = bd.session.query(Computador).all()

    lista_computadores = [ _.json() for _ in computadores ]

    resposta = jsonify(lista_computadores)
    resposta.headers.add("Access-Control-Allow-Origin", "*")

    return resposta


@app.route('/incluir_computador', methods=['POST'])
def incluir_computador():
    resposta = jsonify({ "resultado": "ok", "detalhes": "ok" })

    dados = request.get_json()

    try:
        computador = Computador(**dados)

        bd.session.add(computador)
        bd.session.commit()

    except Exception as e:
        resposta = jsonify({ "resultado": "erro", "detalhes": str(e) })

    resposta.headers.add("Access-Control-Allow-Origin", "*")

    return resposta


@app.route('/excluir_computador/<int:computador_id>', methods=['DELETE'])
def excluir_computador(computador_id):
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    try:
        Computador.query.filter(Computador.id == computador_id).delete()
        bd.session.commit()

    except Exception as e:
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})

    resposta.headers.add("Access-Control-Allow-Origin", "*")

    return resposta


@app.route('/listar_usuarios', methods=['GET'])
def listar_usuarios():
    usuarios = bd.session.query(Usuario).all()

    lista_usuarios = [ _.json() for _ in usuarios ]

    resposta = jsonify(lista_usuarios)
    resposta.headers.add("Access-Control-Allow-Origin", "*")

    return resposta


@app.route('/listar_lanhouses', methods=['GET'])
def listar_lanhouses():
    lanhouses = bd.session.query(LanHouse).all()

    lista_lanhouses = [ _.json() for _ in lanhouses ]

    resposta = jsonify(lista_lanhouses)
    resposta.headers.add("Access-Control-Allow-Origin", "*")

    return resposta