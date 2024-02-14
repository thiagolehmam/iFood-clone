import os

class Restaurante:
    def __init__(self, nome, categoria, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo

    def ativar_desativar(self):
        self.ativo = not self.ativo

    def __str__(self):
        return f"Nome: {self.nome}, Categoria: {self.categoria}, Ativo: {'Sim' if self.ativo else 'Não'}"

    @classmethod
    def cadastrar_novo_restaurante(cls):
        ''' Cadastra um novo restaurante '''
        nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
        categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
        return cls(nome_do_restaurante, categoria)

    @staticmethod
    def listar_restaurantes(restaurantes):
        ''' Lista os restaurantes presentes na lista '''
        print('Listando restaurantes:')
        for restaurante in restaurantes:
            print(restaurante)

    @staticmethod
    def alternar_estado_restaurante(restaurantes):
        ''' Altera o estado ativo/desativado de um restaurante '''
        nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
        restaurante_encontrado = False
        for restaurante in restaurantes:
            if restaurante.nome == nome_restaurante:
                restaurante_encontrado = True
                restaurante.ativar_desativar()
                mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante.ativo else f'O restaurante {nome_restaurante} foi desativado com sucesso'
                print(mensagem)
                break
        if not restaurante_encontrado:
            print('O restaurante não foi encontrado')

