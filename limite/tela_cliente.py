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
                nome = input("Nome: ")
                cpf = input("CPF: ")
                idade = super().le_num_inteiro("Idade: ")
                telefone = input("Telefone: ")
                endereco = input("Endereco: ")
                return {"nome": nome, "cpf": cpf, "telefone": telefone,
                        "idade": idade, "endereco": endereco}
            except:
                print("Dados inválidos")

    def mostra_cliente(self, dados_cliente):
        print("Nome do cliente: ", dados_cliente["nome"])
        print("CPF: ", dados_cliente["cpf"])
        print("Idade: ", dados_cliente["idade"])
        print("Telefone: ", dados_cliente["telefone"])
        print("Endereco: ", dados_cliente["endereco"])
        print("\n")

    def seleciona_cliente(self):
        cpf = input("CPF do cliente que deseja selecionar: ")
        return cpf

