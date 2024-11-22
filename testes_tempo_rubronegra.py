import time
from arvore_rubronegra import BibliotecaRubroNegra


def inserir_rb(n, arvore_rb):
    for i in range(n):
        arvore_rb.inserir_livro(i, f"Livro {i}", f"Autor {i}", f"Editora {i}")
    return arvore_rb


def tempo_insercao_rb(n):
    arvore_rb = BibliotecaRubroNegra()

    start_time = time.time()
    arvore_rb = inserir_rb(n, arvore_rb)
    end_time = time.time()

    tempo_final = end_time - start_time

    print(f"Tempo para inserir {n} itens na árvore Rubro-Negra: {tempo_final:.7f} s")
    return tempo_final, arvore_rb


def tempo_busca_rb(arvore, id):
    start_time = time.time()
    livro = arvore.buscar_livro(id)
    end_time = time.time()

    tempo_final = end_time - start_time
    
    print(f"Tempo para buscar o ID aleatório {id} na árvore Rubro-Negra: {tempo_final:.7f} s")

    if livro is not None:
        print(f"ID - {livro.chave}\n{livro.titulo}\n{livro.autor}\n{livro.editora}")
    else:
        print(f"Livro com ID {id} não foi encontrado na árvore")


def tempo_remocao_rb(arvore, id):
    start_time = time.time()
    arvore.remover_livro(id)
    end_time = time.time()

    tempo_final = end_time - start_time
    
    print(f"\nO livro foi removido com sucesso.")
    print(f"Tempo para remover o ID aleatório {id} da árvore Rubro-Negra: {tempo_final:.7f} s")
    arvore.verificar_balanceamento()


def remocao_n_rb(arvore, n):
    
    start_time = time.time()
    for i in range(n):
        arvore.remover_livro(i)
    end_time = time.time()

    tempo_final = end_time - start_time

    print(f"\nTempo para remover {n} itens da árvore Rubro-Negra: {tempo_final:.7f} s")
    arvore.verificar_balanceamento()