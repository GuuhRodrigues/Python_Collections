from abc import ABCMeta, abstractmethod

class Conta(metaclass=ABCMeta):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    @abstractmethod
    def quando_mes_vira(self):
        pass

    def __str__(self):
        return ">>Código {} e saldo {}<<".format(self._codigo, self._saldo)

class ContaCorrente(Conta):
    def quando_mes_vira(self):
        self._saldo -= 2

class ContaPoupanca(Conta):
    def quando_mes_vira(self):
        self._saldo *= 1.01
        self._saldo -= 3

class ContaIvenstimento(Conta):
    pass

conta_gu = ContaCorrente(7)
conta_isa = ContaPoupanca(10)

conta_gu.deposita(700)
conta_isa.deposita(1000)

print(conta_gu)
print(conta_isa)

conta_gu.quando_mes_vira()
conta_isa.quando_mes_vira()

print(conta_gu)
print(conta_isa)

# polimorfismo

conta_gu = ContaCorrente(7)
conta_isa = ContaPoupanca(10)

conta_gu.deposita(700)
conta_isa.deposita(1000)

contas = [conta_gu, conta_isa]
for conta in contas:
    conta.quando_mes_vira()
    print(conta)

#numpy  - para lidar com melhor desempenho para expressoes matematicas, para instalar !pip install numpy, caso nao tenha
# import numpy as np(variavel para chamar o numpyl neste caso seria o "np")

