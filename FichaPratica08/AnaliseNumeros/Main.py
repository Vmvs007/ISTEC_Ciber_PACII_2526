from AnaliseNumeros.BibliotecaNumeros import *

print("_____ Bem-vindo/a ao Programa de Análise de um Número _____")
numero = int(input("Insira um número: "))

while(True):
    print(f"\n_*_*_*_ Análise do Número: {numero} _*_*_*_ ")
    print("1. Par ou Impar")
    print("2. Positivo ou Negativo")
    print("3. Primo")
    print("4. Perfeito")
    print("5. Triangular")
    print("6. Trocar de Número")
    print("0. Sair")

    opcao=int(input("Opção: "))

    match(opcao):

        case 1:
            if par(numero):
                print("Par")
            else:
                print("Impar")

        case 2:
            if positivo(numero):
                print("Positivo")
            else:
                print("Negativo")

        case 3:
            if primo(numero):
                print("Primo")
            else:
                print("Não primo")

        case 4:
            print()

        case 5:
            print()

        case 6:
            print()

        case 0:
            print("\nA encerrar o programa...")
            break

        case _:
            print("\nOpção não reconhecida!")
