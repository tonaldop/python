# metodos abstratos (são metodos normais)
# metodos que não tem corpo
from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Saldo precisa ser numerico.")

        self._saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Saldo precisa ser numerico.")

        self.saldo += valor

    def detalhes(self):
        print(f'Agencia: {self.agencia}', end=' ')
        print(f'Conta: {self.conta}', end=' ')
        print(f'Saldo: {self.saldo}')

    @abstractmethod
    def sacar(self, valor):
        ...


class ContaPoupanca(Conta):

    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente')
            return

        self.saldo -= valor


cp = ContaPoupanca(3518, 1002161, 0)
cp.depositar(100)
cp.detalhes()
cp.sacar(10)
cp.detalhes()
