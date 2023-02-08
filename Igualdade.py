class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return ">>Código {} e saldo {}<<".format(self._codigo, self._saldo)

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        return self._codigo == outro._codigo and self._saldo == outro._saldo

class  ContaMultiploSalario(ContaSalario):
    pass

conta1 = ContaSalario(1)
conta2 = ContaMultiploSalario(2)

isinstance(ContaSalario(1), ContaSalario)