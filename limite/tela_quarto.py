from limite.tela import Tela


class TelaQuarto(Tela):

    def tela_opcoes(self):
        escolhas = [1,2,3,4,0]
        print("-------- QUARTOS ----------")
        print("Escolha a opção")
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
                if numero <= 0:
                    raise ValueError #CRIAR ERRO ESPECÍFICO?

                valor_diaria = super().le_num_inteiro("Valor da diária: ")
                if valor_diaria <= 0:
                    raise ValueError #CRIAR ERRO ESPECÍFICO?

                descricao = input("Descrição: ")
                return {"numero": numero, "valor_diaria": valor_diaria,
                        "descricao": descricao, "tipo": tipo}

            except ValueError:
                print("Valores inseridos inválidos")

    #Não será possível alterar o tipo do quarto, logo foi necessária uma nova função mais específica    
    def pega_dados_alteracao_quarto(self):
        print("-------- DADOS QUARTO --------")
        while True:
            try:
                numero = super().le_num_inteiro("Número: ")
                if numero <= 0 :
                    raise ValueError #CRIAR ERRO ESPECÍFICO?

                valor_diaria = super().le_num_inteiro("Valor da diária: ")
                if valor_diaria <= 0:
                    raise ValueError #CRIAR ERRO ESPECÍFICO?
                descricao = input("Descrição: ")

                return {"numero": numero, "valor_diaria": valor_diaria,
                        "descricao": descricao}

            except ValueError:
                print("Valores inseridos inválidos")        

    def mostra_quarto(self, dados_quarto):
        print("Quarto tipo ", dados_quarto["tipo"])
        print("Número: ", dados_quarto["numero"])
        print("Valor da diária: ", dados_quarto["valor_diaria"])
        print("Descrição: ", dados_quarto["descricao"])
        print("\n")

    def seleciona_quarto(self):
        while True:
            try:
                numero = super().le_num_inteiro("Número do quarto que deseja selecionar: ")
                return numero

            except ValueError:
                print("Valor inserido inválido")
