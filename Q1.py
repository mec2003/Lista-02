class Bola:
    def __init__(self, cor, circun, material):
        self.cor = cor
        self.circun = circun
        self.material = material

    def trocaCor (self, novaCor):
        self.cor = novaCor

    def mostraCor (self):
        print (f"A cor é: {self.cor}")

cor1 = input ("cor da bola 1: ")
circun1 = input ("Cincunferencia da bola 1: ")
mat1 = input ("Material da bola 1: ")

cor2 = input ("cor da bola 2: ")
circun2 = input ("Cincunferencia da bola 2: ")
mat2 = input ("Material da bola 2: ")

bola1 = Bola(cor1, circun1, mat1)
bola2 = Bola(cor2, circun2, mat2) 

print (f"Os atributos da bola 1 são: {bola1.cor}, {bola1.circun} e {bola1.material}")
print (f"Os atributos da bola 2 são: {bola2.cor}, {bola2.circun} e {bola2.material}")

r = input("Deseja trocar a cor da bola 1? (S/N)")

if r == "S":
    nC = input ("Qual cor você deseja? ")
    bola1.trocaCor(nC)
    bola1.mostraCor()
else:
    print ("OK")