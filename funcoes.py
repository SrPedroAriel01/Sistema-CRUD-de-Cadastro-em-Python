import json
from pessoa import Pessoa

# VALIDADORES

def validar_nome():
    while True:
        nome = input("Nome: ").strip()
        if nome != "":
            return nome
        print("❌ Nome não pode ser vazio.")


def validar_idade():
    while True:
        try:
            idade = int(input("Idade: "))
            if idade >= 0:
                return idade
            else:
                print("❌ Idade não pode ser negativa.")
        except:
            print("❌ Digite um número válido.")

# CADASTRAR

def cadastrar(lista):
    print("\n--- Cadastro ---")

    nome = validar_nome()

    # impedir nomes duplicados
    for pessoa in lista:
        if pessoa.nome.lower() == nome.lower():
            print("⚠️ Nome já cadastrado.")
            return

    idade = validar_idade()

    pessoa = Pessoa(nome, idade)
    lista.append(pessoa)

    print("✅ Pessoa cadastrada com sucesso.")

# LISTAR

def listar(lista):
    print("\n--- Lista ---")

    if not lista:
        print("Nenhuma pessoa cadastrada.")
        return

    for pessoa in lista:
        print(f"Nome: {pessoa.nome} | Idade: {pessoa.idade}")

# BUSCAR

def buscar(lista):
    nome = input("Digite o nome para buscar: ").lower()
    encontrou = False

    for pessoa in lista:
        if nome in pessoa.nome.lower():
            print(f"Nome: {pessoa.nome} | Idade: {pessoa.idade}")
            encontrou = True

    if not encontrou:
        print("Pessoa não encontrada.")

# REMOVER

def remover(lista):
    nome = input("Digite o nome para remover: ").strip().lower()

    encontrados = [p for p in lista if p.nome.lower() == nome]

    if not encontrados:
        print("Pessoa não encontrada.")
        return

    # se tiver mais de um
    if len(encontrados) > 1:
        print("\nForam encontradas várias pessoas:")
        for i, p in enumerate(encontrados):
            print(f"{i} - {p.nome} ({p.idade})")

        try:
            escolha = int(input("Escolha o índice: "))
            pessoa = encontrados[escolha]
        except:
            print("Opção inválida.")
            return
    else:
        pessoa = encontrados[0]

    confirma = input(f"Tem certeza que deseja remover {pessoa.nome}? (s/n): ").lower()

    if confirma == "s":
        lista.remove(pessoa)
        print("✅ Pessoa removida.")
    else:
        print("Operação cancelada.")



# ATUALIZAR


def atualizar(lista):
    nome = input("Digite o nome da pessoa: ").strip().lower()

    encontrados = [p for p in lista if p.nome.lower() == nome]

    if not encontrados:
        print("Pessoa não encontrada.")
        return

    # múltiplos resultados
    if len(encontrados) > 1:
        print("\nForam encontradas várias pessoas:")
        for i, p in enumerate(encontrados):
            print(f"{i} - {p.nome} ({p.idade})")

        try:
            escolha = int(input("Escolha o índice: "))
            pessoa = encontrados[escolha]
        except:
            print("Opção inválida.")
            return
    else:
        pessoa = encontrados[0]

    print(f"\nAtual atual: Nome: {pessoa.nome} | Idade: {pessoa.idade}")

    novo_nome = input("Novo nome (ENTER para manter): ").strip()
    nova_idade = input("Nova idade (ENTER para manter): ").strip()

    # preparar novos valores
    nome_final = pessoa.nome
    idade_final = pessoa.idade

    if novo_nome != "":
        nome_final = novo_nome

    if nova_idade != "":
        try:
            idade_final = int(nova_idade)
        except:
            print("Idade inválida.")
            return

    print("\n--- Confirmação ---")
    print(f"Antes: {pessoa.nome} | {pessoa.idade}")
    print(f"Depois: {nome_final} | {idade_final}")

    confirma = input("Confirmar alteração? (s/n): ").lower()

    if confirma == "s":
        pessoa.nome = nome_final
        pessoa.idade = idade_final
        print("✅ Atualizado com sucesso.")
    else:
        print("Operação cancelada.")

# SALVAR

def salvar(lista):
    try:
        dados = [p.to_dict() for p in lista]
        with open("dados.json", "w") as f:
            json.dump(dados, f, indent=4)
    except Exception as e:
        print("Erro ao salvar:", e)


# CARREGAR

def carregar():
    try:
        with open("dados.json", "r") as f:
            dados = json.load(f)
            return [Pessoa(p["nome"], p["idade"]) for p in dados]
    except:
        return []