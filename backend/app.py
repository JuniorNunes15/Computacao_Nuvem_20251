# app.py
from flask import Flask, request, jsonify
from models import Contato, db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configuração do banco de dados (ex: RDS MySQL)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:admin123@localhost/contatos_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o banco de dados
db.init_app(app)

# Rotas da API
@app.route('/contatos', methods=['GET'])
def listar_contatos():
    contatos = Contato.query.all()
    return jsonify([{'id': c.id, 'nome': c.nome, 'email': c.email, 'telefone': c.telefone} for c in contatos])

@app.route('/contatos', methods=['POST'])
def adicionar_contato():
    data = request.json
    novo_contato = Contato(
        nome=data['nome'],
        email=data['email'],
        telefone=data['telefone']
    )
    db.session.add(novo_contato)
    db.session.commit()
    return jsonify(novo_contato.serialize())  # Retorne o contato adicionado

@app.route('/contatos/<int:id>', methods=['DELETE'])
def excluir_contato(id):
    contato = Contato.query.get_or_404(id)
    db.session.delete(contato)
    db.session.commit()
    return jsonify({'status': 'Contato excluído'}), 200

@app.route('/contatos/<int:id>', methods=['PUT'])
def atualizar_contato(id):
    contato = Contato.query.get_or_404(id)
    data = request.json
    contato.nome = data.get('nome', contato.nome)
    contato.email = data.get('email', contato.email)
    contato.telefone = data.get('telefone', contato.telefone)
    db.session.commit()
    return jsonify({'status': 'Contato atualizado'}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados
    app.run(debug=True)