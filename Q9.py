class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f'Ponto(x={self.x}, y={self.y})')


class Retangulo:
    def __init__(self, ponto_inicial, largura, altura):
        self.ponto_inicial = ponto_inicial
        self.largura = largura
        self.altura = altura

    def encontrar_centro(self):
        x_centro = self.ponto_inicial.x + self.largura / 2
        y_centro = self.ponto_inicial.y + self.altura / 2
        return Ponto(x_centro, y_centro)

def main():
    retangulo = None

    while True:
        print("Menu:")
        print("1. Criar um retângulo")
        print("2. Encontrar o centro do retângulo")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            x = float(input("Digite a coordenada x do ponto inicial: "))
            y = float(input("Digite a coordenada y do ponto inicial: "))
            largura = float(input("Digite a largura do retângulo: "))
            altura = float(input("Digite a altura do retângulo: "))
            retangulo = Retangulo(Ponto(x, y), largura, altura)
            print("Retângulo criado com sucesso!")
        elif escolha == "2":
            if retangulo is not None:
                centro = retangulo.encontrar_centro()
                centro.imprimir()
            else:
                print("Crie um retângulo primeiro.")
        elif escolha == "3":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
