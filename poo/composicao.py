class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def insere_enderecos(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def lista_enderecos(self):
        for k in self.enderecos:
            print(k.cidade, k.estado)


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado


c1 = Cliente('Luiz', 32)
c1.insere_enderecos('Belo Horizonte', 'MG')

c2 = Cliente('Maria', 27)
c2.insere_enderecos('Bahia', 'BA')
c2.insere_enderecos('Rio de Janeiro', 'RJ')

c3 = Cliente('Michelle', 22)
c3.insere_enderecos('São Paulo', 'SP')

c1.lista_enderecos()
c2.lista_enderecos()
c3.lista_enderecos()