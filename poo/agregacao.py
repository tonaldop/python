class Carrinho:
    def __init__(self):
        self.produto = []

    def inserir_produto(self, produtos):
        self.produto.append(produtos)

    def lista_produto(self):
        for produto in self.produto:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for p in self.produto:
            total += p.valor

        return total


class Protudo:
    def __init__(self, nome,valor):
        self.nome = nome
        self.valor = valor


carrinho = Carrinho()
p1 = Protudo('Camiseta', 50)
p2 = Protudo('iPhone', 10050)
p3 = Protudo('Caneca', 19.90)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.lista_produto()
print(carrinho.soma_total())


