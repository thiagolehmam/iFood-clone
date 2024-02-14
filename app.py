
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

    def cadastrar_novo_restaurante(self):
        ''' Essa função é responsável por cadastrar um novo restaurante '''
        self.exibir_subtitulo('Cadastro de novos restaurantes')
        restaurante = Restaurante.cadastrar_novo_restaurante()
        self.restaurantes.append(restaurante)
        print(f'O restaurante {restaurante.nome} foi cadastrado com sucesso!')
        self.voltar_ao_menu_principal()

    def listar_restaurantes(self):
        ''' Lista os restaurantes presentes na lista '''
        Restaurante.listar_restaurantes(self.restaurantes)
        self.voltar_ao_menu_principal()

    def alternar_estado_restaurante(self):
        ''' Altera o estado ativo/desativado de um restaurante '''
        Restaurante.alternar_estado_restaurante(self.restaurantes)
        self.voltar_ao_menu_principal()

    def escolher_opcao(self):
        ''' Solicita e executa a opção escolhida pelo usuário '''
        try:
            opcao
