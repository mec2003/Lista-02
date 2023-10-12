class Retangulo:
    def __init__(self, comprimento=0, largura=0):
        self.comprimento = comprimento
        self.largura = largura

    def mudarLados(self):
        print("\n1.Comprimento")
        print("2.Largura")
        lado = input("Insira a opção que deseja alterar: ")

        if lado == "1":
            novoComprimento = float(input("Insira o novo valor: "))
            self.comprimento = novoComprimento
        elif lado == "2":
            novaLargura = float(input("Insira o novo valor: "))
            self.largura = novaLargura
        else:
            print("Opção Inválida")

    def verificarValor(self):
        print("\n1.Comprimento")
        print("2.Largura")
        lado = input("Insira a opção que deseja verificar: ")

        if lado == "1":
            print(f"Valor do comprimento: {self.comprimento}")
        elif lado == "2":
            print(f"Valor da largura: {self.largura}")
        else:
            print("Opção Inválida")

    def calcularArea(self):
        area = self.comprimento * self.largura
        return area

    def calcularPerimetro(self):
        perimetro = (2 * self.comprimento) + (2 * self.largura)
        return perimetro

print("____________BOB CONSTRUTOR_____________")

print("Insira as dimensões, em metros, do local")

comprimento = float(input("Comprimento: "))
largura = float(input("Largura: "))

local = Retangulo(comprimento, largura)

pisos = local.calcularArea()
rodape = local.calcularPerimetro()

print(f"Serão necessários {pisos} metros quadrados de piso")
print(f"Serão necessários {rodape} metros de rodapé")

while True:
    print("\n1.Verificar Dimensões")
    print("2.Alterar Dimensões")
    print("3.Recalcular medidas")
    print("4.Finalizar")
    opcao = input("Insira a opção que deseja: ")

    if opcao == "1":
        local.verificarValor()
    elif opcao == "2":
        local.mudarLados()
    elif opcao == "3":
        pisos = local.calcularArea()
        rodape = local.calcularPerimetro()
        print(f"Serão necessários {pisos} metros quadrados de piso")
        print(f"Serão necessários {rodape} metros de rodapé")
        
    elif opcao == "4":
        break
    else:
        print("Opção Inválida")
