class contaCorrente:
    def __init__(self, numero, nome, saldo=0):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo

    def alterarNome(self, novoNome):
        self.nome = novoNome
        print(f"Nome do correntista alterado para {novoNome}")

    def deposito(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")

    def saque(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")
        elif valor <= 0:
            print("Valor de saque inválido. O valor deve ser positivo.")
        else:
            print("Saldo insuficiente")


minhaConta = contaCorrente(12345, "Maria Eduarda", 60000.0)

print(f"Conta: {minhaConta.numero}")
print(f"Correntista: {minhaConta.nome}")
print(f"Saldo: R${minhaConta.saldo:.2f}")

minhaConta.deposito(500.0)
minhaConta.saque(200.0)

minhaConta.alterarNome("Duda")