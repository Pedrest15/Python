from typing import Any

class ArvBin:
    def __init__(self, dado: Any = None, esq: Any = None, dir: Any = None):
        self.dado: Any = dado
        self.esq: Any = esq
        self.dir: Any = dir
    
    def inserir(self, valor: Any):
        if self.dado == None: #no raiz vazio
            self.dado = valor
            return
        
        if valor < self.dado:
            if self.esq is None: #no vazio
                self.esq = ArvBin()
                self.esq.dado = valor
                return
            self.esq.inserir(valor) #chamada recursiva
        else:
            if self.dir is None: #no vazio
                self.dir = ArvBin()
                self.dir.dado = valor
                return
            self.dir.inserir(valor) #chamada recursiva

    def remover(self, valor: Any) -> bool:
        if self.dado == None: #no raiz vazio
            return False #erro na remocao

        atual = self
        while atual is not None: #busca o no desejado
            if atual.dado == valor:
                break
            elif valor < atual.dado:
                pai = atual
                atual = atual.esq
                esta_esq = True
            else:
                pai = atual
                atual = atual.dir
                esta_esq = False     

        if (atual is None) or (atual.dado != valor):
            return False #erro na remocao

        num_filhos = 0
        if atual.esq != None:
            num_filhos += 1
        if atual.dir != None:
            num_filhos += 1

        if num_filhos == 0: #no folha
            if esta_esq:
                pai.esq = None
            else:
                pai.dir = None

        elif num_filhos == 1:
            if esta_esq:
                if atual.esq is not None:
                    pai.esq = atual.esq
                elif atual.dir is not None:
                    pai.esq = atual.dir
            else:
                if atual.esq is not None:
                    pai.dir = atual.esq
                elif atual.dir is not None:
                    pai.dir = atual.dir

        elif num_filhos == 2:
            menor = atual.dir
            pai_menor = atual
            while menor.esq is not None: #busca o menor elemento na subarvore a direita do atual
                pai_menor = menor
                menor = menor.esq
 
            if esta_esq:
                if atual.esq is not None:
                    menor.esq = atual.esq
                if atual.dir is not None and atual.dir is not menor:
                    menor.dir = atual.dir
                pai.esq = menor

            else:
                if atual.esq is not None:
                    menor.esq = atual.esq
                if atual.dir is not None and atual.dir is not menor:
                    menor.dir = atual.dir
                pai_menor.esq = None
                pai.dir = menor
        del atual

        return True #remocao concluida

    def buscar(self, valor: Any) -> bool:
        if self.dado == None:
            return False #falha na busca

        atual = self
        while atual is not None:
            if atual.dado == valor:
                return True #elemento encontrado
            if valor < atual.dado:
                atual = atual.esq
            else:
                atual = atual.dir
        
        return False #falha na busca

    def arv_vazia(self) -> bool:
        if self.dado == None:
            return True #esta vazia
        return False

    def pre_ordem(self):
        if self.dado == None:
            return
        
        print(self.dado)

        if self.esq is not None:
            self.esq.pre_ordem()

        if self.dir is not None:
            self.dir.pre_ordem()

    def em_ordem(self):
        if self.dado == None:
            return
        
        if self.esq is not None:
            self.esq.em_ordem()

        print(self.dado)

        if self.dir is not None:
            self.dir.em_ordem()

    def pos_ordem(self):
        if self.dado == None:
            return

        if self.esq is not None:
            self.esq.pos_ordem()

        if self.dir is not None:
            self.dir.pos_ordem()

        print(self.dado)

if __name__ == '__main__':
    arvore = ArvBin()
    lista = [40, 20, 50, 10, 30, 70, 60, 11, 35, 25, 45]

    for i in lista:
        arvore.inserir(i)
    
    print('--> Testando ordens de impressão:')
    arvore.pre_ordem()
    print('-----xx-----')
    arvore.em_ordem()
    print('-----xx-----')
    arvore.pos_ordem()
    print()
    
    print('--> Testando remocao:')
    print(arvore.remover(50))
    arvore.pre_ordem()
