class Pilha():
  def __init__(self, dado = None, prox = None):
    self.dado = []

  def push(self, elemento):
    self.dado.append(elemento)

  def pop(self):
    if len(self.dado) != 0: #se a pilha não estiver vazia
      self.dado.pop(len(self.dado) - 1)

  def tamanho(self):
    return len(self.dado)

def main():
  pilha = Pilha()
  
  while(1):
    codigo = int(input())
    if codigo == -1:
      break
    elif codigo == 0:
      pilha.pop()
    else:
      pilha.push(codigo)

  #percorre a pilha do topo para o começo
  for letra in pilha.dado[::-1]:
    #imprime caracter ASCII do valor na pilha
    print(chr(letra), end='')

main()
