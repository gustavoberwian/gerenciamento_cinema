# Imports
import os
import string
import csv

# Inicializando variáveis
valor_ingresso = 0
linhas = 0
colunas = 0
filename = ""
# Matriz principal
matriz_assentos = []
# Matriz de apoio para salvar em arquivo csv
reservas = []


def cria_matriz():
    # Função responsável por criar a matriz dos assentos

    # Chama variáveis globais
    global matriz_assentos
    global linhas
    global colunas

    # Loop nas linhas
    for i in range(linhas):
        linha = []
        # Loop nas colunas
        for j in range(colunas):
            # Insere valor na lista temporária da linha
            linha.append("'")

        # Insere lista temporária criada na matriz assentos
        matriz_assentos.append(linha)


def mostra_matriz():
    # Função responsável por mostrar a matriz dos assentos

    # Chama variáveis globais
    global matriz_assentos
    global linhas
    global colunas

    # Lógica para mostra números das colunas
    numeros = ["%.2d" % i for i in range(1, colunas+1)]
    print(' ', end="")
    for i in range(len(numeros)):
        print(' ', numeros[i], '', end="")
    print()

    # Lógica para mostra matriz com letras do alfabeto na primeira coluna
    alfabeto = list(string.ascii_uppercase)
    for i in range(len(matriz_assentos)):
        print(alfabeto[i], end="")
        for j in range(len(matriz_assentos[i])):
            print(' ', matriz_assentos[i][j], ' ', end="")
        print()


def verifica_assento(linha, coluna):
    # Função que verifica se assento está ocupado ou livre

    # Chama variável global
    global matriz_assentos

    if matriz_assentos[linha][coluna] == "'":
        # Se estiver livre retorna True
        return True
    elif matriz_assentos[linha][coluna] == "X":
        # Se estiver ocupado retorna False
        return False


def realiza_reserva(linha, coluna, sexo, idade):
    # Função responsável por realizar a reserva

    # Chama variável global
    global matriz_assentos

    # Converte a linha passada em letra para número
    linha_int = ord(linha) - 97
    # Converte assento para ocupado
    matriz_assentos[linha_int][coluna - 1] = "X"
    # Insere linha na matriz de apoio
    reservas.append(linha.upper() + str(coluna).zfill(1) + ',' + sexo + ',' + idade)


def exclui_reserva(linha, coluna):
    # Função responsável por excluir a reserva

    # Chama variável global
    global matriz_assentos
    global reservas

    # Converte a linha passada em letra para número
    linha_int = ord(linha) - 97
    # Converte assento para livre
    matriz_assentos[linha_int][coluna - 1] = "'"

    # Loop na matriz de apoio para remover linha
    for item in reservas[:]:
        if item.find(linha.upper() + str(coluna).zfill(1)) != -1:
            reservas.remove(item)


def option_1():
    # Função para opção 1 escolhida (Carregar arquivo)

    # Chama variáveis globais
    global matriz_assentos
    global filename
    global reservas

    # Solicita nome do arquivo a ser carregado
    filename = input("Informe o nome do arquivo: ")
    # Caso arquivo não exista retorna ao menu
    if not os.path.exists("reservas/" + filename + ".csv"):
        return

    # Inicializa matriz de apoio
    rows = []
    # Abre arquivo para leitura
    with open("reservas/" + filename + ".csv", "r") as csvfile:
        # Define cabeçalho do arquivo
        csvreader = csv.reader(csvfile)
        # Pula cabeçalho do arquivo
        next(csvreader)
        # Adiciona linhas a matriz de apoio ignorando cabeçalho
        for row in csvreader:
            rows.append(row)

    # Loop em matriz de apoio
    for row in rows:
        # Inicializando variáveis
        linha_str = 0
        coluna_str = 0
        sexo = ""
        idade = 0
        # Loop na linha
        for i in range(len(row)):
            # Se coluna for 0 (Nome do assento)
            if i == 0:
                linha = ord(row[i][0]) - 65
                linha_str = row[i][0]
                coluna = int(row[i][1:]) - 1
                coluna_str = row[i][1:]
                matriz_assentos[linha][coluna] = 'X'
            # Se coluna for 1 (Sexo do ocupante)
            if i == 1:
                sexo = row[i]
            # Se coluna for 2 (Idade do ocupante)
            if i == 2:
                idade = row[i]

        # Insere linhas na matriz de apoio com as informações obtidas
        reservas.append(linha_str + coluna_str + ',' + sexo + ',' + idade)


