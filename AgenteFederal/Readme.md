<h1>Exercício para Praticar Pilhas</h1>
<div align="justify" >
  <p>Você é um agente federal que está trabalhando em dupla. Seu parceiro está em campo e você ficou na
base para dar o apoio necessário para ele. Em uma madrugada muito chuvosa você é acordado com uma
ligação do seu parceiro avisando que ele interceptou uma mensagem de um grupo terrorista, mas ele foi
descoberto e o grupo estáatrá dele. Ele sabe que será capturado ao amanhecer e por isso precisa te passar
a mensagem nesse instante.</p>
  <p>Seu parceiro te informa que a mensagem é uma sequência numérica codificado em ASCII. Contudo, ele
suspeita que a ligação esteja sendo grampeada e por isso ele irá te informar a mensagem de acordo com o
código de encriptação criado por vocês.</p>
  <p>Escreva um programa que recebe a mensagem e no fim mostre a frase de forma legível.
A frase pode conter até 10 mil caracteres. E deve ser usado uma pilha como estrutura de dados para auxiliar.
</p>
  
  <h2>Código de Encriptação</h2>
  <li>Toda mensagem é recebida de trás para frente, ou seja, o último dígito na realidade é o primeiro da
sequência.
  <li>Sempre que você receber o número 0, você deve desconsiderar o último dígito falado pela sua dupla,
pois é um valor errado para esconder a verdadeira mensagem.
  <li>Quando você recebe o núumero -1 a mensagem é encerrada e você deve desconsiderar qualquer inrformação 
    que ele te informar após isso, pois é informação falsa.</li>
  
   <h2>Entrada</h2>
   <p>A entrada consiste em uma sequência numérica.</p>
    
   <h2>Saída</h2>
   <p>A saída consiste em uma frase escrita.</p>
