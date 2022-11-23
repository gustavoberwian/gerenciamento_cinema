# Imports
import os
import string
import csv

# Inicializando variáveis
valor_ingresso = 0
linhas = 0
colunas = 0
matriz_assentos = []
filename = ''


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


def realiza_reserva(linha, coluna, sexo, idade):
    global matriz_assentos

    f = open("reservas/temp.csv", "a")
    f.write(linha.upper() + str(coluna).zfill(1) + ',' + sexo + ',' + idade + '\n')
    f.close()

    linha_int = ord(linha) - 97
    coluna_int = coluna - 1
    matriz_assentos[linha_int][coluna_int] = "X"


def exclui_reserva(linha, coluna):
    print(linha, coluna)


def option_1():
    global matriz_assentos
    global filename

    filename = input("Informe o nome do arquivo: ")
    rows = []
    with open("reservas/" + filename + ".csv", "r") as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            rows.append(row)

    for row in rows:
        # parsing each column of a row
        for i in range(len(row)):
            if i == 0:
                linha = ord(row[i][0]) - 65
                coluna = int(row[i][1:]) - 1
                matriz_assentos[linha][coluna] = 'X'


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
        sexo = ''
        idade = ''
        rows = []
        with open("reservas/" + filename + ".csv", "r") as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                rows.append(row)

        for row in rows:
            # parsing each column of a row
            for i in range(len(row)):
                if i == 1:
                    if linha.upper()+str(coluna).zfill(1) == row[0]:
                        sexo = row[i]
                if i == 2:
                    if linha.upper() + str(coluna).zfill(1) == row[0]:
                        idade = row[i]

        print(f'O assento {linha.upper()}{str(coluna).zfill(2)} está reservado por {sexo}, {idade} anos')


def option_3():
    global matriz_assentos
    mostra_matriz()
    linha = input("Digite a letra da fileira do(s) assentos(s): ")
    primeiro_assento = int(input("Digite a coluna do primeiro assento: "))
    ultimo_assento = int(input("Digite a coluna do último assento: "))

    linha_int = ord(linha) - 97
    todas_livres = True
    for coluna in range(primeiro_assento, ultimo_assento + 1):
        coluna_int = coluna - 1
        if not verifica_assento(linha_int, coluna_int):
            todas_livres = False

    if not todas_livres:
        print("Um ou mais assentos escolhidos estão reservados. Não foi possível realizar a reserva.")
        return
    else:
        if os.path.exists("reservas/temp.csv"):
            os.remove("reservas/temp.csv")
        f = open("reservas/temp.csv", "x")
        f.close()
        f = open("reservas/temp.csv", "w")
        f.write('Assento,Sexo,Idade\n')
        f.close()
        for coluna in range(primeiro_assento, ultimo_assento + 1):
            sexo = input(f"Sexo do ocupante do assento {linha.upper()}{str(coluna).zfill(2)} (F) feminino, (M) masculino: ")
            idade = input(f"Idade do ocupante do assento {linha.upper()}{str(coluna).zfill(2)}: ")
            realiza_reserva(linha, coluna, sexo, idade)


def option_4():
    global matriz_assentos
    mostra_matriz()
    linha = input("Digite a letra da fileira do(s) assentos(s): ")
    primeiro_assento = int(input("Digite a coluna do primeiro assento: "))
    ultimo_assento = int(input("Digite a coluna do último assento: "))

    for coluna in range(primeiro_assento, ultimo_assento + 1):
        exclui_reserva(linha, coluna)


def option_5():
    mostra_matriz()


def option_6():
    print('opção 6 escolhida')


def option_7():
    global filename

    filename = input(print('Informe o nome do arquivo a ser salvo: '))
    os.rename('reservas/temp.csv', 'reservas/' + filename + '.csv')


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


if __name__ == '__main__':
    inicio()
