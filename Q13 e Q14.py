class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def obter_nome(self):
        return self.nome

    def obter_salario(self):
        return self.salario

    def aumentar_salario(self, porcentual_de_aumento):
        if porcentual_de_aumento > 0:
            aumento = self.salario * (porcentual_de_aumento / 100)
            self.salario += aumento


harry = Funcionario("Harry", 25000)
print(f"Nome: {harry.obter_nome()}")
print(f"Salário: R${harry.obter_salario():.2f}")
   
harry.aumentar_salario(10)
print(f"Novo salário após aumento de 10%: R${harry.obter_salario():.2f}")
