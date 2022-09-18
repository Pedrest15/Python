<h1>Exercício para Praticar Filas</h1>

<div align = 'justify'>
  <p>Durante a pandemia do coronavírus, vários estabelecimentos comerciais precisaram repensar como organizam suas filas de forma a atender todos os clientes de maneira eficiente, mas priorizando os grupos de
risco. Nesse sentido, você foi designado como desenvolvedor da estrutura de dados gerenciadora, uma fila de
prioridade, que será responsável por organizar os consumidores com um critério justo.</p>
  
  <p>Cada pessoa da fila será caracterizada por seu nome, idade e se a mesma possui ou não uma condição
de saúde agravante para a COVID 19 como, por exemplo, diabetes, asma e pneumonia. O critério se o
indivíduo possui alguma condição de saúde ou não, é um booleano (1 para sim, e 0 para não).
Assim, a prioridade na fila segue os seguintes critérios, de maneira decrescente:</p>
  
  <ol>
  <li>Pessoas Idosas (idade igual ou acima de 60 anos) e com condição agravante de saúde.
  <li>Pessoas com condição agravante de saúde.
  <li>Pessoas idosas.
  <li>Pessoas não idosas e sem condições agravantes de saúde
  </ol>
  
  <p>Com isso, caso uma fila possua somente pessoas do público 4, por exemplo, seu funcionamento seguirá
o First In First Out (FIFO), ou seja, a primeira pessoa que entrou na fila será a primeira a ser atendida.
Entrentando, caso alguma pessoa de outro grupo, com maior prioridade, entre na fila, ela passará na frente
de todos os outros com menor prioridade, de forma com que o contato desta com as outras seja minimizado.
    Caso pessoas do mesmo grupo entrem na fila, a ordem segue o FIFO, portanto, se duas pessoas do grupo
1 entrarem na fila, elas irão ser as primeiras da fila, mas a que entrou antes é a que será atendida.</p>
  
  <h2>Entrada</h2>
  <p>A primeira linha contém um número N que indica quantas ações foram feitas na fila 1 <= N <= 100 e
    as próximas N linhas seguirão o formato de Ação Parâmetros (quando necessário). As ações são:</p>
  
  <li><b>ENTRA</b>: Quando esta ação é executada, será passado como parâmetro o nome inicial da pessoa, sua
idade e se possui alguma condição de saúde.
  <li><b>SAI</b>: Quando esta ação é executada, deve-se retirar uma pessoa da fila, de acordo com a estrutura
FIFO. Se a fila tiver vazia, deve ser mostrado ”FILA VAZIA” como saída.
    
   <h2>SAÍDA</h2>
   <p>Para cada comando ”SAI” da fila, deve ser mostrado em seu terminal o nome, idade e condição de saúde
da próxima pessoa a ser atendida.</p>
