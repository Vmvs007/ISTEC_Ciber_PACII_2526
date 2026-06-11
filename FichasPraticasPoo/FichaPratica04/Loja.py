from FichaPratica04.Arma import Arma
from FichaPratica04.Armadura import Armadura
from FichaPratica04.Pocao import Pocao


class Loja:
    def __init__(self):
        self.__armaDisponivel = None
        self.__armaduraDisponivel = None
        self.__pocaoDisponivel = None

    def getArmaDisponivel(self):
        return self.__armaDisponivel

    def getArmaduraDisponivel(self):
        return self.__armaduraDisponivel

    def getPocaoDisponivel(self):
        return self.__pocaoDisponivel

    def setArmaDisponivel(self, arma):
        self.__armaDisponivel = arma

    def setArmaduraDisponivel(self, armadura):
        self.__armaduraDisponivel = armadura

    def setPocaoDisponivel(self, pocao):
        self.__pocaoDisponivel = pocao

    def gerarProdutos(self, numeroMasmorra):
        # TODO:
        # Podes alterar os atributos dos objetos abaixo.
        # A ideia é que quanto mais avançada for a masmorra,
        # melhores e mais caros sejam os produtos.

        if numeroMasmorra == 1:
            self.__armaDisponivel = Arma("Dar nome 1", 3, 20)
            self.__armaduraDisponivel = Armadura("Dar nome 2", 2, 18)
            self.__pocaoDisponivel = Pocao("Dar nome 3", 20, 10)

        elif numeroMasmorra == 2:
            self.__armaDisponivel = Arma("Dar nome 1", 6, 45)
            self.__armaduraDisponivel = Armadura("Dar nome 2", 4, 40)
            self.__pocaoDisponivel = Pocao("Dar nome 3", 35, 25)

        elif numeroMasmorra == 3:
            self.__armaDisponivel = Arma("Dar nome 1", 9, 75)
            self.__armaduraDisponivel = Armadura("Dar nome 2", 7, 70)
            self.__pocaoDisponivel = Pocao("Dar nome 3", 50, 40)

        elif numeroMasmorra == 4:
            self.__armaDisponivel = Arma("Dar nome 1", 13, 110)
            self.__armaduraDisponivel = Armadura("Dar nome 2", 10, 100)
            self.__pocaoDisponivel = Pocao("Dar nome 3", 70, 60)

        else:
            self.__armaDisponivel = Arma("Dar nome 1", 18, 160)
            self.__armaduraDisponivel = Armadura("Dar nome 2", 15, 150)
            self.__pocaoDisponivel = Pocao("Dar nome 3", 100, 90)

    def mostrarProdutos(self):
        print("\n===== LOJA DO FERREIRO =====")
        print("O ferreiro olha para ti e diz:")
        print('"Não sei o que é um carregador USB-C, mas tenho espadas e outras coisas."')

        print("\n1 - Arma disponível")
        if self.__armaDisponivel is not None:
            self.__armaDisponivel.mostrarDados()
        else:
            print("Nenhuma arma disponível.")

        print("\n2 - Armadura disponível")
        if self.__armaduraDisponivel is not None:
            self.__armaduraDisponivel.mostrarDados()
        else:
            print("Nenhuma armadura disponível.")

        print("\n3 - Poção disponível")
        if self.__pocaoDisponivel is not None:
            self.__pocaoDisponivel.mostrarDados()
        else:
            print("Nenhuma poção disponível.")

    def comprarArma(self, jogador):
        # TODO:
        # 1. Verificar se existe arma disponível.
        # 2. Verificar se o jogador tem moedas suficientes.
        # 3. Se tiver, gastar moedas e equipar a arma.
        # 4. Mostrar mensagem adequada.

        print("[TODO] O método comprarArma() ainda não foi implementado.")

    def comprarArmadura(self, jogador):
        # TODO:
        # 1. Verificar se existe armadura disponível.
        # 2. Verificar se o jogador tem moedas suficientes.
        # 3. Se tiver, gastar moedas e equipar a armadura.
        # 4. Mostrar mensagem adequada.

        print("[TODO] O método comprarArmadura() ainda não foi implementado.")

    def comprarPocao(self, jogador):
        # TODO:
        # 1. Verificar se existe poção disponível.
        # 2. Verificar se o jogador tem moedas suficientes.
        # 3. Se tiver, gastar moedas e guardar a poção.
        # 4. Mostrar mensagem adequada.

        print("[TODO] O método comprarPocao() ainda não foi implementado.")

