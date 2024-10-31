from limite.tela import Tela


class TelaReserva(Tela):

    def tela_opcoes(self):
        escolhas = [0,1,2,3,4,5]
        print("-------- RESERVAS ----------")
        print("Escolha uma opção")
        print("1- Efetuar Reserva")
        print("2- Alterar Reserva")
        print("3- Listar Reservas")
        print("4- Excluir Reservas")
        print("5- Adicionar Serviço Utilizado")
        print("0- Retornar")
        while True:
            try:
                escolha = super().le_num_inteiro("Escolha: ", escolhas)
                return escolha

            except ValueError:
                print("Escolha inválida")

    def seleciona_reserva(self):
        while True:
            try:
                id = super().le_num_inteiro("ID da reserva que deseja selecionar: ")
                return id

            except ValueError:
                print("Valor inserido inválido")

    def seleciona_cliente(self):
        cpf = input("CPF do cliente que deseja selecionar: ")
        return cpf

    def seleciona_quarto(self):
        while True:
            try:
                numero = super().le_num_inteiro("Número do quarto que deseja selecionar: ")
                return numero

            except ValueError:
                print("Valor inserido inválido")

    def pega_tempo_estadia(self):
        while True:
            try:
                tempo_estadia = super().le_num_inteiro("Tempo de estadia: ")
                return tempo_estadia

            except ValueError:
                print("Valor inserido inválido, por favor insira um número inteiro maior do que 0")

    def mostra_reserva(self, dados_reserva):
        print("ID: ", dados_reserva["id"])
        print("Nome do Cliente: ", dados_reserva["nome_cliente"])
        print("CPF do Cliente: ", dados_reserva["cpf_cliente"])
        print("Número do Quarto: ", dados_reserva["numero_quarto"])
        print("Valor da Diária: ", dados_reserva["valor_diaria"])
        print("Tempo de Estadia (em dias): ", dados_reserva["tempo_estadia"])
        #print("Serviços Utilizados: ", dados_reserva["servicos_utilizados"])
        print("Valor Total: ", dados_reserva["valor_total"])
        print("\n")