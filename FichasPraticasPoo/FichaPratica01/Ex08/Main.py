from FichaPratica01.Ex08.Produto import Produto

produto1 = Produto("Bolachas Água e Sal", 1.5)
produto2 = Produto("Coca-Cola", 1.25)
produto3 = Produto("Queijo", 4)

produto1.exibirDetalhes()
produto2.exibirDetalhes()
produto3.exibirDetalhes()

print("_____________________________________________")

produto1.adicionarStock(10)
produto2.adicionarStock(50)
produto2.adicionarStock(12)

produto1.exibirDetalhes()
produto2.exibirDetalhes()
produto3.exibirDetalhes()

print("_____________________________________________")

produto1.vender(45)
produto2.vender(15)

produto1.exibirDetalhes()
produto2.exibirDetalhes()
produto3.exibirDetalhes()