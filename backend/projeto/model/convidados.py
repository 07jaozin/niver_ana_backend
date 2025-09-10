from backend.projeto.extensao.extensao import db

class Convidado(db.Model):
    id = db.Column(db.Integer, primary_key = True,  autoincrement = True)
    nome = db.Column(db.String(100), nullable = False)