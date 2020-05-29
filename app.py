from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Atividades


app = Flask(__name__)
api = Api(app)


class Pessoa(Resource):
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome': pessoa.nome,
                'idade': pessoa.idade,
                'id': pessoa.id
            }
        except AttributeError:
            response = {
                'status': 'error',
                'message': 'Pessoa não encontrada'
            }

        return response

    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()

        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }

        return response

    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        pessoa.delete()
        message = 'Pessoa removida com sucesso.'
        response = {'status': 'successs', 'message': message}

        return response


class ListaPessoa(Resource):
    def get(self):
        pessoas = Pessoas.query.all()
        response = ([{'id': i.id, 'nome': i.nome, 'idade': i.idade} for i in pessoas])
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {'id': pessoa.id, 'nome': pessoa.nome, 'idade': pessoa.idade}
        return response


class ListaAtividades(Resource):
    def get(self):
        dados = Atividades.query.all()
        response = [{'id': i.id, 'pessoa': i.pessoa.nome, 'nome': i.nome} for i in dados]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa': atividade.pessoa.nome,
            'nome': atividade.nome,
            'id': atividade.id
        }
        return response


api.add_resource(Pessoa, '/pessoas/<string:nome>/')
api.add_resource(ListaPessoa, '/pessoas/')
api.add_resource(ListaAtividades, '/atividades/')

if __name__ == "__main__":
    app.run(debug=True)
