from limite.tela import Tela


class TelaReserva(Tela):

    def tela_opcoes(self):
        escolhas = [0,1,2,3,4,5,6,7]
        print("-------- RESERVAS ----------")
        print("Escolha uma opção")
        print("1- Efetuar Reserva")
        print("2- Alterar Reserva")
        print("3- Listar Reservas")
        print("4- Excluir Reservas")
        print("5- Adicionar Serviço Utilizado")
        print("6- Extender Estadia")
        print("7- Adicionar Valor Extra")
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

    def pega_dias_extensao(self):
        while True:
            try:
                qt_dias = super().le_num_inteiro("Quantos dias deseja adicionar à estadia: ")
                return qt_dias

            except ValueError:
                print("Valor inserido inválido, por favor insira um número inteiro maior do que 0")

    def pega_valor_extra(self):
        while True:
            try:
                valor_extra = super().le_num_inteiro("Valor extra que deseja adicionar à reserva: ")
                return valor_extra

            except ValueError:
                print("Valor inserido inválido, por favor insira um número inteiro maior do que 0")

    def pega_tempo_estadia(self):
        while True:
            try:
                tempo_estadia = super().le_num_inteiro("Tempo de estadia: ")
                return tempo_estadia

            except ValueError:
                print("Valor inserido inválido, por favor insira um número inteiro maior do que 0")

    def seleciona_servico(self):
        while True:
            try:
                id = super().le_num_inteiro("ID do serviço que deseja selecionar: ")
                return id

            except ValueError:
                print("Valor inserido inválido")

    def mostra_reserva(self, dados_reserva):
        print("ID: ", dados_reserva["id"])
        print("SITUAÇÃO: ", dados_reserva["situacao"])
        print("Nome do Cliente: ", dados_reserva["nome_cliente"])
        print("CPF do Cliente: ", dados_reserva["cpf_cliente"])
        print("Número do Quarto: ", dados_reserva["numero_quarto"])
        print(f"Valor da Diária: R${dados_reserva['valor_diaria']},00")
        print("Tempo de Estadia: ", dados_reserva["tempo_estadia"])
        print("Serviços Utilizados: ", dados_reserva["servicos_utilizados"])
        print(f"Valor Total: R${dados_reserva['valor_total']},00")
        print("\n")
