class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, comida):
        self.bucho.append(comida)

    def verBucho(self):
        return self.bucho

    def digerir(self):
        if len(self.bucho) > 0:
            comida_digerida = self.bucho.pop(0)
            print(f"{self.nome} digeriu {comida_digerida}.")
        else:
            print(f"{self.nome} não tem nada no estômago para digerir.")


macaco1 = Macaco("Júlio")
macaco2 = Macaco("Alfredo")

macaco1.comer("Banana")
macaco1.comer("Maçã")
macaco1.comer("Pêssego")

macaco2.comer("Pão")
macaco2.comer("Queijo")
macaco2.comer("Carne")

print(f"{macaco1.nome} tem no estômago: {macaco1.verBucho()}")
print(f"{macaco2.nome} tem no estômago: {macaco2.verBucho()}")

macaco1.digerir()
macaco2.digerir()

print(f"{macaco1.nome} tem no estômago: {macaco1.verBucho()}")
print(f"{macaco2.nome} tem no estômago: {macaco2.verBucho()}")
