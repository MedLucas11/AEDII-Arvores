# Define o nó da árvore AVL, com os atributos desejados para o sistema de biblioteca
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
    # A árvore é iniciada apenas com uma raíz vazia
    def __init__(self):
        self.raiz = None
    
    
    # Método para retornar a altura do nó, presente na estrutura NodeAVL
    def _altura(self, node):
        if not node:
            return 0
        return node.altura
    
   
    # Método para atualizar a altura: 1 (próprio nó) + a maior altura entre a subárvore esquerda e direita
    def _atualiza_altura(self, node):
        node.altura = 1 + max(self._altura(node.esquerda), self._altura(node.direita))

    
    # Método para calcular o fator de balanceamento do nó. Caso seja maior que 1, a árvore estará "pesada" à esquerda. Se for menor que -1 estará "pesada" à direita.
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
    
    
    # Método para inserir itens na árvore.
    def inserir(self, raiz, id_livro, titulo, autor, editora):
        # Caso base: ao encontrar um nó Nulo (None), atribui um novo nó com as caracteríticas passadas 
        if not raiz:
            return NodeAVL(id_livro, titulo, autor, editora)
        
        # Se o id a ser inserido for menor que o nó atual, insere recursivamente na subárvore esquerda
        elif id_livro < raiz.chave:
            raiz.esquerda = self.inserir(raiz.esquerda, id_livro, titulo, autor, editora)
        
        # Se o id a ser inserido for maior que o nó atual, insere recursivamente na subárvore direita
        else:
            raiz.direita = self.inserir(raiz.direita, id_livro, titulo, autor, editora)
        
        self._atualiza_altura(raiz) # Atualiza a altura dos nós que foram percorridos

        balanco = self._fator_balanceamento(raiz) # Calcula o fator de balanceamento dos nós percorridos

        # Se encontrar desbalanceamento, realiza as rotações específicas para balancear
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

    
    # Método para buscar uma chave na árvore
    def buscar(self, raiz, id_livro):
        if raiz is None or raiz.chave == id_livro:
            return raiz
        
        if id_livro < raiz.chave:
            return self.buscar(raiz.esquerda, id_livro)
        
        return self.buscar(raiz.direita, id_livro)
    
    
    def buscar_livro(self, id_livro):
        return self.buscar(self.raiz, id_livro)

    
    # Método para remover uma chave da árvore e balancear caso necessário
    def remover(self, raiz, id_livro):
        # Se a raiz está vazia, não há o que remover.
        if raiz is None:
            return raiz
        
        # Se o id a ser removido for menor que o nó atual, percorre recursivamente a subárvore esquerda
        if id_livro < raiz.chave:
            raiz.esquerda = self.remover(raiz.esquerda, id_livro)
        
        # Se o id a ser removido for maior que o nó atual, percorre recursivamente a subárvore direita
        elif id_livro > raiz.chave:
            raiz.direita = self.remover(raiz.direita, id_livro)
        
        # Ao encontrar o nó a ser removido, entramos nos casos de remoção da ABB
        else:
            # Se o nó for uma folha, remover normalmente
            if raiz.esquerda is None and raiz.direita is None:
                raiz = None
            
            # Se o nó só possui filho direito, remove o nó alvo e o filho se torna o novo nó
            elif raiz.esquerda is None:
                raiz = raiz.direita
            
            # Se o nó só possui filho esquerdo, remove o nó alvo e o filho se torna o novo nó
            elif raiz.direita is None:
                raiz = raiz.esquerda
            
            # Se o nó possui ambos os filhos, escolhe a menor das chaves maiores que o nó para tomar o lugar.
            else:
                raiz.chave, raiz.titulo, raiz.autor, raiz.editora = self._minimo(raiz.direita)
                raiz.direita = self.remover(raiz.direita, raiz.chave) # Remove a chave escolhida da subárvore direita, para não haver duplicatas e rebalancear caso necessário.

        
        # Se a árvore não ficar vazia, entramos nos casos de balanceamento.
        if raiz is not None:
            self._atualiza_altura(raiz)
            balanco = self._fator_balanceamento(raiz)

            if balanco > 1 and self._fator_balanceamento(raiz.esquerda) >= 0:
                return self._rotacao_direita(raiz)
            
            if balanco < -1 and self._fator_balanceamento(raiz.direita) <= 0:
                return self._rotacao_esquerda(raiz)
            
            if balanco > 1 and self._fator_balanceamento(raiz.esquerda) < 0:
                return self._rotacao_dupla_direita(raiz)
            
            if balanco < -1 and self._fator_balanceamento(raiz.direita) > 0:
                return self._rotacao_dupla_esquerda(raiz)
        
        return raiz
    
    
    # Método auxiliar da remoção, para encontrar a menor chave e retornar todos seus atributos.
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
            print(f"\nNó desbalanceado encontrado! ID: {node.chave}, Fator de Balanceamento: {balanco}")
        
        return self._verifica_balanceamento(node.esquerda) and self._verifica_balanceamento(node.direita)
    
    
    def verifica_arvore_balanceada(self):
        if self._verifica_balanceamento(self.raiz):
            print("\nA árvore AVL está balanceada!")
        else:
            print("\nA árvore AVL NÃO está balanceada")
    
    
    def emprestimo(self, id_livro, aluno):
        livro = self.buscar_livro(id_livro)
        livro.emprestado_por.append(aluno)
        livro.disponivel = False
        
        print(f"\nEmpréstimo realizado com sucesso!")
    

    def lista_emprestimos(self, id_livro):
        livro = self.buscar_livro(id_livro)

        print(f"\nLista de empréstimos do livro {id_livro} - {livro.titulo}: {livro.emprestado_por}")


    def devolucao(self, id_livro):
        livro = self.buscar_livro(id_livro)
        livro.disponivel = True

        print(f"\n{id_livro} - {livro.titulo} devolvido com sucesso!")
