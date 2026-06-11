class ContaBancaria:
    def __init__(self, iban, titular):
        self.__iban = iban
        self.__titular = titular
        self.__saldo = 0

    def depositar(self, valor):
        self.__saldo += valor

    def levantar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            print("Levantamento efetuado")
        else:
            print("Não tem saldo para esse levantamento")

    def transferir(self, contaDestino, valor):

        if self.__saldo >= valor:
            self.__saldo -= valor
            contaDestino.__saldo += valor
            print("Transferencia efetuada")
        else:
            print("Não tem saldo para essa transferencia")

    def exibirDetalhes(self):
        print(f"{self.__iban} | {self.__titular} | {self.__saldo} €")
