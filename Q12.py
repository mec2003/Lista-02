class ContaInvestimento:
    def __init__(self, saldo_inicial, taxa_juros):
        self.saldo = saldo_inicial
        self.taxa_juros = taxa_juros / 100  

    def adicioneJuros(self):
        juros = self.saldo * self.taxa_juros
        self.saldo += juros

    def get_saldo(self):
        return self.saldo

poupanca = ContaInvestimento(1000.00, 10)

for _ in range(5):
    poupanca.adicioneJuros()

print("Saldo após 5 aplicações de juros:", poupanca.get_saldo())