def option_2():
    # Função para opção 2 escolhida (Conferir status de assento)

    # Chama variáveis globais
    global linhas
    global colunas
    global matriz_assentos

    # Chama função que mostra matriz
    mostra_matriz()

    # Solicita ao usuário a letra da fileira
    linha = input(print('Informe a letra da fileira: '))
    # Converte letra da fileira em número da linha
    linha_int = ord(linha) - 97
    # Solicita ao usuário o número da coluna
    coluna = int(input(print('Informe o número da coluna: ')))

    # Chama função verifica assento
    if verifica_assento(linha_int, coluna - 1):
        # Caso True mostra que assento está livre
        print(f'O assento {linha.upper()}{str(coluna).zfill(2)} está livre')
    else:
        # Caso False mostra que assento está ocupado e mostra sexo e idade
        # Lógica para buscar sexo e idade do assento informado
        sexo = ''
        idade = ''
        rows = []
        with open("reservas/" + filename + ".csv", "r") as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)
            for row in csvreader:
                rows.append(row)

        for row in rows:
            for i in range(len(row)):
                if i == 1:
                    if linha.upper()+str(coluna).zfill(1) == row[0]:
                        sexo = row[i]
                if i == 2:
                    if linha.upper() + str(coluna).zfill(1) == row[0]:
                        idade = row[i]

        print(f'O assento {linha.upper()}{str(coluna).zfill(2)} está reservado por {sexo}, {idade} anos')


def option_3():
    # Função para opção 3 escolhida (Realizar reserva)

    # Chama variáveis globais
    global matriz_assentos

    # Chama função que mostra matriz
    mostra_matriz()

    # Solicita linha do assento
    linha = input("Digite a letra da fileira do(s) assentos(s): ")
    # Solicita primeiro assento da lista
    primeiro_assento = int(input("Digite a coluna do primeiro assento: "))
    # Solicita último assento da lista
    ultimo_assento = int(input("Digite a coluna do último assento: "))

    # Converte linha letra para int
    linha_int = ord(linha) - 97
    # Inicializa variável
    todas_livres = True
    # Loop em assentos informados
    for coluna in range(primeiro_assento, ultimo_assento + 1):
        # Caso um assento está ocupado todas_livres = False
        if not verifica_assento(linha_int, coluna - 1):
            todas_livres = False

    if not todas_livres:
        # Se uma ocupada
        print("Um ou mais assentos escolhidos estão reservados. Não foi possível realizar a reserva.")
        return
    else:
        # Se todas livres
        for coluna in range(primeiro_assento, ultimo_assento + 1):
            # Solicita sexo e idade para cada assento
            sexo = input(f"Sexo do ocupante do assento {linha.upper()}{str(coluna).zfill(2)} (F) feminino, (M) masculino: ")
            idade = input(f"Idade do ocupante do assento {linha.upper()}{str(coluna).zfill(2)}: ")
            # Chama função para realizar reserva
            realiza_reserva(linha, coluna, sexo, idade)


def option_4():
    # Função para opção 4 escolhida (Liberar assentos)

    # Chama variáveis globais
    global matriz_assentos

    # Chama função que mostra matriz
    mostra_matriz()

    # Solicita linha do assento
    linha = input("Digite a letra da fileira do(s) assentos(s): ")
    # Solicita primeiro assento da lista
    primeiro_assento = int(input("Digite a coluna do primeiro assento: "))
    # Solicita último assento da lista
    ultimo_assento = int(input("Digite a coluna do último assento: "))

    for coluna in range(primeiro_assento, ultimo_assento + 1):
        # Chama função que excluir reservas
        exclui_reserva(linha, coluna)


def option_5():
    # Função para opção 5 escolhida (Mostrar matriz)

    # Chama função que mostra matriz
    mostra_matriz()


def option_6():
    # Função para opção 6 escolhida (Relatórios)
    print('opção 6 escolhida')


def option_7():
    # Função para opção 7 escolhida (Salvar dados)

    # Chama variáveis globais
    global filename
    global reservas

    # Define para vazio o valor do filename
    filename = ""

    while os.path.exists("reservas/" + filename + ".csv") or filename == "":
        # Define filename caso não exista nenhum arquivo com esse nome
        filename = input(print('Informe o nome do arquivo a ser salvo: '))

    # Cria arquivo com nome informado
    f = open("reservas/" + filename + ".csv", "x")
    f.close()
    # Abre arquivo no modo de escrita
    f = open("reservas/" + filename + ".csv", "w")
    # Insere cabeçalho
    f.write('Assento,Sexo,Idade\n')
    for item in reservas:
        # Insere conteúdo da matriz de apoio
        f.write(item + '\n')
    f.close()


def inicio():
    # Função inicial

    # Limpa a tela
    os.system('cls' if os.name == 'nt' else 'clear')

    # Chama variáveis globais
    global valor_ingresso
    global linhas
    global colunas

    # Solicita valor do ingresso
    valor_ingresso = input(print('Digite o valor do ingresso: '))
    # Solicita número de linhas
    linhas = int(input(print('Digite a quantidade de fileiras: ')))
    # Solicita número de colunas
    colunas = int(input(print('Digite a quantidade de assentos por fileira: ')))

    # Chama função cria matriz
    cria_matriz()
    # Chama função mostra matriz
    mostra_matriz()

    # While para executar menu
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


def menu():
    # Menu com as opções de escolha

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
