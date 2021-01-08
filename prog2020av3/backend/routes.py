from config import app, bd, jsonify, request
from models import Computador


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
