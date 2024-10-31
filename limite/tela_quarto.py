from limite.tela import Tela


class TelaQuarto(Tela):

    def tela_opcoes(self):
        escolhas = [1,2,3,4,0]
        print("-------- QUARTOS ----------")
        print("Escolha uma opção")
        print("1- Incluir Quarto")
        print("2- Alterar Quarto")
        print("3- Listar Quartos")
        print("4- Excluir Quarto")
        print("0- Retornar")

        while True:
            try:
                escolha = super().le_num_inteiro("Escolha: ", escolhas)
                return escolha

            except ValueError:
                print("Escolha inválida")

    def pega_dados_quarto(self):
        print("-------- DADOS QUARTO --------")
        print("Qual tipo de quarto deseja?")
        print("1- Standard")
        print("2- Suíte")
        print("3- Luxo")
        tipos_validos = [1,2,3]
        while True:
            try:
                tipo = super().le_num_inteiro("Tipo: ", tipos_validos)
                numero = super().le_num_inteiro("Número: ")
                valor_diaria = super().le_num_inteiro("Valor da diária: ")
                descricao = input("Descrição: ")

                return {"numero": numero, "valor_diaria": valor_diaria,
                        "descricao": descricao, "tipo": tipo}

            except ValueError:
                print("Valores inseridos inválidos")

    #Não será possível alterar o tipo do quarto, e será possível alterar o status,
    #logo foi necessária uma nova função mais específica
    def pega_dados_alteracao_quarto(self):
        print("-------- DADOS QUARTO --------")
        while True:
            try:
                numero = super().le_num_inteiro("Número: ")
                valor_diaria = super().le_num_inteiro("Valor da diária: ")
                descricao = input("Descrição: ")
                print("\n")
                status = self.pega_status_quarto()

                return {"numero": numero, "valor_diaria": valor_diaria,
                        "descricao": descricao, "status": status}

            except ValueError: 
                print("Valores inseridos inválidos")        

    def mostra_quarto(self, dados_quarto):
        print("Quarto tipo", dados_quarto["tipo"])
        print("Número: ", dados_quarto["numero"])
        print(f"Valor da diária: R${dados_quarto['valor_diaria']},00")
        print("Descrição: ", dados_quarto["descricao"])
        print("Status: ", dados_quarto["status"])
        print("\n")

    def seleciona_quarto(self):
        while True:
            try:
                numero = super().le_num_inteiro("Número do quarto que deseja selecionar: ")
                return numero

            except ValueError:
                print("Valor inserido inválido")

    def pega_status_quarto(self):
        escolhas = [1,2,3]

        print("Qual status você deseja?")
        print("1- Disponível")
        print("2- Ocupado")
        print("3- Manutenção")
        while True:
            try:
                status = super().le_num_inteiro("Status: ", escolhas) #CRIAR ERRO ESPECÍFICO?
                if status == 1:
                    return "Disponível"
                if status == 2:
                    return "Ocupado"
                if status == 3:
                    return "Manutenção"
            except ValueError:
                print("Valor inserido inválido")
