from arvore_avl import ArvoreAVL
import pickle


def salvar_biblioteca(biblioteca, nome_arquivo):
    nome_arquivo += ".pkl"
    with open(nome_arquivo, 'wb') as arquivo:
        pickle.dump(biblioteca, arquivo)
    print("\nBiblioteca salva com sucesso!")


def carregar_biblioteca(nome_arquivo):
    try:
        with open(nome_arquivo, 'rb') as arquivo:
            biblioteca = pickle.load(arquivo)
        print("\nBiblioteca carregada com sucesso!")
        return biblioteca
    except FileNotFoundError:
        print("\nArquivo de biblioteca não encontrado.")


def add_livro(biblioteca):
    while True:
        id_livro = int(input("Digite o ID do livro a ser adicionado: "))
        existencia = biblioteca.buscar_livro(id_livro)

        if existencia is not None:
            print("\nEste ID já existe na biblioteca, digite outro (ou remova o existente).")
        else:
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o(a) autor(a) do livro: ")
            editora = input("Digite a editora do livro: ")
            biblioteca.inserir_livro(id_livro, titulo, autor, editora)
            print("\nLivro adicionado com sucesso!")
            break
            

def del_livro(biblioteca):
    while True:
        id_livro = int(input("Digite o ID do livro a ser removido: "))
        existencia = biblioteca.buscar_livro(id_livro)

        if existencia is None:
            print("\nEste ID não existe na biblioteca. Não foi possível remover.")
        else:
            biblioteca.remover_livro(id_livro)
            print("\nLivro removido com sucesso!")
            break


def info(biblioteca, id_livro):
    livro = biblioteca.buscar_livro(id_livro)
    
    if livro is not None:
        print(f"\nID: {id_livro}")
        print(f"Título: {livro.titulo}")
        print(f"Autor: {livro.autor}")
        print(f"Editora: {livro.editora}\n")
    
    else:
        print("\nLivro não encontrado!")


def disponibilidade(biblioteca, id_livro):
    livro = biblioteca.buscar_livro(id_livro)
    
    if livro is not None:
        if livro.disponivel:
            return True
        else:
            return False
    else:
        print("\nLivro não encontrado na biblioteca")


def emprestar(biblioteca, id_livro, aluno):
        return biblioteca.emprestimo(id_livro, aluno)


def lista_emprestimo(biblioteca, id_livro):
    livro = biblioteca.buscar_livro(id_livro)
    
    if livro is not None:
        return biblioteca.lista_emprestimos(id_livro)
    else:
        print("\nLivro não encontrado na biblioteca")


def devolver(biblioteca, id_livro):
    livro = biblioteca.buscar_livro(id_livro)

    if livro is not None:
        return biblioteca.devolucao(id_livro)
    else:
        print("O livro não foi emprestado desta biblioteca")


def exibir_menu():
    print("\n-- Sistema gerenciador de bibliotecas (Árvore AVL) --\n")
    print("1. Criar biblioteca")
    print("2. Selecionar biblioteca")
    print("3. Adicionar livro à biblioteca")
    print("4. Remover livro da biblioteca")
    print("5. Buscar informações de livro na biblioteca")
    print("6. Verificar disponibilidade do livro")
    print("7. Emprestar livro")
    print("8. Listar empréstimos")
    print("9. Devolver livro")
    print("10. Salvar biblioteca")
    print("11. Carregar biblioteca")
    print("12. Verificar balanceamento da árvore")
    print("13. Sair do sistema")


def menu_principal():
    bibliotecas = {}
    biblioteca_atual = None
    
    while True:
        exibir_menu()
        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            nome_biblioteca = input("Digite o nome que deseja para biblioteca: ")
            nova_biblioteca = ArvoreAVL()
            bibliotecas[nome_biblioteca] = nova_biblioteca
            print(f"\n{nome_biblioteca} criada com sucesso!")
        
        elif opcao == 2:
            if not bibliotecas:
                print("\nNenhuma biblioteca disponível. Crie uma primeiro")
            else:
                print("\nBibliotecas disponíveis:")
                for nome in bibliotecas.keys():
                    print(f"- {nome}")
                escolha = input("Digite o nome da biblioteca que gostaria de gerenciar: ")
                if escolha in bibliotecas:
                    biblioteca_atual = bibliotecas[escolha]
                    print(f"\nBiblioteca '{escolha}' selecionada.")
                else:
                    print("\nBiblioteca não encontrada.")
        
        elif opcao == 3:
            if biblioteca_atual is None:
                print("\nNenhuma biblioteca para gerenciar selecionada!")
            else:
                add_livro(biblioteca_atual)
        
        elif opcao == 4:
            if biblioteca_atual is None:
                print("\nNenhuma biblioteca para gerenciar selecionada!")
            else:
                del_livro(biblioteca_atual)
        
        elif opcao == 5:
            if biblioteca_atual is None:
                print("\nNenhuma biblioteca para gerenciar selecionada!")
            else:
                id_livro = int(input("Digite o ID do livro que deseja saber mais: "))
                info(biblioteca_atual, id_livro)

        elif opcao == 6:
            if biblioteca_atual is None:
                print("\nNenhuma biblioteca para gerenciar selecionada!")
            else:
                id_livro = int(input("Digite o ID do livro que deseja verificar a disponibilidade: "))
                disp = disponibilidade(biblioteca_atual, id_livro)
                
                if disp == True:
                    print("\nLivro disponível para empréstimo!")
                else:
                    print("\nLivro NÃO disponível para empréstimo. Aguarde a devolução")

        elif opcao == 7:
            if biblioteca_atual is None:
                print("\nNenhuma biblioteca para gerenciar selecionada!")
            else:
                id_livro = int(input("Digite o ID do livro: "))
                if disponibilidade(biblioteca_atual, id_livro):
                    aluno = []
                    nome = input("Digite o nome do aluno que irá emprestar: ")
                    ra = input("Digite o RA do aluno que irá emprestar: ")
                    aluno.append(nome)
                    aluno.append(ra)
                    emprestar(biblioteca_atual, id_livro, aluno)
                else:
                    print("\nLivro já emprestado. Aguarde a devolução")
        

        elif opcao == 8:
            if biblioteca_atual is None:
                print("Nenhuma biblioteca para gerenciar selecionada!")
            else:
                id_livro = int(input("Digite o ID do livro que gostaria de saber a lista de empréstimos: "))
                lista_emprestimo(biblioteca_atual, id_livro)
        

        elif opcao == 9:
            if biblioteca_atual is None:
                print("Nenhuma biblioteca para gerenciar selecionada!")
            else:
                id_livro = int(input("Digite o ID do livro que gostaria de devolver: "))
                devolver(biblioteca_atual, id_livro)
        
        elif opcao == 10:
            if biblioteca_atual is None:
                print("Nenhuma biblioteca para gerenciar selecionada!")
            else:
                nome = input("Digite o nome que gostaria salvar o arquivo: ")
                salvar_biblioteca(biblioteca_atual, nome)
        
        elif opcao == 11:
            nome = input("Digite o nome do arquivo de biblioteca para carregar: ")
            biblioteca_atual = carregar_biblioteca(nome)
        
        
        elif opcao == 12:
            if biblioteca_atual is None:
                print("Nenhuma biblioteca para gerenciar selecionada!")
            else:
                biblioteca_atual.verifica_arvore_balanceada()
        
        elif opcao == 13:
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Digite uma opção válida.")

if __name__ == "__main__":
    menu_principal()
