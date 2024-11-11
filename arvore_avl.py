class NodeAVL:
    def __init__(self, id_livro, titulo, autor, editora):
        self.chave = id_livro
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.emprestado_por = []
        self.disponivel = True
        self.esquerda = None
        self.direita = None
        self.altura = 1


class ArvoreAVL:
    def __init__(self):
        self.raiz = None
    
    
    def _altura(self, node):
        if not node:
            return 0
        return node.altura
    
   
    def _atualiza_altura(self, node):
        node.altura = 1 + max(self._altura(node.esquerda), self._altura(node.direita))

    
    def _fator_balanceamento(self, node):
        if not node:
            return 0
        return self._altura(node.esquerda) - self._altura(node.direita)
    
    
    def _rotacao_direita(self, a):
        b = a.esquerda
        T2 = b.direita

        b.direita = a
        a.esquerda = T2

        self._atualiza_altura(a)
        self._atualiza_altura(b)

        return b

    
    def _rotacao_esquerda(self, b):
        a = b.direita
        T2 = a.esquerda

        a.esquerda = b
        b.direita = T2

        self._atualiza_altura(b)
        self._atualiza_altura(a)

        return a
    
    
    def _rotacao_dupla_esquerda(self, a):
        a.direita = self._rotacao_direita(a.direita)
        return self._rotacao_esquerda(a)
    
    
    def _rotacao_dupla_direita(self, a):
        a.esquerda = self._rotacao_esquerda(a.esquerda)
        return self._rotacao_direita(a)
    
    
    def inserir(self, raiz, id_livro, titulo, autor, editora):
        if not raiz:
            return NodeAVL(id_livro, titulo, autor, editora)
        elif id_livro < raiz.chave:
            raiz.esquerda = self.inserir(raiz.esquerda, id_livro, titulo, autor, editora)
        else:
            raiz.direita = self.inserir(raiz.direita, id_livro, titulo, autor, editora)
        
        self._atualiza_altura(raiz)

        balanco = self._fator_balanceamento(raiz)

        if balanco > 1 and id_livro < raiz.esquerda.chave:
            return self._rotacao_direita(raiz)
        
        if balanco < -1 and id_livro > raiz.direita.chave:
            return self._rotacao_esquerda(raiz)
        
        if balanco > 1 and id_livro > raiz.esquerda.chave:
            return self._rotacao_dupla_direita(raiz)
        
        if balanco < -1 and id_livro < raiz.direita.chave:
            return self._rotacao_dupla_esquerda(raiz)

        return raiz

    
    def inserir_livro(self, id_livro, titulo, autor, editora):
        self.raiz = self.inserir(self.raiz, id_livro, titulo, autor, editora)

    
    def buscar(self, raiz, id_livro):
        if raiz is None or raiz.chave == id_livro:
            return raiz
        
        if id_livro < raiz.chave:
            return self.buscar(raiz.esquerda, id_livro)
        
        return self.buscar(raiz.direita, id_livro)
    
    
    def buscar_livro(self, id_livro):
        return self.buscar(self.raiz, id_livro)

    
    def remover(self, raiz, id_livro):
        if raiz is None:
            return raiz
        
        if id_livro < raiz.chave:
            raiz.esquerda = self.remover(raiz.esquerda, id_livro)
        
        elif id_livro > raiz.chave:
            raiz.direita = self.remover(raiz.direita, id_livro)
        
        else:
            if raiz.esquerda is None and raiz.direita is None:
                raiz = None
            
            elif raiz.esquerda is None:
                raiz = raiz.direita
            
            elif raiz.direita is None:
                raiz = raiz.esquerda
            
            else:
                
                raiz.chave, raiz.titulo, raiz.autor, raiz.editora = self._minimo(raiz.direita)
                raiz.direita = self.remover(raiz.direita, raiz.chave)
        
        if raiz is not None:
            self._atualiza_altura(raiz)
            balanco = self._fator_balanceamento(raiz)

            # Verifica se a árvore precisa de alguma rotação
            if balanco > 1 and self._fator_balanceamento(raiz.esquerda) >= 0:
                return self._rotacao_direita(raiz)
            
            if balanco < -1 and self._fator_balanceamento(raiz.direita) <= 0:
                return self._rotacao_esquerda(raiz)
            
            if balanco > 1 and self._fator_balanceamento(raiz.esquerda) < 0:
                return self._rotacao_dupla_direita(raiz)
            
            if balanco < -1 and self._fator_balanceamento(raiz.direita) > 0:
                return self._rotacao_dupla_esquerda(raiz)
        
        return raiz
    
    
    def _minimo(self, raiz):
        atual = raiz
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual.chave, atual.titulo, atual.autor, atual.editora
    
   
    def remover_livro(self, id_livro):
        self.raiz = self.remover(self.raiz, id_livro)

    
    def _verifica_balanceamento(self, node):
        if node is None:
            return True
        
        balanco = self._fator_balanceamento(node)

        if balanco < -1 or balanco > 1:
            print(f"Nó desbalanceado encontrado! ID: {node.chave}, Fator de Balanceamento: {balanco}")
        
        return self._verifica_balanceamento(node.esquerda) and self._verifica_balanceamento(node.direita)
    
    
    def verifica_arvore_balanceada(self):
        if self._verifica_balanceamento(self.raiz):
            print("A árvore AVL está balanceada!")
        else:
            print("A árvore AVL NÃO está balanceada")
    
    
    def emprestimo(self, id_livro, aluno):
        livro = self.buscar_livro(id_livro)
        livro.emprestado_por.append(aluno)
        livro.disponivel = False
        
        print(f"Empréstimo realizado com sucesso!")
    

    def lista_emprestimos(self, id_livro):
        livro = self.buscar_livro(id_livro)

        print(f"Lista de empréstimos do livro {id_livro} - {livro.titulo}: {livro.emprestado_por}")


    def devolucao(self, id_livro):
        livro = self.buscar_livro(id_livro)
        livro.disponivel = True

        print(f"{id_livro} - {livro.titulo} devolvido com sucesso!")
