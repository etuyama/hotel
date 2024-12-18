from limite.tela import Tela


class TelaReserva(Tela):

    def tela_opcoes(self):
        escolhas = [0,1,2,3,4,5,6,7,8,9]
        print("-------- RESERVAS ----------")
        print("Escolha uma opção")
        print("1- Efetuar Reserva")
        print("2- Alterar Reserva")
        print("3- Listar Reservas Pendentes")
        print("4- Excluir Reservas")
        print("5- Adicionar Serviço Utilizado")
        print("6- Extender Estadia")
        print("7- Adicionar Valor Extra")
        print("8- Listar Todas Reservas")
        print("9- Gerar relatórios")
        print("0- Retornar")

        escolha = super().le_num_inteiro("Escolha: ", escolhas)
        return escolha

    def seleciona_reserva(self):
        id = super().le_num_inteiro("ID da reserva que deseja selecionar: ")
        return id

    def seleciona_cliente(self):
        cpf = input("CPF do cliente que deseja selecionar: ")
        return cpf

    def seleciona_quarto(self):
        numero = super().le_num_inteiro("Número do quarto que deseja selecionar: ")
        return numero

    def pega_dias_extensao(self):
        qt_dias = super().le_num_inteiro("Quantos dias deseja adicionar à estadia: ")
        return qt_dias

    def pega_valor_extra(self):
        valor_extra = super().le_num_inteiro("Valor extra que deseja adicionar à reserva: ")
        return valor_extra

    def pega_tempo_estadia(self):
        tempo_estadia = super().le_num_inteiro("Tempo de estadia: ")
        return tempo_estadia

    def tela_relatorio(self):
        escolhas = [0,1,2,3]
        print("Selecione o tipo de relatório que deseja gerar:")
        print("1- Tipos de quarto mais reservados")
        print("2- Meses com mais reservas realizadas")
        print("3- Clientes que mais fizeram reservas")
        print("0- Retornar")

        escolha = super().le_num_inteiro("Escolha: ", escolhas)
        return escolha

    def seleciona_servico(self):
        id = super().le_num_inteiro("ID do serviço que deseja selecionar: ")
        return id

    def seleciona_ano(self):
        ano = super().le_num_inteiro(
            "Para qual ano deseja gerar o relatório? (Ex 2024): "
        )
        return ano
    def mostra_reserva(self, dados_reserva):
        print("ID: ", dados_reserva["id"])
        print("Data da reserva: ", dados_reserva["data_reserva"])
        print("Situação: ", dados_reserva["situacao"])
        print("Nome do Cliente: ", dados_reserva["nome_cliente"])
        print("CPF do Cliente: ", dados_reserva["cpf_cliente"])
        print("Número do Quarto: ", dados_reserva["numero_quarto"])
        print(f"Valor da Diária: R${dados_reserva['valor_diaria']},00")
        print("Tempo de Estadia: ", dados_reserva["tempo_estadia"])
        print("Serviços Utilizados: ", dados_reserva["servicos_utilizados"])
        print(f"Valor Total: R${dados_reserva['valor_total']},00")
        print("\n")
