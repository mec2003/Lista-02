class Quadrado:
    def __init__ (self, lado):
        self.lado = lado

    def mudarLado (self, novoLado):
        self.lado = novoLado

    def calcularArea (self):
        area = self.lado * self.lado
        print (f"A area de um quadrado de lado {self.lado} é {area}")

ladin = float(input("Qual o tamanho do lado do quadrado? "))
quadrado = Quadrado(ladin)
quadrado.calcularArea()

r = input("Deseja trocar o tamanho do lado? (S/N)").upper()

if r == "S":
    ladao = float(input("Insira o novo valor: "))
    quadrado.mudarLado(ladao)
    quadrado.calcularArea()

else:
    print("Fim do programa")

    
