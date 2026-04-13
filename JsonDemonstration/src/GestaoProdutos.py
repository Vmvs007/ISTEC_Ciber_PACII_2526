from src.BibliotecaFicheiros import readFile
from src.BibliotecaProdutos import *

listaDicionariosProdutos = readFile('../res/produtos.json')

while (True):
    print("\n\n---------- Programa de Gestão de Produtos ----------")
    print("1. Consultar todos os Produtos")
    print("2. Consultar por ID")
    print("3. Filtrar por Preço (mais baratos que X)")
    print("4. Ver stock baixo")
    print("5. Produto mais caro")
    print("0. Sair")

    opcao = int(input("Opção: "))
    print("\n")

    if (opcao == 1):
        print("Consultar todos os Produtos")
        consultarTodosProdutos(listaDicionariosProdutos)

    elif (opcao == 2):
        print("Consultar por ID")
        idProdutoPesquisar = int(input("ID: "))
        consultarProdutoPorID(listaDicionariosProdutos,idProdutoPesquisar)

    elif (opcao == 3):
        print("Filtrar por Preço (mais baratos que X)")


    elif (opcao == 4):
        print("Ver stock baixo")


    elif (opcao == 5):
        print("Produto mais caro")
        produtoMaisCaro(listaDicionariosProdutos)

    elif (opcao == 0):
        print("A encerrar...")
        break
    else:
        print("Opção Inválida:", opcao)
