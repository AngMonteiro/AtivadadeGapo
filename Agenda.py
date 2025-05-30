# Agenda simples em Python
agenda = {}

def adicionar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    agenda[nome] = {"telefone": telefone, "email": email}
    print(f"\nContato '{nome}' adicionado com sucesso.\n")

def visualizar_contatos():
    if not agenda:
        print("\nAgenda vazia.\n")
        return
    print("\n--- Contatos ---")
    for nome, dados in agenda.items():
        print(f"Nome: {nome}")
        print(f"Telefone: {dados['telefone']}")
        print(f"Email: {dados['email']}\n")

def buscar_contato():
    nome = input("Digite o nome para buscar: ")
    contato = agenda.get(nome)
    if contato:
        print(f"\nNome: {nome}")
        print(f"Telefone: {contato['telefone']}")
        print(f"Email: {contato['email']}\n")
    else:
        print(f"\nContato '{nome}' não encontrado.\n")

def remover_contato():
    nome = input("Digite o nome do contato a remover: ")
    if nome in agenda:
        del agenda[nome]
        print(f"\nContato '{nome}' removido.\n")
    else:
        print(f"\nContato '{nome}' não encontrado.\n")

def menu():
    while True:
        print("=== AGENDA ===")
        print("1. Adicionar contato")
        print("2. Visualizar contatos")
        print("3. Buscar contato")
        print("4. Remover contato")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_contato()
        elif opcao == '2':
            visualizar_contatos()
        elif opcao == '3':
            buscar_contato()
        elif opcao == '4':
            remover_contato()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# Inicia o programa
menu()
