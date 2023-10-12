class bombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        qtlitros = valor / self.valorLitro
        if qtlitros <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= qtlitros
            return f"Abastecidos {qtlitros:.2f} litros de {self.tipoCombustivel}. Valor total: R$ {valor:.2f}"
        else:
            return "Desculpe, combustível insuficiente na bomba."

    def abastecerPorLitro(self, litros):
        if litros <= self.quantidadeCombustivel:
            valor_a_pagar = litros * self.valorLitro
            self.quantidadeCombustivel -= litros
            return f"Abastecidos {litros:.2f} litros de {self.tipoCombustivel}. Valor total: R$ {valor_a_pagar:.2f}"
        else:
            return "Desculpe, combustível insuficiente na bomba."

    def alterarValor(self, novo_valor_litro):
        self.valorLitro = novo_valor_litro

    def alterarCombustivel(self, novo_tipo_combustivel):
        self.tipoCombustivel = novo_tipo_combustivel

    def alterarQuantidadeCombustivel(self, nova_quantidade):
        self.quantidadeCombustivel = nova_quantidade

    def mostrarStatus(self):
        return f"Tipo de Combustível: {self.tipoCombustivel}\nValor por Litro: R$ {self.valorLitro:.2f}\nQuantidade de Combustível na Bomba: {self.quantidadeCombustivel:.2f} litros"



bomba = bombaCombustivel("Gasolina", 5.0, 1000.0)
print(bomba.mostrarStatus())
print(bomba.abastecerPorValor(50.0))
print(bomba.abastecerPorLitro(10.0))
bomba.alterarValor(5.5)
bomba.alterarCombustivel("Álcool")
bomba.alterarQuantidadeCombustivel(800.0)
print(bomba.mostrarStatus())
