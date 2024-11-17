import random
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
    
    print(f"O livro foi removido com sucesso.")
    print(f"Tempo para remover o ID aleatório {id} da árvore Rubro-Negra: {tempo_final:.7f} s")


def main():
    n = int(input("Digite a quantidade de itens que gostaria de inserir nas árvores para realizar os testes: "))

    id_busca = random.randint(0, n-1)
    id_remocao = random.randint(0, n-1)

    print("\n-- TESTE DO TEMPO DE INSERÇÃO DE ITENS --")
    rb_tempo, arvore_rb = tempo_insercao_rb(n)
    print(f"Em média, o tempo de inserção de cada item na árvore Rubro-Negra foi: {rb_tempo/n:.7f} s")

    print("\n-- TESTE DO TEMPO DE BUSCA ALEATÓRIA --")
    tempo_busca_rb(arvore_rb, id_busca)

    print("\n-- TESTE DO TEMPO DE REMOÇÃO ALEATÓRIA --")
    tempo_remocao_rb(arvore_rb, id_remocao)


main()

