from models import Pessoas


def insere_pessoa():
    pessoa = Pessoas(nome='Cacilds', idade=40)
    pessoa.save()


def consulta():
    pessoa = Pessoas.query.all()
    print(pessoa)
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    print(pessoa)


def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Cacilds').first()
    pessoa.nome = 'Birits'
    pessoa.save()


def exclui_pessoa(self):
    pessoa = Pessoas.query.filter_by(nome='Cacilds').first()
    pessoa.delete()


if __name__ == '__main__':
    consulta()
