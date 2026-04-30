from funcoes import *

def menu():
    print("\n--- MENU ---")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Buscar")
    print("4 - Atualizar")
    print("5 - Remover")
    print("0 - Sair")


def main():
    lista = carregar()

    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar(lista)

        elif opcao == "2":
            listar(lista)

        elif opcao == "3":
            buscar(lista)

        elif opcao == "4":
            atualizar(lista)

        elif opcao == "5":
            remover(lista)

        elif opcao == "0":
            salvar(lista)
            print("💾 Dados salvos. Encerrando...")
            break

        else:
            print("❌ Opção inválida.")

        # salva automaticamente após qualquer ação válida
        salvar(lista)


if __name__ == "__main__":
    main()