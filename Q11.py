class Carro:
    def __init__(self, km_litros):
        self.km_litros = km_litros
        self.nivel_de_combustivel = 0

    def andar(self, distancia):
        combustivel_necessario = distancia / self.km_litros

        if combustivel_necessario <= self.nivel_de_combustivel:
            self.nivel_de_combustivel -= combustivel_necessario
        else:
            print("Quantidade Insuficiente")

    def adicionarGasolina(self, litros):
        self.nivel_de_combustivel += litros

    def obterGasolina(self):
        return self.nivel_de_combustivel