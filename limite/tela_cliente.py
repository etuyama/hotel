from limite.tela import Tela


class TelaCliente(Tela):

    def tela_opcoes(self):
        escolhas = [1,2,3,4,0]
        print("-------- CLIENTES ----------")
        print("Escolha uma opção")
        print("1 - Incluir Cliente")
        print("2 - Alterar Cliente")
        print("3 - Listar Clientes")
        print("4 - Excluir Cliente")
        print("0 - Retornar")
        while True:
            try:
                escolha = super().le_num_inteiro("Escolha: ", escolhas)
                return escolha

            except ValueError:
                print("Escolha inválida")

    def pega_dados_cliente(self):
        print("-------- DADOS CLIENTE --------")
        while True:
            try:
                nome = super().le_string("Nome: ")
                cpf = super().le_cpf("CPF: ")
                data_nascimento = super().le_data(
                    "Data de nascimento (DD/MM/AAAA): "
                )
                telefone = super().le_telefone(
                    "Telefone (Formato: DDD123456789, DDD com 0 na frente): "
                )
                endereco = super().le_string("Endereco: ")
                return {"nome": nome, "cpf": cpf, "telefone": telefone,
                        "data_nascimento": data_nascimento, "endereco": endereco}
            except ValueError:
                print("Dados inválidos.")


    def mostra_cliente(self, dados_cliente):
        print("Nome do cliente: ", dados_cliente["nome"])
        print("CPF: ", dados_cliente["cpf"])
        print("Data de nascimento: ", dados_cliente["data_nascimento"])
        print("Telefone: ", dados_cliente["telefone"])
        print("Endereco: ", dados_cliente["endereco"])
        print("\n")

    def seleciona_cliente(self):
        cpf = input("CPF do cliente que deseja selecionar: ")
        return cpf

