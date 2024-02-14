class Restaurante:
    def __init__(self, nome, categoria, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo

    def alternar_estado(self):
        ''' Altera o estado ativo/desativado do restaurante '''
        self.ativo = not self.ativo

    def __str__(self):
        return f"Nome: {self.nome}, Categoria: {self.categoria}, Ativo: {'Sim' if self.ativo else 'Não'}"

    @classmethod
    def criar_restaurante(cls, nome, categoria):
        ''' Cria um novo restaurante '''
        return cls(nome, categoria)

    @staticmethod
    def listar_todos(restaurantes):
        ''' Lista todos os restaurantes '''
        print('Listando restaurantes:')
        for restaurante in restaurantes:
            print(restaurante)

    @staticmethod
    def encontrar_por_nome(restaurantes, nome):
        ''' Encontra um restaurante pelo nome '''
        for restaurante in restaurantes:
            if restaurante.nome == nome:
                return restaurante
        return None
