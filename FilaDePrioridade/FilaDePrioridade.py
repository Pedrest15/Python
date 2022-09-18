class Pessoa():
  def __init__(self, nome = None, idade = None, caso_grave = None):
    self.nome = nome
    self.idade = idade
    self.caso_grave = caso_grave
    self.prioridade = 0

  def _prioridade(self):
    if self.caso_grave == 1:
      self.prioridade += 2
    if self.idade >= 60:
      self.prioridade += 1

class Fila():
  def __init__(self):
    self.dado = []

  def inserir(self, elemento):
    assert isinstance(elemento, Pessoa)
    self.dado.append(elemento)
  
  def remover(self):
    self.dado.pop(0)




def ordena_fila(fila):
  i = len(fila.dado) - 1
  while (fila.dado[i].prioridade > fila.dado[i - 1].prioridade) and i > 0:
    aux = fila.dado[i-1]
    fila.dado[i-1] = fila.dado[i]
    fila.dado[i] = aux
    i -= 1  

def entra(fila, acao):
  pessoa = Pessoa(acao[1], int(acao[2]), int(acao[3]))
  pessoa._prioridade()
  fila.inserir(pessoa)
  ordena_fila(fila)

def sai(fila):
  if len(fila.dado) == 0:
    print('FILA VAZIA')
  else:
    print("{} {} {}".format(fila.dado[0].nome, fila.dado[0].idade, fila.dado[0].caso_grave))
    fila.remover()
        
def main():
  fila = Fila()
  
  num_acoes = int(input(""))

  for _ in range(num_acoes):
    acao = input('')
    acao = acao.split(' ')
    if len(acao) > 1: #comando ENTRA 
      entra(fila, acao)
    else: #comando SAI
      sai(fila)
      
main()