class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome.title()
        self.categoria = categoria.upper()
        self.ativo = False
        Restaurante.restaurantes.append(self)

    @classmethod
    def listar_todos(cls):
        for restaurante in cls.restaurantes:
            print(f'Nome: {restaurante.nome}, Categoria: {restaurante.categoria}, Ativo: {restaurante.ativo}')

    @classmethod
    def alternar_estado(cls, nome_restaurante):
        for restaurante in cls.restaurantes:
            if restaurante.nome == nome_restaurante:
                restaurante.ativo = not restaurante.ativo
                return f'O restaurante {restaurante.nome} foi ativado' if restaurante.ativo else f'O restaurante {restaurante.nome} foi desativado'

    @classmethod
    def cadastrar_novo(cls, nome, categoria):
        novo_restaurante = Restaurante(nome, categoria)
        return f'O restaurante {novo_restaurante.nome} foi cadastrado com sucesso!'
