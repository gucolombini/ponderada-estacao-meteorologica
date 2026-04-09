from flask import Flask,request,jsonify,render_template
from flask_cors import CORS
import database


app = Flask(__name__)
CORS(app)

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/historico")
def historico():
    return render_template("historico.html")

@app.route("/editar")
def editar():
    return render_template("editar.html")

@app.route("/", methods=["GET"])
def index():
    leituras = database.ultimas_leituras(10)
    return jsonify([dict(l) for l in leituras])

@app.route("/leituras", methods=["GET"])
def listar():
    leituras = database.listar_leituras()
    return jsonify([dict(l) for l in leituras])

@app.route('/leituras', methods=['POST'])
def criar():
    dados = request.get_json()
    if not dados:
        return jsonify({'erro': 'JSON inválido'}), 400
    id_novo = database.inserir_leitura(
        dados['temperatura'],
        dados['umidade']
    )
    return jsonify({'id': id_novo, 'status': 'criado'}), 201

@app.route('/leituras/<int:id>', methods=['GET'])
def detalhe(id):
    leitura = database.achar_leitura(id)
    if not leitura:
        return jsonify({'erro': 'Leitura não encontrada'}), 404
    return jsonify(dict(leitura)), 201

@app.route('/leituras/<int:id>', methods=['PUT'])
def atualizar(id):
    leitura = database.achar_leitura(id)
    if not leitura:
        return jsonify({'erro': 'Leitura não encontrada'}), 404
    dados = request.get_json()
    if not isinstance(dados, dict):
        return jsonify({'erro': 'JSON inválido'}), 400
    if 'temperatura' not in dados or 'umidade' not in dados:
        return jsonify({'erro': 'Campos obrigatórios'}), 400
    try:
        temperatura = float(dados['temperatura'])
        umidade = float(dados['umidade'])
    except (ValueError, TypeError):
        return jsonify({'erro': 'Valores devem ser numéricos'}), 400
    resultado = database.atualizar_leitura(id, temperatura, umidade)
    if not resultado:
        return jsonify({'erro': 'Falha na atualização'}), 500
    leitura_atualizada = database.achar_leitura(id)
    return jsonify(dict(leitura_atualizada)), 200

@app.route('/leituras/<int:id>', methods=['DELETE'])
def deletar(id):
    sucesso = database.deletar_leitura(id)
    if not sucesso:
        return jsonify({'erro': 'Leitura não encontrada'}), 404
    return jsonify({'status': 'deletado'}), 200

@app.route('/api/estatisticas', methods=['GET'])
def estatisticas():
    minutos = request.args.get("minutos", default=10, type=int)
    stats = database.estatisticas(minutos)
    if not stats:
        return jsonify({'erro': 'Sem dados'}), 404
    return jsonify(stats), 200

if __name__ == "__main__":
    app.run(debug=True)