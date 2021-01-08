from config import app, bd, jsonify
from models import Computador


@app.route('/', methods=['GET'])
def index():
  return '''<h1>Página inicial</h1>
            <br />
            <a href="/listar_computadores">
                Clique para listar os computadores cadastrados
            </a>'''


@app.route('/listar_computadores')
def listar_computadores():
    computadores = bd.session.query(Computador).all()

    lista_computadores = [ _.json() for _ in computadores ]

    resposta = jsonify(lista_computadores)
    resposta.headers.add("Access-Control-Allow-Origin", "*")

    return resposta
