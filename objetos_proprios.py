class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return ">>Código {} e saldo {} <<".format(self.codigo, self.saldo)


conta_gu = ContaCorrente(7)
conta_isa = ContaCorrente(10)

contas = [conta_gu, conta_isa]

conta_gu.deposita(700)
conta_isa.deposita(1000)

print(contas[0])
print(contas[1])
