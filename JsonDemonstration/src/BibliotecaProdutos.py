def consultarTodosProdutos(listaProdutos):
    for produtoAtual in listaProdutos:
        print(produtoAtual)


def consultarProdutoPorID(listaProdutos, idPesquisar):
    for produtoAtual in listaProdutos:
        if produtoAtual['id'] == idPesquisar:
            print(produtoAtual)


def filtrarProdutosPrecoMaximo(listaProdutos, precoMaximo):
    for produtoAtual in listaProdutos:
        if produtoAtual['preco'] <= precoMaximo:
            print(produtoAtual)


def filtrarProdutosStockBaixo(listaProdutos):
    for produtoAtual in listaProdutos:
        if produtoAtual['stock'] <= 5:
            print(produtoAtual)


def produtoMaisCaro(listaProdutos):
    produtoCaro = {}
    precoMaisCaro = 0

    for produtoAtual in listaProdutos:
        if produtoAtual['preco'] > precoMaisCaro:
            produtoCaro = produtoAtual
            precoMaisCaro = produtoAtual['preco']

    print(produtoCaro)
