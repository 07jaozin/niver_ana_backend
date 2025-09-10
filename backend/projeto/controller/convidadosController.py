from backend.projeto.model.convidados import Convidado
from backend.projeto.extensao.extensao import db

class ConvidadoController:
     
     @staticmethod
     def insercao(nome):
          pessoa = Convidado(nome = nome)
          db.session.add(pessoa)
          db.session.commit()
          return True
     
     @staticmethod
     def listar():
          todos = Convidado.query.all()

          return todos
          

