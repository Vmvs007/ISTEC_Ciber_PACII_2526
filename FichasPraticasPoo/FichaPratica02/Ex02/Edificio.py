class Edificio:
    def __init__(self, nome, rua, cidade, corFachada, numAndares, garagem):
        self.__nome = nome
        self.__rua = rua
        self.__cidade = cidade
        self.__corFachada = corFachada
        self.__numAndares = numAndares
        self.__garagem = garagem

    def getNome(self):
        return self.__nome

    def getRua(self):
        return self.__rua

    def getCorFachada(self):
        return self.__corFachada

    def setCorFachada(self, corFachada):
        self.__corFachada = corFachada
