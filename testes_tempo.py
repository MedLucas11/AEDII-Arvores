from arvore_avl import ArvoreAVL
import time, random


def inserir_avl(n, arvore_avl):
    for i in range(n):
        arvore_avl.inserir_livro(i, f"Livro {i}", f"Autor {i}", f"Editora {i}")
    
    return arvore_avl


def tempo_insercao_avl(n):
    arvore_avl = ArvoreAVL()

    start_time = time.time()
    arvore_avl = inserir_avl(n, arvore_avl)
    end_time = time.time()

    tempo_final = end_time - start_time

    print(f"Tempo para inserir {n} itens na árvore AVL: {tempo_final:.7f} s")
    return tempo_final, arvore_avl


def tempo_busca_avl(arvore, id):
    
    start_time = time.time()
    livro = arvore.buscar_livro(id)
    end_time = time.time()

    tempo_final = end_time - start_time
    
    print(f"Tempo para buscar o ID aleatório {id} na árvore AVL: {tempo_final:.7f} s")

    
    if livro is not None:
        print(f"ID - {livro.chave}\n{livro.titulo}\n{livro.autor}\n{livro.editora}")
    else:
        print(f"Livro com ID {id} não foi encontrado na árvore")
    
    
def tempo_remocao_avl(arvore, id):
   
    start_time = time.time()
    arvore.remover_livro(id)
    end_time = time.time()

    tempo_final = end_time - start_time
    
    print(f"O livro foi removido com sucesso.")
    print(f"Tempo para remover o ID aleatório {id} da árvore AVL: {tempo_final:.7f} s")
    arvore.verifica_arvore_balanceada()
    

def main():
    n = int(input("Digite a quantidade de itens que gostaria de inserir nas árvores para realizar os testes: "))

    id_busca = random.randint(0, n)
    id_remocao = random.randint(0, n)

    print("\n-- TESTE DO TEMPO DE INSERÇÃO DE ITENS --")
    avl_tempo, arvore_avl = tempo_insercao_avl(n)
    #rb_tempo, arvore_rb = tempo_insercao_rb(n)

    print(f"Em média, o tempo de inserção de cada item na árvore AVL foi: {avl_tempo/n:.7f} s")


    print("\n-- TESTE DO TEMPO DE BUSCA ALEATÓRIA --")
    tempo_busca_avl(arvore_avl, id_busca)
    #tempo_busca_rb(arvore_rb, id_busca)

    
    print("\n-- TESTE DO TEMPO DE REMOÇÃO ALEATÓRIA --")
    tempo_remocao_avl(arvore_avl, id_remocao)
    #tempo_remocao_rb(arvore_rb, id_remocao)


main()
