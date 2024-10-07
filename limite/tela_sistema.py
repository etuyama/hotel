
class TelaSistema():

    def tela_opcoes(self):
        escolhas = [1,2,3,4,0]
        print("-------- SisHotel -------- ")
        print("Escolha uma opção")
        print("1 - Clientes")
        print("2 - Reservas")
        print("3 - Serviços")
        print("4 - Quartos")
        print("0 - Sair")
        escolha = int(input("Escolha: "))

        if escolha in escolhas:
            return escolha
        else:
            print("Ecolha inválida")
            self.tela_opcoes()