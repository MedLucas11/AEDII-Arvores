from arvore_rubronegra import BibliotecaRubroNegra
import time, random


def inserir_rubro_negra(n, arvore):
    for i in range(n):
        arvore.adicionar_livro(i, f"Livro {i}", f"Autor {i}", f"Editora {i}")
    return arvore


def tempo_insercao_rubro_negra(n):
    arvore = BibliotecaRubroNegra()

    start_time = time.time()
    arvore = inserir_rubro_negra(n, arvore)
    end_time = time.time()

    tempo_final = end_time - start_time

    print(f"Tempo para inserir {n} itens na árvore Rubro-Negra: {tempo_final:.7f} s")
    return tempo_final, arvore


def tempo_busca_rubro_negra(arvore, id):
    start_time = time.time()
    livro = arvore.buscar_livro(id)
    end_time = time.time()

    tempo_final = end_time - start_time

    print(f"Tempo para buscar o ID aleatório {id} na árvore Rubro-Negra: {tempo_final:.7f} s")

    if livro is not None:
        print(f"ID - {livro.chave}\n{livro.titulo}\n{livro.autor}\n{livro.editora}")  # Alteração: usar livro.chave
    else:
        print(f"Livro com ID {id} não foi encontrado na árvore")


def tempo_remocao_rubro_negra(arvore, chave):
    inicio = time.time()
    arvore.remover_livro(chave)
    fim = time.time()
    tempo_total = fim - inicio
    print(f"Tempo de remoção do livro com chave {chave}: {tempo_total:.6f} segundos.")



def main():
    n = int(input("Digite a quantidade de itens que gostaria de inserir na árvore para realizar os testes: "))

    id_busca = random.randint(0, n - 1)

    print("\n-- TESTE DO TEMPO DE INSERÇÃO DE ITENS --")
    rubro_negra_tempo, arvore_rubro_negra = tempo_insercao_rubro_negra(n)

    print(f"Em média, o tempo de inserção de cada item na árvore Rubro-Negra foi: {rubro_negra_tempo / n:.7f} s")

    print("\n-- TESTE DO TEMPO DE BUSCA ALEATÓRIA --")
    tempo_busca_rubro_negra(arvore_rubro_negra, id_busca)

    print("\n-- TESTE DO TEMPO DE REMOÇÃO ALEATÓRIA --")
    tempo_remocao_rubro_negra(arvore_rubro_negra, id_busca)  # Chamada da remoção para demonstrar


if __name__ == "__main__":
    main()
