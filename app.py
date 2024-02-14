import os
from modelos.restaurante import Restaurante

class App:
    def __init__(self):
        self.restaurantes = []

    def exibir_nome_do_programa(self):
        ''' Exibe o nome estilizado do programa na tela '''
        print("""
              
      𝑖𝐹𝑜𝑜𝑑
              
        """)

    def exibir_opcoes(self):
        ''' Exibe as opções disponíveis no menu principal '''
        print('1. Cadastrar restaurante')
        print('2. Listar restaurantes')
        print('3. Alternar estado do restaurante')
        print('4. Sair\n')

    def finalizar_app(self):
        ''' Exibe mensagem de finalização do aplicativo '''
        self.exibir_subtitulo('Finalizar app')

    def voltar_ao_menu_principal(self):
        ''' Solicita uma tecla para voltar ao menu principal '''
        input('\nDigite uma tecla para voltar ao menu ')
        self.main()

    def opcao_invalida(self):
        ''' Exibe mensagem de opção inválida e retorna ao menu principal '''
        print('Opção inválida!\n')
        self.voltar_ao_menu_principal()

    def exibir_subtitulo(self, texto):
        ''' Exibe um subtítulo estilizado na tela '''
        os.system('cls')
        linha = '*' * (len(texto))
        print(linha)
        print(texto)
        print(linha)
        print()

    def escolher_opcao(self):
        ''' Solicita e executa a opção escolhida pelo usuário '''
        try:
            opcao_escolhida = int(input('Escolha uma opção: '))
            if opcao_escolhida == 1:
                self.cadastrar_novo_restaurante()
            elif opcao_escolhida == 2:
                self.listar_restaurantes()
            elif opcao_escolhida == 3:
                self.alternar_estado_restaurante()
            elif opcao_escolhida == 4:
                self.finalizar_app()
            else:
                self.opcao_invalida()
        except ValueError:
            self.opcao_invalida()

    def main(self):
        ''' Função principal que inicia o programa '''
        os.system('cls')
        self.exibir_nome_do_programa()
        self.exibir_opcoes()
        self.escolher_opcao()

    def cadastrar_novo_restaurante(self):
        ''' Essa função é responsável por cadastrar um novo restaurante '''
        self.exibir_subtitulo('Cadastro de novos restaurantes')
        nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
        categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
        restaurante = Restaurante.criar_restaurante(nome_do_restaurante, categoria)
        self.restaurantes.append(restaurante)
        print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
        self.voltar_ao_menu_principal()

    def listar_restaurantes(self):
        ''' Lista os restaurantes presentes na lista '''
        self.exibir_subtitulo('Listando restaurantes')
        Restaurante.listar_todos(self.restaurantes)
        self.voltar_ao_menu_principal()

    def alternar_estado_restaurante(self):
        ''' Altera o estado ativo/desativado de um restaurante '''
        self.exibir_subtitulo('Alterando estado do restaurante')
        nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
        restaurante = Restaurante.encontrar_por_nome(self.restaurantes, nome_restaurante)
        if restaurante:
            restaurante.alternar_estado()
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante.ativo else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
        else:
            print('O restaurante não foi encontrado')
        self.voltar_ao_menu_principal()

if __name__ == '__main__':
    app = App()
    app.main()
