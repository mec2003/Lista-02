class Televisão:
    def __init__(self):
        self.canal = 1
        self.volume = 10

    def alterar_canal(self, novoCanal):
        if 1 <= novoCanal <= 100:
            self.canal = novoCanal
            print(f'Canal alterado para {self.canal}')
        else:
            print('Canal inválido. Escolha um canal entre 1 e 100.')

    def aumentar_volume(self):
        if self.volume < 100:
            self.volume += 1
            print(f'Volume aumentado para {self.volume}')
        else:
            print('Volume máximo atingido.')

    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1
            print(f'Volume diminuído para {self.volume}')
        else:
            print('Volume mínimo atingido.')

    def mostrar_status(self):
        print(f'Canal: {self.canal}')
        print(f'Volume: {self.volume}')


def main():
    tv = Televisor()

    while True:
        print("\nControle Remoto da TV")
        print("1 - Alterar Canal")
        print("2 - Aumentar Volume")
        print("3 - Diminuir Volume")
        print("4 - Mostrar Status")
        print("0 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "0":
            print("Desligando a TV.")
            break
        elif escolha == "1":
            novo_canal = int(input("Digite o número do canal desejado: "))
            tv.alterar_canal(novo_canal)
        elif escolha == "2":
            tv.aumentar_volume()
        elif escolha == "3":
            tv.diminuir_volume()
        elif escolha == "4":
            tv.mostrar_status()
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
