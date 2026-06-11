class Retangulo:
    def __init__(self, largura, altura, cor):
        self.__largura = largura
        self.__altura = altura
        self.__cor = cor

    def area(self):
        return self.__largura * self.__altura

    def perimetro(self):
        return (self.__largura + self.__altura) * 2
