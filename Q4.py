class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, novaIdade):
        if self.idade < 21:
            crescer = novaIdade - self.idade
            novaAltura = (0.05 * crescer) + self.altura
            self.altura = novaAltura
            self.idade = novaIdade
        else:
            self.idade = novaIdade

    def engordar(self, kg):
        self.peso = self.peso + kg

    def emagrecer(self, kg):
        self.peso = self.peso - kg

    def crescer(self, m):
        self.altura = self.altura + m

nome1 = input("Insira o nome: ")
idade1 = int(input("Insira a idade: "))
peso1 = float(input("Insira o peso em kg: "))
altura1 = float(input("Insira a altura em metros: "))

pessoa1 = Pessoa(nome1, idade1, peso1, altura1)

while True:
    print("\nOpções:")
    print("1. Envelhecer")
    print("2. Engordar")
    print("3. Emagrecer")
    print("4. Crescer")
    print("5. Sair")

    opcao = input("Escolha um número para selecionar a opção que deseja: ")

    if opcao == "1":
        anos = int(input("Insira a nova idade: "))
        pessoa1.envelhecer(anos)
        print(f"Nova idade: {pessoa1.idade}")
        print(f"Nova altura: {pessoa1.altura}")

    elif opcao == "2":
        kg = float(input("Insira quantos quilitchos a mais: "))
        pessoa1.engordar(kg)
        print(f"Novo peso de {pessoa1.nome}: {pessoa1.peso} kg")

    elif opcao == "3":
        kg = float(input("Insira quantos quilitchos a menos: "))
        pessoa1.emagrecer(kg)
        print(f"Novo peso de {pessoa1.nome}: {pessoa1.peso} kg")

    elif opcao == "4":
        m = float(input("Insira quantos metros a mais de altura: "))
        pessoa1.crescer(m)
        print(f"Nova altura de {pessoa1.nome}: {pessoa1.altura} m")

    elif opcao == "5":
        break
    else:
        print("Opção inválida. Tente novamente.")