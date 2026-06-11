class Carro:
    def __init__(self, marca,modelo,cor,anoFabrico):
        self.__marca=marca
        self.__modelo = modelo
        self.__cor = cor
        self.__anoFabrico = anoFabrico

    def ligar(self):
        print(f"O {self.__marca} {self.__modelo} {self.__cor} está ligado...")