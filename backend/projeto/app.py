from flask import Flask, request, jsonify
from flask_cors import CORS
from backend.projeto.controller.convidadosController import ConvidadoController
from backend.projeto.extensao.extensao import db
from backend.projeto.config.config import Config  # importa a config

app = Flask(__name__)
app.config.from_object(Config)  # aplica a configuração do banco
CORS(app)

# inicializa o SQLAlchemy com o app
db.init_app(app)

metodo = ConvidadoController()

with app.app_context():
    db.create_all()

@app.route("/api/rsvp", methods=["POST"])
def rsvp():
    data = request.get_json()
    name = data.get("name", "").strip()

    if not name:
        return jsonify({"error": "Nome obrigatório"}), 400

    if not metodo.insercao(name):
        return jsonify({"error": "Erro ao salvar o nome"}), 400
    
    print(f"Confirmação recebida de: {name}")
    return jsonify({"message": "Presença confirmada!", "name": name}), 200


@app.route('/nomes')
def listar():
    lista_convidados = metodo.listar()
    guests = []
    for li in lista_convidados:
        conv = {
            "id": li.id,  
            "name": li.nome
        }
        guests.append(conv)

    #return jsonify(guests), 200
    return "<h1>Hello world</h1>", 500


if __name__ == "__main__":
    app.run(debug=True, port=8080)
