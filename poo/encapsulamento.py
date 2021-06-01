"""
    public, protect, private
"""


class BaseDeDados:

    def __init__(self):  # construtor
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.dados['clientes'].items():
            print(id, nome)

    def apagar_clientes(self, id):
        del self.__dados['clientes']['id']


bd = BaseDeDados()
bd.inserir_cliente(1, 'Tonaldo Pereira')
bd.inserir_cliente(2, 'Rose Mayri')
bd.inserir_cliente(3, 'Eva Lina')
bd.lista_clientes()