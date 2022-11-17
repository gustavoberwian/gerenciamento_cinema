# Imports
import os
import string

# Inicializando variáveis
valor_ingresso = 0
linhas = 0
colunas = 0
matriz_assentos = []


def cria_matriz():
    global matriz_assentos
    global linhas
    global colunas
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append("'")

        matriz_assentos.append(linha)


def mostra_matriz():
    global matriz_assentos
    global linhas
    global colunas

    numeros = ["%.2d" % i for i in range(1, colunas+1)]
    print(' ', end="")
    for i in range(len(numeros)):
        print(' ', numeros[i], '', end="")
    print()

    alfabeto = list(string.ascii_uppercase)
    for i in range(len(matriz_assentos)):
        print(alfabeto[i], end="")
        for j in range(len(matriz_assentos[i])):
            print(' ', matriz_assentos[i][j], ' ', end="")
        print()


def verifica_assento(linha, coluna):
    global matriz_assentos
    if matriz_assentos[linha][coluna] == "'":
        return True
    elif matriz_assentos[linha][coluna] == "X":
        return False


def option_1():
    print('opção 1 escolhida')


def option_2():
    global linhas
    global colunas
    global matriz_assentos
    mostra_matriz()

    linha = input(print('Informe a letra da fileira: '))
    linha_int = ord(linha) - 97
    coluna = int(input(print('Informe o número da coluna: ')))
    coluna_int = coluna - 1

    if verifica_assento(linha_int, coluna_int):
        print(f'O assento {linha.upper()}{str(coluna).zfill(2)} está livre')
    else:
        print(f'O assento {linha.upper()}{str(coluna).zfill(2)} está reservado')



def option_3():
    print('opção 3 escolhida')


def option_4():
    print('opção 4 escolhida')


def option_5():
    mostra_matriz()


def option_6():
    print('opção 6 escolhida')


def option_7():
    print('opção 7 escolhida')


def inicio():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela
    global valor_ingresso
    valor_ingresso = input(print('Digite o valor do ingresso: '))
    global linhas
    linhas = int(input(print('Digite a quantidade de fileiras: ')))
    global colunas
    colunas = int(input(print('Digite a quantidade de assentos por fileira: ')))

    cria_matriz()
    mostra_matriz()

    escolha = '0'

    while escolha != '9':

        escolha = menu()

        if escolha == '1':
            option_1()
        elif escolha == '2':
            option_2()
        elif escolha == '3':
            option_3()
        elif escolha == '4':
            option_4()
        elif escolha == '5':
            option_5()
        elif escolha == '6':
            option_6()
        elif escolha == '7':
            option_7()
        elif escolha == '9':
            print('\nSaindo...\n')
            exit()
        else:
            print('\nOpção desconhecida!\n')

        input('Pressione ENTER para continuar')


# Menu com as opções de escolha
def menu():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela
    print('\n..:: Cinema ::..\n')
    print('[1] Carregar dados')
    print('[2] Consultar situação de um assento')
    print('[3] Fazer reserva(s)')
    print('[4] Liberar reserva(s)')
    print('[5] Ver mapa do cinema')
    print('[6] Ver relatórios')
    print('[7] Salvar dados')
    print('[9] Sair\n')

    # Solicita que usuário informe uma opção e guarda em variável
    selecionado = input(print('Escolha uma opção: '))

    # Retorna opção selecionada
    return selecionado


# def update(row, col, val):
#     matrix[rows[row]][cols[col]] = val

if __name__ == '__main__':
    inicio()
