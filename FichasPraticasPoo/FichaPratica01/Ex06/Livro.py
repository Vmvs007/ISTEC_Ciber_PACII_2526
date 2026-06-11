class Livro:
    def __init__(self, titulo, autor, categoria, numPaginas, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__categoria = categoria
        self.__numPaginas = numPaginas
        self.__isbn = isbn

    def exibirDetalhes(self):
        print(f"{self.__titulo} | {self.__autor} | {self.__categoria} + | Num. Páginas: {self.__numPaginas} | ISBN: {self.__isbn}")