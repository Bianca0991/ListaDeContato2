agenda = {}

def adicionar_contato(nome, telefone):
    agenda[nome] = telefone
    print(f"Contato {nome} adicionado com sucesso!")

def listar_contatos():
    if agenda:
        print("Lista de contatos:")
        for nome, telefone in agenda.items():
            print(f"Nome: {nome}, Telefone: {telefone}")
    else:
        print("A agenda está vazia.")

def buscar_contato(nome):
    if nome in agenda:
        print(f"Nome: {nome}, Telefone: {agenda[nome]}")
    else:
        print(f"Contato {nome} não encontrado.")

def menu():
    print("\n### Agenda Telefônica ###")
    print("1 - Adicionar contato")
    print("2 - Listar contatos")
    print("3 - Buscar contato por nome")
    print("4 - Sair")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            adicionar_contato(nome, telefone)
        elif opcao == '2':
            listar_contatos()
        elif opcao == '3':
            nome = input("Digite o nome do contato que deseja buscar: ")
            buscar_contato(nome)
        elif opcao == '4':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if _name_ == "_main_":
    main()