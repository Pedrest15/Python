class Pilha():
  def __init__(self, dado = None, prox = None):
    self.dado = dado
    self.prox = prox

  def push(self, dado):
    if self.dado == None:
      self.dado = dado
    else:
      atual = self
      while atual.prox is not None:
        atual = atual.prox
      atual.prox = Pilha(dado)
    return

  def pop(self):
    if self.prox == None: #pilha com um elemento apenas
      self.dado = None
      return
    atual = self
    ant = None
    while atual.prox is not None:
      ant = atual
      atual = atual.prox
    ant.prox = None
    return
    
  def estah_vazia(self):
    if self.dado == None:
      return True
    return False

  def tamanho(self):
    if self.estah_vazia():
      return 0
    cnt = 1
    atual = self
    while atual.prox is not None:
      atual = atual.prox
      cnt += 1
    return cnt

  def topo(self):
    atual = self
    while atual.prox is not None:
      atual = atual.prox
    return atual.dado
    
  def imprimir(self):
    atual = self
    while atual.prox is not None:
      atual = atual.prox
    print(atual.dado)
    return

def main():
  pilha = Pilha()
  while(1):
    elemento = int(input())
    if elemento == -1:
      break
    elif elemento == 0:
      print('Quantidade de elementos: {}'.format(pilha.tamanho()))
    elif elemento == 10:
      print(pilha.topo())
    elif elemento == 20:
      valor1 = pilha.topo()
      pilha.pop()
      valor2 = pilha.topo()
      pilha.pop()
      pilha.push(valor1 + valor2)
    else:
      pilha.push(elemento)

  print()
  tam = pilha.tamanho()
  if tam == 0:
    print("Pilha Vazia")
  else:
      
      for _ in range(tam):
        pilha.imprimir()
        pilha.pop()
    
main()