import os

restaurantes = [{'nome':'Sushi Gol','categoria':'japonesa','ativo': False},
                {'nome':'Pizza Suprema','categoria':'pizza','ativo': True},
                {'nome':'Cantina','categoria':'italiana','ativo': False}
                ]

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando o app')

def voltar_ao_menu_princpal():
    input('\nDigite uma tecla para voltar ao menu principal')
    main()

def opcao_invalida():
    print('Opção Inválida!\n')
    voltar_ao_menu_princpal()


def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()



def cadastrar_novo_restaurante():
    
    exibir_subtitulo('cadastro de novos restaurantes\n')

    nome_do_restaurante = input('Digite o nome do restaurantes que deseja cadastrar:')

    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')

    dados_do_restaurante = {'nome':nome_do_restaurante,'categoria':categoria,'ativo':False}

    restaurantes.append(dados_do_restaurante)

    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!' )

    voltar_ao_menu_princpal()
    
def listar_restaurantes():
    exibir_subtitulo('Listando os Restaurantes')

    print(f'{'Nome: '.ljust(20)} | {'Categoria: '.ljust(20)} | Status ')

    for restaurante in restaurantes:

        print('_'*60)
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado'if restaurante['ativo'] else 'desativado'
        print(f'{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
        print('_' * 60)
    voltar_ao_menu_princpal()


def alternar_estado_do_restaurante():
    exibir_subtitulo('Alternando o estado do Restaurante')

    nome_restaurante = input('Digite o nome do restaurante que deseja alterar do estado: ')

    restautante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restautante_encontrado = True

            restaurante['ativo'] = not restaurante['ativo']

            mensagem = f'o restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'o restaurante {nome_restaurante} foi desativado com sucesso'

            print(mensagem)
    if not restautante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_princpal()


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print()
        # opcao_escolhida = int(opcao_escolhida)
        
        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            alternar_estado_do_restaurante()
        elif opcao_escolhida == 4: 
            finalizar_app()
        else:
            opcao_invalida()
    except: 
        opcao_invalida()


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()