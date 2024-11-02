from limite.tela import Tela
from exceptions.valor_invalido_exception import ValorInvalidoException

class TelaHotel(Tela):

    def tela_opcoes(self):
        escolhas = [1,2,3,4,5,6,0]
        print("-------- HOTEL ---------- ")
        print("Escolha uma opção")
        print("1 - Realizar Check-out")
        print("2 - Finalizar Manutenção de Quarto")
        print("3 - Pagar Funcionário")
        print("4 - Pagar Despesa")
        print("5 - Mostrar Avaliação")
        print("6 - Mostrar Saldo")
        print("0 - Retornar")

        escolha = super().le_num_inteiro("Escolha: ", escolhas)
        print()
        return escolha

    def le_avaliacao(self, mensagem, escolhas_validas):
        while True:
            escolha = input(mensagem)
            print()
            try:
                escolha_avaliacao = int(escolha)
                if escolhas_validas and escolha_avaliacao not in escolhas_validas:
                    raise ValorInvalidoException

                return escolha_avaliacao

            #se for inserido qualquer valor não numérico a avaliação é dada como não feita
            except ValueError:
                escolha = "N/A"
                return escolha

            #caso tenha sido inserido algum número inteiro inválido,
            #  o usuário pode tentar novamente
            except ValorInvalidoException as e:
                print(e)

    def pega_avaliacao_hotel(self):
        escolhas = [1,2,3,4,5]
        print("Qual avaliação do cliente para a reserva?")
        print("1 - PÉSSIMA")
        print("2 - RUIM")
        print("3 - RAZOÁVEL")
        print("4 - BOA")
        print("5 - EXCELENTE")
        print("N - Reserva não avaliada")

        escolha = self.le_avaliacao("Escolha uma opção: ", escolhas)
        print("Opção escolhida: ", escolha)
        print()
        return escolha

    def pega_dados_despesa(self):
        valor = super().le_num_inteiro("Valor da despesa: ")
        descricao = super().le_string("Descrição Breve: ")
        return {"valor": valor, "descricao": descricao}

    def seleciona_reserva(self):
        id = super().le_num_inteiro("ID da reserva que deseja selecionar: ")
        return id

    def seleciona_quarto(self):
        numero = super().le_num_inteiro("Número do quarto que deseja selecionar: ")
        return numero

    def seleciona_funcionario(self):
        cpf = input("CPF do funcionário que deseja selecionar: ")
        print()
        return cpf
    

