SISTEMA PARA GERENCIAMENTO DE CINEMA

Início:
	- Valor ingresso
	- Fileiras (linhas)  ---
					 ---> Sala de cinema
	- Assentos (colunas) ---

Menu:
	- Carregar dados
		-> ingresso.txt
			> Registro reserva
			> Nome
			> Idade
			> Sexo
			> Asssento

Consultar assento:
	- Letra para linha
	- Número para coluna
	- Retorna situação do assento (liberado ou reservado)
	- Reservado
		-> Sexo
		-> Idade
		-> Valor pago de acordo com idade

Fazer reserva de "n" assentos:
	- Solicita assento inicial
	- Solicita n assentos desejados
	- Verifica situação de cada um
	- Caso nenhum disponível avisar usuário e não reservar
	- Não sobrepor reservas
	- Solicitar sexo e idade para cada reserva

Liberar reserva de "n" assentos:
	- Mesmo que anterior só que para desfazer reserva

Ver mapa cinema:
	- Liberados
		-> "."
	- Reservados
		-> "X"

Relatórios:
	- Tabela mostrando assento, sexo, idade, valor
	- Total de assentos separados por status
	- Total de reservas
	- Gráfico
		-> Total pagamentos inteira (18 a 59 anos)
		-> Total pagamentos meia-entrada (0 a 17 anos e 60 ou mais anos)
		-> 

Salvar dados:
	- Usuário informa nome do arquivo
	- Sistema salva reservas

Sair:
	- Encerra programa
