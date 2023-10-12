class Tamagushi:
    def _init_(self, nome, idade, fome=None, saude=100):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

def criar_fazenda(num_bichinhos):
    fazenda = []
    for i in range(num_bichinhos):
        nome = input(f"Digite o nome do bichinho {i + 1}: ")
        idade = int(input(f"Digite a idade do bichinho {i + 1}: "))  # Convert input to int
        bichinho = Tamagushi(nome, idade)
        fazenda.append(bichinho)
    return fazenda

def acoes_fazenda(fazenda):
    while True:
        print("\nOpções:")
        print("1. Alimentar todos os bichinhos")
        print("2. Dar banho em todos os bichinhos")
        print("3. Brincar com todos os bichinhos")
        print("4. Ouvir todos os bichinhos")
        print("5. Sair da fazenda")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            for bichinho in fazenda:
                bichinho.fome += 20
                print(f"{bichinho.nome} foi alimentado!")

        elif opcao == "2":
            for bichinho in fazenda:
                bichinho.saude += 30
                print(f"{bichinho.nome} tomou banho!")

        elif opcao == "3":
            for bichinho in fazenda:
                horas = int(input(f"Por quantas horas {bichinho.nome} deve brincar? "))
                total = 7 * horas
                bichinho.saude += total
                print(f"{bichinho.nome} brincou por {horas} horas e ganhou {total} de saúde!")

        elif opcao == "4":
            for bichinho in fazenda:
                print(f"{bichinho.nome} diz: Estou bem!")

        elif opcao == "5":
            print("Saindo da fazenda.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if _name_ == "_main_":
    print("_FAZENDA DE BICHINHOS___")
    num_bichinhos = int(input("Quantos bichinhos você deseja criar na fazenda? "))
    fazenda = criar_fazenda(num_bichinhos)
    print("Fazenda de bichinhos criada com sucesso!")

    while True:
        acoes_fazenda(fazenda)
