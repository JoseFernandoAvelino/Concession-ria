# 3
# Criar a função para carregar o estoque de carros
def carregar_estoque():
    with open("estoque_carros.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        return [{"nome": partes[0],
                "preco": float(partes[1]),
                 "ano": int(partes[2]),
                 "estado": partes[3]}
                for linha in linhas
                for partes in [linha.strip().split(",")]]

# 5
# Criar a função para salvar o estoque de carros quando o usuário cadastrar um novo carro


def salvar_estoque(estoque):
    with open("estoque_carros.txt", "w") as arquivo:
        for carro in estoque:
            arquivo.write(f"{carro['nome']},{carro['preco']},{
                          carro['ano']},{carro['estado']}\n")

# 5
# Criar a função para cadastrar os carros, com (nome, preço, ano, estado de conservação) e salvar no arquivo txt


def cadastrar_carro(estoque):
    nome = input("Digite o nome do carro: ").strip()
    preco = float(input("Digite o preço do carro: ").strip())
    ano = int(input("Digite o ano de fabricação do carro: ").strip())
    estado = input("Digite o estado do carro: ").strip()
    carro = {"nome": nome, "preco": preco, "ano": ano, "estado": estado}
    estoque.append(carro)
    salvar_estoque(estoque)
    print("Carro cadastrado!")

# 4
# Criar a função para procurar os carros no estoque de acordo com a pesquisa do usuário


def procurar_carro(estoque, pesquisa):
    if isinstance(pesquisa, float):
        carros_encontrados = [
            carro for carro in estoque if carro["preco"] <= pesquisa]
    else:
        carros_encontrados = [
            carro for carro in estoque if carro["estado"].lower() == pesquisa.lower()]

    if carros_encontrados:
        for carro in carros_encontrados:
            print(f"Nome: {carro['nome']}, Preço: R$ {carro['preco']:.2f}, Ano: {
                  carro['ano']}, Estado: {carro['estado']}")
    else:
        print("Carro não encontrado!")

# 6
# Criar um menu interativo com as opções de cadastrar um novo carro, pesquisar carros ou sair ao digitar 0


def menu():
    estoque = carregar_estoque()

    while True:
        print("\nMenu:")
        print("1. Cadastrar um novo carro")
        print("2. Pesquisar carros")
        print("0. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_carro(estoque)
        elif opcao == "2":
            # 1
            # Criar mecanismo para filtrar a pesquisa do usuário entre preço ou estado de conservação
            entrada = input(
                "Digite um preço máximo ou estado do carro: ").strip()
            try:
                pesquisa = float(entrada)
            except ValueError:
                pesquisa = entrada
            procurar_carro(estoque, pesquisa)
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


menu()
