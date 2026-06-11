from FichaPratica02.Ex10.ContaBancaria import ContaBancaria

conta1 = ContaBancaria("PT50 1234", "Joaquim")
conta2 = ContaBancaria("PT50 2233", "Joana")
conta3 = ContaBancaria("PT50 2233", "Jorge")

conta1.exibirDetalhes()
conta2.exibirDetalhes()

print("____________________________")

conta1.depositar(100)
conta2.depositar(25)

conta1.exibirDetalhes()
conta2.exibirDetalhes()

print("____________________________")

conta1.levantar(5)
conta2.levantar(1000)

conta1.exibirDetalhes()
conta2.exibirDetalhes()

print("____________________________")

conta1.transferir(conta2,30)

conta1.exibirDetalhes()
conta2.exibirDetalhes()