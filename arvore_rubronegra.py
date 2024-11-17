class NoRubroNegro:
    def __init__(self, chave, titulo, autor, editora):
        self.chave = chave
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.cor = "vermelho"  # Todos os novos nós são inicialmente vermelhos
        self.esquerda = None
        self.direita = None
        self.pai = None


class BibliotecaRubroNegra:
    def __init__(self):
        self.NULO = NoRubroNegro(None, None, None, None)
        self.NULO.cor = "preto"  # Nós NULOS são pretos
        self.raiz = self.NULO

    def _rotacao_esquerda(self, no):
        y = no.direita
        no.direita = y.esquerda
        if y.esquerda != self.NULO:
            y.esquerda.pai = no
        y.pai = no.pai
        if no.pai is None:
            self.raiz = y
        elif no == no.pai.esquerda:
            no.pai.esquerda = y
        else:
            no.pai.direita = y
        y.esquerda = no
        no.pai = y

    def _rotacao_direita(self, no):
        y = no.esquerda
        no.esquerda = y.direita
        if y.direita != self.NULO:
            y.direita.pai = no
        y.pai = no.pai
        if no.pai is None:
            self.raiz = y
        elif no == no.pai.direita:
            no.pai.direita = y
        else:
            no.pai.esquerda = y
        y.direita = no
        no.pai = y

    def _balancear_insercao(self, no):
        while no.pai and no.pai.cor == "vermelho":
            if no.pai == no.pai.pai.esquerda:
                tio = no.pai.pai.direita
                if tio.cor == "vermelho":  # Caso 1: O tio é vermelho
                    no.pai.cor = "preto"
                    tio.cor = "preto"
                    no.pai.pai.cor = "vermelho"
                    no = no.pai.pai
                else:
                    if no == no.pai.direita:  # Caso 2: O nó é filho direito
                        no = no.pai
                        self._rotacao_esquerda(no)
                    # Caso 3: O nó é filho esquerdo
                    no.pai.cor = "preto"
                    no.pai.pai.cor = "vermelho"
                    self._rotacao_direita(no.pai.pai)
            else:
                tio = no.pai.pai.esquerda
                if tio.cor == "vermelho":  # Caso 1: O tio é vermelho
                    no.pai.cor = "preto"
                    tio.cor = "preto"
                    no.pai.pai.cor = "vermelho"
                    no = no.pai.pai
                else:
                    if no == no.pai.esquerda:  # Caso 2: O nó é filho esquerdo
                        no = no.pai
                        self._rotacao_direita(no)
                    # Caso 3: O nó é filho direito
                    no.pai.cor = "preto"
                    no.pai.pai.cor = "vermelho"
                    self._rotacao_esquerda(no.pai.pai)
        self.raiz.cor = "preto"

    def inserir_livro(self, chave, titulo, autor, editora):
        novo_no = NoRubroNegro(chave, titulo, autor, editora)
        novo_no.esquerda = self.NULO
        novo_no.direita = self.NULO
        pai = None
        atual = self.raiz

        while atual != self.NULO:
            pai = atual
            if novo_no.chave < atual.chave:
                atual = atual.esquerda
            else:
                atual = atual.direita

        novo_no.pai = pai
        if pai is None:
            self.raiz = novo_no
        elif novo_no.chave < pai.chave:
            pai.esquerda = novo_no
        else:
            pai.direita = novo_no

        if novo_no.pai is None:
            novo_no.cor = "preto"
            return

        if novo_no.pai.pai is None:
            return

        self._balancear_insercao(novo_no)

    def buscar_livro(self, chave):
        atual = self.raiz
        while atual != self.NULO:
            if chave == atual.chave:
                return atual
            elif chave < atual.chave:
                atual = atual.esquerda
            else:
                atual = atual.direita
        return None

    def _transplante(self, u, v):
        if u.pai is None:
            self.raiz = v
        elif u == u.pai.esquerda:
            u.pai.esquerda = v
        else:
            u.pai.direita = v
        v.pai = u.pai

    def _minimo(self, no):
        while no.esquerda != self.NULO:
            no = no.esquerda
        return no

    def remover_livro(self, chave):
        no = self.buscar_livro(chave)
        if no is None:
            print(f"Nó com chave {chave} não encontrado.")
            return

        y = no
        y_cor_original = y.cor
        if no.esquerda == self.NULO:
            x = no.direita
            self._transplante(no, no.direita)
        elif no.direita == self.NULO:
            x = no.esquerda
            self._transplante(no, no.esquerda)
        else:
            y = self._minimo(no.direita)
            y_cor_original = y.cor
            x = y.direita
            if y.pai == no:
                x.pai = y
            else:
                self._transplante(y, y.direita)
                y.direita = no.direita
                y.direita.pai = y
            self._transplante(no, y)
            y.esquerda = no.esquerda
            y.esquerda.pai = y
            y.cor = no.cor

        if y_cor_original == "preto":
            self._balancear_remocao(x)

    def _balancear_remocao(self, x):
        while x != self.raiz and x.cor == "preto":
            if x == x.pai.esquerda:
                w = x.pai.direita
                if w.cor == "vermelho":
                    w.cor = "preto"
                    x.pai.cor = "vermelho"
                    self._rotacao_esquerda(x.pai)
                    w = x.pai.direita
                if w.esquerda.cor == "preto" and w.direita.cor == "preto":
                    w.cor = "vermelho"
                    x = x.pai
                else:
                    if w.direita.cor == "preto":
                        w.esquerda.cor = "preto"
                        w.cor = "vermelho"
                        self._rotacao_direita(w)
                        w = x.pai.direita
                    w.cor = x.pai.cor
                    x.pai.cor = "preto"
                    w.direita.cor = "preto"
                    self._rotacao_esquerda(x.pai)
                    x = self.raiz
            else:
                w = x.pai.esquerda
                if w.cor == "vermelho":
                    w.cor = "preto"
                    x.pai.cor = "vermelho"
                    self._rotacao_direita(x.pai)
                    w = x.pai.esquerda
                if w.direita.cor == "preto" and w.esquerda.cor == "preto":
                    w.cor = "vermelho"
                    x = x.pai
                else:
                    if w.esquerda.cor == "preto":
                        w.direita.cor = "preto"
                        w.cor = "vermelho"
                        self._rotacao_esquerda(w)
                        w = x.pai.esquerda
                    w.cor = x.pai.cor
                    x.pai.cor = "preto"
                    w.esquerda.cor = "preto"
                    self._rotacao_direita(x.pai)
                    x = self.raiz
        x.cor = "preto"

