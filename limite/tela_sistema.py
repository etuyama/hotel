from tela import Tela


class TelaSistema(Tela):

    def tela_opcoes(self):
        escolhas = [1,2,3,4,0]
        print("-------- SisHotel -------- ")
        print("Escolha uma opção")
        print("1 - Clientes")
        print("2 - Reservas")
        print("3 - Serviços")
        print("4 - Quartos")
        print("0 - Sair")
        while True:
            try:
                escolha = int(input("Escolha: "))
                print(escolha)
                if escolha not in escolhas:
                    raise ValueError #CRIAR ERRO ESPECÍFICO
                return escolha

            except ValueError:
                print("Valor inserido inválido")
            