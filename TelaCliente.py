
class TelaCliente():
    def tela_opcoes(self):
        escolhas = [1,2,3,4,0]
        print("-------- CLIENTES ----------")
        print("Escolha a opção")
        print("1 - Incluir Cliente")
        print("2 - Alterar Cliente")
        print("3 - Listar Clientes")
        print("4 - Excluir Cliente")
        print("0 - Retornar")

        escolha = int(input("Escolha: "))
        if escolha in escolhas:
            return escolha
        else:
            print("Escolha inválida")
            self.tela_opcoes()

    def pega_dados_cliente(self):
        print("-------- DADOS CLIENTE --------")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        idade = input("Idade: ")
        telefone = input("Telefone: ")
        endereco = input("Endereco: ")
        if isinstance(nome, str) and isinstance(cpf, str) and \
                isinstance(idade, int) and isinstance(telefone, str) and \
                isinstance(endereco, str):
            return {"nome" : nome, "cpf" : cpf, "telefone" : telefone,
                    "idade" : idade, "endereco" : endereco}
        else:
            print("Dados inválidos")
            self.pega_dados_cliente()

    def mostra_cliente(self, dados_cliente):
        print("Nome do cliente: ", dados_cliente["nome"])
        print("CPF: ", dados_cliente["cpf"])
        print("Idade: ", dados_cliente["idade"])
        print("Telefone: ", dados_cliente["telefone"])
        print("Endereco: ", dados_cliente["endereco"])
        print("\n")

    def seleciona_cliente(self):
        cpf = str(input("CPF do cliente que deseja selecionar: "))
        return cpf

    def mostra_mensagem(self, mensagem):
        print(mensagem)
