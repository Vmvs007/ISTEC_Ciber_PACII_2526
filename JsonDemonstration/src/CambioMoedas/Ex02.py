from src.BibliotecaFicheiros import readFile, saveFile


taxas = readFile("../../res/cambios.json")

usernameCorreto = "admin"
passwordCorreta = "123456"

opcao = 1

# MENU PRINCIPAL
while (opcao != 0):
    print("\n\nBem-vindo/a ao programa de Câmbio de Moedas")
    print("1. Cliente")
    print("2. Administrador")
    print("0. Guardar e Sair")

    opcao = int(input("Opção: "))

    match (opcao):
        case 1:  # Cliente

            opcaoCliente = 1
            while (opcaoCliente != 0):

                print("\n\n***** MENU CLIENTE *****")
                print("1. Consultar Taxas de Câmbio")
                print("2. Cambiar Moedas")
                print("0. Voltar ao Menu Inicial")

                opcaoCliente = int(input("Opção: "))

                match (opcaoCliente):
                    case 1:
                        print("Consultar Taxas de Câmbio")

                        for moedaAtual in taxas:
                            print(f"{moedaAtual}: {taxas[moedaAtual]}")

                    case 2:
                        print("Cambiar Moedas")
                        moedaOrigem = input("Moeda Origem (Ex: USD | EUR | GBP): ").strip().upper()
                        valor = float(input("Valor: "))
                        moedaDestino = input("Moeda Destino (Ex: USD | EUR | GBP): ").strip().upper()

                        if (moedaOrigem not in taxas and moedaDestino not in taxas):
                            print("MOEDAS INVÁLIDAS")
                        elif (valor <= 0):
                            print("VALOR DEVE SER SUPERIOR A 0")
                        else:
                            # Correu tudo bem
                            valorCambio = (taxas[moedaDestino] * valor) / taxas[moedaOrigem]

                            print(f"Valor Cambiado: {valorCambio} {moedaDestino}")

                    case 0:
                        print("")

                    case _:
                        print("Opção Inválida!")

        case 2:  # Administrador

            # Login
            usernameIntroduzido = input("Username:")
            passwordIntroduzida = input("Password:")

            if (usernameIntroduzido == usernameCorreto and passwordIntroduzida == passwordCorreta):
                opcaoAdmin = 1
                while (opcaoAdmin != 0):

                    print("\n\n***** MENU ADMINISTRADOR *****")
                    print("1. Alterar Taxas")
                    print("2. Adicionar Nova Moeda")
                    print("3. Alterar Password")
                    print("0. Voltar ao Menu Inicial")

                    opcaoAdmin = int(input("Opção: "))

                    match (opcaoAdmin):
                        case 1:
                            print("Alterar Taxas")
                            moedaAlterada = input("Moeda a Alterar (Ex: USD | EUR | GBP): ").strip().upper()
                            novoValorCambio = float(input("Novo Valor: "))

                            if moedaAlterada not in taxas:
                                print("MOEDA INEXISTENTE")
                            elif novoValorCambio < 0:
                                print("VALOR NÃO PODE SER INFERIOR A 0")
                            else:
                                # Correu tudo bem
                                taxas[moedaAlterada] = novoValorCambio

                        case 2:
                            print("Adicionar Nova Moeda")
                            moedaNova = input("Moeda Nova (Ex: USD | EUR | GBP): ").strip().upper()
                            valorCambio = float(input("Novo Valor: "))

                            if moedaNova in taxas:
                                print("MOEDA EXISTENTE! NÃO PODE CRIAR DE NOVO")
                            elif valorCambio < 0:
                                print("VALOR NÃO PODE SER INFERIOR A 0")
                            else:
                                # Correu tudo bem
                                taxas[moedaNova] = valorCambio

                        case 3:
                            print("Alterar Password")
                            passwordCorreta = input("Nova password: ")

                        case 0:
                            print("")

                        case _:
                            print("Opção Inválida!")

            else:
                print("Credenciais Inválidas")

        case 0:  # Sair
            print("Obrigado. Até à próxima!")

        case _:
            print("Opção Inválida!")

# Sair do programa...
saveFile("../../res/cambios.json", taxas)
