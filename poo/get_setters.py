class Produtos:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    # Getter
    @property
    def preco(self):
        return self._preco

    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome.upper()


p1 = Produtos('Camiseta', 50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produtos('Caneca', 'R$10')
p2.desconto(15)
print(p2.nome, p2.preco)


