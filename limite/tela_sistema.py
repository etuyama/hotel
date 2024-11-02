from limite.tela import Tela
# COLOCAR \n em algumas mensagens para melhorar a visibilidade do usuário(todas as telas)
# Função listar dos controladores ficando com dois espaços entre os dados


class TelaSistema(Tela):

    def tela_opcoes(self):
        escolhas = [1,2,3,4,5,6,0]
        print("-------- Sistema Hotel -------- ")
        print("Escolha uma opção")
        print("1 - Clientes")
        print("2 - Reservas")
        print("3 - Serviços")
        print("4 - Quartos")
        print("5 - Funcionários")
        print("6 - HOTEL ")
        print("0 - Sair")

        escolha = super().le_num_inteiro("Escolha: ", escolhas)
        return escolha
