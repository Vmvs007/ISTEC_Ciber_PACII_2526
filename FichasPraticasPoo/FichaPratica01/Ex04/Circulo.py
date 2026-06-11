class Circulo:
    def __init__(self, cor, raio):
        self.__cor = cor
        self.__raio = raio

    def area(self):
        return 3.14 * (self.__raio ** 2)

    def perimetro(self):
        return 2 * 3.14 * self.__raio
