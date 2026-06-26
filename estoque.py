# Sistema de Controle de Estoque e Vendas
# versao 1.0 - feito rapido pra entregar antes do prazo
# autor: equipe antiga

import datetime

SENHA_ADMIN = "1234"  # senha do admin
LIMITE_DESCONTO_VENDA = 100.0
TAXA_DESCONTO_VENDA = 0.10
LIMITE_DESCONTO_RELATORIO = 200.0
TAXA_DESCONTO_RELATORIO = 0.15

produtos = []


# funcao que adiciona produto
def add(n, p, q, hist=None):
    if hist is None:
        hist = []
    produtos.append({"nome": n, "preco": p, "qtd": q})
    hist.append(n)
    print("Produto adicionado!")


def aplicar_desconto(total, limite_desconto, taxa_desconto):
    if total > limite_desconto:
        return total * (1 - taxa_desconto)
    return total


def vender(nome, quantidade):
    for produto in produtos:
        if produto["nome"] == nome:
            if produto["qtd"] >= quantidade:
                produto["qtd"] -= quantidade
                total = calcular_total(produto["preco"], quantidade)
                print(f"Venda realizada. Total: {total:.2f}")
                return total
            print("Estoque insuficiente")
            return 0
    print("Produto nao encontrado")
    return 0


# calcula o total de uma compra (usado no relatorio)
def calcular_total(preco, quantidade):
    total = preco * quantidade
    return aplicar_desconto(
        total,
        LIMITE_DESCONTO_RELATORIO,
        TAXA_DESCONTO_RELATORIO,
    )


def listar():
    print("=== PRODUTOS ===")
    for x in produtos:
        print(x["nome"] + " - R$" + str(x["preco"]) + " - qtd: " + str(x["qtd"]))


def relatorio_estoque_baixo():
    print("=== ESTOQUE BAIXO ===")
    for x in produtos:
        if x["qtd"] < 5:        # estoque baixo
            print(x["nome"] + " esta com estoque baixo (" + str(x["qtd"]) + ")")


# funcao antiga, nao usamos mais
# def exportar():
#     f = open("dados.txt", "w")
#     for x in produtos:
#         f.write(str(x))
#     f.close()


def relatorio_vendas():
    # TODO: implementar de verdade
    pass


def ler_numero_inteiro(mensagem, minimo=None):
    while True:
        valor = input(mensagem)
        try:
            numero = int(valor)
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")
            continue

        if minimo is not None and numero < minimo:
            print(f"Valor inválido. O valor deve ser maior ou igual a {minimo}.")
            continue

        return numero


def ler_numero_real(mensagem, minimo=None):
    while True:
        valor = input(mensagem)
        try:
            numero = float(valor)
        except ValueError:
            print("Valor inválido. Digite um número real.")
            continue

        if minimo is not None and numero < minimo:
            print(f"Valor inválido. O valor deve ser maior ou igual a {minimo}.")
            continue

        return numero


def menu():
    while True:
        print("\n1-Cadastrar  2-Vender  3-Listar  4-Estoque baixo  5-Admin  0-Sair")
        op = input("Opcao: ")
        if op == "1":
            n = input("Nome: ")
            p = ler_numero_real("Preco: ", minimo=0.01)
            q = ler_numero_inteiro("Qtd: ", minimo=1)
            add(n, p, q)
        elif op == "2":
            n = input("Nome do produto: ")
            q = ler_numero_inteiro("Quantidade: ", minimo=1)
            vender(n, q)
        elif op == "3":
            listar()
        elif op == "4":
            relatorio_estoque_baixo()
        elif op == "5":
            s = input("Senha: ")
            if s == SENHA_ADMIN:
                print("Acesso liberado")
            else:
                print("Senha errada")
        elif op == "0":
            break
        else:
            print("Opcao invalida")


if __name__ == "__main__":
    menu()
