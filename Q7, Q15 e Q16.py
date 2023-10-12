class Tamagushi:
    def __init__(self, nome, idade, fome = 0, saude = 100):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def alterar_fome(self, nova_fome):
        self.fome = nova_fome

    def alterar_saude(self, nova_saude):
        self.saude = nova_saude

    def alterar_idade(self, nova_idade):
        self.idade = nova_idade

    def retornar_nome(self):
        return self.nome

    def retornar_fome(self):
        return self.fome

    def retornar_saude(self):
        return self.saude

    def retornar_idade(self):
        return self.idade

    def calcular_humor(self):
        humor = (self.saude - self.fome)
        return humor



print("_____________NOVO JOGO_______________")
nome = input("\nComo você gostaria de chamar o bichinho? ")
idade = input("Qual a idade dele? ")

bichinho = Tamagushi(nome, idade)

print(f"\n{bichinho.nome} criado com sucesso!")

print("--------------------------------------------")
print(f"Fome = {bichinho.fome}       Saúde = {bichinho.saude}       Humor = {bichinho.calcular_humor()}")
print("--------------------------------------------")
print(f"Lembre-se que quando mais saudável e menos faminto, mais bem humorado é {bichinho.nome}.")

while True:
    print("\n1.Alimentar")
    print("2.Dar Banho")
    print("3.Brincar")
    print("4.Sair do Jogo")

    opcao = input(f"\nO que você quer fazer com o {bichinho.nome}? ")

    if opcao == "1":
        print("\n1.Almoço no Anjinho(+ 20)")
        print("2.Água do bloco H (- 10)")
        print("3.Yakisoba no CCMN (+ 40)")
        print("4.Bandejão (- 30)")

        num = input(f"\nO que quer fazer com {bichinho.nome}? ")

        if num == "1":
            print(f"\n{bichinho.nome} adorou! \n + 20 em fome")
            bichinho.fome += 20 
            print("--------------------------------------------")
            print(f"Fome = {bichinho.fome}       Saúde = {bichinho.saude}       Humor = {bichinho.calcular_humor()}")
            print("--------------------------------------------")


        elif num == "2":
            print(f"\n{bichinho.nome} detestou! \n - 10 em Fome")
            bichinho.fome -= 10 
            print("--------------------------------------------")
            print(f"Fome = {bichinho.fome}       Saúde = {bichinho.saude}       Humor = {bichinho.calcular_humor()}")
            print("--------------------------------------------")


        elif num == "3":
            print(f"\n{bichinho.nome} adorou! \n + 40 em Fome")
            bichinho.fome += 40 
            print("--------------------------------------------")
            print(f"Fome = {bichinho.fome}       Saúde = {bichinho.saude}       Humor = {bichinho.calcular_humor()}")
            print("--------------------------------------------")


        elif num == "4":
            print(f"\n{bichinho.nome} detestou muito! \n - 30 em Fome")
            bichinho.fome -= 30 
            print("--------------------------------------------")
            print(f"Fome = {bichinho.fome}       Saúde = {bichinho.saude}       Humor = {bichinho.calcular_humor()}")
            print("--------------------------------------------")


        else:
            print("\nOpção Inválida")

    elif opcao == "2":
        print ('\n"Um banho nesse calor é um alívio e agora estou lempenho!" \n + 30 em Saúde')
        bichinho.saude += 30
        print("--------------------------------------------")
        print(f"Fome = {bichinho.fome}       Saúde = {bichinho.saude}       Humor = {bichinho.calcular_humor()}")
        print("--------------------------------------------")

    elif opcao == "3":
        print("\n1.Programar em Python (+ 7 por hora)")
        print("2.Programar em C (- 5 por hora)")
        print("3.Jogar um futECA (+ 15 por hora)")
        print("4.Estudar para física 2 (- 10 por hora)")

        num = input(f"\nO que quer fazer com {bichinho.nome}? ")

        if num == "1" or num == "2" or num == "3" or num == "4":
            horas = int(input("Por quantas horas você quer brincar? "))
            if horas < 1:
                print("Número de horas inválido. Deve ser pelo menos 1 hora.")
            else:
                if num == "1":
                    print(f"\n{bichinho.nome} adorou!")
                    total = 7 * horas
                    print(f"+ {total} em Saúde")
                    bichinho.saude += total
                    print("--------------------------------------------")
                    print(f"Fome = {bichinho.fome}       Saúde = {bichinho.saude}       Humor = {bichinho.calcular_humor()}")
                    print("--------------------------------------------")

                elif num == "2":
                    print(f"\n{bichinho.nome} detestou!")
                    total = 5 * horas
                    print(f"- {total} em Saúde")
                    bichinho.saude -= total
                    print("--------------------------------------------")
                    print(f"Fome = {bichinho.fome}       Saúde = {bichinho.saude}       Humor = {bichinho.calcular_humor()}")
                    print("--------------------------------------------")

                elif num == "3":
                    print(f"\n{bichinho.nome} adorou muito!")
                    total = 15 * horas
                    print(f"+ {total} em Saúde")
                    bichinho.saude += total
                    print("--------------------------------------------")
                    print(f"Fome = {bichinho.fome}       Saúde = {bichinho.saude}       Humor = {bichinho.calcular_humor()}")
                    print("--------------------------------------------")

                elif num == "4":
                    print(f"\n{bichinho.nome} detestou muito.")
                    total = 10 * horas
                    print(f"- {total} em Saúde")
                    bichinho.saude -= total
                    print("--------------------------------------------")
                    print(f"Fome = {bichinho.fome}       Saúde = {bichinho.saude}       Humor = {bichinho.calcular_humor()}")
                    print("--------------------------------------------")

        else:
            print("\nOpção Inválida")


    elif opcao == "4":
        print(f"\n{bichinho.nome} vai sentir sua falta!\n")
        break


    else:
        print("Opção Inválida")