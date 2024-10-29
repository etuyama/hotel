from limite.tela import Tela


class TelaServico(Tela):

    def tela_opcoes(self):
        escolhas = [1,2,3,4,0]
        print("-------- SERVIÇOS -------- ")
        print("Escolha a opção")
        print("1 - Adicionar Serviço")
        print("2 - Alterar Serviço")
        print("3 - Listar Serviços")
        print("4 - Excluir Serviço")
        print("0 - Retornar")
        while True:
            try:
                escolha = super().le_num_inteiro("Escolha: ", escolhas)
                return escolha

            except ValueError:
                print("Escolha inválida")

    def pega_dados_servico(self):
        print("-------- DADOS SERVIÇO --------")
        while True:
            try:
                nome = input("Nome do Serviço: ")

                id = super().le_num_inteiro("ID do serviço: ")
                if id <= 0:
                    raise ValueError

                descricao = input("Descricao: ")

                preco = super().le_num_inteiro("Preço: ")

                if preco < 0:
                    raise ValueError

                return {
                    "nome": nome,
                    "descricao": descricao,
                    "preco": preco,
                    "id": id
                }
            except ValueError:
                print("Valor inserido inválido.")


    def mostra_servico(self, dados_servico):
        print("Serviço: ", dados_servico["nome"])
        print("ID: ", dados_servico["id"])
        print("Descriçao: ", dados_servico["descricao"])
        print(f"Preco: R$ {dados_servico["preco"]},00")
        print("\n")

    def seleciona_servico(self):
        while True:
            try:
                id = super().le_num_inteiro(
                    "Digite o ID do serviço que deseja selecionar: "
                )
                return id

            except ValueError:
                print("Valor inserido inválido.")

    def mostra_mensagem(self, mensagem):
        print(mensagem)