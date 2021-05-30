class Pessoa:
    ano_atual = 2019  # atributo da class

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):  # atributo da instancia
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_id(cls):
        ...


p1 = Pessoa('Tonaldo', 32)
p1.get_ano_nascimento()
