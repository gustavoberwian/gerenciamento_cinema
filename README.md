# SISTEMA PARA GERENCIAMENTO DE CINEMA

## Sistema básico para gerenciamento de cinema

=================

Cenário: Ao iniciar o programa, será solicitado ao usuário informar o valor do ingresso, a 
quantidade de fileiras (linhas) e quantos assentos por fileira (colunas) o cinema 
comporta. Com esses dados, deve-se criar uma matriz para gerenciar as reservas. Cada posição 
dessa matriz representa um assento, que deve armazenar a idade e o sexo do ocupante. 

Menu: 
 
O programa deverá conter um menu com as seguintes funcionalidades: 
 
1. Carregar dados: usuário informa o nome do arquivo que contém o registro das reservas e 
o programa atualiza a matriz com os dados lidos do arquivo; 
2. Consultar situação de um assento: usuário informa o assento (letra da linha e número da 
coluna) e o programa retorna se está liberado ou reservado. Caso esteja reservado, retornar 
o sexo e a idade do ocupante, seguido do valor pago conforme a idade; 
3. Fazer reservas de “n” assentos: “n” assentos na mesma fileira, a partir de um assento 
informado pelo usuário. Caso não existam “n” assentos disponíveis a partir do assento 
informado, avisar o usuário e não fazer nenhuma reserva. Não deve permitir sobreposição  
de assentos previamente reservados. A cada assento a ser reservado, solicitar o sexo e a  
idade do ocupante; 
4. Liberar reserva de “n” assentos: na mesma fileira, a partir de um assento informado; 
5. Visualizar mapa do cinema: mostrar o mapa do cinema em formato tabular, com os 
assentos liberados representados por “·” e os reservados representados por um “X”; 
6. Relatórios:
   - Listagem em formato de tabela apresentando as informações das reservas do cinema 
   (assento, sexo, idade, valor); 
   - Quantidade total de assentos do cinema, divididos entre liberados e reservados; 
   - Quantidade de reservas, dividido por sexo; 
   - Gráfico e quantidade de pagantes inteira (18 a 59 anos) e meia entrada (crianças e 
   adolescentes 0 a 17 anos e idosos 60 anos ou mais). Mostrar as 3 classificações, com 
   quantidades, percentuais e valor arrecadado por faixa. Mostrar também a receita 
   total; 
7. Salvar dados: usuário informa o nome do arquivo e o programa salva as reservas; 
8. Sair: Encerra o programa