class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta
    
    @ferramenta.setter
    def ferramenta(self, valor):
        self.__ferramenta = valor


class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    @staticmethod
    def escrever():
        print('Caneta está escrevendo...')


class Maquina:
    def __init__(self):
        ...

    @staticmethod
    def escrever():
        print('Máquina está escrevendo...')


escritor = Escritor('Joãozinho')
print(escritor.nome)

caneta = Caneta('Bic')
print(caneta.marca)

maquina = Maquina()
print(maquina.escrever())
