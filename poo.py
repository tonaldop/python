class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return

        if self.falando:
            print(f'{self.nome} já está falando.')
            return
        print(f'{self.nome} está falando {assunto}')

    def parar_falar(self):
        if self.falando:
            print(f'{self.nome} não está falando')
            return
        print(f'{self.nome} parou de falar.')

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return

        print(f'{self.nome} parou de comer.')
        self.comendo = False


p1 = Pessoa('Luiz', 33)
p1.comer('maçã')
p1.parar_comer()
p1.comer('jaca')




